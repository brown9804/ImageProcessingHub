# Preanalysis for Image - Filter Spectrum

Costa Rica

Belinda Brown, belindabrownr04@gmail.com

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![GitHub](https://badgen.net/badge/icon/github?icon=github&label)](https://github.com) [![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/)
[brown9804](https://github.com/brown9804)

---------------

In order to run the program successfully, the following must be contained on your machine:

----------
OpenCV 4.1.2

Python 3.7.7

Numpy 1.15.2

The images used for the analysis are in .jpg format

----------

It allows to analyze the different present characteristics of each image. Content:

1. HSV filter
2. Curr Mask filter
3. To RGB filter
4. To gray filter
5. Image threshold filter
6. MedianBlur filter
7. GaussianBlur filter
8. Binary inverted threshold filter
9. Floodfilled image filter 
10. Floodfill inverted filter
11. Foreground filter


## How to

### Run the program

**1. Change in location of images to verify**

The path where the folder containing the images you want to analyze must be modified. This part of the code is the corresponding block:

~~~~~
###### Directory with images verify
img_dir = ''
~~~~~

You must enter the address corresponding to your machine in parentheses, for example:

/Users/belindabrown/Desktop/PreAnalysis_Img_Recognition/ImgtoAnalyse

**2. Change in results path**

The path where the folder containing the images you want to analyze must be modified. This part of the code is the corresponding block:

~~~~~
result_folder_path = ''
~~~~~

For example:

/Users/belindabrown/Desktop/PreAnalysis_Img_Recognition/Results/

**3. Algorithm execution**

In order for the Python interpreter to run the algorithm. You must go to the terminal or console that your machine own.

~~~~~
<Inside_programs_general_folder>$ make
~~~~~

