import cv2
import tkinter as tk
from PIL import Image, ImageTk

vid = cv2.VideoCapture(0)
if not vid.isOpened():
    raise ValueError("Unable to open video source", 0)
root = tk.Tk()


out = cv2.VideoWriter("sample.mp4",cv2.VideoWriter_fourcc(*'H264'),10,(640, 480))
canvas = tk.Canvas(root, height=480, width=640)
canvas.pack()


def x():
    ret, frame = vid.read()
    if ret:
        out.write(cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
        photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
        root.one = photo
        canvas.create_image(0, 0, image = photo, anchor = tk.NW)
    root.after(100, x)
    
    

# When everything done, release the capture
x()
root.mainloop()
vid.release()
cv2.destroyAllWindows()
