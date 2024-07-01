# High Resolution Image Mosaic in Python
June 2019

You will need to use Python, so it is recommended to update it or download it.

This program creates a mosaic of an input image with images from a directory. If you want to download images of puppies, go to the following link:
https://www.kaggle.com/jessicali9530/stanford-dogs-dataset

To run the program, you should have the following Python libraries:
- opencv
- matplotlib
- numpy

The installation is done as follows:

- If your computer runs on Windows operating system, execute the following in the command line or console:
```
python get-pip.py to install pip
pip3 install opencv-python
pip3 install matplotlib
pip3 install numpy-python
```

- If your computer runs on Mac or Linux operating system, execute the following in the command line or console:
```
curl -O https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo pip3 install opencv-python
sudo pip3 install matplotlib
sudo pip3 install numpy
```

To run the program, you should execute the following command:

```python main.py imagen.jpg directory```

Where imagen.jpg is the image to convert (if the image has another extension, put it, for example, if it is png put imagen.png) and directory is the image directory with which the mosaic will be created.
