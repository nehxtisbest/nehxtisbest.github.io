import shutil
import os

new_file_name = input("New file name: ")


if os.path.exists("template.txt"):
    shutil.copy("template.txt", new_file_name)
    print(f"Successfully created '{new_file_name}' from template.txt!")
else:
    print("Error: 'template.txt' does not exist in this folder.")



name = input("song name: ")
soundfile = input("sound file: ")
target_file = soundfile



# Safely expand the '~' to the full home directory path
source = os.path.expanduser(f"~/storage/downloads/{soundfile}")
destination = f"static/songs/{soundfile}"

try:
    os.makedirs("static/songs/", exist_ok=True)
    shutil.move(source, destination)
    print(f"Successfully moved {soundfile} to static/songs/")

except FileNotFoundError:
    print(f"Error: The file {source} could not be found.")
except PermissionError:
    print("Error: Permission denied. Check your Termux storage permissions.")



with open('songlist.txt', "r", encoding="utf-8") as f:                                                           songlist = f.read()

try:
    with open(new_file_name, "r", encoding="utf-8") as f:
        content = f.read()

    
    content = content.replace("<newname>", name)
    content = content.replace("<newfile>", soundfile)
    content = content.replace("<songlist>", songlist)


    with open(new_file_name, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Successfully updated tags inside '{new_file_name}'!")

except FileNotFoundError:
    print(f"Error: The file '{new_file_name}' could not be found.")

with open('songlist.txt', "r", encoding="utf-8") as f:
    songlist = f.read()

new = f'<li><a href="{new_file_name}" class="abbreviate">{name}</a></li>'


new_songlist = new + songlist



for file_name in os.listdir("."):
    if os.path.isfile(file_name) and file_name.endswith(".html"):
        
        with open(file_name, "r", encoding="utf-8") as f:
            file_text = f.read()

        if new not in file_text: 
            newtext = file_text.replace(songlist, new_songlist)
            with open(file_name, "w", encoding="utf-8") as f:
                    f.write(newtext)
            print(f"Updated songlist inside: {file_name}")


with open('songlist.txt', "w", encoding="utf-8") as f:                                                               f.write(new_songlist)



