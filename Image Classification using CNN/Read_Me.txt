Requirements:

To make this program functional you need basic Python libraries like numpy, matplotlib and also opencv and tensorflow.

to install all you need to execute these commands in cmd

pip install opencv-python
pip install tensorflow
pip install numpy
pip install matplotlib


How to test on a new image?

Step 1:
Download any image from the internet of the below given ten items.

Step 2:
Scale the image into 32 x 32 size

Step 3:
Store the image in the same folder where you have this execution file.

Step 4:
For the image that you want to test, pass the name of that image into this line in the code below:

img = cv.imread('horse.jpg')

Replace horse.jpg with your image name.

List of class names that this program classifies:

The images that this program can classify are:

1. Plane
2. Car
3. Bird
4. Cat
5. Deer
6. Dog
7. Frog
8. Horse
9. Ship
10. Truck

Note:

Make sure to ask any questions that you want.

For the first time, the program might take some time to download the data.

No time will be taken to train the model as I have already provided the trained model with the execution files. 

You do not need to download anything else additionally.

Try your own selected images and check if the predictions are good or not.

Make the code your own enjoy :) 

