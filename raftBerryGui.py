#raftBerryGui code to upgrade the previous version of the raftBerry
#
#Frame manager code derived from youtube user sentdex 
#Special thanks to reddit user novel_yet_trivial for helping with grid issues.



import Tkinter as tk
from Tkinter import *
from tkColorChooser import askcolor  
import subprocess


BUTTON_FONT=("Helvettica",20)
LARGE_FONT= ("Helvettica", 20)
VERSION="raftBerry v0.1"

class raftBerry(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
#        tk.Tk.iconbitmap(self,default='clienticon.ico')
        tk.Tk.wm_title(self, VERSION)
	self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
	container = tk.Frame(self)
	container.columnconfigure(0, weight=1)
	container.rowconfigure(0, weight=1)
	container.grid(row=0, column=0, sticky=N+S+E+W)

        self.frames = {}

        for F in (StartPage, NavPage, MapPage, LightPage, MultiPage, RocketPage, ExitPage):
        	frame = F(container, self)
        	self.frames[F] = frame
		frame.grid(row=0, column=0, sticky=N+S+E+W)
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
	for x in range(2):
		self.columnconfigure(x, weight=1)
	for y in range(4):
		self.rowconfigure(y, weight=1)
        
        label = tk.Label(self, text="raftBerry Menu", font=LARGE_FONT).grid(row=0, column=0, columnspan=2, sticky=N+S+E+W)
        Navbutton =tk.Button(self, text="Navigation", font=BUTTON_FONT, command=lambda: controller.show_frame(NavPage)).grid(row=1, column=0, sticky=N+S+E+W)
	Mapbutton =tk.Button(self, text="Map", font=BUTTON_FONT, command=lambda: controller.show_frame(MapPage)).grid(row=1, column=1, sticky=N+S+E+W)
	Lightbutton =tk.Button(self, text="Lighting", font=BUTTON_FONT, command=lambda: controller.show_frame(LightPage)).grid(row=2, column=0, sticky=N+S+E+W)
	Multibutton =tk.Button(self, text="Multimedia", font=BUTTON_FONT, command=lambda: controller.show_frame(MultiPage)).grid(row=2, column=1, sticky=N+S+E+W)
	Rocketbutton =tk.Button(self, text="Rocket Launcher", font=BUTTON_FONT, command=lambda: controller.show_frame(RocketPage)).grid(row=3, column=0, sticky=N+S+E+W)
	Exitbutton =tk.Button(self, text="Exit", font=BUTTON_FONT, command=lambda: controller.show_frame(ExitPage)).grid(row=3, column=1, sticky=N+S+E+W)

class NavPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
	for x in range(1):
                self.columnconfigure(x, weight=1)
        for y in range(2):
                self.rowconfigure(y, weight=1)

        label = tk.Label(self, text="Navigation", font=LARGE_FONT).grid(row=0, column=0, sticky="NSEW", columnspan=2)
        Mbutton =tk.Button(self,text="Main Page",font=BUTTON_FONT,command=lambda:controller.show_frame(StartPage)).grid(row=1, column=0, sticky="NSEW")

class ExitPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
	for x in range(2):
                self.columnconfigure(x, weight=1)
        for y in range(3):
                self.rowconfigure(y, weight=1)
        label = tk.Label(self, text="Exit Menu", font=LARGE_FONT).grid(row=0, column=0, sticky="NSEW", columnspan=2)
        Mbutton =tk.Button(self,text="Main Page",font=BUTTON_FONT,command=lambda:controller.show_frame(StartPage)).grid(row=1, column=1, sticky="NSEW")
	Exitbutton =tk.Button(self,text="Exit Application",font=BUTTON_FONT,command=lambda:exit()).grid(row=2, column=1, sticky="NSEW")
	Rebootbutton =tk.Button(self,text="Reboot System",font=BUTTON_FONT,command=lambda:call(["sudo", "reboot"])).grid(row=1, column=0, sticky="NSEW")
	Shutdownbutton =tk.Button(self,text="Shutdown System",font=BUTTON_FONT,command=lambda:call(["sudo", "poweroff"])).grid(row=2, column=0, sticky="NSEW")


class MapPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
	for x in range(1):
                self.columnconfigure(x, weight=1)
        for y in range(2):
                self.rowconfigure(y, weight=1)
        label = tk.Label(self, text="Maps", font=LARGE_FONT).grid(row=0, column=0, sticky="NSEW", columnspan=2)
        Mbutton =tk.Button(self,text="Main Page",font=BUTTON_FONT,command=lambda:controller.show_frame(StartPage)).grid(row=1, column=0, sticky="NSEW")

class LightPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
	for x in range(2):
                self.columnconfigure(x, weight=1)
        for y in range(4):
                self.rowconfigure(y, weight=1)
        label = tk.Label(self, text="Lighting Control", font=LARGE_FONT).grid(row=0, column=0, sticky="NSEW", columnspan=2)
        Mbutton =tk.Button(self,text="Main Page",font=BUTTON_FONT,command=lambda:controller.show_frame(StartPage)).grid(row=4, column=0, sticky="NSEW")
        Colorbutton =tk.Button(self,text="Pick Color",font=BUTTON_FONT,command=lambda:getColor()).grid(row=1, column=0, sticky="NSEW")

	
class MultiPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
	for x in range(1):
                self.columnconfigure(x, weight=1)
        for y in range(4):
                self.rowconfigure(y, weight=1)
        label = tk.Label(self, text="Multimedia", font=LARGE_FONT).grid(row=0, column=0, sticky="NSEW", columnspan=2)
	projector = IntVar()
	nes = IntVar()
	Checkbutton(self, text="Projector",font=BUTTON_FONT,relief=tk.RAISED, variable=projector, padx=10, pady=10).grid(row=1,column=0, sticky="NSEW")
	Checkbutton(self, text="NES",font=BUTTON_FONT,relief=tk.RAISED, variable=nes, padx=10, pady=10).grid(row=2,column=0, sticky="NSEW")
        Mbutton =tk.Button(self,text="Main Page",font=BUTTON_FONT,command=lambda:controller.show_frame(StartPage)).grid(row=3, column=0, sticky="NSEW")

class RocketPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
	for x in range(2):
                self.columnconfigure(x, weight=1)
        for y in range(4):
                self.rowconfigure(y, weight=1)
        label = tk.Label(self, text="Rocket Launcher Page", font=LARGE_FONT).grid(row=0, column=0, sticky="NSEW", columnspan=2)
	launchbutton =tk.Button(self,text="Initiate Launch",font=BUTTON_FONT,command=lambda:speak("Initiating Launch Sequence")).grid(row=1, column=0, sticky="NSEW")
	azimuthScale =tk.Scale(self, orient=tk.HORIZONTAL, label="Azimuth", ).grid(row=2, column=0, sticky="NSEW")
	elevationScale = tk.Scale(self, orient=tk.VERTICAL, label="Elevation", ).grid(row=0, column=2, sticky="NSEW")
        Mbutton =tk.Button(self,text="Main Page",font=BUTTON_FONT,command=lambda:controller.show_frame(StartPage)).grid(row=3, column=0, sticky="NSEW")

def getColor():
	color = askcolor()
	print color

def speak(text):
	subprocess.Popen(["espeak", "-v", "female3", text])

app = raftBerry()
app.attributes('-zoomed', True)
app.mainloop()
