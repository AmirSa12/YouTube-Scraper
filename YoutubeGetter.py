import requests                     #
from bs4 import BeautifulSoup as bs #
from tkinter import *               #
from tkinter import messagebox      #
from tkinter.filedialog import *    #
import os                           #
from textwrap import wrap           #
#####################################

# --------------------------------- #
#          Window settings          #
# --------------------------------- #

window = Tk()
window.title("YouTube Scraper")
window.geometry("450x233+600+250")
window.resizable(height=False,width=False)
window.configure(bg="#212F3D")
window.option_add('*tearOff',FALSE)
window.iconbitmap("YT.ico")

# --------------------------------- #
#             Main funcs            #
# --------------------------------- #

""" These are called after a valid link input """
def liketodis(like,dislike):
    global result
    like_num = like.strip().replace(",","")
    dislikes_num = dislike.strip().replace(",","")
    likes_and_dislikes = int(like_num) + int(dislikes_num)
    rate = round(likes_and_dislikes/100,2)
    result = round(int(like_num)/rate,2)
    return (result)

def lencount(name):
    result = len(name)
    return result

def main(link):
        global video
        global likes
        global dislikes
        info = requests.get(link)
        sp = bs(info.content,"lxml")
        
        title = sp.find("span",id="eow-title").text # TITLE OF THE VID  1
        likes = sp.find("button",title="I like this").text  # LIKES     2
        dislikes = sp.find("button",title="I dislike this").text   #DISLIKES    3
        views = sp.find("div",class_="watch-view-count").text   #VIEWS          4
        video_publish_date = sp.find("strong",class_="watch-time-text").text #PUBLISHE DATE     5
        channel_name = sp.find("div",class_="yt-user-info").text   #CHANNEL NAME                6
        channel_sub_count = sp.find("span",class_="yt-subscription-button-subscriber-count-branded-horizontal yt-subscriber-count").text    #SUBS   7
        try:
            video_category = sp.find("ul",class_="content watch-info-tag-list").text   #CATEGORY    8
        except AttributeError:
            video_category = "No Category"
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
        result_text.insert(8.0,f"Likes to Dislikes ››  {liketodis(likes,dislikes)}%\n")
        result_text.insert(9.0,f"Video Publish Date ››  {video_publish_date.strip()}\n")
        result_text.insert(10.0,f"Video Tages ››  {video_tags.strip()}\n")
        result_text.insert(11.0,f"Video Category ››  {video_category.strip()}\n")
    
        result_text.tag_config("red", foreground="red")
        result_text.tag_config("light-red", foreground="#EC7063")
        result_text.tag_config("green", foreground="#2ECC71")
        result_text.tag_config("gray", foreground="#BDC3C7")
        result_text.tag_config("light-blue", foreground="#5DADE2")
        result_text.tag_config("dark-gray", foreground="#616A6B")
        result_text.tag_config("purple", foreground="#A569BD")
        result_text.tag_config("whatever", foreground="#D5D8DC")
        result_text.tag_config("blue-but-white", foreground="#73C6B6")

        """ This may look confusing, but it's all Tkinter stuff. 
            It's for coloring a specific part of the inserted text """
        result_text.tag_add("red",f"{2}.{len('Channel Name ››  ')}" , f"{2}.{lencount(channel_name)+ len('Channel Name ››  ')}")
        result_text.tag_add("light-red",f"{3}.{len('Channel Subs ››  ')}" , f"{3}.{lencount(channel_sub_count)+ len('Channel Subs ››  ')}")
        result_text.tag_add("light-blue",f"{4}.{len('Video Title ››  ')}" , f"{4}.{lencount(title)+ len('Video Title ››  ')}")
        result_text.tag_add("gray",f"{5}.{len('Video Views ››  ')}" , f"{5}.{lencount(views)+ len('Video Views ››  ')}")
        result_text.tag_add("green",f"{6}.{len('Video Likes ››  ')}" , f"{6}.{lencount(likes)+ len('Video Likes ››  ')}")
        result_text.tag_add("red",f"{7}.{len('Video Dislikes ››  ')}" , f"{7}.{lencount(dislikes)+ len('Video Dislikes ››  ')}")
        result_text.tag_add("blue-but-white",f"{8}.{len('Likes to Dislikes ››  ')}" , f"{8}.{lencount(str(result))+ len('Likes to Dislikes ››  %')}")  # added '%' so it also changes color
        result_text.tag_add("dark-gray",f"{9}.{len('Video Publish Date ››  ')}" , f"{9}.{lencount(video_publish_date)+len('Video Publish Date ››  ')}")
        result_text.tag_add("purple",f"{10}.{len('Video Tages ››  ')}" , f"{10}.{lencount(video_tags)+ len('Video Tages ››  ')}")
        result_text.tag_add("whatever",f"{11}.{len('Video Category ››  ')}" , f"{11}.{lencount(video_category)+ len('Video Category ››  ')}")

# --------------------------------- #
#        Tkinter Function           #
# --------------------------------- #

video = 0
def open_link_file():
    def link_loop():
        with open(f"{full_path}/{file_name}" ,"r+",encoding="utf8") as links:
            all_links = links.read().strip()
        all_links = wrap(all_links,43)
        for link in all_links:
            print(f"checking {link}")
            main(link)
        loading_text.grid_forget()

    open_links = askopenfilename(filetype=[("Text files","*.txt")])
    full_path = os.path.dirname(open_links) # Full path without the file name 
    file_name = os.path.basename(open_links) # File name with the format (.txt) Only

    """ Loading Frame """
    loading_text.grid(row=1,column=0,columnspan=10)
    loading_text.tag_config("small", font="Fixedsys 9")
    loading_text.insert(1.0,"\n")
    loading_text.insert(2.0,"\n")
    loading_text.insert(4.0,"\n")
    loading_text.insert(3.0,"LOADING\n")
    loading_text.insert(5.0,"Avoid clicking on the screen (Beta Mode)")
    loading_text.tag_configure("center", justify='center')
    loading_text.tag_add("center", 1.0 , "end")
    loading_text.tag_add("small",5.0, f"{5}.{len('Avoid clicking on the screen (Beta Mode)')}")
    """ Starting Link Scraping"""
    window.after(500,link_loop)
    
""" Some link validation and stuff """
def check_entry(event=None):
    get_text = link_entry.get()
    get_text = get_text.strip()
    print(get_text)
    if "youtube" in get_text or "youtu.be" in get_text:
        try:
            main(get_text)
        except AttributeError:
             err = messagebox.showerror("Ops...","Something is wrong with the link\nMake sure it redirects to a Youtube video!")
        except ConnectionError:
            err = messagebox.showerror("Connection","No Conncetion. Make sure you are connected to the internet or\n a VPN if you can't access YT normaly.")
    elif len(get_text) == 0:
        link_entry["bg"] = "#E74C3C"
        err = messagebox.showerror("Invalid","Please input a valid link")
    else:
        link_entry["bg"] = "#E74C3C"
        err = messagebox.showerror("Invalid","This is not a YT video link")

""" If the Entry was not gray, Change it to gray """
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
loading_text = Text(window,bg="black",fg="orange",width=37,height=8,font="none 16",relief=SOLID)

""" Drop Down Menu """
menu_bar = Menu(window)
window.configure(menu=menu_bar)
file_sub_menu = Menu(menu_bar)
menu_bar.add_cascade(label="File", menu=file_sub_menu)
file_sub_menu.add_separator()
file_sub_menu.add_command(label="Open Link File",command=open_link_file)
file_sub_menu.add_command(label="Exit",command=lambda:window.quit())
file_sub_menu.add_separator()

# --------------------------------- #
#              Bindings             #
# --------------------------------- #

""" Some binding for the Entry """
link_entry.bind("<Button-1>",entry)
link_entry.bind("<Key>",entry)
link_entry.bind("<Return>",check_entry)

# --------------------------------- #
#             Main Loop             #
# --------------------------------- #

window.mainloop()