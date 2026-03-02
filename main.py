from my_tracking import Tracking, process_video_in_chunks
from ultralytics import YOLO
from utils import read_video, save_video

def main():
    video_path = "input/car.mp4"
    output_path = "output_video.avi"
    model_path = "license_plate_detector.pt"

    tracker = Tracking(model=YOLO(model_path))

    frames = read_video(video_path)

    chunked_frames = process_video_in_chunks(frames)
    annotated_frames = []

    for chunk in chunked_frames:
        tracks = tracker.get_object(chunk)
        annotated_chunk = tracker.annotation(chunk, tracks)
        annotated_frames.extend(annotated_chunk)

    save_video(annotated_frames, output_path)

if __name__ == "__main__":
    main()