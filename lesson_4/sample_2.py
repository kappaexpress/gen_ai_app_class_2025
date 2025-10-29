# 必要なライブラリのインポート
import os  # 環境変数にアクセスするために使用
from google import genai  # Google GenAI APIのメインモジュール
from google.genai import types  # APIリクエストとレスポンスの型定義

# 環境変数からGemini APIキーを取得
api_key = os.environ.get("GEMINI_API_KEY")

# Google GenAI クライアントの初期化
client = genai.Client(
    api_key=api_key,
)

# 使用するモデルの指定
model = "gemini-flash-lite-latest"

# Few-Shotプロンプティングの例
# 少数の例を使ってAIに学習させる方法
# モデルがタスクの文脈をより良く理解し、予測可能な結果を得ることができる

print("=== Zero-Shot プロンプティングの例 ===")
print("(例を与えずに分類を依頼)\n")

# Zero-Shot（例なし）の場合
zero_shot_prompt = """テキストを中立的、否定的、または肯定的に分類してください。

テキスト: テストはまずまずでした。
"""

contents = [
    types.Content(
        role="user",
        parts=[types.Part.from_text(text=zero_shot_prompt)],
    ),
]

response = client.models.generate_content(
    model=model,
    contents=contents,
    config=types.GenerateContentConfig(),
)

print("--- Zero-Shot の結果 ---")
print(response.text)
print("------\n")

# Few-Shotプロンプティングの実行
print("\n=== Few-Shot プロンプティングの例 ===")
print("(複数の例を与えて分類を依頼)\n")

few_shot_prompt = """これは素晴らしい! // 肯定的
これは酷い! // 否定的
普通な番組だな // 中立的
あの映画は最高だった! // 肯定的

テキストを中立的、否定的、または肯定的に分類してください。

テキスト: テストはまずまずでした。
"""

contents = [
    types.Content(
        role="user",
        parts=[types.Part.from_text(text=few_shot_prompt)],
    ),
]

response = client.models.generate_content(
    model=model,
    contents=contents,
    config=types.GenerateContentConfig(),
)

print("--- Few-Shot の結果 ---")
print(response.text)
print("------\n")
