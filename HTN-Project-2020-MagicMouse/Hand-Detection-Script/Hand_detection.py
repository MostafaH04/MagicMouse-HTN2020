#importing azure cognitive services for custom vision
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials

#Importing other Libaries used for the project
import imutils #used to resize at the end
import pyautogui #used for controlling the mouse
pyautogui.FAILSAFE = False
import cv2 #used to capture, save and display image and visuals
import os #used to delete the temporary image after it is created
#Importing PySerial Used for Serial Communication with the Arduino
import serial

#Defining keys, ids and endpoint to access azure
endpoint = "https://eastus.api.cognitive.microsoft.com/"
training_key = "801a4d52997c4d1a867c367471484fe3"
prediction_key = "135d863df7e042fcad1fb5d42c011edc"
resource_id = "/subscriptions/557ea86a-5b35-49e6-8744-907bcc129f41/resourceGroups/HandClassifier/providers/Microsoft.CognitiveServices/accounts/HTN-Resource"

credentials = ApiKeyCredentials(in_headers={"Training-key": training_key})
train = CustomVisionTrainingClient(endpoint, credentials)
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predict = CustomVisionPredictionClient(endpoint, prediction_credentials)

#Gets the projects available
projects = train.get_projects()

#Finds the project used for HTN - Under projects
for p in projects:
    if p.name == "HandPredictionModel":
        project = p

#Gets the project q
iterations = train.get_iterations("27fd7ed7-6ac0-402a-9896-a934561262b9") 

#Opens webcam
vidFeed = cv2.VideoCapture(0)


#Loop that occurs while the webcam is open
while (vidFeed.isOpened()):
    #Defining keypressed (waits and listens for key presses)
    keyPressed = cv2.waitKey(2)    
    
    #Importing the code that detects the arduino Input
    

    #define frame as the frame of webcam feed
    ret, frame = vidFeed.read()

    #Changes the size of the image such that the aspect ratio is kept the same
    frame = imutils.resize(frame, width = 400)

    #Writes the image as a folder to be used with customvision.ai
    cv2.imwrite("Temp_image.jpg", frame)

    #Gets the predictions based on the image
    with open("Temp_image.jpg", mode = "rb") as modelImage:
        output = predict.detect_image(project.id, "HandPrediction-PyTest4", modelImage)
    
   

    modelPredictions = []
    #Stores the predictions with a probability higher than 50% in the array modelPredictions
    for prediction in output.predictions:
        if prediction.probability > 0.3:
            modelPredictions.append(prediction)
            
            print(prediction.tag_name + " detected with prob of " + str(prediction.probability))
    
    #Used to determine the size of the image
    frame.shape
    
    #left click functionality
    mouseDown = False;

    if len(modelPredictions) > 1:
        if mouseDown == False:
            pyautogui.click()
            mouseDown = True
    elif len(modelPredictions) == 0:
        mouseDown = False

    #Draws the boxes around the "hands"
    if mouseDown == False:
        for predic in modelPredictions:


            #Finding the coordinates of the top left of the box
            xPos = int(predic.bounding_box.left * frame.shape[1])
            yPos = int(predic.bounding_box.top * frame.shape[0])

            #Finding the width and height of the box
            width = int(predic.bounding_box.width * frame.shape[1])
            height = int(predic.bounding_box.height * frame.shape[0])

            #Finds the width and height of the screen, then finds the ratio between the size of the screen and the images
            sWidth, sHeight = pyautogui.size()
            fWidth = frame.shape[1]
            fHeight = frame.shape[0]
            
            yMultiplier = sHeight / (fHeight)
            xMulitplier = sWidth / (fWidth)

            #Draws the rectangl around the "hands" using openCV
            frame = cv2.rectangle(frame, (xPos, yPos), (xPos + width, yPos + height), (168, 109, 50), 1)
            frame = cv2.circle(frame, (int(xPos + (width)/2), int(yPos + (height)/2)), 3, (168, 109, 50), 1)
            
            #Moves the mouse relative to the position of the hand
            pyautogui.moveTo(sWidth - (int(xPos + (width/2))) * xMulitplier, (int(yPos + (height/2))) * yMultiplier)
            

    #Displays the image 
    cv2.imshow("Display", frame)

    os.remove("Temp_image.jpg")

    if keyPressed == ord('q'):
        break

vidFeed.release()
cv2.destroyAllWindows()
quit()

