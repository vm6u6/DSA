import os
import zipfile
import glob
import shutil
import numpy as np
import PIL.Image
import argparse

def select_gender ( gender, img ):
    L = len(img); i = 0
    while i < L:
        if img[i][3:6] != str(gender) or img[i][-4:-1] != "jpg" or img[i] == '':
            img.pop(i)
            L = L - 1
        else:
            i = i + 1

# def select_age( age_range, dirpath ):

def main():
    dirpath = "D:\\age_gender\Data\AFAD_Full\AFAD_Full.txt"
    savepath = "./datasets/female/"
    gender = 112 # select gender: 111 for men/ 112 for wemon
    height = 256
    width = 256
    output_filename = "female_" + str(height)
    
    f = open( dirpath, 'r' )
    image_filenames = f.read()
    if len(image_filenames) == 0:
        print('No input images found')
    # without \n in the txt file on the behind of each line
    data_into_list = image_filenames.replace('\n', ' ').split("./")

    select_gender( gender, data_into_list )

    print( "[Loading...]" )
    for i in range(len(data_into_list)):
        img_dir = "D:\\age_gender\Data\AFAD_Full\\" + str(data_into_list[i])
        new_img = PIL.Image.open(img_dir).resize( (height, width ) )
        new_img.save( savepath + str(i) + ".jpg", 'JPEG', quality=90)
    
    shutil.make_archive(output_filename, 'zip', savepath)
    print( "[DONE!]" )
    print()

if __name__ == '__main__':
    main()