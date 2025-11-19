"""
会話履歴を保持するチャットボット
================================
st.session_stateを使って会話履歴を保持するシンプルなエコーボット

実行方法:
streamlit run 3_chat_with_history.py
"""

import streamlit as st

# ページ設定
st.set_page_config(
    page_title="会話履歴付きチャット", page_icon="💬", layout="centered"
)

st.title("💬 会話履歴を保持するチャットボット")
st.caption("st.session_stateを使った履歴管理の実装例")

# サイドバー: 実装の詳細
with st.sidebar:
    st.header("📚 実装の詳細")
    st.markdown("""
    ## セッション状態の重要性

    Streamlitは、ユーザーの操作ごとにスクリプト全体を再実行します。
    そのため、変数は毎回リセットされてしまいます。

    ### 問題
    ```python
    messages = []  # 毎回空のリストに戻る！
    ```

    ### 解決策: st.session_state
    ```python
    if "messages" not in st.session_state:
        st.session_state.messages = []
    ```

    ## 実装のポイント

    ### 1. セッション状態の初期化
    ```python
    if "messages" not in st.session_state:
        st.session_state.messages = []
    ```

    ### 2. 履歴の再描画
    ```python
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    ```

    ### 3. 新規メッセージの処理
    ```python
    if prompt := st.chat_input("入力..."):
        # ユーザーメッセージを追加
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        # ボットの応答を生成
        response = f"エコー: {prompt}"

        # ボットの応答を追加
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })
    ```

    ## メッセージのデータ構造

    ```python
    message = {
        "role": "user",           # または "assistant"
        "content": "メッセージ内容"
    }
    ```

    ## よくある間違い

    ### ❌ 間違い
    ```python
    st.session_state.messages = []  # 毎回リセットされる
    ```

    ### ✅ 正しい
    ```python
    if "messages" not in st.session_state:
        st.session_state.messages = []
    ```
    """)

    st.divider()

    # 会話クリアボタン
    if st.button("🗑️ 会話をクリア", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

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
    # ユーザーメッセージを履歴に追加・表示
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    # エコーボットの応答
    response = f"エコー: {prompt}"

    # ボットの応答を表示・履歴に追加
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(response)

    st.session_state.messages.append({"role": "assistant", "content": response})
