import os
import openai

openai.api_key = "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"

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="where is france?",
  temperature=0.5,
  max_tokens=2000,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
  stop=["You:"]
)
print(response["choices"][0]["text"])