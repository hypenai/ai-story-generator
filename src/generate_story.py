import openai

def generate_horror_story(prompt, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a horror story writer."},
            {"role": "user", "content": prompt}
        ]
    )
    story = response['choices'][0]['message']['content'].strip()
    return story
