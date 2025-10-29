# 課題1: 都道府県データの取得と集計（テンプレート）
# 生成AIから都道府県情報をJSON形式で取得し、統計処理を行う

import os
import json
from google import genai
from google.genai import types

# 環境変数からGemini APIキーを取得
api_key = os.environ.get("GEMINI_API_KEY")

# Google GenAI クライアントの初期化
client = genai.Client(api_key=api_key)

# 使用するモデルの指定
model = "gemini-flash-lite-latest"

# TODO: プロンプトを作成してください
# ヒント: 5つの都道府県（例: 東京都、大阪府、北海道、沖縄県、愛知県）について
# 都道府県名、人口（万人）、面積（km²）、県庁所在地の情報を
# JSON配列形式で出力するように指示してください
prompt = """
(ここにプロンプトを記述してください)
"""

# プロンプトの構築
contents = [
    types.Content(
        role="user",
        parts=[types.Part.from_text(text=prompt)],
    ),
]

# APIを呼び出してコンテンツを生成
print("=== AIに都道府県データを生成させています... ===\n")
response = client.models.generate_content(
    model=model,
    contents=contents,
    config=types.GenerateContentConfig(),
)

print("--- AIからのレスポンス ---")
print(response.text)
print("------\n")

# JSONとしてパースして処理
try:
    # TODO: レスポンスからJSON部分を抽出してください
    # ヒント: sample_1.pyを参考に、マークダウンのコードブロック（```json や ```）を除去する
    response_text = response.text.strip()

    # ここにコードブロック除去のコードを記述してください


    # TODO: JSONをパースしてください
    prefectures = None  # ここを修正してください

    print("=== パースされたデータ ===")
    print(json.dumps(prefectures, ensure_ascii=False, indent=2))
    print("------\n")

    # TODO: ここから統計処理を実装してください
    print("=== 統計情報 ===")

    # 1. 合計人口を計算してください
    total_population = 0  # ここを修正してください
    print(f"合計人口: {total_population}万人")

    # 2. 平均人口を計算してください
    average_population = 0  # ここを修正してください
    print(f"平均人口: {average_population:.1f}万人")

    # 3. 最も人口が多い都道府県を見つけてください
    # ヒント: max()関数とlambdaを使う
    max_population_pref = None  # ここを修正してください
    print(f"最も人口が多い都道府県: {max_population_pref['name']} ({max_population_pref['population']}万人)")

    # 4. 最も面積が大きい都道府県を見つけてください
    max_area_pref = None  # ここを修正してください
    print(f"最も面積が大きい都道府県: {max_area_pref['name']} ({max_area_pref['area']}km²)")

    print("------\n")

    # 詳細情報の表示
    print("=== 各都道府県の詳細 ===")
    for pref in prefectures:
        print(f"{pref['name']}")
        print(f"  人口: {pref['population']}万人")
        print(f"  面積: {pref['area']}km²")
        print(f"  県庁所在地: {pref['capital']}")
        print()

except json.JSONDecodeError as e:
    print(f"JSON解析エラー: {e}")
    print("AIのレスポンスがJSON形式ではありませんでした。")
except KeyError as e:
    print(f"データ構造エラー: {e}")
    print("期待されるキーが見つかりませんでした。")
except Exception as e:
    print(f"予期しないエラー: {e}")
