#raftBerryGui code to upgrade the previous version of the raftBerry
#
#Frame manager code derived from youtube user sentdex 
#Special thanks to reddit user novel_yet_trivial for helping with grid issues.

from Tkinter import *
import Tkinter as tk
from tkColorChooser import askcolor  
import subprocess, ttk, time, ImageTk

VERSION="raftBerry v0.2"

class raftBerry(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, VERSION)
	img = PhotoImage(file='images/raftBerryPi.gif')
	self.tk.call('wm', 'iconphoto', self._w, img)
	self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
	self.style = ttk.Style()
	self.style.configure('.',font=('Helvetica', 36))
	container = ttk.Frame(self)
	container.columnconfigure(0, weight=1)
	container.rowconfigure(0, weight=1)
	container.grid(row=0, column=0, sticky=N+S+E+W)
	self.frames = {}

        for F in (StartPage, NavPage, MapPage, LightPage, MultiPage, RocketPage, ExitPage, LogoPage):
        	frame = F(container, self)
        	self.frames[F] = frame
		frame.grid(row=0, column=0, sticky=N+S+E+W)
	
        self.show_frame(LogoPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)
	for x in range(2):
		self.columnconfigure(x, weight=1)
	for y in range(4):
		self.rowconfigure(y, weight=1)
        
        label = ttk.Label(self, text="raftBerry Menu").grid(row=0, column=0, columnspan=3, sticky="NSEW")
        Navbutton =ttk.Button(self, text="Navigation", command=lambda: controller.show_frame(NavPage)).grid(row=1, column=0, sticky=N+S+E+W)
	Mapbutton =ttk.Button(self, text="Map", command=lambda: controller.show_frame(MapPage)).grid(row=1, column=1, sticky=N+S+E+W)
	Lightbutton =ttk.Button(self, text="Lighting", command=lambda: controller.show_frame(LightPage)).grid(row=2, column=0, sticky=N+S+E+W)
	Multibutton =ttk.Button(self, text="Multimedia", command=lambda: controller.show_frame(MultiPage)).grid(row=2, column=1, sticky=N+S+E+W)
	Rocketbutton =ttk.Button(self, text="Rocket Launcher", command=lambda: controller.show_frame(RocketPage)).grid(row=3, column=0, sticky=N+S+E+W)
	Exitbutton =ttk.Button(self, text="Exit", command=lambda: controller.show_frame(ExitPage)).grid(row=3, column=1, sticky=N+S+E+W)

class NavPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)
	for x in range(1):
                self.columnconfigure(x, weight=1)
        for y in range(2):
                self.rowconfigure(y, weight=1)

        label = ttk.Label(self, text="Navigation").grid(row=0, column=0, sticky="NSEW", columnspan=2)
        Mbutton =ttk.Button(self,text="Main Page",command=lambda:controller.show_frame(StartPage)).grid(row=1, column=0, sticky="NSEW")

class LogoPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
	canvas = Canvas(self, width=800, height=480)
	canvas.grid(row=0, column=0, sticky="NSEW")
	photoimage = ImageTk.PhotoImage(file="images/raftBerryPi.png")
	canvas.create_image(0,0,image=photoimage)



class ExitPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)
	for x in range(2):
                self.columnconfigure(x, weight=1)
        for y in range(3):
                self.rowconfigure(y, weight=1)
        label = ttk.Label(self, text="Exit Menu").grid(row=0, column=0, sticky="NSEW", columnspan=2)
        Mbutton =ttk.Button(self,text="Main Page",command=lambda:controller.show_frame(StartPage)).grid(row=1, column=1, sticky="NSEW")
	Exitbutton =ttk.Button(self,text="Exit Application",command=lambda:exit()).grid(row=2, column=1, sticky="NSEW")
	Rebootbutton =ttk.Button(self,text="Reboot System",command=lambda:call(["sudo", "reboot"])).grid(row=1, column=0, sticky="NSEW")
	Shutdownbutton =ttk.Button(self,text="Shutdown System",command=lambda:call(["sudo", "poweroff"])).grid(row=2, column=0, sticky="NSEW")


class MapPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)
	for x in range(1):
                self.columnconfigure(x, weight=1)
        for y in range(2):
                self.rowconfigure(y, weight=1)
        label = ttk.Label(self, text="Maps").grid(row=0, column=0, sticky="NSEW", columnspan=2)
        Mbutton =ttk.Button(self,text="Main Page",command=lambda:controller.show_frame(StartPage)).grid(row=1, column=0, sticky="NSEW")

class LightPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)
	for x in range(2):
                self.columnconfigure(x, weight=1)
        for y in range(4):
                self.rowconfigure(y, weight=1)
        label = ttk.Label(self, text="Lighting Control").grid(row=0, column=0, sticky="NSEW", columnspan=2)
        Mbutton =ttk.Button(self,text="Main Page",command=lambda:controller.show_frame(StartPage)).grid(row=4, column=0, sticky="NSEW")
        Colorbutton =ttk.Button(self,text="Pick Color",command=lambda:getColor()).grid(row=1, column=0, sticky="NSEW")

	
class MultiPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)
	for x in range(1):
                self.columnconfigure(x, weight=1)
        for y in range(4):
                self.rowconfigure(y, weight=1)
        label = ttk.Label(self, text="Multimedia").grid(row=0, column=0, sticky="NSEW", columnspan=2)
	projector = IntVar()
	nes = IntVar()
	Checkbutton(self, text="Projector",relief=tk.RAISED, variable=projector, padx=10, pady=10).grid(row=1,column=0, sticky="NSEW")
	Checkbutton(self, text="NES",relief=tk.RAISED, variable=nes, padx=10, pady=10).grid(row=2,column=0, sticky="NSEW")
        Mbutton =ttk.Button(self,text="Main Page",command=lambda:controller.show_frame(StartPage)).grid(row=3, column=0, sticky="NSEW")

class RocketPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)
	for x in range(2):
                self.columnconfigure(x, weight=1)
        for y in range(4):
                self.rowconfigure(y, weight=1)
        label = ttk.Label(self, text="Rocket Launcher Page").grid(row=0, column=0, sticky="NSEW", columnspan=2)
	launchbutton =ttk.Button(self,text="Initiate Launch",command=lambda:speak("Initiating Launch Sequence")).grid(row=1, column=0, sticky="NSEW")
#	azimuthScale =ttk.Scale(self, orient=tk.HORIZONTAL, label="Azimuth", ).grid(row=2, column=0, sticky="NSEW")
#	elevationScale = ttk.Scale(self, orient=tk.VERTICAL, label="Elevation", ).grid(row=0, column=2, sticky="NSEW")
        Mbutton =ttk.Button(self,text="Main Page",command=lambda:controller.show_frame(StartPage)).grid(row=3, column=0, sticky="NSEW")

def getColor():
	color = askcolor()
	print color

def speak(text):
	subprocess.Popen(["espeak", "-v", "female3", text])

app = raftBerry()
app.attributes('-zoomed', True)
app.mainloop()
