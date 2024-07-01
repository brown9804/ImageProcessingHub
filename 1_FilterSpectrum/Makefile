#Python3

#                   For Preanlysis
##--------------------------------Makefile------------------------------------
##
## Copyright (C) 2020 by Belinda Brown Ramírez (belindabrownr04@gmail.com)
##	                 Preanlysis for a Image recognition system
##
##-----------------------------------------------------------------------------


# Making python makefile because we need to
# delete the result photos


#******************************************************************************
############  		Modify this part with your own
############ 			files/folders paths.
#******************************************************************************
SRC = ./src/
RESULTS = ./output/



#******************************************************************************
############ 						Run python script
#******************************************************************************
all:  analize

analize:
	python3 $(SRC)main.py

#******************************************************************************
############ 							CLEAN FOR ALL
#******************************************************************************


.PHONY: clean
clean:
	rm -rf $(RESULTS)*.jpg
