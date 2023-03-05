import cv2
import dlib
import numpy as np
from eyes_functions import (
    eye_center_points,
    blinking_ratio,
    eye_region,
)
from constants import (
    LEFT_EYE_POINTS,
    RIGHT_EYE_POINTS,
    BLINK_RATIO,
)


def detecting():
    face_detector = dlib.get_frontal_face_detector()
    points_predictor = dlib.shape_predictor('landmark/shape_predictor_68_face_landmarks.dat')

    while True:
        _, frame = open_camera.read()
        height, width, _ = frame.shape

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        mask_frame = np.zeros((height, width), np.uint8)

        faces = face_detector(gray_frame)
        for face in faces:
            eye_points_mask = points_predictor(gray_frame, face)

            left_eye_region = eye_region(eye_points_mask, LEFT_EYE_POINTS)
            right_eye_region = eye_region(eye_points_mask, RIGHT_EYE_POINTS)

            left_eye_points = eye_center_points(eye_points_mask, LEFT_EYE_POINTS)
            right_eye_points = eye_center_points(eye_points_mask, RIGHT_EYE_POINTS)

            # Left eye, horizontal and vertical lines
            cv2.line(frame, left_eye_points[0], left_eye_points[1], (0, 255, 255), 2)
            cv2.line(frame, left_eye_points[2], left_eye_points[3], (0, 255, 255), 2)

            # Right eye, horizontal and vertical lines
            cv2.line(frame, right_eye_points[0], right_eye_points[1], (0, 255, 255), 2)
            cv2.line(frame, right_eye_points[2], right_eye_points[3], (0, 255, 255), 2)

            left_eye_ratio = blinking_ratio(left_eye_points)
            right_eye_ratio = blinking_ratio(right_eye_points)
            eyes_blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2

            if eyes_blinking_ratio > BLINK_RATIO:
                cv2.putText(frame, 'Blink hard', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 3, (255), 2)
            
            cv2.polylines(mask_frame, [left_eye_region], True, 255, 2)
            cv2.fillPoly(mask_frame, [left_eye_region], 255)
            cv2.polylines(mask_frame, [right_eye_region], True, 255, 2)
            cv2.fillPoly(mask_frame, [right_eye_region], 255)

            eyes_frame = cv2.bitwise_and(gray_frame, gray_frame, mask=mask_frame)
            cv2.imshow('Eyes', eyes_frame)

        cv2.imshow('Camera', frame)

        key = cv2.waitKey(1)
        if key == 27:
            break


if __name__ == '__main__':
    open_camera = cv2.VideoCapture(0)

    detecting()

    open_camera.release()
    cv2.destroyAllWindows()
