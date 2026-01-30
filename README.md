# Face Blurring Tool

A simple and effective Python tool to automatically blur faces in images, videos, or real-time via webcam, using MediaPipe for face detection.

## 📋 Features

- **Image Mode**: Blur faces in a static image
- **Video Mode**: Process a complete video and blur all detected faces
- **Webcam Mode**: Blur faces in real-time from your webcam

## 🛠️ Requirements

- Python 3.7+
- OpenCV
- MediaPipe

## 📦 Installation

1. Clone or download this repository

2. Install the required dependencies:
```bash
pip install opencv-python mediapipe
```

## 🚀 Usage

### Webcam Mode (default)
```bash
python face_blur.py --mode webcam
```

Press `ESC` to quit.

### Image Mode
```bash
python face_blur.py --mode image --filePath path/to/image.jpg
```

The processed image will be saved to `./output/output.png`

### Video Mode
```bash
python face_blur.py --mode video --filePath path/to/video.mp4
```

The processed video will be saved to `./output/output.mp4`

## ⚙️ Arguments

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `--mode` | str | `webcam` | Execution mode: `webcam`, `image`, or `video` |
| `--filePath` | str | `None` | Path to image or video file (required for image/video modes) |

## 📁 Project Structure
```
.
├── face_blur.py          # Main script
├── README.md             # Documentation
└── output/               # Output folder (created automatically)
    ├── output.png        # Processed image
    └── output.mp4        # Processed video
```

## 🔧 Detection Parameters

The script uses MediaPipe Face Detection with the following parameters:
- **model_selection**: 0 (model optimized for short distance, < 2 meters)
- **min_detection_confidence**: 0.5 (minimum confidence threshold for detection)

You can adjust these parameters in the code according to your needs.

## 📝 Examples
```bash
# Blur faces in a group photo
python face_blur.py --mode image --filePath photos/group.jpg

# Blur faces in a surveillance video
python face_blur.py --mode video --filePath videos/surveillance.mp4

# Real-time usage
python face_blur.py --mode webcam
```

## 🔄 How It Works

1. **Face Detection**: MediaPipe detects faces in the image/frame
2. **Coordinate Extraction**: Bounding boxes of faces are retrieved
3. **Blur Application**: A gaussian blur (30x30) is applied to each detected face
4. **Save**: The result is displayed (webcam) or saved (image/video)

## ⚙️ Customization

### Modify Blur Intensity

In the `process_img()` function, change the `(30, 30)` values:
```python
img[y1:y1 + h, x1:x1 + w, :] = cv2.blur(img[y1:y1 + h, x1:x1 + w, :], (50, 50))
```

### Change Detection Model
```python
# model_selection=0 : short distance (< 2m)
# model_selection=1 : long distance (> 2m)
with mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5) as face_detection:
```

### Adjust Detection Confidence
```python
# Value between 0.0 and 1.0
# Higher = fewer false positives, but may miss faces
min_detection_confidence=0.7
```

## ⚠️ Important Notes

- Default blur is 30x30 pixels
- Output videos use MP4V codec with 25 FPS
- The `output/` folder is created automatically
- Output files overwrite previous files

## 🐛 Troubleshooting

### "Cannot open webcam"
- Check that your webcam is connected
- Try changing `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)`

### "Failed to read video"
- Check that the file path is correct
- Ensure the video format is supported (mp4, avi, mov, etc.)

### Slow Performance
- Reduce video/webcam resolution
- Use `model_selection=0` for better performance

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Improve documentation

## 📄 License

This project is free to use for educational and personal purposes.

## 🙏 Acknowledgments

- [MediaPipe](https://google.github.io/mediapipe/) for face detection
- [OpenCV](https://opencv.org/) for image processing

---

**Privacy Note**: This tool is designed to protect privacy by blurring faces. Make sure you have the necessary permissions before processing images/videos of people.
