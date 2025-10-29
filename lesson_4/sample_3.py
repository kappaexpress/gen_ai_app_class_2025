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

# Chain-of-Thought (CoT) プロンプティング
# 複雑な問題を解決するための思考過程を模倣する
# ステップバイステップで思考過程を述べるプロンプトを作成する

print("=== 通常のプロンプト（CoTなし）===")
print("(思考過程を示さずに質問)\n")

# CoTなしの場合
without_cot_prompt = """下記の質問にTrueまたはFalseで回答してください。
このグループの奇数を合計すると偶数になります。: 15、32、5、13、82、7、1。
A:
"""

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

# Chain-of-Thought プロンプティングの実行
print("\n=== Chain-of-Thought (CoT) プロンプティング ===")
print("(思考過程の例を示して質問)\n")

cot_prompt = """このグループの奇数を合計すると偶数になります。: 4、8、9、15、12、2、1。
A: 奇数を全て加えると(9, 15, 1)25になります。答えはFalseです。

このグループの奇数を合計すると偶数になります。: 17、10、19、4、8、12、24。
A: 奇数を全て加えると(17, 19)36になります。答えはTrueです。

このグループの奇数を合計すると偶数になります。: 16、11、14、4、8、13、24。
A: 奇数を全て加えると(11, 13)24になります。答えはTrueです。

このグループの奇数を合計すると偶数になります。: 17、9、10、12、13、4、2。
A: 奇数を全て加えると(17, 9, 13)39になります。答えはFalseです。

下記の質問にTrueまたはFalseで回答してください。
このグループの奇数を合計すると偶数になります。: 15、32、5、13、82、7、1。
A:
"""

contents = [
    types.Content(
        role="user",
        parts=[types.Part.from_text(text=cot_prompt)],
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
