import tkinter as tk
from clip import Clip
import cv2
from PIL import Image, ImageTk


class GUI:
    def __init__(self, master, clip):
        self.clip = clip
        self.master = master
        self.canvas = tk.Canvas(self.master, height=720, width=1280)
        self.canvas.pack()

        self.toolbar = tk.Frame(self.master, bg="gray")
        self.toolbar.place(relwidth=1, relheight=0.1, rely=0.9)

        self.stopPhoto = tk.PhotoImage(file="icons8-stop-30.png")
        self.stopBtn = tk.Button(self.toolbar, image=self.stopPhoto, bg="gray")
        self.stopBtn.image = self.stopPhoto
        self.stopBtn.place(relx = 0.5, rely = 0.1)

        self.recPhoto = tk.PhotoImage(file="icons8-record-30.png")
        self.recBtn = tk.Button(self.toolbar, image=self.recPhoto, bg="gray")
        self.recBtn.image = self.recPhoto
        self.recBtn.place(relx = 0.4, rely = 0.1)

        self.shotPhoto = tk.PhotoImage(file="icons8-screenshot-30.png")
        self.shotBtn = tk.Button(self.toolbar, image=self.shotPhoto, bg="gray")
        self.shotBtn.image = self.shotPhoto
        self.shotBtn.place(relx = 0.6, rely = 0.1)

        self.savePhoto = tk.PhotoImage(file="icons8-save-30.png")
        self.saveBtn = tk.Button(self.toolbar, image=self.savePhoto, bg="gray")
        self.saveBtn.image = self.savePhoto
        self.saveBtn.place(relx = 0.01, rely = 0.1)

        self.updateImage()
        self.master.mainloop()
        

    def updateImage(self):
        frame, format = self.clip.startCam()
        
        format.write(cv2.cvtColor(frame,cv2.COLOR_RGB2BGR))
        photo = ImageTk.PhotoImage(image = Image.fromarray(frame))
        self.master.one = photo
        self.canvas.create_image(0, 0, image = photo, anchor = tk.NW)
        self.master.after(100, self.updateImage)
            
        
     
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Webcam Recorder")
    clip = Clip()
    main_gui = GUI(root, clip)
    
    clip.__del__()
    


    

