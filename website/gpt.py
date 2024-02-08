from openai import OpenAI
client = OpenAI()

def gptTest(text):
    response = client.embeddings.create(
        input=text,
        model="text-embedding-3-large"
    )

    return(response.data[0].embedding)
    

# from openai import OpenAI
# client = OpenAI()

# def gptTest():
#     completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#         {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#     ]
#     )

#     print(completion.choices[0].message)
# gptTest()