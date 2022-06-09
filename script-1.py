## copy all image files from ./pics to ./output
def copy_files(source, destination):
    import os
    import shutil
    for file in os.listdir(source):
        if file.endswith(".jpeg"):
            shutil.copy(source + file, destination)

## change the file name to file_size.jpeg
def change_file_name(source, destination):
    import os
    import shutil
    for file in os.listdir(source):
        if file.endswith(".jpeg"):
            shutil.move(source + file, destination + file.replace(".jpeg", ".{}".format(os.path.getsize(source + file))))

## define an entry point
if __name__ == "__main__":
    copy_files("./pics/", "./output/")
    change_file_name("./output/", "./output/")
