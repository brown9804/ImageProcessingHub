
#Python3


##--------------------------------Main file------------------------------------
##
## Copyright (C) 2020 by Belinda Brown Ramírez (belindabrownr04@gmail.com)
##	                 Preanlysis for a Image recognition system
##
##-----------------------------------------------------------------------------

#******************************************************
#               IMPORTING
#******************************************************

import cv2
import numpy as np
from PIL import Image
import datetime
import time
import os
import glob


#******************************************************
#               DEFINITIONS
#******************************************************


def viewImage(image):
	cv2.namedWindow('Display', cv2.WINDOW_NORMAL)
	cv2.imshow('Display', image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

#######################################################
#                     1
#######################################################

def hsv_filter(image,result_folder):
	os_t = time.time()
	hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	cv2.imwrite(str(result_folder)+'HSV_%s.jpg'%os_t, hsv_img)
	print('\n'+str(result_folder)+'HSV_%s.jpg'%os_t + '--> DONE')
	return hsv_img

#######################################################
#                     2
#######################################################

def curr_mask_filter(image, hsv_image,result_folder):
	green_low = np.array([42,59,13])
	green_high = np.array([249,255,250])
	curr_mask = cv2.inRange(hsv_image, green_low, green_high)
	green = np.uint8([[[0,255,0 ]]])
	hsv_image[curr_mask > 0] = green
	os_t = time.time()
	cv2.imwrite(str(result_folder)+'CUR_MASK%s.jpg'%os_t,hsv_image)
	print('\n'+str(result_folder)+'CUR_MASK%s.jpg'%os_t+ '--> DONE')

#######################################################
#                     3
#######################################################

def to_RGB_filter(image_x_filter,result_folder):
	RGB_again = cv2.cvtColor(image_x_filter, cv2.COLOR_HSV2RGB)
	os_t = time.time()
	cv2.imwrite(str(result_folder)+'RGB%s.jpg'%os_t,RGB_again)
	print('\n'+str(result_folder)+'RGB%s.jpg'%os_t+ '--> DONE')
	return RGB_again

#######################################################
#                     4
#######################################################

def to_gray_filter(image,result_folder):
	gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
	os_t = time.time()
	cv2.imwrite(str(result_folder)+'GRAY%s.jpg'%os_t,gray)
	print('\n'+str(result_folder)+'GRAY%s.jpg'%os_t+ '--> DONE')
	return gray

#######################################################
#                     5
#######################################################

def image_threshold_filter(image,result_folder):
	ret, threshold = cv2.threshold(image, 90, 255, 0)
	os_t = time.time()
	cv2.imwrite(str(result_folder)+'GRAY_Threshold%s.jpg'%os_t,threshold)
	print('\n'+str(result_folder)+'GRAY_Threshold%s.jpg'%os_t+ '--> DONE')

#######################################################
#                     6
#######################################################

def medianBlur_filter(image,result_folder):
	blur_image = cv2.medianBlur(image, 3)
	os_t = time.time()
	cv2.imwrite(str(result_folder)+'medianBlur%s.jpg'%os_t,blur_image)
	print('\n'+str(result_folder)+'medianBlur%s.jpg'%os_t+ '--> DONE')


#######################################################
#                     7
#######################################################


def GaussianBlur_filter(image, result_folder):
	gauss_img = cv2.GaussianBlur(image, (9, 9), 2, 2)
	os_t = time.time()
	cv2.imwrite(str(result_folder)+'GaussianBlur%s.jpg'%os_t,gauss_img)
	print('\n'+str(result_folder)+'GaussianBlur%s.jpg'%os_t+ '--> DONE')

#######################################################
#                     8
#######################################################

def binary_inv_threshold(image,result_folder):
	# Threshold.
	# first_value -> Set values equal to or above 220 to 0.
	# second_value ->  values below 220 to 255.
	th, img_th = cv2.threshold(image, 220, 255, cv2.THRESH_BINARY_INV);
	os_t = time.time()
	cv2.imwrite(str(result_folder)+'Binary_Inv_Threshold%s.jpg'%os_t,img_th)
	print('\n'+str(result_folder)+'Binary_Inv_Threshold%s.jpg'%os_t+ '--> DONE')
	return img_th

#######################################################
#                     9
#######################################################
def floodfilled_img(image,result_folder):
	h, w = image.shape[:2] # sizes
	mask = np.zeros((h+2, w+2), np.uint8)
	cv2.floodFill(image, mask, (0,0), 255)
	os_t = time.time()
	cv2.imwrite(str(result_folder)+'Floodfilled%s.jpg'%os_t,image)
	print('\n'+str(result_folder)+'Floodfilled%s.jpg'%os_t+ '--> DONE')
	return image

#######################################################
#                     10
#######################################################

def floodfill_inv(image,result_folder):
	im_floodfill_inv = cv2.bitwise_not(image)
	os_t = time.time()
	cv2.imwrite(str(result_folder)+'Floodfilled_Inv%s.jpg'%os_t,im_floodfill_inv)
	print('\n'+str(result_folder)+'Floodfilled_Inv%s.jpg'%os_t+ '--> DONE')
	return im_floodfill_inv

#######################################################
#                     11
#######################################################

def foreground(image0, image1,result_folder):
	img_combi = image0 | image1
	os_t = time.time()
	cv2.imwrite(str(result_folder)+'IMG_COMBI%s.jpg'%os_t,img_combi)
	print('\n'+str(result_folder)+'IMG_COMBI%s.jpg'%os_t+ '--> DONE')

#******************************************************
#              MAIN
#******************************************************
######	Directory with images verify
img_dir = '/Users/belindabrown/Desktop/PreAnalysis_Img_Recognition/ImgtoAnalyse'
result_folder_path = '/Users/belindabrown/Desktop/PreAnalysis_Img_Recognition/Results'
data_path = os.path.join(img_dir,'*.jpg')
files = glob.glob(data_path)
print("Amount of images that is going to be analized:			", len(files))
######	Analyzing all the images in the folder
for img in sorted(files):
	##### Read each image
	f1 = cv2.imread(img)
	print("\n\n***************\n\n", img, "\n\n***************\n\n") #picture name
	hsv_img_fil = hsv_filter(f1,result_folder_path)
	curr_mask_filter(f1, hsv_img_fil,result_folder_path)
	gray_img = to_gray_filter(f1,result_folder_path)
	image_threshold_filter(gray_img,result_folder_path)
	medianBlur_filter(f1,result_folder_path)
	GaussianBlur_filter(f1,result_folder_path)
	bin_img_th = binary_inv_threshold(f1,result_folder_path)
	image_ff_filter = floodfilled_img(bin_img_th,result_folder_path)
	image_ffinv_filter = floodfill_inv(image_ff_filter,result_folder_path)
	foreground(bin_img_th, image_ffinv_filter,result_folder_path)
