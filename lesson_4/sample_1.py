# 必要なライブラリのインポート
import os  # 環境変数にアクセスするために使用
import json  # JSON形式の出力を扱うために使用
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
# gemini-flash-lite-latestは高速で軽量なFlashモデルの最新版
model = "gemini-flash-lite-latest"

# プロンプトの要素を明確に示す例
# - 命令: ユーザーの質問に基づいて回答する
# - 文脈: 藤井聡太氏のタイトル獲得記録
# - 入力データ: 「藤井聡太が初めて獲得したタイトルは何ですか？」
# - 出力指示子: JSON形式で出力

prompt = """ユーザーの質問に下記の藤井聡太氏のタイトル獲得記録に基づいて回答してください。(命令)
すべての回答はjson形式で出力してください。(出力指示子)

藤井聡太氏のタイトル獲得記録(文脈)
タイトルに関する最年少記録
初タイトル獲得(第91期棋聖戦) - 17歳11か月
二冠(第61期王位戦) - 18歳1か月
三冠(第6期叡王戦) - 19歳1か月
四冠(第34期竜王戦) - 19歳3か月
五冠(第71期王将戦) - 19歳6か月
六冠(第48期棋王戦) - 20歳8か月
七冠(第81期名人戦) - 20歳10か月
八冠(第71期王座戦) - 21歳2か月

ユーザー: 藤井聡太が初めて獲得したタイトルは何ですか？(入力データ)
"""

# プロンプトの構築
contents = [
    types.Content(
        role="user",  # メッセージの送信者(ユーザー)を指定
        parts=[
            types.Part.from_text(text=prompt),
        ],
    ),
]

# コンテンツ生成の設定
generate_content_config = types.GenerateContentConfig()

# Gemini APIを呼び出してコンテンツを生成
response = client.models.generate_content(
    model=model,  # 使用するモデル
    contents=contents,  # プロンプト内容
    config=generate_content_config,  # 生成設定
)

# 生成結果の表示
print("--- 生成結果 ---")
print(response.text)
print("------\n")

# JSONとしてパースして表示
try:
    # レスポンスからJSON部分を抽出
    response_text = response.text.strip()
    # マークダウンのコードブロックを除去
    if response_text.startswith("```json"):
        response_text = response_text[7:]
    if response_text.startswith("```"):
        response_text = response_text[3:]
    if response_text.endswith("```"):
        response_text = response_text[:-3]

    json_data = json.loads(response_text.strip())
    print("--- JSON形式で解析した結果 ---")
    print(json.dumps(json_data, ensure_ascii=False, indent=2))
    print("------\n")
except json.JSONDecodeError as e:
    print(f"JSON解析エラー: {e}\n")

