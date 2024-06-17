import os
import argparse
from src.generate_story import generate_horror_story
from src.text_to_speech import text_to_speech
from src.image_generator import generate_image
from src.video_creator import create_video
from PIL import Image

def main(prompt, api_key, audio_file, video_file):
    story = generate_horror_story(prompt, api_key)
    print("Generated Horror Story:")
    print(story)

    text_to_speech(story, audio_file)

    sentences = story.split('. ')
    images = []
    for i, sentence in enumerate(sentences):
        image_file = f"image_{i}.png"
        generate_image(sentence, image_file)
        images.append(Image.open(image_file))

    create_video(audio_file, images, video_file)

    for i in range(len(sentences)):
        os.remove(f"image_{i}.png")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Horror Story Generator")
    parser.add_argument('--prompt', type=str, default="Write a horror story about a haunted house.",
                        help='Prompt for the story generator')
    parser.add_argument('--api_key', type=str, help='OpenAI API key (optional, will use api_key.txt if not provided)')
    parser.add_argument('--audio_file', type=str, default="horror_story.mp3", help='Output audio file name')
    parser.add_argument('--video_file', type=str, default="horror_story_video.avi", help='Output video file name')

    args = parser.parse_args()

    # Read API key from file if not provided as argument
    if not args.api_key:
        with open('api_key.txt', 'r') as file:
            args.api_key = file.read().strip()

    main(args.prompt, args.api_key, args.audio_file, args.video_file)
