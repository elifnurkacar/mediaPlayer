from tkinter import *
import tkinter
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
import tkinter as tk, threading
import cv2
from tkinter import filedialog
import time
import numpy as np
import sys
from threading import Lock
import threading
from threading import Thread
selected_image = None
path = None
s_row = None
e_row = None
s_col = None
e_col = None
send_button = None
cropped = None
clip_img = None
rotate_im = None
angle = 0
new_size = None
panel = None

panelC = None
panelB = None

cap = None
frame = None
path2 = None
out = None
panelD = None

d = None

openImage = None
cut = None
rotate = None
back = None

buttonImage = None
buttonVideo = None
buttonQuit = None
mainWindow = None

cut_video = None
thread4=None
##save counts##
i = 0
j = 0

video_frame=None

my_label = None
save = None

open = None
stop = None

frame2 = None

s_frame = None
e_frame = None
send_frames = None

condition = 1

crop_img = None

zoom_in = None
zoom_out = None
x = 0
y = 0
fourcc = None

currentFrame = 0
count2 = 0
a = 0

temp_crop = 0
temp_pause = 0
temp_play = 0

rect = None
start_x = None
start_y = None

curX=None
curY=None
canvas=None
screen_count=0

ileri=None

forward_count=0
ileri_sayac=0
back_count=0
geri_sayac=0

lenght=0
slider_con=False

start_frame=0
end_frame=0

_frame=0
crop_img=None
name=None
asd=False
cap_crop=None
w1=None
label=None
ileri_s=0
thread=None
thread2=None
thread3=None
thread4=None

count_thread4=0
geri=0
count=0
thread_stop=0
lock=None
w1=None
WINDOW_WİDTH=800
WINDOW_HEIGHT=600

RESIZE_WIDHT=800
RESIZE_HEIGHT=450
array = []
class medya:

    def __init__(self, selected_image, path,  cropped,start_x,start_y, clip_img, rotated, new_size,canvas):
        self.new_size = new_size
        self.selected_image = selected_image
        self.path = path
        self.cropped = cropped
        self.clip_img = clip_img
        self.rotated = rotated
        self.start_x=start_x
        self.start_y=start_y
        self.canvas=canvas

    def __set__(self, selected_image):
        self.selected_image = selected_image
    def __set__(self, canvas):
        self.canvas = canvas
    def __set__(self, clip_img):
        self.clip_img = clip_img

    def __set__(self, path):
        self.path = path

    def __set__(self, cropped):
        self.cropped = cropped

    def __set__(self, s_row):
        self.s_row = s_row

    def __set__(self, e_row):
        self.e_row = e_row

    def __set__(self, s_col):
        self.s_col = s_col

    def __set__(self, e_col):
        self.e_col = e_col

    def show_image(self):
        global selected_image, panelC,screen_count,path
        if screen_count==0:

                path = filedialog.askopenfilename(title = "Select file",filetypes = (("jpeg files","*.jpg"),
                                                                                     ("all files","*.png")))
                if path is not None:
                  self.selected_image = Image.open(path)

                  self.selected_image = self.selected_image.resize((680, 530))
                  self.tk_im = ImageTk.PhotoImage(self.selected_image)


                  self.canvas.create_image(0, 0, anchor="nw", image=self.tk_im)
                  screen_count=1
        elif screen_count==1:

                path = filedialog.askopenfilename()
                self.selected_image = Image.open(path)
                self.selected_image = self.selected_image.resize((680, 530))
                self.canvas.destroy()

                self.canvas = Canvas(mainWindow)
                self.canvas.config(cursor='cross',bg='silver')
                self.canvas.pack(padx=0, pady=0, ipadx=100, ipady=130)

                self.tk_im = ImageTk.PhotoImage(self.selected_image)
                self.canvas.create_image(0, 0, anchor="nw", image=self.tk_im)


    def save_inf(self):
        self.save_img = Tk()
        self.save_img.title("Clip information")
        self.save_img.geometry("300x200")
        self.save_img.configure(background="grey")

        LABEL_ROW1 = Label(self.save_img, text='File Name', bg="dark gray")
        LABEL_ROW1.grid(row=2)
        self.name_c = Entry(self.save_img, width=20)
        self.name_c.grid(row=2, column=1)

        self.send_name = Button(self.save_img, text="Send", bg="darkgray", command=self.save_image)
        self.send_name.grid(row=4, column=1)
    def save_image(self):
        global panelB, cropped, selected_image, i, j, rotate_im,curX,curY,rect
        name=self.name_c.get()
        self.save_img.destroy()
        if cropped is not None:
            self.canvas.delete(rect)
            self.cropped = self.selected_image.crop((self.start_x, self.start_y, curX, curY))
            self.cropped.save("%s.jpg"%name)
            messagebox.showinfo("  ", "Image is saved :)")
            cropped=0
        if rotate_im == 1:

            #self.rotate_img.destroy()
            self.selected_image = Image.open(path)
            self.rotated = self.selected_image.rotate(self.angle)
            #self.new_size = self.rotated.resize((300, 290), Image.NEAREST)
            self.rotated.save("%s.jpg" % name)
            rotate_im=0

    def on_button_press(self, event):

        global rect,cropped
        if rect is not None:
              self.canvas.delete(rect)
        if cropped == 1:
              self.start_x = event.x
              self.start_y = event.y

              rect = self.canvas.create_rectangle(self.start_x, self.start_y, 1, 1)
              print(self.start_x,self.start_y)
    def on_move_press(self, event):
        global rect,curX,curY,cropped
        if cropped ==1:
           curX, curY = (event.x, event.y)

           self.canvas.coords(rect, self.start_x, self.start_y, curX, curY)
    def on_button_release(self, event):
        global curX,curY,selected_image,cropped,rect,path

        #self.canvas.delete(rect)
        #self.save_inf()
        #self.canvas.delete(rect)
        pass
    def clip(self):
        global mainWindow,cropped,rect
        cropped = 1
        if rect is not None:
               self.canvas.delete(rect)
        rotate_im=0
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
    def rotate(self):
        count = 0
        global selected_image, angle, rotate_im, new_size,cropped
        cropped = 0
        rotate_im = 1
        #self.angle_in.destroy()
        self.selected_image = Image.open(path)
        self.selected_image = self.selected_image.resize((680, 500))
        self.angle = int(self.angle_in.get())

        self.rotated = self.selected_image.rotate(self.angle)




        self.im = ImageTk.PhotoImage(self.rotated)
        self.can.create_image(0, 0,anchor="nw" , image=self.im)


        if self.name_rtimg.get() is not None:
            self.rotated.save("%s.jpg"%self.name_rtimg.get())
            messagebox.showinfo("  ","Rotated image is saved :)")
    def rotate_inf(self):

        self.rotate_img = tk.Toplevel()
        self.rotate_img.title("Rotate information")
        self.rotate_img.geometry("800x600+200+50")
        self.rotate_img.configure(background="silver")


        image17 = Image.open("picture-02.png")
        photo17 = ImageTk.PhotoImage(image17)
        self.can = Canvas(self.rotate_img)
        self.can.config(cursor='cross', bg='silver')
        self.can.grid(row=0,column=0,ipadx=130,ipady=100)
        #self.can.create_image(310, 250, anchor="nw", image=photo17)

        LABEL_COL2 = Label(self.rotate_img, text='Angle', bg="silver")
        LABEL_COL2.grid(row=1,column=0)
        self.angle_in = Entry(self.rotate_img, width=20)
        self.angle_in.grid(row=2, column=0)

        LABEL_ROW3 = Label(self.rotate_img, text='File Name', bg="silver")
        LABEL_ROW3.grid(row=3,column=0)
        self.name_rtimg = Entry(self.rotate_img, width=20)
        self.name_rtimg.grid(row=4, column=0)

        self.send_angle = Button(self.rotate_img, text="Send", bg="silver", command=self.rotate)
        self.send_angle.grid(row=5, column=0)
def nothing(x):
    pass
c1 = medya(selected_image, path, cropped, clip_img, rotate_im, new_size,canvas,start_x,start_y,)
def image():
    global buttonQuit, buttonVideo, buttonImage, mainWindow, zoom_out, zoom_in, openImage, cut, rotate, back, save
    mainWindow.title('IMAGE VIEWER')
    mainWindow.configure(bg='white')
    buttonImage.destroy()
    buttonVideo.destroy()

    image17 = Image.open("picture-02.png")
    photo17 = ImageTk.PhotoImage(image17)
    c1.canvas = Canvas(mainWindow)
    c1.canvas.config(cursor='cross', bg='silver')
    c1.canvas.pack(padx=0, pady=0, ipadx=150, ipady=130)
    c1.canvas.create_image(310, 250, anchor="nw", image=photo17)

    image12 = Image.open("back_mavi.png")
    photo12 = ImageTk.PhotoImage(image12)
    back = Button(mainWindow, image=photo12,border=0, command=BackMain, bg="white")
    back.image=photo12
    back.place(relx=0.0, rely=0.9, relheight=0.1, relwidth=0.1)


    image13 = Image.open("open_mavi.png")
    photo13 = ImageTk.PhotoImage(image13)
    openImage = Button(mainWindow, image=photo13,border=0, command=c1.show_image, bg="white")
    openImage.image=photo13
    openImage.place(relx=0.1, rely=0.9, relheight=0.1, relwidth=0.1)

    image14 = Image.open("Cut.png")
    photo14 = ImageTk.PhotoImage(image14)
    cut = Button(mainWindow, image=photo14,border=0, command=c1.clip, bg="white")
    cut.image=photo14
    cut.place(relx=0.2, rely=0.9, relheight=0.1, relwidth=0.1)

    image15 = Image.open("rotate_ccw.png")
    photo15 = ImageTk.PhotoImage(image15)
    rotate = Button(mainWindow, image=photo15,border=0, command=c1.rotate_inf, bg="white")
    rotate.image=photo15
    rotate.place(relx=0.3, rely=0.9, relheight=0.1, relwidth=0.1)

    image16 = Image.open("save__.png")
    photo16 = ImageTk.PhotoImage(image16)
    save = Button(mainWindow, image=photo16,border=0, command=c1.save_inf, bg="white")
    save.image=photo16
    save.place(relx=0.4, rely=0.9, relheight=0.1, relwidth=0.1)

    mainWindow.mainloop()
class video:
    def __init__(self, cap, path2, frame, frame2,name,w1 ,image):
        self.cap = cap;
        self.path2 = path2
        self.frame = frame
        self.frame2 = frame2
        self.name=name
        self.w1=w1
        self.image=image
    def __set__(self, cap):
        self.cap = cap
    def __set__(self, fourcc):
        self.fourcc = fourcc
    def __set__(self, path2):
        self.path2 = path2
    def __set__(self, frame):
        self.frame = frame

    def crop_inf(self):
        global crop_img

        crop_img = Tk()
        crop_img.title("Clip information")
        crop_img.geometry("300x200")
        crop_img.configure(background="silver")
        LABEL_ROW3 = Label(crop_img, text='File Name', bg="silver")
        LABEL_ROW3.grid(row=3)
        self.name = Entry(crop_img, width=20)
        self.name.grid(row=3, column=1)
        send_frames = Button(crop_img, text="Send", bg="silver", command=self.crop_video)
        send_frames.grid(row=5, column=1)
        return True
    def crop_video(self):

        global cap,crop_img, frame,_frame, out, e_frame, s_frame, crop_img, a, temp_crop, my_label,slider_con,asd,cap_crop,crop_image,temp_pause
        slider_con=False
        if _frame==0:#######start
            _frame=1
            slider_con=0
            self.start =self.w1.get()
            messagebox.showinfo("  ", "Start Frame is saved :)")
        elif _frame==1:#########end
            _frame=2
            self.finish = self.w1.get()
            messagebox.showinfo("  ", "End Frame is saved :)")
        elif  _frame==2:
            if crop_img is not None:
                    print('herererere')
                    a=0
                    self.filename = self.name.get()
                    crop_img.destroy()
                    cap_crop = cv2.VideoCapture(path2)
                    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
                    width = cap_crop.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
                    height = cap_crop.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float
                    out = cv2.VideoWriter('%s.avi' % self.filename, fourcc, 20.0, (int(width), int(height)))
                    print(self.start, self.finish)
                    while 1:
                        ret, crop_image = cap_crop.read()
                        if int(a) >= self.start and int(a) < self.finish:
                            out.write( crop_image)

                        elif int(a)==self.finish :
                            messagebox.showinfo("  ", "Cutted Video is saved :)")
                            break
                        a = a + 1
                    _frame=0
                    cap_crop= cv2.VideoCapture('%s.avi' % self.filename)

                    while (cap_crop.isOpened()):
                        ret, frame = cap_crop.read()
                        cv2.imshow('frame', frame)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            #temp_pause=0
                            break
                    #temp_pause=1
                    #self.stream(my_label)
                    out.release()

        print('_frame=%d'%_frame)
    def send_name(self):

        name_img = Tk()
        name_img.title("Clip information")
        name_img.geometry("200x100")
        name_img.configure(background="dark gray")

        LABEL_ROW1 = Label(name_img, text='File Name', bg="dark gray")
        LABEL_ROW1.grid(row=0)
        name = Entry(name_img, width=20)
        name.grid(row=0, column=1)

        send_name = Button(name_img, text="Send", bg="dark gray", command=self.crop_video)
        send_name.grid(row=2, column=1)
    def crop_information(self):
        global e_frame, s_frame, send_frames, crop_img
        crop_img = Tk()
        crop_img.title("Clip information")
        crop_img.geometry("300x200")
        crop_img.configure(background="silver")

        LABEL_ROW1 = Label(crop_img, text='Start Frame', bg="silver")
        LABEL_ROW1.grid(row=0)
        s_frame = Entry(crop_img, width=20)
        s_frame.grid(row=0, column=1)

        LABEL_ROW2 = Label(crop_img, text='End Frame', bg="silver")
        LABEL_ROW2.grid(row=1)
        e_frame = Entry(crop_img, width=20)
        e_frame.grid(row=1, column=1)

        LABEL_ROW3 = Label(crop_img, text='File Name', bg="silver")
        LABEL_ROW3.grid(row=3)
        self.name = Entry(crop_img, width=20)
        self.name.grid(row=3, column=1)

        send_frames = Button(crop_img, text="Send", bg="silver", command=self.crop_video)
        send_frames.grid(row=5, column=1)
    def forward(self):
        global forward_count,ileri_sayac
        forward_count=1
        ileri_sayac=250
    def nothing(SELF,*arg):
        pass
    def show(self,label):
        global path2,count,frame_image

        time.sleep(0.009)
        img = cv2.resize(self.image, (800,450), interpolation=cv2.INTER_LINEAR)
        frame_image = ImageTk.PhotoImage(Image.fromarray(img))

        label.config(image=frame_image)
        label.image = frame_image
    def read_frames(self):
        global thread4,i
        #self.lock=threading.Lock()
        #self.lock.acquire()
        for self.image in self.cap.iter_data():
             img = cv2.resize(self.image, (800, 450), interpolation=cv2.INTER_LINEAR)
             self.array[i]=img
             i+=1
        #self.lock.release()
    def stream(self, label):
        global path2, temp_pause, temp_play, a,mainWindow,ileri_sayac,image,back_count,geri_sayac
        global forward_count,lenght,slider_con,thread_stop,geri,ileri_s,lock,i,cap,count_thread4,thread2,count,video_frame
        #count=0
       # i=0
        self.array=[]
        if temp_crop == 0:
            #for self.image in self.cap.iter_data():
            while cap.isOpened():
                if count_thread4 == 0:  # okuma
                    if temp_pause == 0:
                        ret, video_frame = cap.read()
                        count_thread4 = 1
                    elif temp_pause == 1:
                        ret, video_frame = cap.read()
                if temp_pause is not 1:
                     if forward_count == 0:
                           if count ==self.w1.get():
                                      img = cv2.resize(video_frame, (800, 450))
                                      rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                                      frame_image = ImageTk.PhotoImage(Image.fromarray(rgb))
                                      my_label.config(image=frame_image)
                                      my_label.image = frame_image
                                      count+=1
                                      self.w1.set(count)
                           elif count<self.w1.get():
                                count+=1
                           elif count>self.w1.get():#geriye alma
                               count=0
                               self.stream(my_label)
                     elif forward_count == 1:
                         ileri_sayac -= 1
                         if ileri_sayac==0:
                            forward_count=0
                            self.w1.set(count+250)
                elif temp_pause == 1:
                     slider_con==False
                     while True:
                         if temp_play == 1:
                                 temp_play = 0
                                 temp_pause = 0
                                 break
                         if slider_con:
                             if count < self.w1.get():
                                 time.sleep(0.01)
                                 count += 1
                                 print('count küçüktür=%d'%count)
                                 break
                             elif count > self.w1.get():
                                 # geriye alma
                                 time.sleep(0.00001)
                                 geri=1
                                 count = 0
                                 break
                             elif count==self.w1.get():
                                 geri = 0
                                 break
        self.w1.set(0)
        self.stream(label)
    def slider(self,a):
        global slider_con,frame_image,label,thread2,thread,count_thread4,lock,thread_stop,video_frame
        slider_con=True
        if temp_pause==1:
            img = cv2.resize(video_frame, (800, 450))
            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            frame_image = ImageTk.PhotoImage(Image.fromarray(rgb))
            my_label.config(image=frame_image)
            my_label.image = frame_image
    def show_video(self):
        global  path2, frame, len , s_frame, e_frame, panel,cap, fourcc, condition, currentFrame, count2, out,my_label,temp_play,lock,thread2,array,w1
        if self.w1 is not None:
            self.w1.destroy()
        path2 = filedialog.askopenfilename(title="Select file",
                                 filetypes=(("all files", "*.avi"), ("mp4 files", "*.mp4")))
        if my_label is not None:
            my_label.destroy()
            my_label = tk.Label(mainWindow)
            my_label.pack(side="top")
            temp_play = 1
        len = 0
        #cap = imageio.get_reader(path2)
        cap=cv2.VideoCapture(path2)
        len = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        #len=cap._meta['nframes']
        print(len)
        w1=Scale(mainWindow,from_=0,to=len,orient=HORIZONTAL,length=800,fg='black')
        w1.config(command=self.slider)
        w1.pack()
        thread = MyThread()
        thread.start()
        array.append(thread)
        time.sleep(0.009)
    def pause(self):
        global temp_pause,temp_play,thread_stop
        thread_stop=1
        temp_pause = 1
        temp_play=0
    def play(self):
        global temp_play,temp_pause,slider_con,thread_stop
        thread_stop=0
        temp_play = 1
        temp_pause=0
        slider_con=True
c3 = video(cap, path2, frame, frame2,name,w1,image )
class MyThread(Thread):
    def run(self):
        global path2, temp_pause, temp_play, a, mainWindow, ileri_sayac, image, back_count, geri_sayac,video_frame
        global forward_count, lenght, slider_con, thread_stop, geri, ileri_s, lock, i, cap, count_thread4, thread2, count,array,w1
        if temp_crop == 0:
            while cap.isOpened():
                ret, video_frame = cap.read()
                if temp_pause == 0:
                    if forward_count == 0:
                        if count == w1.get():
                            img = cv2.resize(video_frame, (800, 450))
                            rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                            frame_image = ImageTk.PhotoImage(Image.fromarray(rgb))
                            my_label.config(image=frame_image)
                            my_label.image = frame_image
                            count += 1
                            w1.set(count)
                        elif count < w1.get():
                            print(count)
                            count += 1
                        elif count > w1.get():  # geriye alma
                            count = 0
                            break
                    elif forward_count == 1:
                        ileri_sayac -= 1
                        if ileri_sayac == 0:
                            forward_count = 0
                            w1.set(count + 250)
                elif temp_pause == 1:
                    slider_con == False
                    while True:
                        if temp_play == 1:
                            temp_play = 0
                            temp_pause = 0
                            break
                        if slider_con:
                            if count < w1.get():
                                count += 1
                                print('count küçüktür=%d' % count)
                                break
                            elif count > w1.get():
                                # geriye alma
                                geri = 1
                                count = 0
                                break
play=None
pause=None
cut_video=None
c2 = video(cap, path2, frame, frame2,name,w1,image )
save_video=None
def video_main():
    global cap, path2, mainWindow, my_label,save_video,lock
    global buttonQuit, buttonVideo, buttonImage, mainWindow,play,cut_video,pause,ileri,open,back
    mainWindow.title('VIDEO PLAYER')
    mainWindow.configure(bg="white")

    buttonImage.destroy()
    buttonVideo.destroy()
    #buttonQuit.destroy()

    image7 = Image.open("video-generic.png")
    photo7 = ImageTk.PhotoImage(image7)
    my_label = tk.Label(mainWindow,image=photo7,bg='silver')
    my_label.image=photo7
    my_label.pack(padx=0,pady=0,ipadx=700,ipady=220)

    image3 = Image.open("open_mavi.png")
    photo3 = ImageTk.PhotoImage(image3)

    open = Button(mainWindow,image=photo3,command=c2.show_video,border=0)
    open.image = photo3
    open["bg"] = "white"
    open.place(relx=0.3, rely=0.87, relheight=0.15, relwidth=0.1)



    image = Image.open("blue_play.png")
    photo = ImageTk.PhotoImage(image)
    play = Button(mainWindow,image=photo,command=c2.play,border=0)
    play.image = photo
    play["bg"] = "white"

    play.place(relx=0.4, rely=0.87, relheight=0.15, relwidth=0.1)

    image2 = Image.open("blue_stop.png")
    photo2 = ImageTk.PhotoImage(image2)
    pause = Button(mainWindow, image=photo2,text="Pause", bg="white",border=0, command=c2.pause)
    pause.image=photo2
    pause.place(relx=0.5, rely=0.87, relheight=0.15, relwidth=0.1)

    image4 = Image.open("Cut.png")
    photo4 = ImageTk.PhotoImage(image4)
    cut_video = Button(mainWindow,image=photo4, text="Cut", bg="white",border=0, command=c2.crop_video)
    cut_video.image = photo4
    cut_video.place(relx=0.60, rely=0.87, relheight=0.15, relwidth=0.1)

    image5 = Image.open("save__.png")
    photo5 = ImageTk.PhotoImage(image5)
    save_video = Button(mainWindow,image=photo5, text="Save",border=0, bg="white", command=c2.crop_inf)
    save_video.image=photo5
    save_video.place(relx=0.87, rely=0.87, relheight=0.15, relwidth=0.1)

    image6 = Image.open("back_mavi.png")
    photo6 = ImageTk.PhotoImage(image6)
    back = Button(mainWindow,image=photo6,border=0, text="Back to MainWindow", command=BackMain, bg="white")
    back.image = photo6
    back.place(relx=0.0, rely=0.87, relheight=0.15, relwidth=0.1)


    #ileri = Button(mainWindow, text="Forward", bg="grey",command=c2.forward)
    #ileri.place(relx=0.8, rely=0.81, relheight=0.09, relwidth=0.2)

    mainWindow.mainloop()
def clearScreen():
    global panelB, panelC, mainWindow,c1,geri,ileri,save_video ,openImage, cut, rotate, back, save, cut_video, zoom_out, zoom_in, my_label
    #m1=medya(selected_image, path,  cropped, clip_img, rotated, new_size,canvas,start_x,start_y,)
    if panelB is not None:
        panelB.destroy()
    if panelC is not None:
        panelC.destroy()
    if openImage is not None:
        openImage.destroy()
    if cut is not None:
        cut.destroy()
    if rotate is not None:
        rotate.destroy()
    if c2.w1 is not None:
        c2.w1.destroy()
    if save is not None:
        save.destroy()
    if open is not None:
        open.destroy()
    if cut_video is not None:
        cut_video.destroy()
    if back is not None:
        back.destroy()
    if zoom_in is not None:
        zoom_in.destroy()
    if zoom_out is not None:
        zoom_out.destroy()
    if my_label is not None:
        my_label.destroy()
    if c1.canvas is not None:
        c1.canvas.destroy()
    if ileri is not None:
        ileri.destroy()
    if play is not None:
        play.destroy()
    if pause is not None:
        pause.destroy()
    if cut_video is not None:
        cut_video.destroy()
    if save_video is not None:
        save_video.destroy()
    if w1 is not None:
        w1.destroy()
def BackMain():
    global buttonImage, buttonVideo, buttonQuit, mainWindow
    mainWindow.title('MEDIA PLAYER')
    mainWindow.configure(bg="white")

    clearScreen()

    image10 = Image.open("synfig_icon.png")
    photo10 = ImageTk.PhotoImage(image10)
    buttonImage = tkinter.Button(mainWindow, image=photo10, border=0, width=20, height=3, bg="white", command=image)
    buttonImage.image = photo10
    buttonImage.place(relx=0.2, rely=0.7, relheight=0.2, relwidth=0.3)

    image11 = Image.open("v-generic_big.png")
    photo11 = ImageTk.PhotoImage(image11)
    buttonVideo = tkinter.Button(mainWindow, image=photo11, border=0, width=20, height=3, bg="white",
                                 command=video_main)
    buttonVideo.image = photo11
    buttonVideo.place(relx=0.5, rely=0.7, relheight=0.2, relwidth=0.3)

    #buttonQuit = tkinter.Button(mainWindow, text="QUIT", bg="dark blue", command=quit)
    #buttonQuit.place(relx=0.7, rely=0.9, relheight=0.1, relwidth=0.3)

    mainWindow.mainloop()
def Main():
    global buttonImage, buttonVideo, buttonQuit, mainWindow

    mainWindow = tk.Tk()
    mainWindow.title("MEDIA PLAYER")
    mainWindow.configure(background="white")
    mainWindow.geometry("800x600+200+50")

    image10 = Image.open("synfig_icon.png")
    photo10 = ImageTk.PhotoImage(image10)
    buttonImage = tkinter.Button(mainWindow, image=photo10,border=0, width=20, height=3, bg="white", command=image)
    buttonImage.image=photo10
    buttonImage.place(relx=0.2, rely=0.7, relheight=0.2, relwidth=0.3)

    image11 = Image.open("v-generic_big.png")
    photo11 = ImageTk.PhotoImage(image11)
    buttonVideo = tkinter.Button(mainWindow, image=photo11,border=0, width=20, height=3, bg="white", command=video_main)
    buttonVideo.image=photo11
    buttonVideo.place(relx=0.5, rely=0.7, relheight=0.2, relwidth=0.3)

    #buttonQuit = tkinter.Button(mainWindow, text="QUIT", bg="dark blue", command=quit)
    #buttonQuit.place(relx=0.7, rely=0.9, relheight=0.1, relwidth=0.3)

    mainWindow.mainloop()
Main()