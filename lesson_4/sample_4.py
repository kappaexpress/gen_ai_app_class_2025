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

# Zero-shot CoT (Chain-of-Thought) プロンプティング
# 元のプロンプトに「ステップバイステップで考えてみましょう」という文言を追加することで、
# 例を示さなくても思考過程を促すことができる

print("=== 通常のプロンプト（Zero-shot CoTなし）===")
print("(ステップバイステップの指示なし)\n")

# Zero-shot CoTなしの場合
without_cot_prompt = """50円硬貨と100円硬貨が合わせて15枚ある。金額の合計が1200円だとすると、100円硬貨は何枚あるか。"""

contents = [
    types.Content(
        role="user",
        parts=[types.Part.from_text(text=without_cot_prompt)],
    ),
]

response = client.models.generate_content(
    model=model,
    contents=contents,
    config=types.GenerateContentConfig(),
)

print("--- 結果 ---")
print(response.text)
print("------\n")

# Zero-shot CoT プロンプティングの実行
print("\n=== Zero-shot CoT プロンプティング ===")
print("(「ステップバイステップで考えてみましょう」を追加)\n")

zero_shot_cot_prompt = """50円硬貨と100円硬貨が合わせて15枚ある。金額の合計が1200円だとすると、100円硬貨は何枚あるか。

ステップバイステップで考えてみましょう。
"""

contents = [
    types.Content(
        role="user",
        parts=[types.Part.from_text(text=zero_shot_cot_prompt)],
    ),
]

response = client.models.generate_content(
    model=model,
    contents=contents,
    config=types.GenerateContentConfig(),
)

print("--- 結果 ---")
print(response.text)
print("------\n")

