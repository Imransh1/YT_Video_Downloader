from tkinter import *
from pytube import YouTube
from pytube import Playlist
from PIL import ImageTk, Image
import tkinter.font as font
from tkinter import messagebox
import threading
import os

root =Tk()
root.title("YouTube Video Downloader")
root.minsize(1170,470)
root.maxsize(1170,470)

HEIGHT = 470
WIDTH = 1170
FONT = font.Font(family ="Times New Roman", size ="16", weight ="bold")

x = 0
i = 1
a = 1
b = 1

def download_fn(link):
    global x,a,b
    if 'playlist' in link:
        p = Playlist(link)
        a = len(p.video_urls)
        b = a
        for j in range(len(p.video_urls)):
            downloader(p.video_urls[j])
            if x == 1 and j!= len(p.video_urls) - 1:
                j+=1
                downloader(p.video_urls[j])
            else:
                pass
    else:
        downloader(link)

def downloader(link):
    global i,a,x,b
    try:
        yt = YouTube(link)
        # Check for the link on YouTube
        try:
            button1.configure(state=DISABLED)
            if button1['state'] == DISABLED:
                FONT = font.Font(family ="Times New Roman", size ="12", weight ="bold")
                label5 = Label(frame, text = f'Downloading: {i}/{a}. Please Wait!' , font = FONT, bd =5, fg= "#0d1137",bg="white")
                label5.place(relx = 0.615, rely = 0.5, relheight =0.1)
                
            else:
                pass

            Path = r"C:\Users\Asus\Downloads\YT_Downloads" 
            # Your path goes here
            
            yd = yt.streams.get_highest_resolution().download(Path)
             
            # Get the highest resolution available for download
            # And download to the specified path.
            
            last_backslash = yd.rfind("\\")
            res = list(yd)
            res.insert(last_backslash + 1, str(i) + " ")
            res = ''.join(res)
            os.rename(yd, str(res))
            label5.destroy()
            
            # Rename downloaded file names
            # Using variable i to add a serial number to downloaded files 
            if i==b:
                messagebox.showinfo('Successful!',rf'{i}/{a} Video Downloaded Successfully. Path: {Path}')
                i = 1
                a = 1
                button1.configure(state= NORMAL )
            else:
                i+=1
            
            
        except:
            if i and b == 1:
                messagebox.showerror('Error',f'Could Not Download {yt.title}.')
                label5.destroy()
            else:
                x = 1
                b = b - 1
                i+=1
                messagebox.showerror('Error',f'Could Not Download {yt.title}.')
                # Incase of Download error this will be executed.

    except:
        
        if entry.get() == ' Paste Your Link Here':
            messagebox.showerror('Error','URL Cannot Be Blank!')
        else: 
            messagebox.showerror('Connection Error','Invalid URL!')

def cmd():
    cd = threading.Timer(1, lambda:download_fn(entry.get()))
    cd.start()


canvas = Canvas(root,height = HEIGHT, width = WIDTH)
canvas.pack()

frame=Frame(root,bg="white")
frame.place(relwidth=1,relheight=1)

background_image = ImageTk.PhotoImage(Image.open(r"Logo.png"))
background_label = Label(frame, image = background_image)
background_label.place(relx=-0.03,relwidth = 0.63, relheight =1)


label1 = Label(frame, text = "Download YouTube Videos In One Click!", font =FONT, bd =5, fg= "#0d1137",bg="white")
label1.place(relx = 0.62, rely = 0.1, relheight =0.1)



FONT = font.Font(family ="Times New Roman", size ="12", weight ="bold")
label2 = Label(frame, text = "Enter Video/Playlist link Address: ", font =FONT, bd =5, fg= "black",bg="white")
label2.place(relx = 0.615, rely = 0.25, relheight =0.1)

entry = Entry(frame, font = ("Times New Roman", 11), fg = "black", bg = '#48C9B0')
entry.place(relx = 0.615, rely = 0.35,relwidth=0.38, relheight = 0.07)
entry.insert(0, " Paste Your Link Here")

button1 = Button(root, text = "Download", font = FONT, bg = "#48C9B0", fg = "black", activeforeground = "black", activebackground = "#48C9B0", command=cmd)
button1.place(relx = 0.615,rely = 0.45,relwidth = 0.13, relheight = 0.07)

label2 = Label(frame, text = "Instructions: ", font = FONT, bd =5, fg= "#0d1137",bg="white")
label2.place(relx = 0.615, rely = 0.6, relheight =0.1)

FONT = font.Font(family ="Times New Roman", size ="11", weight ="normal")
label2 = Label(frame, text = "@Imransh1 Github ", font = FONT, bd =5, fg= "#0d1137",bg="white")
label2.place(relx = 0.87, rely = 0.90, relheight =0.1)


TEXT="1. Enter the link from YouTube.\n2. Video/Playlist must be older than 24 hours.\n3. This is only made for learning purpose.\n4. Any misuse is not advised."
label2 = Label(frame, text = TEXT, font =FONT, bd =5, fg= "#0d1137",justify=LEFT,bg="white")
label2.place(relx = 0.615, rely = 0.7, relheight =0.19)


root.mainloop()