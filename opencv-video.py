import cv2

video = cv2.VideoCapture("1.mkv")
# video = cv2.VideoCapture(0)


def nothing(_):
    pass


cv2.namedWindow("Video", cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("Threshold", "Video", 0, 255, nothing)
cv2.setTrackbarPos("Threshold", "Video", 7)

if not video.isOpened():
    print("Error opening video file")

while True:
    ret, frame = video.read()

    if not ret:
        break

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    threshold = cv2.getTrackbarPos("Threshold", "Video")
    _, frame = cv2.threshold(frame, threshold, 255, cv2.THRESH_BINARY)

    cv2.imshow("Video", frame)

    # Delay for 30 milliseconds (33 frames per second)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
