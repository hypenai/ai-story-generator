import os
from src.generate_story import generate_horror_story
from src.text_to_speech import text_to_speech
from src.image_generator import generate_image
from src.video_creator import create_video
from PIL import Image

def main():
    api_key = 'your-openai-api-key'
    prompt = "Write a horror story about a haunted house."
    story = generate_horror_story(prompt, api_key)
    print("Generated Horror Story:")
    print(story)

    audio_file = "horror_story.mp3"
    text_to_speech(story, audio_file)

    sentences = story.split('. ')
    images = []
    for i, sentence in enumerate(sentences):
        image_file = f"image_{i}.png"
        generate_image(sentence, image_file)
        images.append(Image.open(image_file))

    video_file = "horror_story_video.avi"
    create_video(audio_file, images, video_file)

    for i in range(len(sentences)):
        os.remove(f"image_{i}.png")

if __name__ == "__main__":
    main()
