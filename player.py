from tkinter import*
from PIL import Image,ImageTk
from tkinter import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3


root=Tk()
root.geometry('1200x700')
root.title("Heart'sBeat")
root.resizable(False,False)
root.configure(background="black")

def unmutemusic():
  global currentvol
  root.unmutebutton.grid_remove()
  root.mutebutton.grid()
  mixer.music.set_volume(currentvol)

def mutemusic():
  global currentvol
  root.mutebutton.grid_remove()
  root.unmutebutton.grid()
  currentvol=mixer.music.get_volume()
  mixer.music.set_volume(0)
    

def resumemusic():
  root.resumebutton.grid_remove()
  root.pausebutton.grid()
  mixer.music.unpause()
  AudioStatusLabel.configure(text="playing......")


def volumeup():
  vol=mixer.music.get_volume()
  if(vol>=vol*100):

    mixer.music.set_volume(vol+0.1)
  else:
    mixer.music.set_volume(vol+0.05)
    progressbar_volume_Label.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    progressbar_volume['value']=mixer.music.get_volume()*100  

def volumedown():
  vol=mixer.music.get_volume()
  if(vol<=vol*100):

    mixer.music.set_volume(vol-0.05)
  else:
    mixer.music.set_volume(vol-0.05)
    progressbar_volume_Label.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
    progressbar_volume['value']=mixer.music.get_volume()*100  



def stopmusic():
  mixer.music.stop()
  AudioStatusLabel.configure(text="stop")
 

def pausemusic():
  mixer.music.pause()
  root.pausebutton.grid_remove()
  root.resumebutton.grid()
  AudioStatusLabel.configure(text="Paused")

def playmusic():
  ad=audiotrack.get()
  mixer.music.load(ad)
  Progressbar_lbl.grid()
  root.mutebutton.grid()
  mixer.music.play()
  progressbas_music_Label.grid()
  mixer.music.set_volume(0.4)
  progressbar_volume['value']=40
  progressbar_volume_Label['text']='40%'
  AudioStatusLabel.configure(text="playing..")

  song=MP3(ad)
  total_song_Length=int(song.info.length)
  progressbar_music['maximum']=total_song_Length
  progressbar_music_StartEnd.configure(text='{}'.format(str(datetime.timedelta(seconds=total_song_Length))))

  def func():

     current_song_length=mixer.music.get_pos()/1000
     progressbar_music['value']=current_song_length
     progressbar_music_StartTime.configure(text='{}'.format(str(datetime.timedelta(seconds=current_song_length))))
     progressbar_music.after(2,func)

  func()  




def musicurl():
  try:
    dd=filedialog.askopenfilename(initialdir='E:/Punjabi music',title='Select Audio File',
                                  filetype=(('MP3','*.mp3'),('WAV','*.wav')))

  except:
    dd=filedialog.askopenfilename(title='Select Audio Tile',filetype=(('MP3','*.mp3'),('WAV','*.wav')))  

  audiotrack.set(dd)                                   







#=================================

audiotrack=StringVar()
currentvol=0
total_song_Length=0


# ============ global variable ===============

def createwidths():

    global progressbar_music_StartEnd,progressbar_music_StartTime,progressbar_music
    global AudioStatusLabel,Progressbar_lbl,progressbar_volume,progressbar_volume_Label,progressbas_music_Label

    #===================== background image==============================

image = Image.open("C:\\Users\\NIDHI KUSHWAHA\\Documents\\musimg2.jpg")
photo = ImageTk.PhotoImage(image)

label=Label(root,image=photo,background="grey")
label.place(x=0,y=0)

# ===================labels================================================

music_label= Label(root,text="Heart'sBeat!",font=('Times New Roman',60,'bold'),fg="purple",bg="black")
music_label.grid(row=0,column=2)

TrackLabel=Label(root,text="Select Audio Track",font=('Times New Roman',20,'bold','italic'),fg="white",bg="black")
TrackLabel.grid(row=3,column=0,padx=5,pady=10)

AudioStatusLabel= Label(root,text="",bg="red")
AudioStatusLabel.grid(row=4,column=0)

  # ========================================================================================================

Track_Label_Entry=Entry(root, font=('Times New Roman',20,'bold'),bg="white",fg="purple",width=60,textvariable=audiotrack)
Track_Label_Entry.grid(row=3,column=2,padx=3,pady=10)




image1 = Image.open("C:\\Users\\NIDHI KUSHWAHA\\Documents\\project ss\\search.jpg")
image1 = image1.resize((35, 29), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(image1)

root.searchbutton = Button(root,font=('Times New Roman',14,'italic','bold'), text="Search  ",fg="white",bg="purple",image = photo1,compound=RIGHT, width=120,command=musicurl)
root.searchbutton.grid(row=4, column=3)

image2 = Image.open("C:\\Users\\NIDHI KUSHWAHA\\Documents\\project ss\\play.jpg")
image2 = image2.resize((35, 29), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(image2)

root.playbutton = Button(root,font=('Times New Roman',14,'italic','bold'), text="Play  ",fg="white",bg="purple",image = photo2,compound=RIGHT, width=130,command=playmusic)
root.playbutton.grid(row=6, column=0)

image3 = Image.open("C:\\Users\\NIDHI KUSHWAHA\\Documents\\project ss\\pause.jpg")
image3 = image3.resize((35, 29), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(image3)

root.pausebutton = Button(root,font=('Times New Roman',14,'italic','bold'), text="Pause  ",fg="white",bg="purple",image = photo3,compound=RIGHT, width=170,command=pausemusic)
root.pausebutton.grid(row=6, column=2,padx=25)

image4 = Image.open("C:\\Users\\NIDHI KUSHWAHA\\Documents\\project ss\\stop.jpg")
image4 = image4.resize((35, 29), Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(image4)

root.stopbutton = Button(root,font=('Times New Roman',14,'italic','bold'), text="Stop  ",fg="white",bg="purple",image = photo4,compound=RIGHT, width=130,command=stopmusic)
root.stopbutton.grid(row=7, column=0,pady=25)

image5 = Image.open("C:\\Users\\NIDHI KUSHWAHA\\Documents\\project ss\\volup.jpg")
image5 = image5.resize((35, 29), Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(image5)

root.volupbutton = Button(root,font=('Times New Roman',14,'italic','bold'), text="Volume Up  ",fg="white",bg="purple",image = photo5,compound=RIGHT, width=170,command=volumeup)
root.volupbutton.grid(row=7, column=2,pady=25)

image6 = Image.open("C:\\Users\\NIDHI KUSHWAHA\\Documents\\project ss\\voldown.jpg")
image6 = image6.resize((35, 29), Image.ANTIALIAS)
photo6 = ImageTk.PhotoImage(image6)

root.voldownbutton = Button(root,font=('Times New Roman',14,'italic','bold'), text="Volume Down  ",fg="white",bg="purple",image = photo6,compound=RIGHT, width=170,command=volumedown)
root.voldownbutton.grid(row=8, column=2,pady=25)

image7 = Image.open("C:\\Users\\NIDHI KUSHWAHA\\Documents\\project ss\\mute.jpg")
image7 = image7.resize((35, 29), Image.ANTIALIAS)
photo7 = ImageTk.PhotoImage(image7)

root.mutebutton = Button(root,font=('Times New Roman',14,'italic','bold'), text="Mute  ",fg="white",bg="purple",image = photo7,compound=RIGHT, width=130,command=mutemusic)
root.mutebutton.grid(row=8, column=0,pady=25)
root.mutebutton.grid_remove()

image8 = Image.open("C:\\Users\\NIDHI KUSHWAHA\\Documents\\project ss\\unmute.jpg")
image8 = image8.resize((35, 29), Image.ANTIALIAS)
photo8 = ImageTk.PhotoImage(image8)

root.unmutebutton = Button(root,font=('Times New Roman',14,'italic','bold'), text="Unmute  ",fg="white",bg="purple",image = photo8,compound=RIGHT, width=130,command=unmutemusic)
root.unmutebutton.grid(row=8, column=0,pady=25)
root.unmutebutton.grid_remove()

image9 = Image.open("C:\\Users\\NIDHI KUSHWAHA\\Documents\\project ss\\resume.jpg")
image9 = image9.resize((35, 29), Image.ANTIALIAS)
photo9 = ImageTk.PhotoImage(image9)

root.resumebutton = Button(root,font=('Times New Roman',14,'italic','bold'), text="Resume  ",fg="white",bg="purple",image = photo9,compound=RIGHT, width=130,command=resumemusic)
root.resumebutton.grid(row=6, column=2,pady=25)
root.resumebutton.grid_remove()

# ========================Progress bar========================
Progressbar_lbl=Label(root,text="",bg="white")
Progressbar_lbl.grid(row=8,column=3,rowspan=3)
Progressbar_lbl.grid_remove()

progressbar_volume=Progressbar(Progressbar_lbl,orient=VERTICAL,mode="determinate",value=40,length=230)
progressbar_volume.grid(row=0,column=0,ipadx=5)

progressbar_volume_Label=Label(Progressbar_lbl,text="40%",bg="lightgrey",width=3)
progressbar_volume_Label.grid(row=0,column=0)

#========================================

progressbas_music_Label=Label(root,text="",bg="red")
progressbas_music_Label.grid(row=12,column=0,columnspan=3,padx=15,pady=15)
progressbas_music_Label.grid_remove()

progressbar_music_StartTime=Label(progressbas_music_Label,text="0:00:0",bg="#9999ff",width=7)
progressbar_music_StartTime.grid(row=0,column=0)

progressbar_music=Progressbar(progressbas_music_Label,orient=HORIZONTAL,mode="determinate",value=0,length=250)
progressbar_music.grid(row=0,column=1,ipadx=350,ipady=0)

progressbar_music_StartEnd=Label(progressbas_music_Label,text="0:00:0",bg="#9999ff")
progressbar_music_StartEnd.grid(row=0,column=2)








# ============================================================
mixer.init()
createwidths()
root.mainloop()
