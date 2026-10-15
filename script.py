import os
import subprocess

name = input("name: ") 
url = input("url: ") 
filename = input("file: ") 

# Expand the '~' to the full home directory path safely
source_path = os.path.expanduser(f"~/storage/downloads/{filename}")
destination_path = "static/images/posters/"

# Run the mv command
subprocess.run(["mv", source_path, destination_path])

# Your existing string formatting
string = f'<a href="{url}"><img class="poster-image" src="static/images/posters/{filename}" alt="{name}"><div class="poster-title">{name}</div></a>' 

print(string)

