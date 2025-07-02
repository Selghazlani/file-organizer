import os
import shutil

# choose the folder you wanna organize (replace with your own path)
FOLDER_PATH = r"C:\Users\LENOVO\OneDrive\Bureau\op1"

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"]
}

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def organize_files(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # skip folders
        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()

        moved = False
        for folder_name, extensions in FILE_TYPES.items():
            if file_ext in extensions:
                destination_folder = os.path.join(folder_path, folder_name)
                create_folder(destination_folder)
                shutil.move(file_path, os.path.join(destination_folder, filename))
                print(f"Moved: {filename} → {folder_name}")
                moved = True
                break

        if not moved:
            others_folder = os.path.join(folder_path, "Others")
            create_folder(others_folder)
            shutil.move(file_path, os.path.join(others_folder, filename))
            print(f"Moved: {filename} → Others")

if __name__ == "__main__":
    organize_files(FOLDER_PATH)
