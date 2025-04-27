import openai
import os

# Set up OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Upload the dataset
upload_response = openai.File.create(
    file=open("dataset.jsonl"),  # Make sure your dataset.jsonl is in the same directory as this script
    purpose='fine-tune'
)

# Get the file ID
file_id = upload_response['id']

# Fine-tune the model
response = openai.FineTune.create(
    training_file=file_id,
    model="gpt-3.5-turbo",  # You can adjust this to a different model like davinci if needed
    n_epochs=2  # Number of epochs (you can adjust this based on your needs)
)

print(f"Fine-tuning started with response: {response}")
