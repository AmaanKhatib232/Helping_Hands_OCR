# Importing important modules for the required project

import numpy as np
import easyocr
import cv2
from cv2 import *
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image
import pyttsx3
#import imutils

# from pytesseract import pytesseract


print("\n")

# Reading the image from the image input or video input

'''
mywebcam = cv2.VideoCapture(0)
#
while True:
     test, image = mywebcam.read()
     #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     print(test)

     cv2.imshow('image', gray)
     cv2.waitKey()

     if cv2.waitKey(1) & 0xFF == ord('s'):
         cv2.imwrite('test1.jpg', gray)
         break
         
mywebcam.release()
cv2.destroyAllWindows()
'''

# Extremely Sorry, due to latest update the above query is discarded from the module .........

# # #

image_path = 'sentence.jpeg'

readMyImage = easyocr.Reader(['en'], gpu=False)
myResult = readMyImage.readtext(image_path)
print(myResult)

 # Drawing the results from the outputText for a single word

# topLeftCoord = tuple(myResult[0][0][0])
# bottomRightCoord = tuple(myResult[0][0][2])
# outputText = myResult[0][1]
# font = cv2.FONT_HERSHEY_COMPLEX
#
# '''
# img = cv2.imread(image_path)
# img = cv2.rectangle(img,topLeftCoord,bottomRightCoord,(0,255,0),3)
# img = cv2.putText(img, outputText, topLeftCoord, font, 0.5, (255,255,255), 2, cv2.LINE_AA)
# plt.imshow(img)
# plt.show()
# '''
#

 # Drawing the results from the outputText for a line of words


img = cv2.imread(image_path)
outputTextFinal = []
spacer = 100
for detection in myResult:
    topLeftCoord = tuple(detection[0][0])
    bottomRightCoord = tuple(detection[0][2])
    text = detection[1]
    #img = cv2.rectangle(img, topLeftCoord, bottomRightCoord, (0, 255, 0), 3)
    #font = cv2.FONT_HERSHEY_SIMPLEX
    #img = cv2.putText(img, text, (20, spacer), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
    spacer += 15
    outputTextFinal.append(text)
    # voice = pyttsx3.init()
    # voice.setProperty("rate", 120)
    # voice.say(outputText)
    # voice.runAndWait()

#plt.imshow(img)

#plt.show()

print(outputTextFinal)

finalString = " ".join(outputTextFinal)
print(finalString)


# Converting Text to Audio

voice = pyttsx3.init()
voice.setProperty("rate", 120)
voice.say(finalString)
voice.runAndWait()


# And the final SDP project is ready......
# Very much excited to continue the same for further modifications.....