# AI Story Generator

This project is an AI-powered horror story generator that converts the generated story into speech and creates a simple video.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/YOUR_USERNAME/ai-story-generator.git
    cd ai-story-generator
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the script with the required OpenAI API key:
    ```bash
    python main.py --api_key YOUR_OPENAI_API_KEY
    ```

2. Customize the prompt, audio file name, and video file name using command-line arguments:
    ```bash
    python main.py --prompt "Write a horror story about a ghost ship lost at sea." --api_key YOUR_OPENAI_API_KEY --audio_file ghost_ship.mp3 --video_file ghost_ship_video.avi
    ```

## License

This project is licensed under the MIT License.
