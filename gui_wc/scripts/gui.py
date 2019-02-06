#!/usr/bin/env python
import rospy	
import Tkinter as tk
from Tkinter import *
from gui_wc.msg import but
import tkMessageBox


simple_publisherf = rospy.Publisher('speed', but, queue_size = 10)#topic and message
rospy.init_node('gui', anonymous = True)#node name

ob=but()#object from message


top = tk.Tk()
speed=0
close_win=0


#buttons functions --------
def forward(): 
   global speed 
   if(speed <=0):
    speed=0
   speed+=1

def backward(): 

   global speed 
   if(speed >=0):
    speed=0
   speed-=1

def stop(): 
   global speed 
   speed=0


def close(): 
   global close_win 
   close_win=1
   
#end of buttons functions---------
       

top.geometry("300x300")
top.title("IWC GUI")
def helloCallBack():
 pass

#----------------------------------------
#write your gui
up= Button(top, text = "forward", command = forward)
up.place(x = 50,y = 50)

down= Button(top, text = "backward", command = backward)
down.place(x = 50,y = 150)

stop= Button(top, text = "stop", command = stop)
stop.place(x = 50,y = 100)

close= Button(top, text = "close", command = close)
close.place(x = 50,y = 200)
#---------------------------------------------

class Mainframe(tk.Frame):

    def __init__(self,master,*args,**kwargs):
 
        tk.Frame.__init__(self,master,*args,**kwargs)

        self.TimerInterval = 10
        self.refresh()
        
    def refresh(self):
        global speed
        ob.speed=speed
        helloCallBack()
        
        simple_publisherf.publish(ob)     
        #Now repeat call
        #the following "if" to close the program
        global close_win
        if(close_win==1):
         global top
         top.quit() 
         top.destroy()
        else:
         self.after(self.TimerInterval,self.refresh)
   
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        Mainframe(self).pack()
        self.mainloop()
                    
# create an App object
# it will run itself
App()

