"""
Chat UIを使ったモック（エコーボット）
====================================
Streamlitのチャット要素の基本的な使い方を学ぶ

実行方法:
streamlit run 2_chat_ui_mock.py
"""

import streamlit as st
import time

# ページ設定
st.set_page_config(
    page_title="Chat UI モック",
    page_icon="💬",
    layout="centered"
)

st.title("💬 Chat UIの基本")
st.caption("Streamlitのチャット要素を使った基本的な実装例")

# タブで異なるサンプルを表示
tab1, tab2, tab3, tab4 = st.tabs([
    "基本的な表示",
    "カスタムアバター",
    "複数の要素",
    "エコーボット"
])

# タブ1: 基本的な表示
with tab1:
    st.header("1. 基本的なチャットメッセージ")

    st.markdown("### ユーザーメッセージ")
    st.code("""
with st.chat_message("user"):
    st.write("こんにちは！")
    """)

    with st.chat_message("user"):
        st.write("こんにちは！")

    st.markdown("### アシスタントメッセージ")
    st.code("""
with st.chat_message("assistant"):
    st.write("はい、どうぞご質問ください。")
    """)

    with st.chat_message("assistant"):
        st.write("はい、どうぞご質問ください。")

# タブ2: カスタムアバター
with tab2:
    st.header("2. カスタムアバター")

    st.markdown("### 絵文字アバター")
    st.code("""
with st.chat_message("user", avatar="👤"):
    st.write("絵文字をアバターに使えます")
    """)

    with st.chat_message("user", avatar="👤"):
        st.write("絵文字をアバターに使えます")

    with st.chat_message("assistant", avatar="🤖"):
        st.write("ロボットのアイコンです")

    st.markdown("### Material Iconsアバター")
    st.code("""
with st.chat_message("assistant", avatar=":material/smart_toy:"):
    st.write("Material Iconsも使えます")
    """)

    with st.chat_message("assistant", avatar=":material/smart_toy:"):
        st.write("Material Iconsも使えます")

    with st.chat_message("system", avatar=":material/settings:"):
        st.write("システムメッセージ")

# タブ3: 複数の要素
with tab3:
    st.header("3. メッセージ内に複数の要素を配置")

    st.code("""
with st.chat_message("assistant"):
    st.write("チャットメッセージ内には、様々な要素を配置できます")
    st.markdown("- リスト項目1\\n- リスト項目2")
    st.code("print('Hello, World!')")

    import pandas as pd
    df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    st.dataframe(df)

    st.line_chart(df)
    """)

    with st.chat_message("assistant"):
        st.write("チャットメッセージ内には、様々な要素を配置できます")
        st.markdown("- リスト項目1\n- リスト項目2\n- リスト項目3")
        st.code("print('Hello, World!')", language="python")

        import pandas as pd
        df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        st.dataframe(df)

        st.line_chart(df)

# タブ4: エコーボット
with tab4:
    st.header("4. シンプルなエコーボット")

    st.markdown("""
    このエコーボットは、ユーザーの入力をそのまま返します。
    ただし、**セッション状態を使っていない**ため、履歴は保持されません。
    """)

    st.code("""
prompt = st.chat_input("メッセージを入力してください")

if prompt:
    # ユーザーメッセージを表示
    with st.chat_message("user"):
        st.markdown(prompt)

    # エコー応答を表示
    with st.chat_message("assistant"):
        st.markdown(f"エコー: {prompt}")
    """)

    st.divider()

    # チャット入力
    prompt = st.chat_input("メッセージを入力してください")

    if prompt:
        # ユーザーメッセージを表示
        with st.chat_message("user"):
            st.markdown(prompt)

        # エコー応答を表示
        with st.chat_message("assistant"):
            st.markdown(f"エコー: {prompt}")

        st.info("💡 **注意**: 新しいメッセージを送信すると、前のメッセージは消えてしまいます。履歴を保持するには `st.session_state` を使う必要があります。")

# サイドバーに説明
with st.sidebar:
    st.header("📚 st.chat_message の使い方")

    st.markdown("""
    ### 基本構文
    ```python
    with st.chat_message(name, avatar=None):
        # メッセージ内容
        st.write("テキスト")
    ```

    ### name パラメータ
    - `"user"` または `"human"`: ユーザー
    - `"assistant"` または `"ai"`: AI
    - その他の文字列: カスタム名

    ### avatar パラメータ
    - 絵文字: `"🤖"`, `"👤"`
    - Material Icons: `:material/smart_toy:`
    - 画像URL
    - ローカルファイルパス
    """)

    st.divider()

    st.header("📚 st.chat_input の使い方")

    st.markdown("""
    ### 基本構文
    ```python
    prompt = st.chat_input("プレースホルダー")
    if prompt:
        # ユーザー入力があった時の処理
        st.write(prompt)
    ```

    ### 特徴
    - ページ下部に固定表示
    - Enter キーで送信
    - 送信時にスクリプトが再実行される
    - 送信がない場合は `None` を返す
    """)
