import streamlit as st
from google import genai
from google.genai import types, errors

# ページ設定
st.set_page_config(
    page_title="Gemini AI チャットボット", page_icon="🤖", layout="centered"
)

st.title("🤖 Gemini AI チャットボット")

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

# セッション状態の初期化
if "messages" not in st.session_state:
    st.session_state.messages = []

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

    # ユーザーメッセージを追加・表示
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
                    # 部分表示
                    message_placeholder.markdown(full_response)

            # 最終表示
            message_placeholder.markdown(full_response)

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
