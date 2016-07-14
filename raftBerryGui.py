#raftBerryGui code to update the previous version of the raftBerry and add absurd features.
#
#Frame manager code derived from youtube user sentdex 
#Thanks novel_yet_trivial

from Tkinter import *
import Tkinter as tk
from tkColorChooser import askcolor  
import subprocess, ttk, time, ImageTk, serial, array

VERSION="raftBerry v0.2"

class raftBerry(tk.Tk):

    def __init__(self, *args, **kwargs):
	tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, VERSION)
	#Set window icon
	img = PhotoImage(file='/home/pi/raftBerryGui/images/raftBerryPi.gif')
	self.tk.call('wm', 'iconphoto', self._w, img)

	self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
	#Set styles
	self.style = ttk.Style()
	self.style.configure('.',font=('Helvetica', 36),background='black', foreground='white', sliderthickness=80, troughcolor='black', borderwidth=5, highlightbackground='red')

	container = ttk.Frame(self)
	container.columnconfigure(0, weight=1)
	container.rowconfigure(0, weight=1)
	container.grid(row=0, column=0, sticky=N+S+E+W)
	self.frames = {}

        for F in (LogoPage, StartPage, NavPage, MapPage, LightPage, MultiPage, RocketPage, ExitPage, CodePage):
        	frame = F(container, self)
        	self.frames[F] = frame
		frame.grid(row=0, column=0, sticky=N+S+E+W)
	
	self.show_frame(StartPage)

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
        
        label = ttk.Label(self, text="raftBerry Menu", anchor=tk.CENTER).grid(row=0, column=0, columnspan=3, sticky="NSEW")
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

class CodePage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)
        for x in range(4):
                self.columnconfigure(x, weight=1)
        for y in range(3):
                self.rowconfigure(y, weight=1)

        #label = ttk.Label(self, text="raftBerry Menu", anchor=tk.CENTER).grid(row=0, column=0, columnspan=3, sticky="NSEW")
        ttk.Button(self, text="1", command=lambda: enterCode(str(1))).grid(row=2, column=0, sticky=N+S+E+W)
        ttk.Button(self, text="2", command=lambda: enterCode(str(2))).grid(row=2, column=1, sticky=N+S+E+W)
        ttk.Button(self, text="3", command=lambda: enterCode(str(3))).grid(row=2, column=2, sticky=N+S+E+W)
        ttk.Button(self, text="4", command=lambda: enterCode(str(4))).grid(row=1, column=0, sticky=N+S+E+W)
        ttk.Button(self, text="5", command=lambda: enterCode(str(5))).grid(row=1, column=1, sticky=N+S+E+W)
        ttk.Button(self, text="6", command=lambda: enterCode(str(6))).grid(row=1, column=2, sticky=N+S+E+W)
        ttk.Button(self, text="7", command=lambda: enterCode(str(7))).grid(row=0, column=0, sticky=N+S+E+W)
        ttk.Button(self, text="8", command=lambda: enterCode(str(8))).grid(row=0, column=1, sticky=N+S+E+W)
        ttk.Button(self, text="9", command=lambda: enterCode(str(9))).grid(row=0, column=2, sticky=N+S+E+W)
	ttk.Button(self, text="Enter", command=lambda: enterCode("enter")).grid(row=0, column=3, sticky=N+S+E+W)
        ttk.Button(self, text="Reset", command=lambda: enterCode("reset")).grid(row=1, column=3, sticky=N+S+E+W)
        MButton =ttk.Button(self, text="Cancel", command=lambda: controller.show_frame(StartPage)).grid(row=2, column=3, sticky=N+S+E+W)


class LogoPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self,parent)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
	canvas = Canvas(self, width=800, height=480)
	canvas.create_line(0, 0, 200, 100)
	logo = ImageTk.PhotoImage(file="/home/pi/raftBerryGui/images/raftBerryPi.png")
	canvas.create_image(400,240,image=logo)
	label = Label(image=logo)
	label.image = logo
	canvas.grid(row=0, column=0, sticky="NSEW")



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
	Rebootbutton =ttk.Button(self,text="Reboot System",command=lambda:subprocess.call(["sudo", "reboot"])).grid(row=1, column=0, sticky="NSEW")
	Shutdownbutton =ttk.Button(self,text="Shutdown System",command=lambda:subprocess.call(["sudo", "poweroff"])).grid(row=2, column=0, sticky="NSEW")


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
	ttk.Checkbutton(self, text="Projector", variable=projector).grid(row=1,column=0, sticky="NSEW")
	ttk.Checkbutton(self, text="NES", variable=nes).grid(row=2,column=0, sticky="NSEW")
        Mbutton =ttk.Button(self,text="Main Page",command=lambda:controller.show_frame(StartPage)).grid(row=3, column=0, sticky="NSEW")

class RocketPage(ttk.Frame):

    def __init__(self, parent, controller):
	ttk.Frame.__init__(self,parent)
	#global elev
	for x in range(2):
                self.columnconfigure(x, weight=1)
        for y in range(3):
                self.rowconfigure(y, weight=1)
        label = ttk.Label(self, text="Rocket Launcher", anchor='center').grid(row=0, column=0, columnspan=3, sticky="NSEW")
	launchbutton =ttk.Button(self,text="Initiate Launch",command=lambda:enterCode("init")).grid(row=1, column=0, sticky="NSEW")
	azimuthScale =ttk.Scale(self, orient=tk.HORIZONTAL, from_ = 1, to = 100).grid(row=3, column=0, columnspan=2, sticky="NSEW")
#	elevationScale = ttk.Scale(self, orient=tk.VERTICAL, from_ = 1, to = 100, variable=elev).grid(row=1, column=1, rowspan=3, sticky="NSEW")
        Mbutton =ttk.Button(self,text="Main Page",command=lambda:controller.show_frame(StartPage)).grid(row=2, column=0, sticky="NSEW")

def getColor():
	color = askcolor()
	print color

def enterCode(i):
	global code
        if i == 'reset':
                code=''
        elif i == 'enter':
                if code=="6969":
                        speak("Launch access, granted")
                        time.sleep(2)
                        speak("sighmultaneously, Activate, arming, keys")
			time.sleep(3)
			#start checking for arming keys
			enterCode("keys")
		else:
			speak("Launch access, denied")
			app.show_frame(StartPage)
        elif i == 'init':
                
                speak("Initiating launch procedure")
                time.sleep(3)
		code=''
		
                speak("Enter launch code")
                app.show_frame(CodePage)
	elif i == 'keys':
		speak("Arming, keys, activated.")
		time.sleep(2)
		speak("Aim tourret and fire when ready")
		
		
	elif i == 'fire':
		speak("Firing in")
		time.sleep(1)
		speak("5")
		time.sleep(1)
		speak("4")
                time.sleep(1)
		speak("3")
                time.sleep(1)
		speak("2")
                time.sleep(1)
		speak("1")
                time.sleep(1)
		speak("Fire!")
		serialIO('Q');
        else:
                code+=i
                print(code)

def speak(text):
	subprocess.Popen(["espeak", "-v", "female3", text], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def serialIO(outCmd):
	if ser.inWaiting() > 0: 
		inCmd=ser.read()
		#if inCmd=='O':
			
	else:
		print("Something fucked up")
	app.after(1000, serialIO('0')) 



#Setup
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=0)
print(ser.name)

app = raftBerry()
#Make the app fullscreen to maximize touchscreen button size.
code=""
app.attributes("-fullscreen", True)
app.config(cursor='none')
app.after(100, serialIO('0'))
app.show_frame(LogoPage)
app.update()
time.sleep(1)
app.show_frame(StartPage)
app.mainloop()
