// Gen AI #8

// Before using this code created using python for story creating in GenAI you have to install the open ai.
// follow the below code and write it in the terminal to do that

// pip install openai

// Code

import openai

# Set your OpenAI API key
openai.api_key = 'your_openai_api_key_here'

# Define the prompt you want to use
prompt = "Write a short story about a brave astronaut exploring a new planet."

# Call the OpenAI API to generate text
response = openai.Completion.create(
    engine="text-davinci-003",  # Use a suitable GPT-3 model
    prompt=prompt,
    max_tokens=150,             # Limit the number of tokens (words) in the response
    temperature=0.7,            # Adjust the creativity level (0 to 1)
    n=1,                        # Number of completions to generate
    stop=None                   # Optional stopping condition
)

# Print the generated story
generated_story = response.choices[0].text.strip()
print("Generated Story:\n", generated_story)
