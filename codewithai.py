import openai
import os

# Set up OpenAI API credentials
openai.api_key = "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"

# Read the input file
with open("planetext.txt", "r") as f:
    input_text = f.read()

# Split the input text into 1000 words chunks
chunks = [input_text[i:i+1000] for i in range(0, len(input_text), 1000)]

# Summarize each chunk using OpenAI API and save the response in a list
responses = []
for chunk in chunks:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt= "summarize the following text : "+chunk,
        temperature=0.5,
        max_tokens=60,
        n = 1,
        stop=None
    )
    summary = response.choices[0].text.strip()
    responses.append(summary)

# Save the response as another .txt file
with open("summary.txt", "w") as f:
    f.write("\n".join(responses))
    
# Confirm that file was created
if os.path.isfile("summary.txt"):
    print("Summary file created successfully.")