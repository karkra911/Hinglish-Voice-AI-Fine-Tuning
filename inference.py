import openai
import os

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Replace 'ft-yourmodel' with the ID of your fine-tuned model
fine_tuned_model = "ft-yourmodel"

# Test the fine-tuned model with some Hinglish prompts
def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model=fine_tuned_model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# Example Hinglish prompts
prompts = [
    "Mujhe ek chai pilao.",
    "Kya kar rahe ho?",
    "Kal ka plan kya hai?"
]

for prompt in prompts:
    print(f"User: {prompt}")
    print(f"Assistant: {generate_response(prompt)}\n")
