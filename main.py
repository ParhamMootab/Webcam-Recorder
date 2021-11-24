import tkinter as tk
from clip import Clip
import cv2
clip = Clip()
class GUI:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, height=700, width=1000)
        self.canvas.pack()

        self.label = tk.Label(self.master)
        self.label.place(relwidth=1, relheight=0.9)

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

    def updateImage(self):
        vid = clip.startCam()
        print(type(vid))
        self.label = tk.Label(self.master, image=vid)
        self.label.image = vid
        self.label.place(relwidth=1, relheight=0.9)
        self.label.after(10, self.updateImage())
     
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Webcam Recorder")
    main_gui = GUI(root)
    root.mainloop()
    Clip.stopCam()
    


    

