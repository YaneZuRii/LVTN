"""
Demo: 1 file mp4 -> ma tran vector (T, 63) (MediaPipe Hand Landmarker).
Chay sau khi da tai video: python demo_video_to_vector.py
"""
from __future__ import annotations

import urllib.request
from pathlib import Path

import cv2
import mediapipe as mp
import numpy as np
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

BASE = Path(__file__).resolve().parent / "vsl-signconnect"
VIDEO = BASE / "Videos" / "D0002.mp4"
LABEL_CSV = BASE / "Text" / "label.csv"
if not LABEL_CSV.is_file():
    LABEL_CSV = Path(__file__).resolve().parent / "Text" / "label.csv"
MODEL_PATH = BASE / "hand_landmarker.task"
MODEL_URL = (
    "https://storage.googleapis.com/mediapipe-models/"
    "hand_landmarker/hand_landmarker/float16/1/hand_landmarker.task"
)
OUT_NPY = BASE / "vectors_demo" / "D0002_vectors.npy"
STRIDE = 5


def ensure_model() -> Path:
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not MODEL_PATH.is_file():
        print("Dang tai model MediaPipe...")
        urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
    return MODEL_PATH


def frame_to_vector_63(hand_landmarks) -> list[float]:
    pts = np.array([[lm.x, lm.y, lm.z] for lm in hand_landmarks], dtype=np.float32)
    pts = pts - pts[0]
    return pts.flatten().tolist()


def read_label(video_name: str) -> str | None:
    if not LABEL_CSV.is_file():
        return None
    for line in LABEL_CSV.read_text(encoding="utf-8").splitlines()[1:]:
        parts = line.split(",", 2)
        if len(parts) >= 3 and parts[1].strip() == video_name:
            return parts[2].strip()
    return None


def video_to_matrix(path: Path, landmarker: vision.HandLandmarker) -> np.ndarray:
    cap = cv2.VideoCapture(str(path))
    if not cap.isOpened():
        raise SystemExit(f"Khong mo duoc {path}")
    rows: list[list[float]] = []
    idx = 0
    while True:
        ok, bgr = cap.read()
        if not ok:
            break
        if idx % STRIDE == 0:
            rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
            result = landmarker.detect(mp_image)
            if result.hand_landmarks:
                rows.append(frame_to_vector_63(result.hand_landmarks[0]))
        idx += 1
    cap.release()
    return np.array(rows, dtype=np.float32)


def main() -> None:
    if not VIDEO.is_file():
        raise SystemExit(f"Chua co video. Chay: python download_vsl_hf.py\n  Expected: {VIDEO}")
    model = ensure_model()
    opts = vision.HandLandmarkerOptions(
        base_options=python.BaseOptions(model_asset_path=str(model)),
        num_hands=1,
        min_hand_detection_confidence=0.5,
        min_hand_presence_confidence=0.5,
        min_tracking_confidence=0.5,
    )
    label = read_label(VIDEO.name)
    with vision.HandLandmarker.create_from_options(opts) as landmarker:
        X = video_to_matrix(VIDEO, landmarker)
    OUT_NPY.parent.mkdir(parents=True, exist_ok=True)
    np.save(OUT_NPY, X)
    print(f"Video: {VIDEO.name} | Label: {label} | shape: {X.shape} | saved: {OUT_NPY}")


if __name__ == "__main__":
    main()