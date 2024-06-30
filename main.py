import tkinter
import cv2  # pip install opencv-python
import PIL.Image, PIL.ImageTk# pip install pillow, The Python Imaging Library adds image processing capabilities to your Python interpreter.
from functools import partial
import threading
import time
import imutils

# function creation
video_name = input("Enter your 'mp4' video file: \n")
stream = cv2.VideoCapture(video_name)
flag = True
def play(speed):
   global flag
   print(f"You clicked on play. speed is {speed}")

   # play the video in reverse
   frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
   stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)

   grabbed, frame = stream.read()
   if not grabbed:
      exit()
   frame = imutils.resize(frame, width = SET_WIDTH, height = SET_HEIGHT)
   frame = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
   canvas.image = frame
   canvas.create_image(0, 0, image = frame, anchor= tkinter.NW)
   if flag:
      canvas.create_text(134, 26, fill="green", font="Times 26 bold", text="Decision Pending")
   flag= not flag

def pending(decision):
   # 1. display decision pending image
   frame = cv2.cvtColor(cv2.imread("decision_pending2.png"), cv2.COLOR_BGR2RGB) # cv2.cvtColor() method is used to convert an image from one color space to another
   frame = imutils.resize(frame, width=SET_WIDTH, height = SET_HEIGHT)
   frame =  PIL.ImageTk.PhotoImage(image =PIL.Image.fromarray(frame))
   canvas.image = frame
   canvas.create_image(0, 0, image= frame, anchor=tkinter.NW)
   # 2. Wait for a second
   time.sleep(2)
   # 3. Display sponser image
   frame = cv2.cvtColor(cv2.imread("sponser1.png"), cv2.COLOR_BGR2RGB) # cv2.imread() method loads an image from the specified file.
   frame = imutils.resize(frame, width=SET_WIDTH, height = SET_HEIGHT) # imutils.resie() is used to resize an image
   frame =  PIL.ImageTk.PhotoImage(image =PIL.Image.fromarray(frame))
   canvas.image = frame
   canvas.create_image(0, 0, image= frame, anchor=tkinter.NW)
   # 4. wait for 1.5 second
   time.sleep(2)
   # 5. Display out/notout image
   if decision == 'out':
      decision_img= 'out2.png'
   elif decision == 'not out':
      decision_img = 'not_out.png'
   frame = cv2.cvtColor(cv2.imread(decision_img), cv2.COLOR_BGR2RGB)
   frame = imutils.resize(frame, width=SET_WIDTH, height = SET_HEIGHT)
   frame =  PIL.ImageTk.PhotoImage(image =PIL.Image.fromarray(frame))
   canvas.image = frame
   canvas.create_image(0, 0, image= frame, anchor=tkinter.NW)

def out():
   thread = threading.Thread(target=pending, args=("out",))
   thread.daemon = 1
   thread.start()
   print("player is out")

def notout():
   thread = threading.Thread(target=pending, args=("not out",)) # .Thread() Returns a thread object that can run a function with zero or more arguments.
   thread.daemon = 1 # The Daemon Thread does not block the main thread from exiting and continues to run in the background
   thread.start()
   print("player is not out")

#width and height of our screen
SET_WIDTH = 650
SET_HEIGHT = 368

# tkinter gui stsrt here
window = tkinter.Tk()
window.title("Sourav;s Third Umpire decision Review system")
cv_img = cv2.cvtColor(cv2.imread("welcome1.png"),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH, height =SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor = tkinter.NW, image= photo) #tkinter.NW set the image at top left corner
canvas.pack()

# Buttons to control playback
btn = tkinter.Button(window, text="<< previous (fast)", width = 50, command= partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<< previous (slow)", width=50, command= partial(play, -5))
btn.pack()

btn = tkinter.Button(window, text="<< previous (very slow)", width=50, command= partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text="Next (very slow) >>", width =50, command=partial(play, 1))
btn.pack()

btn = tkinter.Button(window, text="Next (slow) >>", width=50, command=partial(play, 3))
btn.pack()

btn = tkinter.Button(window, text="Next (fast) >>", width =50, command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text="Give Out", width = 50, command=out)
btn.pack()

btn = tkinter.Button(window, text="Give Not Out", width = 50, command = notout)
btn.pack() # Python | pack() method is used to Pack geometry manager packs widgets relative to the earlier widget.
window.mainloop() # window.mainloop() tells Python to run the Tkinter event loop. 