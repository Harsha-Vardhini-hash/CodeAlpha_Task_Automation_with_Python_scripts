import os

source_dir = 'source_folder'
os.makedirs(source_dir, exist_ok=True)

jpg_filenames = ['photo1.jpg', 'photo2.JPG', 'vacation.jpg']
for name in jpg_filenames:
    with open(os.path.join(source_dir, name), 'w') as f:
        f.write("This is a dummy JPG file.\n")

txt_filenames = ['document1.txt', 'notes.txt']
for name in txt_filenames:
    with open(os.path.join(source_dir, name), 'w') as f:
        f.write("This is a dummy text file.\n")

with open(os.path.join(source_dir, 'image.png'), 'w') as f:
    f.write("This is a dummy PNG file.\n")

print(f"✅ Created {len(jpg_filenames) + len(txt_filenames) + 1} test files in '{source_dir}'")
