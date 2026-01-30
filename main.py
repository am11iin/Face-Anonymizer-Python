import os
import argparse
import cv2
import mediapipe as mp

def process_img(img, face_detection):
    H, W, _ = img.shape
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    out = face_detection.process(img_rgb)

    if out.detections is not None:
        for detection in out.detections:
            bbox = detection.location_data.relative_bounding_box
            x1 = int(bbox.xmin * W)
            y1 = int(bbox.ymin * H)
            w = int(bbox.width * W)
            h = int(bbox.height * H)

            # Blur faces
            img[y1:y1 + h, x1:x1 + w, :] = cv2.blur(img[y1:y1 + h, x1:x1 + w, :], (30, 30))

    return img

#   ARGUMENTS 
parser = argparse.ArgumentParser()
parser.add_argument("--mode", default='webcam', choices=['webcam', 'image', 'video'])
parser.add_argument("--filePath", default=None, help="Path to image or video")
args = parser.parse_args()


#   OUTPUT DIRECTORY 
output_dir = './output'
os.makedirs(output_dir, exist_ok=True)


#  FACE DETECTION 
mp_face_detection = mp.solutions.face_detection

with mp_face_detection.FaceDetection(model_selection=0, min_detection_confidence=0.5) as face_detection:

    #  IMAGE MODE 
    if args.mode == "image":
        if not args.filePath:
            print("Please provide --filePath for image mode.")
            exit()
        img = cv2.imread(args.filePath)
        img = process_img(img, face_detection)
        cv2.imwrite(os.path.join(output_dir, 'output.png'), img)
        print("Image saved to ./output/output.png")

    #  VIDEO MODE 
    elif args.mode == "video":
        if not args.filePath:
            print("Please provide --filePath for video mode.")
            exit()
        cap = cv2.VideoCapture(args.filePath)
        ret, frame = cap.read()
        if not ret:
            print("Failed to read video.")
            exit()

        output_video = cv2.VideoWriter(
            os.path.join(output_dir, 'output.mp4'),
            cv2.VideoWriter_fourcc(*'MP4V'),
            25,
            (frame.shape[1], frame.shape[0])
        )

        while ret:
            frame = process_img(frame, face_detection)
            output_video.write(frame)
            ret, frame = cap.read()

        cap.release()
        output_video.release()
        print("Video saved to ./output/output.mp4")

    #  WEBCAM MODE 
    elif args.mode == "webcam":
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Cannot open webcam.")
            exit()

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame.")
                break

            frame = process_img(frame, face_detection)
            cv2.imshow('Webcam - Press ESC to quit', frame)

            # Quitter si on appuie sur ESC
            if cv2.waitKey(25) & 0xFF == 27:
                break

        cap.release()
        cv2.destroyAllWindows()
        