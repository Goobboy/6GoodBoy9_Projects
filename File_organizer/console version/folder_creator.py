import os

"""This py files is created so that main file won't be too big"""

image_files = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.ico', '.webp')
document_files = ('.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx')
audio_files = ('.mp3', '.wav', '.flac', '.aac')
video_files = ('.mp4', '.avi', '.mkv', '.mov', '.wmv')
archive_files = ('.zip', '.rar', '.7z', '.tar', '.gz')


def folders_create(files, destination):
    """makes a folder of only existing datatype so there will not be an empty folder"""
    source = os.listdir(fr"{files}")
    for file in source:

        try:
            # image_files
            if any(file.endswith(extension) for extension in image_files):
                if not os.path.exists(os.path.join(destination, "image_folder")):
                    print(f"\n{file}")
                    print("Image_Folder created.")
                    os.makedirs(os.path.join(destination, "image_folder"))

            # document_files
            elif any(file.endswith(extension) for extension in document_files):
                if not os.path.exists(os.path.join(destination, "document_folder")):
                    print(f"\n{file}")
                    print("document_folder created.")
                    os.makedirs(os.path.join(destination, "document_folder"))

            # audio_files
            elif any(file.endswith(extension) for extension in audio_files):
                if not os.path.exists(os.path.join(destination, "audio_folder")):
                    print(f"\n{file}")
                    print("audio_folder created.")
                    os.makedirs(os.path.join(destination, "audio_folder"))

            # video_files
            elif any(file.endswith(extension) for extension in video_files):
                if not os.path.exists(os.path.join(destination, "video_folder")):
                    print(f"\n{file}")
                    print("video_folder created.")
                    os.makedirs(os.path.join(destination, "video_folder"))

            # archive_files
            elif any(file.endswith(extension) for extension in archive_files):
                if not os.path.exists(os.path.join(destination, "archive_folder")):
                    print(f"\n{file}")
                    print("archive_folder created.")
                    os.makedirs(os.path.join(destination, "archive_folder"))

            else:
                pass
        except Exception as e:
            print(f"Error:{e}")


if __name__ == '__main__':
    source = r"C:\Users\Shrijan\Desktop"
    destination = r"C:\Organized_Folder"
    folders_create(source,destination)
