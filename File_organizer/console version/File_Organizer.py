import logging
import os
import shutil
import getpass
import time
import folder_creator


def warning(type_msg):
    "Prints warning message."
    if type_msg == "warning":
        level = logging.WARNING
        fmt = '[%(levelname)s] %(message)s'
        logging.basicConfig(level=level, format=fmt)
        logging.warning("Same-named files with matching data types won't overwrite.")
    elif type_msg == "dst_msg":
        level = logging.WARNING
        fmt = '[%(levelname)s] %(message)s'
        logging.basicConfig(level=level, format=fmt)
        logging.warning("An 'Organized_Folder' will be created if it doesn't already exist.")


image_files = (
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.ico', '.webp',
    '.JPG', '.JPEG', '.PNG', '.GIF', '.BMP', '.TIFF', '.TIF', '.ICO', '.WEBP',
    '.svg', '.SVG', '.heic', '.HEIC', '.heif', '.HEIF', '.raw', '.RAW', 
    '.cr2', '.CR2', '.nef', '.NEF', '.arw', '.ARW', '.avif', '.AVIF')

document_files = (
    '.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx',
    '.TXT', '.PDF', '.DOC', '.DOCX', '.XLS', '.XLSX', '.PPT', '.PPTX',
    '.odt', '.ODT', '.ods', '.ODS', '.odp', '.ODP', '.rtf', '.RTF',
    '.csv', '.CSV', '.md', '.MD', '.tex', '.TEX', '.epub', '.EPUB')

audio_files = (
    '.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.opus',
    '.MP3', '.WAV', '.FLAC', '.AAC', '.OGG', '.WMA', '.M4A', '.OPUS',
    '.aiff', '.AIFF', '.ape', '.APE', '.alac', '.ALAC')

video_files = (
    '.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v',
    '.MP4', '.AVI', '.MKV', '.MOV', '.WMV', '.FLV', '.WEBM', '.M4V',
    '.mpeg', '.MPEG', '.mpg', '.MPG', '.3gp', '.3GP', '.ogv', '.OGV')

archive_files = (
    '.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz', '.tar.gz',
    '.ZIP', '.RAR', '.7Z', '.TAR', '.GZ', '.BZ2', '.XZ', '.TAR.GZ',
    '.tgz', '.TGZ', '.tar.bz2', '.TAR.BZ2', '.iso', '.ISO', '.dmg', '.DMG')


def Organizer(files, destination):
    """organizes files from chosen source to destination"""
    source = os.listdir(fr"{files}")
    for file in source:
        print(f"\n{file}")

        try:
            # image_files
            if any(file.endswith(extension) for extension in image_files):
                print("Image")
                shutil.move(os.path.join(files, file), os.path.join(destination, "image_folder"))

            # document_files
            elif any(file.endswith(extension) for extension in document_files):
                print("document_files ")
                shutil.move(os.path.join(files, file), os.path.join(destination, "document_folder"))

            # audio_files
            elif any(file.endswith(extension) for extension in audio_files):
                print("audio_files ")
                shutil.move(os.path.join(files, file), os.path.join(destination, "audio_folder"))

            # video_files
            elif any(file.endswith(extension) for extension in video_files):
                print("video_files ")
                shutil.move(os.path.join(files, file), os.path.join(destination, "video_folder"))

            # archive_files
            elif any(file.endswith(extension) for extension in archive_files):
                print("archive_files ")
                shutil.move(os.path.join(files, file), os.path.join(destination, "archive_folder"))

            else:
                print("not mentioned")
        except Exception as e:
            print(f"Error:{e}")


warning("warning")
time.sleep(1)
username = getpass.getuser()

print("Please Choose a number:\n")

print("Source:")
source_Question = int(input(f"1. Downloads\n2. Desktop\n3. Custom\nchoose: "))
if source_Question == 1:
    source = fr"C:\Users\{username}\Downloads"
elif source_Question == 2:
    source = fr"C:\Users\{username}\Desktop"
    print(source)
elif source_Question == 3:
    print("\nCopy paste a VALID Folder Path:")
    source = input("Source Path: ")
else:
    print("Choose a valid number next time. ")
    exit()
print("\n")

warning("dst_msg")
time.sleep(0.1)
print("Destination:")
destination_Question = int(input("1. Desktop_Organized_Folder\n2. Custom\nchoose: "))
if destination_Question == 1:
    destination = fr"C:\Users\{username}\Desktop\Organized_Folder"
elif destination_Question == 2:
    print("\nCopy paste a VALID Folder Path:")
    destination = input("Destination Path: ")
    destination = os.path.join(destination, "Organized_Folder")
else:
    print("Enter a valid number next time. ")
    exit()

folder_creator.folders_create(source, destination)
Organizer(source, destination)

print("\n\n")
print("__________Task Completed__________")
input("Press Enter to exit.")
exit()

