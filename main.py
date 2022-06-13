## copy all *.jpeg files from ./data to ./output
## rename all files to add filesize to filename like "filename_filesize.jpeg"
def copy_and_rename():

    import os
    import shutil
    import glob
    import re

    # get all jpeg files in ./data
    jpeg_files = glob.glob('data/*.jpeg')

    # copy all jpeg files to ./output
    for jpeg_file in jpeg_files:
        shutil.copy(jpeg_file, 'output')

    # get all jpeg files in ./output
    jpeg_files = glob.glob('output/*.jpeg')

    # rename all files to add filesize to filename like "filename_filesize.jpeg"
    for jpeg_file in jpeg_files:
        # get filesize
        filesize = os.path.getsize(jpeg_file)
        # get filename
        filename = os.path.basename(jpeg_file)
        # get extension
        extension = os.path.splitext(filename)[1]
        # get filename without extension
        filename_without_extension = os.path.splitext(filename)[0]
        # rename file
        new_filename = filename_without_extension + '_' + str(filesize) + extension
        os.rename(jpeg_file, 'output/' + new_filename)


if __name__ == '__main__':
    copy_and_rename()
    print('done')
    