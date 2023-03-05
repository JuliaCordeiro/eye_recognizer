import cv2
import dlib
from eyes_functions import (
    midpoint,
    eye_points,
)
from constants import (
    LEFT_EYE_POINTS,
    RIGHT_EYE_POINTS,
)


def detecting():
    face_detector = dlib.get_frontal_face_detector()
    points_predictor = dlib.shape_predictor('landmark/shape_predictor_68_face_landmarks.dat')

    while True:
        _, frame = open_camera.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_detector(gray_frame)
        for face in faces:
            eye_points_mask = points_predictor(gray_frame, face)

            left_eye_points = eye_points(eye_points_mask, LEFT_EYE_POINTS)
            right_eye_points = eye_points(eye_points_mask, RIGHT_EYE_POINTS)

            # Left eye, horizontal and vertical lines
            cv2.line(frame, left_eye_points[0], left_eye_points[1], (0, 255, 255), 2)
            cv2.line(frame, left_eye_points[2], left_eye_points[3], (0, 255, 255), 2)

            # Right eye, horizontal and vertical lines
            cv2.line(frame, right_eye_points[0], right_eye_points[1], (0, 255, 255), 2)
            cv2.line(frame, right_eye_points[2], right_eye_points[3], (0, 255, 255), 2)

        cv2.imshow('Camera', frame)

        key = cv2.waitKey(1)
        if key == 27:
            break


if __name__ == '__main__':
    open_camera = cv2.VideoCapture(0)

    detecting()

    open_camera.release()
    cv2.destroyAllWindows()
