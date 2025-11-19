"""
SQLiteデータベースを使ったチャット履歴の永続化
==============================================
シンプルな会話履歴の保存と読み込み

実行方法:
1. 必要なパッケージをインストール
   pip install google-genai

2. APIキーを設定
   .streamlit/secrets.toml に設定
   GEMINI_API_KEY = "your_api_key_here"

3. 実行
   streamlit run 5_sqlite_chatbot.py
"""

import streamlit as st
import sqlite3
from google import genai
from google.genai import types, errors

# ページ設定
st.set_page_config(
    page_title="SQLite チャットボット", page_icon="💾", layout="centered"
)

st.title("💾 SQLite チャットボット")

# DBファイル名
DB_FILE = "chat_history.db"


# データベース初期化
def init_database():
    """データベースとテーブルを初期化"""
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """
    )

    conn.commit()
    conn.close()


# メッセージを保存
def save_message(role, content):
    """メッセージをデータベースに保存"""
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute("INSERT INTO messages (role, content) VALUES (?, ?)", (role, content))

    conn.commit()
    conn.close()


# すべてのメッセージを取得
def load_messages():
    """データベースからすべてのメッセージを取得"""
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()

    cur.execute("SELECT role, content FROM messages ORDER BY timestamp ASC")

    messages = []
    for row in cur.fetchall():
        messages.append({"role": row[0], "content": row[1]})

    conn.close()
    return messages


# すべてのメッセージを削除
def clear_all_messages():
    """データベースからすべてのメッセージを削除"""
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("DELETE FROM messages")
    conn.commit()
    conn.close()


# データベース初期化
init_database()

# APIキーの取得
try:
    api_key = st.secrets.get("GEMINI_API_KEY")
except (FileNotFoundError, KeyError):
    api_key = None

# APIキーチェック
if not api_key:
    st.warning("APIキーが設定されていません")
    st.info(
        """
    ### APIキーの設定方法

    #### .streamlit/secrets.toml
    ```toml
    GEMINI_API_KEY = "your_api_key_here"
    ```

    [APIキーを取得](https://aistudio.google.com/apikey)
    """
    )
    st.stop()


# Geminiクライアントの初期化
@st.cache_resource
def init_gemini_client(_api_key):
    """Geminiクライアントを初期化（キャッシュして再利用）"""
    try:
        return genai.Client(api_key=_api_key)
    except Exception as e:
        st.error(f"クライアント初期化エラー: {str(e)}")
        return None


client = init_gemini_client(api_key)

# セッション状態の初期化（起動時にDBから読み込み）
if "messages" not in st.session_state:
    st.session_state.messages = load_messages()

# 会話クリアボタン
if st.session_state.messages:
    if st.button("🗑️ 会話をクリア"):
        clear_all_messages()
        st.session_state.messages = []
        st.rerun()

# メッセージ履歴の表示
for message in st.session_state.messages:
    avatar = "👤" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])

# ユーザー入力
if prompt := st.chat_input("メッセージを入力してください..."):
    # 入力バリデーション
    if not prompt.strip():
        st.warning("メッセージを入力してください")
        st.stop()

    if len(prompt) > 10000:
        st.error("メッセージが長すぎます（最大10000文字）")
        st.stop()

    # ユーザーメッセージを保存・表示
    save_message("user", prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # AIの応答を生成
    with st.chat_message("assistant", avatar="🤖"):
        try:
            # 会話履歴をGemini形式に変換
            contents = []
            for msg in st.session_state.messages:
                role = "user" if msg["role"] == "user" else "model"
                contents.append(
                    types.Content(role=role, parts=[types.Part(text=msg["content"])])
                )

            # ストリーミング生成
            message_placeholder = st.empty()
            full_response = ""

            for chunk in client.models.generate_content_stream(
                model="gemini-flash-lite-latest",
                contents=contents,
                config=types.GenerateContentConfig(),
            ):
                if chunk.text:
                    full_response += chunk.text
                    message_placeholder.markdown(full_response)

            # 最終表示
            message_placeholder.markdown(full_response)

            # データベースに保存
            save_message("assistant", full_response)

            # 履歴に追加
            st.session_state.messages.append(
                {"role": "assistant", "content": full_response}
            )

        except errors.ClientError as e:
            error_message = f"APIエラー: {str(e)}"
            st.error(error_message)

        except Exception as e:
            st.error(f"予期しないエラー: {str(e)}")
            st.exception(e)
