# we can't use grayscale images for training or testing
# this script is to remove grayscale images in the datasets

from datetime import datetime
from scipy.misc import imread, imsave, imresize
import os

def is_grey_scale_2(directory, f):
  count = 0
  for filename in os.listdir(directory):
    if filename.endswith('.jpg'):
      path = os.path.join(directory, filename)
      image = imread(path)
      if len(image.shape) < 3:
        count += 1
        os.remove(path)
        print(path + ", gray scale image is deleted!")
        f.write(path + ", gray scale image is deleted!\n")
  return count

def main():
  f = open(datetime.now().strftime('delete_gray_scale_files_%H_%M_%d_%m_%Y.log'),'w+')
  for name in os.listdir("datasets/young2old"):
    subfolder = os.path.join("datasets/young2old",name)
    if os.path.isdir(subfolder):
      print(subfolder)
      f.write("start to delete gray scale images in " + subfolder + ":\n")
      counts = is_grey_scale_2(subfolder, f)
      if counts == 0:
        print("gray scale image not found in " + subfolder)
        f.write("gray scale image not found in " + subfolder)
      print("deleted " + str(counts) + "gray scale images in " + subfolder)
      f.write("deleted " + str(counts) + "gray scale images in " + subfolder + "\n")

if __name__ == '__main__':
  main()
