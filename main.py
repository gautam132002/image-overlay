# code to overlay images over videos

import cv2
import numpy as np
import os
from PIL import Image, ImageDraw, ImageFilter

import time

###################################################################################################################################################

def deleting_temps():
    l = os.listdir("frame")
    print("deleting temp frames...")
    for i in l:
        file = f"frame/{i}"
        os.remove(file)

    
    print("deleting temp video...")
    os.remove("op.avi")




def calc_fps(ip_file):
    ip_file = f"inp/{ip_file}"
    cap = cv2.VideoCapture(ip_file)

    fps = cap.get(cv2.CAP_PROP_FPS) 
    no_of_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    return ((fps, no_of_frame)) 
    
 
def ext_frames(vid):

    cap = cv2.VideoCapture(f"inp/{vid}")
    suc,frame = cap.read()
    frameid = 0
    while suc:
      cv2.imwrite("frame/%d.jpg" % frameid, frame)   
      suc,frame = cap.read()
      frameid += 1

def render_frames(inp_img,x,y):
    list_of_frames = os.listdir("frame")
    for i in list_of_frames:
        
        frame = Image.open(f"frame/{i}")
        img = Image.open(f"img/{inp_img}")
        frame.paste(img, (x, y))
        frame.save(f"frame/{i}", quality=95)

def con2video(f):
    frame_dir = 'frame' 
    video_name = 'op.avi'
   
	
    images = [img for img in os.listdir(frame_dir)if img.endswith(".jpg") or img.endswith(".jpeg") or img.endswith("png")]
    frame = cv2.imread(os.path.join(frame_dir, images[0]))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, 0, f, (width, height))
    for image in images:
        video.write(cv2.imread(os.path.join(frame_dir, image)))
	

    cv2.destroyAllWindows()
    video.release()
    

def cvn2mp4():
    os.popen("ffmpeg -i 'op.avi' -ac 2 -b:v 2000k -c:a aac -c:v libx264 -b:a 160k -vprofile high -bf 0 -strict experimental -f mp4 'out/result.mp4'")
    return True




##################################################################################################################################################################


if __name__ == "__main__":
    print ("""                                        
 █ █▀▄▀█ █▀▀ █▀█ █░█ █▀▀ █▀█ █░░ ▄▀█ █▄█
 █ █░▀░█ █▄█ █▄█ ▀▄▀ ██▄ █▀▄ █▄▄ █▀█ ░█░
 """)

    temp = 0
    while temp == 0:
        print("press 1 to start and press 0 to stop")
        ip = int(input("@ "))
        if ip == 0:
            temp = 1
        else:
            try:
            
                print("keep video file in inp folder")
                print("enter file name.")
                inp_file_name = input("@ ")
                
                fps,frames = calc_fps(inp_file_name)
                
                print(f"current fps = {fps} and no of frames = {frames}")

                chose = input("do you want to change the fps [y/n] : ")
                chose = chose.upper()
                if chose == "Y":
                    fps = float(input("enter fps @ "))
                    fps = int(fps)
                else:
                    pass
                print("got it...")
                print()
                print("keep overlaying image in img folder.")
                print("enter img name")
                img_name = input("@ ")
                
                print("enter coordinates")
                x = float(input("x coord @ "))
                y = float(input("y coord @ "))

                x = int(x)
                y = int(y)
                print()

                print("initializing...")

                start_time = time.time()

                ## exporting video frames...

                print("exporting video frames...")
                ext_frames(inp_file_name)
                print("sucess...")

                print()

                #rendering image to each frame

                print("rendering frames...")
                render_frames(img_name,x,y)
                print("sucess...")
                print()

                #rendering vedio

                print(f"rendering vedio {(fps)} fps ...")
                con2video(fps)
                cvn2mp4()
                
                print("done video is ready in out folder")
                print()

                #deleting temperory file
                print("do yu wnat to delete temp files ?[y/n]")
                c = input("@ ")
                c = c.upper()
                if c == "Y":
                    

                    print("deleting temp file please donot exit the process...")
                    deleting_temps()
                    print("done you can exit now :)")
                    print()
                    

                else:
                    print("its recomended to delete all temp files..")
                    print("they may cause errors in future processes..")
                    print()
            except:
                print("somethig went wrong...")
                print("check your inputs")
                print("or contact mail => gautamnegi0202@gmail.com")

            print("execution time = %s seconds" %(time.time() - start_time))
            print()
            print("-"*50)
            print()
                
            
             
            

            
            
            
            
            

            
            
            





























        
    
