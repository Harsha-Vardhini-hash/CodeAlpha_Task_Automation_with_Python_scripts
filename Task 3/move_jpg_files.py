import os
import shutil

source_folder = 'source_folder'
destination_folder = 'destination_folder'

os.makedirs(destination_folder, exist_ok=True)

jpg_count = 0
for filename in os.listdir(source_folder):
    # Check if file ends with .jpg (case-insensitive)
    if filename.lower().endswith('.jpg'):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        
        # Move the file
        shutil.move(source_path, destination_path)
        jpg_count += 1
        print(f"Moved: {filename}")

print(f"\n✅ {jpg_count} .jpg files moved from '{source_folder}' to '{destination_folder}'.")
