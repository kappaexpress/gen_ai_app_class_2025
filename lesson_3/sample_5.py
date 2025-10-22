import os
from google import genai
from google.genai import types

api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(
    api_key=api_key,
)

model = "gemini-flash-lite-latest"


def generate(prompt: str) -> str:
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=prompt),
            ],
        ),
    ]

    generate_content_config = types.GenerateContentConfig()

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )

    return response.text


if __name__ == "__main__":
    result = generate("私は田中と言います。覚えておいてください。")
    print("--- 生成結果1 ---")
    print(result)
    print("------\n")

    result = generate("私の名前を教えてください。")
    print("--- 生成結果2 ---")
    print(result)
    print("------\n")
