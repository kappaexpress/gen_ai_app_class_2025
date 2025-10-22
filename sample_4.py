# 必要なライブラリのインポート
import os  # 環境変数にアクセスするために使用
from google import genai  # Google GenAI APIのメインモジュール
from google.genai import types  # APIリクエストとレスポンスの型定義

# 環境変数からGemini APIキーを取得
# セキュリティのため、APIキーはコードに直接記述せず環境変数から取得する
api_key = os.environ.get("GEMINI_API_KEY")

# Google GenAI クライアントの初期化
# このクライアントを通じてGemini APIとやり取りする
client = genai.Client(
    api_key=api_key,
)

# 使用するモデルの指定
# gemini-2.5-proは高性能なGemini 2.5モデルのプロ版
model = "gemini-2.5-pro"

# プロンプト（ユーザーからの入力）の構築
# Contentオブジェクトのリストとして会話履歴を表現する
contents = [
    types.Content(
        role="user",  # メッセージの送信者（ユーザー）を指定
        parts=[
            # Part.from_text()でテキスト形式のメッセージを作成
            types.Part.from_text(text="俳句を作ってください。"),
        ],
    ),
]

# コンテンツ生成の設定
# GenerateContentConfigで生成時の詳細なパラメータを指定できる
generate_content_config = types.GenerateContentConfig()

# Gemini APIを呼び出してコンテンツを生成
# generate_content()メソッドでモデルにプロンプトを送信し、レスポンスを受け取る
response = client.models.generate_content(
    model=model,  # 使用するモデル
    contents=contents,  # プロンプト内容
    config=generate_content_config,  # 生成設定
)

# 生成結果の表示
print("--- 生成結果 ---")
# response.textで生成されたテキストを取得
print(response.text)
print("------\n")

# 使用されたトークン数の表示
print("プロンプトのトークン数:")
print(response.usage_metadata.prompt_token_count)

print("生成されたコンテンツのトークン数:")
print(response.usage_metadata.candidates_token_count)
