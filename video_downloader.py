import customtkinter
import tkinter
from pytube import YouTube

#system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def startDownload():
    try:
        ytLink= link.get()
        ytObject = YouTube(ytLink)
        video = ytObject.streams.get_highest_resolution()
        video.download()
    except:
        print("Youtube link je neplatný")
    print("Sťahovanie dokončené")

#app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube downloader")

#UI
title = customtkinter.CTkLabel(app, text="Vlož youtube link")
title.pack(padx=10, pady=10)

#link
url_var = tkinter.StringVar()
link=customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#Download
download = customtkinter.CTkButton(app, text="Stiahnuť", command=startDownload)
download.pack()

#run
app.mainloop()