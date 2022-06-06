## copy all picture files under ./pics to ./output
## and rename the file name to yyyy-mm-dd-hh-mm-ss format based on the original file's creation time
def main():
    import os
    import shutil
    import time
    import datetime
    import re

    # get current working directory
    cwd = os.getcwd()
    print("Current working directory is: " + cwd)

    # get all files under ./pics
    pics = os.listdir(cwd + "/pics")
    print("All files under ./pics: ")
    print(pics)

    # get current time
    now = datetime.datetime.now()
    print("Current time: " + str(now))

    # get current time in yyyy-mm-dd-hh-mm-ss format
    current_time = now.strftime("%Y-%m-%d-%H-%M-%S")
    print("Current time in yyyy-mm-dd-hh-mm-ss format: " + current_time)

    # create output directory if it doesn't exist
    if not os.path.exists(cwd + "/output"):
        os.mkdir(cwd + "/output")
    print("Output directory created.")

    # copy all files under ./pics to ./output
    for pic in pics:
        shutil.copy(cwd + "/pics/" + pic, cwd + "/output/" + current_time + "-" + pic)
    print("All files copied.")

    # rename all files under ./output
    for pic in os.listdir(cwd + "/output"):
        # get original file name
        original_name = pic.split(".")[0]
        # get original file extension
        original_extension = pic.split(".")[1]
        # get original file creation time
        original_ctime = os.path.getctime(cwd + "/output/" + pic)
        # get original file creation time in yyyy-mm-dd-hh-mm-ss format
        original_ctime_str = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(original_ctime))
        # rename file
        os.rename(cwd + "/output/" + pic, cwd + "/output/" + original_ctime_str + "-" + original_name + "." + original_extension)
    print("All files renamed.")

## define an entry point
if __name__ == '__main__':
    main()