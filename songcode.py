import shutil
import os

def main():
    html_file = input("New html file name: ")
    song_name = input("song name: ")
    soundfile = input("mp3 file: ")

    with open('songlist.txt', "r", encoding="utf-8") as f:                                                           songlist = f.read()


    create_html_file(html_file)
    move_sound_file(soundfile)
    write_to_html(html_file, song_name, soundfile, songlist)
    update_songlists(html_file, song_name, songlist)





def update_songlists(file, name, string):
    new = f'<li><a href="{file}" class="abbreviate">{name}</a></li>'

    new_string = new + string

    for file_name in os.listdir("."):
        if os.path.isfile(file_name) and file_name.endswith(".html"):
        
            with open(file_name, "r", encoding="utf-8") as f:
                file_text = f.read()

            if new not in file_text: 
                newtext = file_text.replace(string, new_string)
                with open(file_name, "w", encoding="utf-8") as f:
                        f.write(newtext)
                print(f"Updated songlist inside: {file_name}")

    with open('songlist.txt', "w", encoding="utf-8") as f:                                                               f.write(new_string)


def write_to_html(file, name, song_file, string):
    try:
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
    
        content = content.replace("<newname>", name)
        content = content.replace("<newfile>", song_file)
        content = content.replace("<songlist>", string)

        with open(file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Successfully updated tags inside '{file}'!")

    except FileNotFoundError:
        print(f"Error: The file '{file}' could not be found.")

def create_html_file(file_name):
    if os.path.exists("template.txt"):
        shutil.copy("template.txt", file_name)
        print(f"Successfully created '{file_name}' from template.txt!")
    else:
        print("Error: 'template.txt' does not exist in this folder.")

def move_sound_file(file):
    source = os.path.expanduser(f"~/storage/downloads/{file}")
    destination = f"static/songs/{file}"

    try:
        os.makedirs("static/songs/", exist_ok=True)
        shutil.move(source, destination)
        print(f"Successfully moved {file} to static/songs/")

    except FileNotFoundError:
        print(f"Error: The file {source} could not be found.")
    except PermissionError:
        print("Error: Permission denied. Check your Termux storage permissions.")

if __name__ == "__main__":
    main()
