import cv2
import numpy as np
from PIL import Image

def create_video(audio_file, images, video_file):
    audio = cv2.VideoCapture(audio_file)
    fps = 1
    frame_width, frame_height = images[0].size
    out = cv2.VideoWriter(video_file, cv2.VideoWriter_fourcc(*'DIVX'), fps, (frame_width, frame_height))

    for image in images:
        img_array = np.array(image)
        img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        out.write(img_array)

    out.release()
