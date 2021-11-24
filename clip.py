import cv2
from PIL import Image, ImageTk
class Clip:
    def __init__(self):
        self.video_stack = []
        self.vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    def startCam(self):
        while True:

            _ , frame = self.vid.read()
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            cv2.imshow("index", frame)
            if cv2.waitKey(1) &0XFF == ord('x'):
                self.vid.release()
                break
        #img = Image.fromarray(cv2image)
        #imgtk = ImageTk.PhotoImage(image = img)
        #return imgtk

    @staticmethod
    def stopCam():
        cv2.destroyAllWindows()

clip = Clip()
clip.startCam()