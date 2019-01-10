import cv2
cap = cv2.VideoCapture(0)
frame = cap.read()
cv2.imshow("capture",frame)
cv2.imwrite("video,jpg",frame)
cap.release()
cv2.destroyALLWindows()
