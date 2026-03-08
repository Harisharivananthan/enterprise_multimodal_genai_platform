import cv2
from multimodal.image_encoder import encode_image


def extract_frames(video_path, frame_interval=30):
    cap = cv2.VideoCapture(video_path)

    frames = []
    count = 0

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        if count % frame_interval == 0:
            frames.append(frame)

        count += 1

    cap.release()
    return frames


def encode_video(video_path):
    frames = extract_frames(video_path)
    vectors = []

    for frame in frames:
        temp_path = "temp_frame.jpg"
        cv2.imwrite(temp_path, frame)

        vector = encode_image(temp_path)
        vectors.append(vector)

    return vectors