import cv2

# Function to draw a box on the object to be tracked
def drawBox(img, bbox):
    x, y, w, h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x, y), ((x + w), (y + h)), (255, 0, 255), 2, 1)
    cv2.putText(img, "Tracking", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

# Function to continuously read the video and track the object
def goal_track(img, bbox):
    tracker = cv2.TrackerCSRT_create()
    tracker.init(img, tuple(bbox))

    while True:
        success, img = check.read()
        if not success:
            print("Video ended.")
            break

        success, bbox = tracker.update(img)

        if success:
            drawBox(img, bbox)
        else:
            cv2.putText(img, "LOST", (75, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        cv2.imshow("Tracking", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Read the video and get the initial box coordinates
check = cv2.VideoCapture('footvolleyball.mp4')  # Replace 'your_video.mp4' with your video file
success, img = check.read()
bbox = cv2.selectROI("Tracking", img, False)
cv2.destroyAllWindows()

# Call the goal_track() function with initial parameters
goal_track(img, bbox)
