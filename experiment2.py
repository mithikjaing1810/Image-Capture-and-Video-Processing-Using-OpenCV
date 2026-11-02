# ==============================================================================
# Developed By: Mithik jain G
# Register No: 212224240087
# Experiment 2: Image Acquisition and Video Processing Using OpenCV
# ==============================================================================

import cv2
import os

def capture_and_save_frame(filename="captured_image.jpg"):
    """Operation 1: Write the frame as a JPG file"""
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(filename, frame)
        print(f"[SUCCESS] Frame captured and saved as '{filename}'")
    else:
        print("[ERROR] Failed to capture frame from webcam.")
    cap.release()

def display_live_video():
    """Operation 2: Display the video"""
    cap = cv2.VideoCapture(0)
    print("Displaying Live Video. Press 'q' to exit...")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cv2.imshow('Live Video Stream', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def display_resized_video(width=640, height=480):
    """Operation 3: Display the video by resizing the window"""
    cap = cv2.VideoCapture(0)
    print(f"Displaying Resized Video ({width}x{height}). Press 'q' to exit...")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        resized_frame = cv2.resize(frame, (width, height))
        cv2.imshow(f'Resized Video ({width}x{height})', resized_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

def display_rotated_video():
    """Operation 4: Rotate and display the video (90 degrees clockwise)"""
    cap = cv2.VideoCapture(0)
    print("Displaying Rotated Video (90 degrees clockwise). Press 'q' to exit...")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        cv2.imshow('Rotated Video (90 Clockwise)', rotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Select an operation to perform:")
    print("1. Write the frame as JPG file")
    print("2. Display the live video")
    print("3. Display the video by resizing the window")
    print("4. Rotate and display the video")
    print("5. Run all operations sequentially")

    choice = input("Enter choice (1-5): ").strip()

    if choice == '1':
        capture_and_save_frame()
    elif choice == '2':
        display_live_video()
    elif choice == '3':
        display_resized_video()
    elif choice == '4':
        display_rotated_video()
    elif choice == '5':
        capture_and_save_frame()
        display_live_video()
        display_resized_video()
        display_rotated_video()
    else:
        print("Invalid choice.")

