# 課題2: 算数問題の自動採点プログラム（テンプレート）
# 生成AIに算数の文章問題を解かせ、自動採点を行う

import os
import json
import re
from google import genai
from google.genai import types

# 環境変数からGemini APIキーを取得
api_key = os.environ.get("GEMINI_API_KEY")

# Google GenAI クライアントの初期化
client = genai.Client(api_key=api_key)

# 使用するモデルの指定
model = "gemini-flash-lite-latest"

# 問題と正解のデータ
problems = [
    {
        "id": 1,
        "question": "りんご1個120円、みかん1個80円です。りんご3個とみかん5個を買うと合計いくらですか？",
        "correct_answer": 760
    },
    {
        "id": 2,
        "question": "太郎君は45ページの本を読んでいます。今日18ページ読みました。残りは何ページですか？",
        "correct_answer": 27
    },
    {
        "id": 3,
        "question": "1個150円のケーキを4個買って、1000円出しました。おつりはいくらですか？",
        "correct_answer": 400
    }
]

# 採点結果を格納するリスト
results = []

print("=== 算数問題の自動採点プログラム ===\n")

# 各問題についてAIに解答させる
for problem in problems:
    print(f"問題{problem['id']}: {problem['question']}")
    print("AIが解答中...\n")

    # TODO: プロンプトを作成してください
    # ヒント: Zero-shot CoT（「ステップバイステップで考えてみましょう」）を使用
    # JSON形式で「計算過程」と「答え」を返すように指示
    prompt = f"""
(ここにプロンプトを記述してください)
問題: {problem['question']}
"""

    # プロンプトの構築
    contents = [
        types.Content(
            role="user",
            parts=[types.Part.from_text(text=prompt)],
        ),
    ]

    # APIを呼び出してコンテンツを生成
    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=types.GenerateContentConfig(),
    )

    print("--- AIの回答 ---")
    print(response.text)
    print("------\n")

    # TODO: AIの回答から答えを抽出してください
    try:
        # レスポンスからJSON部分を抽出
        response_text = response.text.strip()

        # TODO: マークダウンのコードブロックを除去してください
        # ここにコードを記述してください


        # TODO: JSONをパースして答えを取得してください
        ai_response = None  # ここを修正してください
        ai_answer = None  # ここを修正してください

    except (json.JSONDecodeError, KeyError, ValueError):
        # JSONパースに失敗した場合は正規表現で数値を抽出
        print("JSON形式でのパースに失敗。正規表現で数値を抽出します...")
        numbers = re.findall(r'\d+', response.text)
        if numbers:
            # 最後に出現する数値を答えとする
            ai_answer = int(numbers[-1])
        else:
            ai_answer = None
            print("答えを抽出できませんでした。")

    # TODO: 正誤判定を行ってください
    if ai_answer is not None:
        # ここに正誤判定のコードを記述してください
        is_correct = False  # ここを修正してください
        result_mark = "?"  # ここを修正してください

        print(f"AIの答え: {ai_answer}")
        print(f"正解: {problem['correct_answer']}")
        print(f"判定: {result_mark}")

        # TODO: 結果をresultsリストに追加してください


    else:
        print("判定: × (答えを抽出できませんでした)")
        results.append({
            "problem_id": problem['id'],
            "correct": False
        })

    print("\n" + "="*50 + "\n")

# TODO: 最終結果を表示してください（正解数、不正解数、正解率）
print("=== 採点結果 ===")

# ここに結果表示のコードを記述してください
correct_count = 0  # ここを修正してください
total_count = 0  # ここを修正してください
accuracy = 0  # ここを修正してください

print(f"正解数: {correct_count} / {total_count}")
print(f"正解率: {accuracy:.1f}%")

# 各問題の結果を表示
print("\n詳細:")
for result in results:
    mark = "○" if result['correct'] else "×"
    print(f"  問題{result['problem_id']}: {mark}")

print("\n採点完了!")
