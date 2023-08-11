import logging
import os
import shutil
import getpass
import time


def warming_message():
    logging.warning("Careful about different files with same names. You might lose data!")


def warning():
    "Prints warning message."
    level = logging.WARNING
    fmt = '[%(levelname)s] %(message)s'
    logging.basicConfig(level=level, format=fmt)
    warming_message()
    # logging.warning("trying") # this also works


image_files = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif')
document_files = ('.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx')
audio_files = ('.mp3', '.wav', '.flac', '.aac')
video_files = ('.mp4', '.avi', '.mkv', '.mov', '.wmv')
archive_files = ('.zip', '.rar', '.7z', '.tar', '.gz')


def Organizer(files, destination):
    """organizes files from chosen source to destination"""
    for file in files:
        print(f"\n{file}")
        print(type(file))

        # image_files
        if any(file.endswith(extension) for extension in image_files):
            print("Image")


        # document_files
        elif any(file.endswith(extension) for extension in document_files):
            print("document_files ")

        # audio_files
        elif any(file.endswith(extension) for extension in audio_files):
            print("audio_files ")

        # video_files
        elif any(file.endswith(extension) for extension in video_files):
            print("video_files ")

        # archive_files
        elif any(file.endswith(extension) for extension in archive_files):
            print("archive_files ")

        else:
            print("not sure")


warning()
time.sleep(1)
username = getpass.getuser()

print("Please Choose a number:\n")

print("Source:")
source_Question = int(input(f"1. Downloads\n2. Desktop\n3. Custom\nchoose: "))
if source_Question == 1:
    source = os.listdir(fr"C:\Users\{username}\Downloads")
elif source_Question == 2:
    source = os.listdir(fr"C:\Users\{username}\Desktop")
elif source_Question == 3:
    print("\nCopy paste a VALID Folder Path:")
    source = input("Source Path: ")
    source = os.listdir(fr"{source}")
else:
    print("Choose a valid number next time. ")
    exit()

print("\nDestination:")
destination_Question = int(input("1. Desktop_Organized_Folder\n2. Custom\nchoose: "))

if destination_Question == 1:
    destination = (fr"C:\Users\{username}\Desktop\Organized")
elif destination_Question == 2:
    print("\nCopy paste a VALID Folder Path:")
    destination = input("Destination Path: ")

    if not os.path.exists(destination):
        os.makedirs(destination)
    else:
        print(f"Folder exists: {destination}")

else:
    print("Enter a valid number next time. ")
    exit()

Organizer(source, destination)
