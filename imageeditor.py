from PIL import Image , ImageEnhance
import threading
import json
import sys
import os

def image_rotate_90(im,imname):
    rotated=im.transpose(Image.ROTATE_90)
    rotated.show()
    rotated.save('A:\\ImageEditor\\rotated_90_{}'.format(imname))

def image_rotate_180(im,imname):
    rotated=im.transpose(Image.ROTATE_180)
    rotated.show()
    rotated.save('A:\\ImageEditor\\rotated_180_{}'.format(imname))

def image_rotate_270(im,imname):
    rotated=im.transpose(Image.ROTATE_270)
    rotated.show()
    rotated.save('A:\\ImageEditor\\rotated_270_{}'.format(imname))

def image_mirror(im,imname):
    mirrored=im.transpose(Image.FLIP_LEFT_RIGHT)
    mirrored.show()
    mirrored.save('A:\\ImageEditor\\mirrored_{}'.format(imname))

def image_flip_ver(im,imname):
    flipped=im.transpose(Image.FLIP_TOP_BOTTOM)
    flipped.show()
    flipped.save('A:\\ImageEditor\\flipped_{}'.format(imname))

def image_bright(im,factor,imname):
    enhancer=ImageEnhance.Brightness(im)
    rfactor=float(factor)
    im_ench=enhancer.enhance(rfactor)
    im_ench.show()
    im_ench.save('A:\\ImageEditor\\enchanced_{}'.format(imname))

def proccess_image(path,command,factor=0):
    im=Image.open('{}'.format(path))
    imname=os.path.basename(path)
    if command=="rotate-90":
        image_rotate_90(im,imname)
    elif command=="rotate-180":
        image_rotate_180(im,imname)
    elif command=="rotate-270":
        image_rotate_270(im,imname)
    elif command=="mirror":
        image_mirror(im,imname)
    elif command=="flip":
        image_flip_ver(im,imname)
    elif command=="brightness":
        image_bright(im,factor,imname)

f=str(sys.argv)

threads=[]
image_list=[]
lock=threading.RLock()

#Checking if JSON file is registered
if ".json" in f:
    j=json.load(open(sys.argv[1]))
    for image in j:
        path=image["File"]
        command=image["Operation"]
        if command=="brightness":
            factor=image["Factor"]
            image_list.append((path,command,factor))
        else:
            image_list.append((path,command))
else:
    #Setting up for system args
    op_list=[]
    i=1
    while i<len(sys.argv):
        path=sys.argv[i]
        if "brightness" in sys.argv[i+1]:
            op_args=sys.argv[i+1].split(":")
            command=op_args[0]
            factor=op_args[1]
            image_list.append((path,command,factor))
        else:    
            command=sys.argv[i+1]
            image_list.append((path,command))
        i+=2

for image in image_list:
    if image[1]=="brightness":
        t=threading.Thread(target=proccess_image,args=[image[0],image[1],image[2]])
    else:
        t=threading.Thread(target=proccess_image,args=[image[0],image[1]])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()