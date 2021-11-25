import cv2
class Clip:
    def __init__(self):
        self.video_stack = []
        self.vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.format = cv2.VideoWriter("sample.avi",cv2.VideoWriter_fourcc(*'XVID'),10,(1280, 720))
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", 0)

    def startCam(self):
        ret , frame = self.vid.read()
        if ret:
            return (frame, self.format)

    
    def __del__(self):
        self.vid.release()
        cv2.destroyAllWindows()
