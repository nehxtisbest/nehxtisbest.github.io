import os
import subprocess

name = input("movie name: ") 
url = input("url: ") 
filename = input("picture file: ") 

# Expand the '~' to the full home directory path safely
source_path = os.path.expanduser(f"~/storage/downloads/{filename}")
destination_path = "static/images/posters/"

# Run the mv command
subprocess.run(["mv", source_path, destination_path])

# Your existing string formatting
string = f'<a href="{url}">{name}<img class="poster-image" src="static/images/posters/{filename}" alt="{name}"></a>' 

print(string)

