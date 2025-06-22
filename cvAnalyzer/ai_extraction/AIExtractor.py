from huggingface_hub import login, InferenceClient
from ai_extraction.PdfToStringParser import extract_text
import os
from dotenv import load_dotenv


load_dotenv("cvAnalyzer/ai_extraction/.env")
my_token = os.getenv('token')
print(my_token)

# Log in first with your API Token
login(my_token)

# Initialize a client with your API token
client = InferenceClient(
    provider="cerebras",
    api_key=my_token,
    model="meta-llama/Llama-4-Scout-17B-16E-Instruct"
)

# Send a prompt
prompt = """
You are an automated CV parser for computer science students. Your task is to extract information from the following CV text and transform it into a well-structured JSON object. The object should follow this format:

{
  "name": "...",
  "current_workplace": "...",
  "bio": "...",
  "relevant_experience_history": [
    {
      "company": "...",
      "role": "...",
      "start_date": "...",
      "end_date": "...",
      "experiences": "..."
    }
  ],
  "coding_projects": [
    {
      "project_name": "...",
      "technologies": ["..."],
      "description": "...",
      "demoLink":"....",
      "githubLink":"...."
    }
  ]
  "contact": {
    "email": "...",
    "linkedIn": "...",
    "github": "..."
    }
  "other": []
}

Please extract this information as accurately as you can.
If something is missing, do your best to research if its like an organisation and you need description. if you cant find anything with certanty, leave it empty.
your are to create the bio from what you read in first person, 2 senteces.

You are to return text only in the json format nothing else.

Here’s the CV text you should extract from:"""

input = extract_text("resourses/testCV.pdf")


def run(path_to_cv):

    input = extract_text(path_to_cv)

    messages = [
        {"role": "system", 'content': prompt},
        {"role": "user", "content": input}
    ]

    response = client.chat_completion(messages)
    return response.choices[0].message.content
