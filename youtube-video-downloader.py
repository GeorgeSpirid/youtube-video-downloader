from pytube import YouTube
# "tkinter" is a basic grpahig slider
import tkinter as tk
from tkinter import filedialog

def download_video(url,save_path):
    try:
        yt=YouTube(url)
        streams=yt.streams.filter(progressive=True,file_extension="mp4")
        highest_res_stream=streams.get_highest_resolution()
        highest_res_stream.download(output_path=save_path)
        print("Successful Download!")
    except Exception as e:
        print(e)

#url="https://www.youtube.com/watch?v=8-jihyNGeLs"

def open_file_dialog():
    folder=filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

if __name__=="__main__":
    # initialize the window
    root=tk.Tk()
    # to hide the window
    root.withdraw()

    video_url=input("Enter URL: ")
    save_dir=open_file_dialog()

    if save_dir:
        print("Started download...")
        download_video(video_url,save_dir)
    else:
        print("Invalid save location.")