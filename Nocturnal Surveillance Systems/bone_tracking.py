import cv2
import mediapipe as mp

def track_pose():
    # Initialize VideoCapture
    cap = cv2.VideoCapture(0)

    # Initialize Mediapipe solutions
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()

    while True:
        # Read frame from video capture
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the image to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the image and get pose landmarks
        results = pose.process(rgb_frame)
        landmarks = results.pose_landmarks

        # Display the landmarks on the frame
        if landmarks:
            mp.solutions.drawing_utils.draw_landmarks(
                frame, landmarks, mp_pose.POSE_CONNECTIONS)

        # Show the frame
        cv2.imshow('Pose Tracking', frame)

        # Exit on 'q' keypress
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture and close windows
    cap.release()
    cv2.destroyAllWindows()

# Run the pose tracking function
track_pose()
