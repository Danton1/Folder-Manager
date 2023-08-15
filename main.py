# Danton Soares

import os
import re
import shutil
import sys
import customtkinter as tk
from CTkMessagebox import CTkMessagebox
from PIL import Image


def file_already_in_folder(source, filename, folder):
    msg = CTkMessagebox(title="File already in folder!", message=f"A file called \"{filename}\" is already in \"{folder}\"",
                        icon="warning", option_1="Skip", option_2="Overwrite")
    if msg.get() == "Overwrite":
        shutil.move(os.path.join(source, filename), os.path.join(source, folder, filename))


def assert_file_type(source):
    files = os.listdir(source)
    for filename in files:
        if os.path.isfile(os.path.join(source, filename)):
            # if the file is the script being executed
            if filename == "main.py":
                continue
            # If executable
            if re.search(r".+\.(exe|msi)$", filename):
                if not os.path.exists(os.path.join(source, "Programs")):
                    os.makedirs(os.path.join(source, "Programs"))
                if not os.path.exists(os.path.join(source, "Programs", filename)):
                    shutil.move(os.path.join(source, filename), os.path.join(source, "Programs", filename))
                else:
                    file_already_in_folder(source, filename, "Programs")
            # if image
            elif re.search(r".+\.(jpg|jpeg|png|bmp|tiff|ico)$", filename):
                if not os.path.exists(os.path.join(source, "Images")):
                    os.makedirs(os.path.join(source, "Images"))
                if not os.path.exists(os.path.join(source, "Images", filename)):
                    shutil.move(os.path.join(source, filename), os.path.join(source, "Images", filename))
                else:
                    file_already_in_folder(source, filename, "Images")
            # if gif
            elif re.search(r".+\.(gif|webp)$", filename):
                if not os.path.exists(os.path.join(source, "Gifs")):
                    os.makedirs(os.path.join(source, "Gifs"))
                if not os.path.exists(os.path.join(source, "Gifs", filename)):
                    shutil.move(os.path.join(source, filename), os.path.join(source, "Gifs", filename))
                else:
                    file_already_in_folder(source, filename, "Gifs")
            # if compressed file/folder
            elif re.search(r".+\.(rar|zip|7z|xz|bzip2|gzip|wim|tar|gz|arj|deb|pkg|rpm|z)$", filename):
                if not os.path.exists(os.path.join(source, "Compressed Files")):
                    os.makedirs(os.path.join(source, "Compressed Files"))
                if not os.path.exists(os.path.join(source, "Compressed Files", filename)):
                    shutil.move(os.path.join(source, filename), os.path.join(source, "Compressed Files", filename))
                else:
                    file_already_in_folder(source, filename, "Compressed Files")
            # if text files (pdf|txt|doc|docx|odt|rtf|tex|wpd|xml)
            elif re.search(r".+\.(pdf|txt|doc|docx|odt|rtf|tex|wpd|xml|log)$", filename):
                if not os.path.exists(os.path.join(source, "Text Files")):
                    os.makedirs(os.path.join(source, "Text Files"))
                if not os.path.exists(os.path.join(source, "Text Files", filename)):
                    shutil.move(os.path.join(source, filename), os.path.join(source, "Text Files", filename))
                else:
                    file_already_in_folder(source, filename, "Text Files")
            # if spreadsheet (xls|xlsx|xlsm|ods)
            elif re.search(r".+\.(xls|xlsx|xlsm|ods|csv)$", filename):
                if not os.path.exists(os.path.join(source, "Spreadsheets")):
                    os.makedirs(os.path.join(source, "Spreadsheets"))
                if not os.path.exists(os.path.join(source, "Spreadsheets", filename)):
                    shutil.move(os.path.join(source, filename), os.path.join(source, "Spreadsheets", filename))
                else:
                    file_already_in_folder(source, filename, "Spreadsheets")
            # if presentation file
            elif re.search(r".+\.(key|odp|pps|ppt|pptx)$", filename):
                if not os.path.exists(os.path.join(source, "Presentations")):
                    os.makedirs(os.path.join(source, "Presentations"))
                if not os.path.exists(os.path.join(source, "Presentations", filename)):
                    shutil.move(os.path.join(source, filename), os.path.join(source, "Presentations", filename))
                else:
                    file_already_in_folder(source, filename, "Presentations")
            # if audio file
            elif re.search(r".+\.(aif|cda|mid|midi|mp3|mpa|ogg|wav|wma|wpl)$", filename):
                if not os.path.exists(os.path.join(source, "Audio")):
                    os.makedirs(os.path.join(source, "Audio"))
                if not os.path.exists(os.path.join(source, "Audio", filename)):
                    shutil.move(os.path.join(source, filename), os.path.join(source, "Audio", filename))
                else:
                    file_already_in_folder(source, filename, "Audio")
            # if video file
            elif re.search(r".+\.(3g2|3gp|avi|flv|h264|m4v|mkv|mov|mp4|mpg|mpeg|rm|swf|vob|webm|wmv)$", filename):
                if not os.path.exists(os.path.join(source, "Videos")):
                    os.makedirs(os.path.join(source, "Videos"))
                if not os.path.exists(os.path.join(source, "Videos", filename)):
                    shutil.move(os.path.join(source, filename), os.path.join(source, "Videos", filename))
                else:
                    file_already_in_folder(source, filename, "Videos")
            # if programming files
            elif re.search(r".+\.(ahk|anim|asm|asset|bas|bash|bat|builder|c|cgi|class|cls|cmd|coffee|cpp|cql|cs|"
                           r"cson|css|dockerfile|gml|go|graphql|groovy|h|htm|html|ino|ipynb|java|jinja|js|json|kt|ktm|"
                           r"kts|lua|m|mm|mustache|pas|php|phtml|pl|py|pyd|pyp|pyt|pyx|r|rb|rd|rs|rss|rsx|ru|ruby|sass|"
                           r"scss|sh|spec|sql|swift|ts|tsx|ttl|uc|unity|vb|vcl|vue|w|xhtml|xpy|xq|xql|xqm|xquery)$",
                           filename):
                if not os.path.exists(os.path.join(source, "Programming Files")):
                    os.makedirs(os.path.join(source, "Programming Files"))
                if not os.path.exists(os.path.join(source, "Programming Files", filename)):
                    shutil.move(os.path.join(source, filename), os.path.join(source, "Programming Files", filename))
                else:
                    file_already_in_folder(source, filename, "Programming Files")
            # if file extension not on database
            else:
                # if os.path.exists(os.path.join(source, filename)):
                if not os.path.exists(os.path.join(source, "Others")):
                    os.makedirs(os.path.join(source, "Others"))
                if not os.path.exists(os.path.join(source, "Others", filename)):
                    shutil.move(os.path.join(source, filename), os.path.join(source, "Others", filename))
                else:
                    file_already_in_folder(source, filename, "Others")
    success = CTkMessagebox(title="Success!", message=f"The folder \"{os.path.split(my_dir)[1]}\" has been successfully"
                                                      f" organized!", icon="check", option_1="Thanks",
                            option_2="Open folder")
    if success.get() == "Open folder":
        os.startfile(my_dir)


tk.set_appearance_mode("dark")
tk.set_default_color_theme("blue")

root = tk.CTk()

root.geometry("650x300")
root.title("Folder Organizer")
root.iconbitmap(os.path.join(os.getcwd(),"icon", "favicon.ico"))

frame = tk.CTkFrame(master=root)
frame.pack(pady=20, padx=40, fill="both", expand=True)

image = tk.CTkImage(dark_image=Image.open(os.path.join(os.getcwd(),"icon", "explorer_folders.png")))
label = tk.CTkLabel(master=frame, image=image, text=" Folder Organizer", compound="left", font=('Consolas', 24))
label.pack(pady=20, padx=10)

my_dir = ''


def select_folder():
    global my_dir
    my_dir = tk.filedialog.askdirectory()
    if len(my_dir) < 57:
        l1.configure(text=my_dir)
    else:
        last_folder = os.path.split(my_dir)[0].rfind("/")
        print(last_folder)
        compressed_path = f"{my_dir[:3]}...{os.path.split(my_dir)[0][last_folder:]}/{os.path.split(my_dir)[1]}"
        l1.configure(text=compressed_path)


select = tk.CTkButton(master=frame, text="Select Folder", command=lambda: select_folder(), font=('Consolas', 16))
select.pack(pady=12, padx=10)

l1 = tk.CTkLabel(master=frame, text=my_dir, font=('Consolas', 16))
l1.pack(pady=12, padx=10)

button_organize = tk.CTkButton(master=frame, text="Organize!", command=lambda: assert_file_type(my_dir), font=('Consolas', 16))
button_organize.pack(pady=12, padx=10, side = "left", expand = True)


def main(source):
    # assert_file_type(source)
    root.mainloop()


if __name__ == '__main__':
    cwd = os.getcwd()
    main(cwd)
