# Preanalysis for Image Recognition system

----------

University of Costa Rica

Belinda Brown, timna.brown@ucr.ac.cr

March, 2020

----------

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


## Functioning

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

