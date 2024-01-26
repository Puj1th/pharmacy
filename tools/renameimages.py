import os

folder_path = "tools\scrape"  # Change this to the path of your folder
counter = 8

for filename in sorted(os.listdir(folder_path)):
    if os.path.isfile(os.path.join(folder_path, filename)):
        file_extension = os.path.splitext(filename)[1]
        new_name = f"{counter}{file_extension}"

        while os.path.exists(os.path.join(folder_path, new_name)):
            counter += 1
            new_name = f"{counter}{file_extension}"

        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_name))
        counter += 1
