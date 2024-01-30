import os

# Specify the folder name and path
def make_downtube():
    default_videos_folder = os.path.expanduser("~/Videos")
    folder_name = "DownTube"

    # Construct the full path
    full_path = os.path.join(default_videos_folder, folder_name)

    # Check if the folder exists
    if not os.path.exists(full_path):
        try:
            os.makedirs(full_path)
            print(f"Folder '{folder_name}' created successfully at {full_path}")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print(f"View your video at {full_path}")

    return full_path
