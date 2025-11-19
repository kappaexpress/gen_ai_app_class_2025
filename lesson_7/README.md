# Streamlit × Gemini チャットボット サンプルコード

このディレクトリには、StreamlitとGoogle Gemini APIを使ったチャットボット開発の段階的なサンプルコードが含まれています。

## 📁 ファイル構成

```
code/7/
├── 1_streamlit_basics.py        # Streamlitの基本機能
├── 2_chat_ui_mock.py            # Chat UIの基本（モック）
├── 3_chat_with_history.py       # 会話履歴を保持するシンプルなエコーボット
├── 4_gemini_chatbot.py          # Gemini APIを使ったチャットボット
├── 5_sqlite_chatbot.py          # SQLiteで履歴を永続化
├── requirements.txt             # 必要なパッケージ
├── .gitignore                   # Git除外設定
└── README.md                    # このファイル
```

## 🚀 セットアップ

### 1. パッケージのインストール

```bash
pip install -r requirements.txt
```

### 2. APIキーの設定

Google AI StudioでAPIキーを取得します：
https://aistudio.google.com/apikey

#### 方法1: 環境変数（推奨）

```bash
# Linux/Mac
export GEMINI_API_KEY='your_api_key_here'

# Windows（PowerShell）
$env:GEMINI_API_KEY="your_api_key_here"
```

#### 方法2: Streamlit secrets

```bash
mkdir -p .streamlit
cat > .streamlit/secrets.toml << EOF
GEMINI_API_KEY = "your_api_key_here"
EOF
```

## 📚 サンプルコードの説明

### 1. Streamlitの基本 (`1_streamlit_basics.py`)

Streamlitの基本的な機能を学ぶためのコード

**学習内容:**
- テキスト表示
- データ表示（DataFrame、テーブル）
- チャート
- ウィジェット（入力、スライダー、セレクトボックス等）
- レイアウト（サイドバー、カラム、エキスパンダー）
- ステータス表示
- セッション状態の基本

**実行方法:**
```bash
streamlit run 1_streamlit_basics.py
```

**ポイント:**
- `st.session_state`の使い方
- インタラクティブなウィジェット
- レイアウトの構成方法

---

### 2. Chat UIのモック (`2_chat_ui_mock.py`)

Streamlitのチャット要素の基本的な使い方

**学習内容:**
- `st.chat_message`の使い方
- `st.chat_input`の使い方
- カスタムアバター
- メッセージ内に複数の要素を配置
- シンプルなエコーボット

**実行方法:**
```bash
streamlit run 2_chat_ui_mock.py
```

**ポイント:**
- チャットメッセージの表示方法
- アバターのカスタマイズ
- メッセージコンテナの柔軟性

---

### 3. 会話履歴を保持するチャット (`3_chat_with_history.py`)

`st.session_state`を使って会話履歴を保持するシンプルなエコーボット

**学習内容:**
- セッション状態での履歴管理
- 履歴の再描画
- メッセージの追加と表示
- サイドバーでの実装詳細の説明表示

**実行方法:**
```bash
streamlit run 3_chat_with_history.py
```

**ポイント:**
- `st.session_state`の正しい初期化
- 履歴の永続化（セッション内）
- メッセージのデータ構造
- サイドバーでの情報表示

**特徴:**
- メインエリア: シンプルなエコーボットのモック
- サイドバー: セッション状態の実装詳細と会話クリア機能

---

### 4. Gemini APIチャットボット (`4_gemini_chatbot.py`)

Google Gemini APIと連携した本格的なチャットボット

**学習内容:**
- Gemini APIのセットアップ
- クライアントの初期化とキャッシュ
- 会話履歴のGemini形式への変換
- ストリーミング応答
- エラーハンドリング

**実行方法:**
```bash
streamlit run 4_gemini_chatbot.py
```

**必要な設定:**
- `GEMINI_API_KEY`環境変数または`.streamlit/secrets.toml`

**ポイント:**
- `@st.cache_resource`でクライアントをキャッシュ
- ストリーミングでリアルタイム表示
- 適切なエラーハンドリング
- 入力バリデーション

**使用モデル:**
- モデル: `gemini-flash-lite-latest`
- パラメータ: デフォルト設定を使用

---

### 5. SQLite永続化チャットボット (`5_sqlite_chatbot.py`)

会話履歴をSQLiteデータベースに保存し、アプリを再起動しても履歴が残るシンプルなチャットボット

**学習内容:**
- SQLiteデータベースのセットアップ
- シンプルなテーブル設計（messages）
- CRUD操作（作成、読み取り、削除）
- 起動時の履歴自動読み込み
- データベースとセッション状態の同期

**実行方法:**
```bash
streamlit run 5_sqlite_chatbot.py
```

**必要な設定:**
- `GEMINI_API_KEY`環境変数または`.streamlit/secrets.toml`

**ポイント:**
- シンプルなテーブル構造（messagesのみ）
- 起動時にDBから過去の会話を自動読み込み
- メッセージ送信時にリアルタイムでDB保存
- 「会話をクリア」ボタンで全履歴削除

**データベーススキーマ:**
```sql
-- messages テーブル
CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT NOT NULL,
    content TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
```

**主な関数:**
- `init_database()`: データベースとテーブルの初期化
- `save_message()`: メッセージをDBに保存
- `load_messages()`: 起動時に全メッセージを読み込み
- `clear_all_messages()`: 全履歴を削除

---

## 🎯 学習の進め方

### ステップ1: Streamlitの基本を理解
1. `1_streamlit_basics.py`を実行して、Streamlitの基本を学ぶ
2. コードを読んで、各機能の使い方を確認
3. コードを改変して、動作を確認

### ステップ2: Chat UIの使い方を習得
1. `2_chat_ui_mock.py`を実行して、チャット要素を理解
2. 異なるアバターやレイアウトを試す
3. エコーボットの仕組みを理解

### ステップ3: 履歴管理を実装
1. `3_chat_with_history.py`を実行
2. セッション状態の動作を確認
3. サイドバーの実装詳細を読んで理解を深める

### ステップ4: Gemini APIと連携
1. APIキーを設定
2. `4_gemini_chatbot.py`を実行
3. 実際のAIチャットボットの動作を確認
4. エラーハンドリングの動作を確認

### ステップ5: データベース永続化
1. `5_sqlite_chatbot.py`を実行
2. いくつかメッセージを送信
3. アプリを再起動して、履歴が残っていることを確認
4. データベースファイル（`chat_history.db`）を確認
5. 「会話をクリア」ボタンで履歴削除を試す

---

## 💡 重要なポイント

### セッション状態の初期化

❌ **間違い:**
```python
st.session_state.messages = []  # 毎回リセットされる
```

✅ **正しい:**
```python
if "messages" not in st.session_state:
    st.session_state.messages = []
```

### APIキーのセキュリティ

❌ **間違い:**
```python
API_KEY = "AIzaSy..."  # コードに直接書かない！
```

✅ **正しい:**
```python
api_key = st.secrets.get("GEMINI_API_KEY")
# または環境変数から
api_key = os.getenv('GEMINI_API_KEY')
```

### エラーハンドリング

```python
try:
    response = client.models.generate_content(...)
except errors.ClientError as e:
    error_message = f"APIエラー: {str(e)}"
    st.error(error_message)
```

---

## 🔧 トラブルシューティング

### パッケージのインポートエラー

```bash
# google-genaiが見つからない場合
pip install google-genai

# Streamlitが古い場合
pip install --upgrade streamlit
```

### APIキーエラー

1. APIキーが正しく設定されているか確認
2. 環境変数またはsecretsファイルが正しく読み込まれているか確認
3. APIキーの有効期限を確認

### データベースエラー

1. `chat_history.db`ファイルの権限を確認
2. データベースファイルを削除して再作成
3. SQLiteのバージョンを確認

---

## 📖 参考資料

### 公式ドキュメント
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google AI Studio](https://aistudio.google.com/)
- [Gemini API Documentation](https://ai.google.dev/)

### チュートリアル
- [Streamlit Chat Tutorial](https://docs.streamlit.io/develop/tutorials/chat-and-llm-apps/build-conversational-apps)
- [Python SQLite3 Tutorial](https://docs.python.org/3/library/sqlite3.html)
