import requests                     #
from bs4 import BeautifulSoup as bs #
from tkinter import *               #
from tkinter import messagebox      #
#####################################


window = Tk()
window.title("YouTube Scraper")
window.geometry("450x230+600+250")
window.resizable(height=False,width=False)
window.configure(bg="#212F3D")
window.iconbitmap("YT.ico")

# --------------------------------- #
#             Main func             #
# --------------------------------- #
def lencount(name):
    result = len(name)
    return result

def main(link):
        global video
        info = requests.get(link)
        sp = bs(info.content,"lxml")

        title = sp.find("span",id="eow-title").text # TITLE OF THE VID  1
        likes = sp.find("button",title="I like this").text  # LIKES     2
        dislikes = sp.find("button",title="I dislike this").text   #DISLIKES    3
        views = sp.find("div",class_="watch-view-count").text   #VIEWS          4
        video_publish_date = sp.find("strong",class_="watch-time-text").text #PUBLISHE DATE     5
        channel_name = sp.find("div",class_="yt-user-info").text   #CHANNEL NAME                6
        channel_sub_count = sp.find("span",class_="yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count").text    #SUBS   7
        video_category = sp.find("ul",class_="content watch-info-tag-list").text   #CATEGORY    8
        try:
            video_tags = sp.find("span",class_="standalone-collection-badge-renderer-text").text #VIDEO TAGS    9
        except AttributeError:
            video_tags = "No tags"
        video+=1
        result_text.insert(1.0,f"🢃--------------{video}--------------🢃\n")
        result_text.insert(2.0,f"Channel Name ››  {channel_name.strip()}\n")
        result_text.insert(3.0,f"Channel Subs ››  {channel_sub_count.strip()}\n")
        result_text.insert(4.0,f"Video Title ››  {title.strip()}\n")
        result_text.insert(5.0,f"Video Views ››  {views.strip()}\n")
        result_text.insert(6.0,f"Video Likes ››  {likes.strip()}\n")
        result_text.insert(7.0,f"Video Dislikes ››  {dislikes.strip()}\n")
        result_text.insert(8.0,f"Video Publish Date ››  {video_publish_date.strip()}\n")
        result_text.insert(9.0,f"Video Tages ››  {video_tags.strip()}\n")
        result_text.insert(10.0,f"Video Category ››  {video_category.strip()}\n")
    
        result_text.tag_config("red", foreground="red")
        result_text.tag_config("light-red", foreground="#EC7063")
        result_text.tag_config("green", foreground="#2ECC71")
        result_text.tag_config("gray", foreground="#BDC3C7")
        result_text.tag_config("light-blue", foreground="#5DADE2")
        result_text.tag_config("dark-gray", foreground="#616A6B")
        result_text.tag_config("purple", foreground="#A569BD")
        result_text.tag_config("whatever", foreground="#D5D8DC")


        result_text.tag_add("red",f"{2}.{len('Channel Name ››  ')}" , f"{2}.{lencount(channel_name)+ len('Channel Name ››  ')}")
        result_text.tag_add("light-red",f"{3}.{len('Channel Subs ››  ')}" , f"{3}.{lencount(channel_sub_count)+ len('Channel Subs ››  ')}")
        result_text.tag_add("light-blue",f"{4}.{len('Video Title ››  ')}" , f"{4}.{lencount(title)+ len('Video Title ››  ')}")
        result_text.tag_add("gray",f"{5}.{len('Video Views ››  ')}" , f"{5}.{lencount(views)+ len('Video Views ››  ')}")
        result_text.tag_add("green",f"{6}.{len('Video Likes ››  ')}" , f"{6}.{lencount(likes)+ len('Video Likes ››  ')}")
        result_text.tag_add("red",f"{7}.{len('Video Dislikes ››  ')}" , f"{7}.{lencount(dislikes)+ len('Video Dislikes ››  ')}")
        result_text.tag_add("dark-gray",f"{8}.{len('Video Publish Date ››  ')}" , f"{8}.{lencount(video_publish_date)+ len('Video Publish Date ››  ')}")
        result_text.tag_add("purple",f"{9}.{len('Video Tages ››  ')}" , f"{9}.{lencount(video_tags)+ len('Video Tages ››  ')}")
        result_text.tag_add("whatever",f"{10}.{len('Video Category ››  ')}" , f"{10}.{lencount(video_category)+ len('Video Category ››  ')}")


# --------------------------------- #
#        Tkinter Function           #
# --------------------------------- #
video = 0
def check_entry(event=None):
    get_text = link_entry.get()
    get_text = get_text.strip()
    print(get_text)
    if "youtube" in get_text or "youtu.be" in get_text:
        try:
            main(get_text)
        except Exception:
            err = messagebox.showerror("Ops...","Something is wrong with the link\nMake sure it is a Youtube video!")
    elif len(get_text) == 0:
        link_entry["bg"] = "#E74C3C"
        err = messagebox.showerror("Invalid","Please input a valid link")
    else:
        link_entry["bg"] = "#E74C3C"
        err = messagebox.showerror("Invalid","This is not a YT video link")
def entry(event=None):
    if link_entry["bg"] == "gray":
        pass
    else:
        link_entry["bg"] = "gray"
# --------------------------------- #
#              Tkinter              #
# --------------------------------- #
""" Front End """
link = Label(window,text="Link :",font="none 9",bg="#212F3D",fg="#D35400");link.grid(padx=3,pady=5,row=0,column=0,sticky=W)
link_entry = Entry(window,bg="gray",fg="blue",relief=SOLID,font="none 9");link_entry.grid(row=0,column=1,ipady=1.6,ipadx=15,sticky=W)
result_text = Text(window,bg="black",fg="orange",width=64,height=13,font="none 9");result_text.grid(row=1,column=0,columnspan=10)
confirm_button = Button(window,padx=10,text="Confirm",bg="black",fg="orange",font="none 8",relief=SOLID,command=check_entry);confirm_button.grid(row=0,column=2,sticky=W)
clear_button = Button(window,padx=10,text="Clear",bg="black",fg="orange",font="none 8",relief=SOLID,command=lambda:[link_entry.delete(0,END)]);clear_button.grid(row=0,column=3,sticky=W)

# --------------------------------- #
#              Binding              #
# --------------------------------- #

""" Some binding for the Entry """

link_entry.bind("<Button-1>",entry)
link_entry.bind("<Key>",entry)
link_entry.bind("<Return>",check_entry)



window.mainloop()

