# Image Resizer


Application for resizing and converting an image. This application can change image sizes by your custom height *use -H option* , width *use -W option*  or scale an image with your scaling coefficient *use -s option*.
You can set the output filename *use -o option* or application can set new filename, based on input filename and new sizes.
If you set a file extention of your image other than input file extention, application will try to convert your image to the new file type.
Application supports thees file extentions:
['bmp', 'eps', 'gif', 'jpg', 'jpeg', 'png', 'tiff']
And output file can be converted to PDF file type.

# Quick Start

Run application with your command line:
```
python image_resize.py test.jpg -H 150 -o my_new_image.bmp
```
And you can find your converted and resized image file *my_new_image.bmp*

You can use *-h option* for help:
```
python  programm/devman/12_image_resize/image_resize.py -h
usage: image_resize.py [-h] [-W WIDTH] [-H HEIGHT] [-s SCALE] [-o OUTPUT]
                       fname

Resize and/or convert an image. Type it location. Supported files extensions:
['bmp', 'eps', 'gif', 'jpg', 'jpeg', 'png', 'tiff']

positional arguments:
  fname                 File path

optional arguments:
  -h, --help            show this help message and exit
  -W WIDTH, --width WIDTH
                        Set a new width of image
  -H HEIGHT, --height HEIGHT
                        Set a new height of image
  -s SCALE, --scale SCALE
                        Set a scaling coefficient of image. Use s<1 for
                        reduction
  -o OUTPUT, --output OUTPUT
                        Set a new filename
```
# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
