import os
import shutil

directory = os.path.join(os.path.expanduser("~"), "Desktop")

extnesions = {
    ".jpg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".jpeg": "Images",
    ".webp": "Images",
    ".svg": "Images",
    ".ico": "Images",
    ".bmp": "Images",
    ".tiff": "Images",
    ".psd": "Images",
    ".raw": "Images",
    ".heic": "Images",
    ".heif": "Images",
    ".doc": "Documents",
    ".docx": "Documents",
    ".pdf": "Documents",
    ".txt": "Documents",
    ".csv": "Documents",
    ".xls": "Documents",
    ".xlsx": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",
    ".zip": "Compressed",
    ".rar": "Compressed",
    ".7z": "Compressed",
    ".iso": "Compressed",
    ".zip": "Compressed",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".wmv": "Videos",
    ".flv": "Videos",
    ".webm": "Videos",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".aac": "Audio",
    ".ogg": "Audio",
    ".flac": "Audio",
    ".m4a": "Audio",
    ".wma": "Audio",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".aac": "Audio",
    ".ogg": "Audio",
    ".flac": "Audio",
    ".m4a": "Audio",
    ".wma": "Audio",
}


for filename in os.listidr(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()

        if extension in extnesions:
            folder_name = extnesions[extension]

            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            desination_path = os.path.join(folder_path, filename)
            shutil.move(file_path, desination_path)

            print(f"Moved {filename} to {filename} folder.")
        else:
            print(f"Skipped {filename}. Unknown file extension.")
    else:
        print(f"Skipped {filename}. It is a directory.")

print("File organization completed.")