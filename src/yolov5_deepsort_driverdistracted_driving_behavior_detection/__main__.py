### Test Usage
if __name__ == '__main__':
    import yolov5_deepsort_driverdistracted_driving_behavior_detection.myframe as myframe
    import cv2
    import sys

    cam = cv2.VideoCapture(0)
    ok, frame = cam.read()
    if not ok:
        print("Failed to read camera")
        sys.exit(1)

    ret, frame_annot = myframe.frametest(frame)
    print((ret, frame_annot))
