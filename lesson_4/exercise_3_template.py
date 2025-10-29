# 課題3: インタラクティブクイズアプリ（テンプレート）
# 生成AIでクイズ問題を生成し、ユーザーと対話するアプリを作成

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

print("=" * 60)
print("   都道府県クイズアプリ")
print("=" * 60)
print()

# ステップ1: AIにクイズ問題を生成させる
print("クイズ問題を生成中...")
print()

# TODO: Few-Shotプロンプティングで問題形式を例示し、3問のクイズを生成させる
# ヒント: JSON配列形式で、各要素に question, choices, answer を含める
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

# APIを呼び出してクイズを生成
response = client.models.generate_content(
    model=model,
    contents=contents,
    config=types.GenerateContentConfig(),
)

# JSONとしてパース
try:
    # TODO: レスポンスからJSON部分を抽出してパースしてください
    response_text = response.text.strip()

    # ここにコードブロック除去のコードを記述してください


    # JSONをパース
    quiz_questions = None  # ここを修正してください

    print("クイズ問題の生成が完了しました！")
    print()

except json.JSONDecodeError as e:
    print(f"エラー: クイズ問題の生成に失敗しました。")
    print(f"詳細: {e}")
    print("\nデバッグ情報:")
    print(response.text)
    exit(1)

# ステップ2: ユーザーに問題を出題して回答を受け取る
correct_count = 0

for i, quiz in enumerate(quiz_questions, 1):
    print("=" * 60)
    print(f"問題 {i}/3")
    print("=" * 60)
    print()
    print(quiz['question'])
    print()

    # 選択肢を表示
    for j, choice in enumerate(quiz['choices']):
        print(f"  {j + 1}. {choice}")
    print()

    # TODO: ユーザーから回答を受け取る（エラーハンドリング付き）
    # ヒント: while True でループし、try-exceptでエラーを処理
    # input()で入力を受け取り、1-3の範囲内かチェックする
    while True:
        try:
            # ここにユーザー入力を受け取るコードを記述してください
            user_input = None  # ここを修正してください
            user_answer = None  # ここを修正してください（0-indexedに変換）

            # 入力値の範囲チェック
            # ここにコードを記述してください

            break

        except ValueError:
            print("無効な入力です。1から3の数字を入力してください。")
        except KeyboardInterrupt:
            print("\n\nクイズを中断しました。")
            exit(0)

    # TODO: 正誤判定を行う
    correct_answer = quiz['answer']
    is_correct = False  # ここを修正してください

    print()
    if is_correct:
        print("✓ 正解！")
        # TODO: correct_countをインクリメントしてください

    else:
        print(f"✗ 残念！正解は {quiz['choices'][correct_answer]} です。")

    print()

# ステップ3: 最終結果を表示
print("=" * 60)
print("   クイズ終了！")
print("=" * 60)
print()
print(f"正解数: {correct_count} / 3")
print()

# TODO: 正解数に応じたメッセージを表示
# 3問正解: "完璧です！"
# 2問正解: "よくできました！"
# 1問以下: "もう一度チャレンジしてみましょう！"
message = ""  # ここを修正してください

print(message)
print()
print("ご参加ありがとうございました！")
