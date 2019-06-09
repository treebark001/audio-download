from __future__ import unicode_literals
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as ST
import youtube_dl
import os
from threading import Thread
import time


'''
original author:  usertreebark@gmail.com
'''


heart = True

win = tk.Tk()
win.title("youtube music downloader for android")

label_001 = ttk.Label(win, text="enter full URLs or youtube playlists for audio download below:")
label_001.grid(column=1, row=0)
label_002 = ttk.Label(win, text="Status: ")
label_002.grid(column=0, row=3)
label_005 = ttk.Label(win, text="audio downloader v 0.1")
label_005.grid(column=0, row=7)


name_os = tk.StringVar()
name_field_os = ttk.Entry(win, width=80, textvariable=name_os)
name_field_os.grid(column=0, row=12)



def clickMe():
    global heart

    if len(name_os.get()) > 4:
        os.chdir(rf'{name_os.get()}')
    else:
        os.chdir(r'C:\youtube-dl')
    button_002.configure(text=f"clicked!")
    label_001.configure(foreground='red', text='downloading now...')

    label_004.configure(foreground='blue', text='Currently downloading, please wait...')

    try:
        for i in range(10):
            label_002.configure(text=f'Status: downloading audio: {i+1}')
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                if len(field_grab_text[i].get()) > 4:
                    ydl.download([field_grab_text[i].get()])
                    label_001.configure(foreground='green', text='finished downloading')
        label_002.configure(text=f'looks like we are all done, thank you!')
        label_004.configure(foreground='blue', text='')
    except:
        label_001.configure(foreground='purple', text='ERROR ERROR ERROR')

        label_004.configure(text=r" [ ] ")
    finally:
        button_002.configure(text=f"click to download again")
        label_001.configure(foreground='black', text='enter full URLs for download:')
        heart = True

#thread001 = threading.Thread(target=clickMe, name='thread001', args=(1, 2)) #new

field_grab_text = []
field_list = []

for i in range(10):
    name = tk.StringVar()
    name_field = ttk.Entry(win, width=80, textvariable=name)
    field_grab_text.append(name)
    name_field.grid(column=1, row=i+1)
    field_list.append(name_field)

def processing():

    while heart:
        for i in range(10):
            time.sleep(0.5)
            label_002.configure(text=f'downloading now' + '.'*i)


button_002 = ttk.Button(win, text='this button does nothing')
button_002.grid(column=0, row=1)


def clickMe_threaded():
    thread001 = Thread(target=clickMe)
    thread001.start()
    thread002 = Thread(target=processing)
    thread002.start()


button_003 = ttk.Button(win, text='Click me once after entering URL(S)', command=clickMe_threaded)
button_003.grid(column=0, row=2)

ydl_opts = {
    'format': 'bestaudio/best',
}


label_003 = ttk.Label(win, text=r"Target directory below, default is: C:\youtube-dl")
label_003.grid(column=0, row=11)

label_004 = ttk.Label(win, text=r" [ ] ")
label_004.grid(column=0, row=4)

print('\nWelcome to audio downloader!\nKeep this window open to see download the progress\nAuthor:  usertreebark@gmail.com')

win.mainloop()
