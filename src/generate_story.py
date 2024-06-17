import openai

def generate_horror_story(prompt, api_key):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )
    story = response.choices[0].text.strip()
    return story
