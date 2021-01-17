[![Header](https://raw.githubusercontent.com/MostafaH04/MagicMouse-HTN2021/master/magicmouse.png "Header")](https://github.com/MostafaH04/MagicMouse-HTN2021)

# MagicMouse-HTN2021
Project for Hack The North 2021 ~ Touch screen capabilities on desktop

- Includes savedmodel for the model created using Customvision.ai (Was not used in the project it self; just for refrence)
- Includes script used to collect data from webcam
- Includes Hand Detection and Mouse controlling / Magic Mouse Script

# 🖥️ Azure customvision.ai

We used customvision.ai to create an object detection model, and was trained to detect hands using a custom dataset, collected using a python script\n
- We created 7 Iterations
- Total of 758 tagged Images (Overall)
- Used well over 1000 Images to train and test the project


# 🐍 Python
We used python libraries mainly including:
- The Azure provided libary (to get predictions)
- OpenCV
- PyAutoGUI
- Imutils
- OS

# 👍 Advantages:
1. Fun to play with :)
2. Would work better with sites that do not require percision, example: Youtube 
3. Easy to use, simply raise ur hand so that it is seen by the webcam and simply move your mouse

# 👎 Disadvantage:
1. Hard to get used to
2. Could be buggy when trying to click
3. Cannot Reach the edges with it
4. Extremely inprecise
5. Webcam is always on
6. Crashes and Lags constantly

# ❓ How to use:
Since the code includes the prediction and training keys which should not be shared, we couldn't share the model itself, so we provided the savedmodel download, and the capture images python script which allows you to collect your own data set and allows you to test the amazing customvision.ai website where you could try training your own model. 

# ✉️ Contact Us!
Feel free to reach out to us on discord if you want to ask us questions or want to learn more about the project
