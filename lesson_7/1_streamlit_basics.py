"""
Streamlitの基本
================
Streamlitの基本的な使い方を学ぶためのサンプルコード

実行方法:
streamlit run 1_streamlit_basics.py
"""

import streamlit as st
import numpy as np
import pandas as pd

# ページ設定（最初に実行する必要がある）
st.set_page_config(
    page_title="Streamlit 基本",
    page_icon="📚",
    layout="centered"
)

# タイトルとテキスト
st.title("📚 Streamlitの基本")
st.header("1. テキスト表示")
st.write("Streamlitは、Pythonだけで簡単にWebアプリが作れるフレームワークです。")
st.markdown("**太字**や*イタリック*、`コード`も表示できます。")
st.caption("これはキャプションです")

st.divider()

# コード表示
st.header("2. コードの表示")
code = """
import streamlit as st
st.write("Hello, Streamlit!")
"""
st.code(code, language="python")

st.divider()

# データ表示
st.header("3. データの表示")

# データフレーム
df = pd.DataFrame({
    "名前": ["太郎", "花子", "次郎"],
    "年齢": [25, 30, 22],
    "スコア": [85, 92, 78]
})
st.dataframe(df)

# テーブル
st.table(df)

st.divider()

# チャート
st.header("4. チャート")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)
st.line_chart(chart_data)

st.divider()

# ウィジェット
st.header("5. インタラクティブなウィジェット")

# テキスト入力
name = st.text_input("名前を入力してください", "太郎")
st.write(f"こんにちは、{name}さん！")

# スライダー
age = st.slider("年齢を選択", 0, 100, 25)
st.write(f"年齢: {age}歳")

# セレクトボックス
option = st.selectbox(
    "好きな色は？",
    ["赤", "青", "緑", "黄色"]
)
st.write(f"選択した色: {option}")

# チェックボックス
if st.checkbox("詳細を表示"):
    st.write("詳細情報がここに表示されます。")

# ボタン
if st.button("クリックしてください"):
    st.balloons()
    st.success("ボタンがクリックされました！")

st.divider()

# サイドバー
st.header("6. サイドバー")
with st.sidebar:
    st.header("サイドバー設定")
    st.write("サイドバーには設定項目を配置できます。")
    sidebar_option = st.radio(
        "オプションを選択",
        ["オプション1", "オプション2", "オプション3"]
    )
    st.write(f"選択: {sidebar_option}")

st.divider()

# カラム
st.header("7. レイアウト - カラム")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("カラム1")
    st.metric("メトリック1", "100", "+10")

with col2:
    st.write("カラム2")
    st.metric("メトリック2", "200", "-5")

with col3:
    st.write("カラム3")
    st.metric("メトリック3", "300", "+20")

st.divider()

# エキスパンダー
st.header("8. エキスパンダー")
with st.expander("クリックして展開"):
    st.write("ここに詳細情報を配置できます。")
    st.write("長い説明文やコードなどを折りたたんで表示できます。")

st.divider()

# ステータス
st.header("9. ステータス表示")

# 成功メッセージ
st.success("これは成功メッセージです")

# 情報メッセージ
st.info("これは情報メッセージです")

# 警告メッセージ
st.warning("これは警告メッセージです")

# エラーメッセージ
st.error("これはエラーメッセージです")

st.divider()

# プログレスバー
st.header("10. プログレスとスピナー")

import time

if st.button("プログレスバーを表示"):
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i + 1)
    st.success("完了しました！")

if st.button("スピナーを表示"):
    with st.spinner("処理中..."):
        time.sleep(2)
    st.success("処理が完了しました！")

st.divider()

# セッション状態
st.header("11. セッション状態")
st.write("セッション状態を使うと、ページの再実行をまたいでデータを保持できます。")

# カウンターの初期化
if "counter" not in st.session_state:
    st.session_state.counter = 0

# カウンターを増やすボタン
if st.button("カウンターを増やす"):
    st.session_state.counter += 1

st.write(f"カウンター: {st.session_state.counter}")

# リセットボタン
if st.button("リセット"):
    st.session_state.counter = 0
    st.rerun()

st.divider()

# ダウンロードボタン
st.header("12. ダウンロードボタン")

csv_data = df.to_csv(index=False).encode('utf-8-sig')
st.download_button(
    label="CSVをダウンロード",
    data=csv_data,
    file_name="data.csv",
    mime="text/csv"
)

st.divider()

# ファイルアップロード
st.header("13. ファイルアップロード")

uploaded_file = st.file_uploader("ファイルを選択してください", type=['txt', 'csv'])
if uploaded_file is not None:
    st.write("ファイル名:", uploaded_file.name)
    st.write("ファイルサイズ:", uploaded_file.size, "bytes")
