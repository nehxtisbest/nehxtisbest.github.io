import os

# Define the folder path ('.' means the current folder where the script runs)
folder_path = '.'

# The exact strings to search for and replace
target_text = '</ul></nav></body></html>'

new = input('new song code: ')

replacement_text = f'{new}/n/n</ul></nav></body></html>'

# Track how many files were successfully modified
modified_count = 0

# Loop through every file in the directory
for filename in os.listdir(folder_path):
    # Only process files ending with .html
    if filename.endswith('.html'):
        file_path = os.path.join(folder_path, filename)
        
        try:
            # 1. Read the contents of the file
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()

            # 2. Check if the target text exists in this file
            if target_text in file_content:
                updated_content = file_content.replace(target_text, replacement_text)

                # 3. Write the updated content back
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(updated_content)
                
                print(f"Updated: {filename}")
                modified_count += 1
                
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print(f"\nTask complete. Modified {modified_count} file(s).")

