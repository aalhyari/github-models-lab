from openai import OpenAI
from sk import my_sk #import secret key from sk.py file
import os

# Set your PAT token (recommended: use environment variable)
os.environ["GITHUB_TOKEN"] = "<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>"

client = OpenAI(
    base_url="https://models.github.ai/inference/v1",
    api_key=os.environ["GITHUB_TOKEN"]
)

response = client.chat.completions.create(
    model="gpt-4o-mini",     # You may choose any model from Marketplace
    messages=[
        {"role": "user", "content": "Hello GitHub Models! Write one sentence."}
    ]
)

print("Model Response:")
print(response.choices[0].message["content"])
