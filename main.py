import cv2

def detecting():
    while True:
        _, frame = open_camera.read()

        cv2.imshow('Camera', frame)

        key = cv2.waitKey(1)
        if key == 27:
            break


if __name__ == '__main__':
    open_camera = cv2.VideoCapture(0)

    detecting()

    open_camera.release()
    cv2.destroyAllWindows()
