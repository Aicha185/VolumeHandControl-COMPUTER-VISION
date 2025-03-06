import cv2
import mediapipe as mp
import time


class HandDetector:

    def __init__(self, mode = False , maxHands = 2 , detectionCon= 0.5 , trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands 
        self.mpDraw = mp.solutions.drawing_utils #To draw the hand landmarks on the screen
        self.results = None # to stock the detection's result
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,1, self.detectionCon, self.trackCon)

##################################################################
    #Function to detect the hand
#################################################################3
    def findHands(self , img , draw = True):

        imgRGB = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw :
                    self.mpDraw.draw_landmarks(img , handLms , self.mpHands.HAND_CONNECTIONS)

        
        return img
    
###########################################################################
    #Function to find the position of the hand landmarks
###########################################################################
    def findPositionHand(self , img , draw = True , NoHand = 0):
        landMarksList = []

        if self.results and self.results.multi_hand_landmarks:

            if len(self.results.multi_hand_landmarks) > NoHand:

                myHand = self.results.multi_hand_landmarks[NoHand]
                for id ,lm in enumerate(myHand.landmark):

                    height , width , channel = img.shape
                    cx , cy = int(lm.x * width) , int(lm.y * height)
                    landMarksList.append([id , cx , cy])
                    if draw :
                        cv2.circle(img, (cx,cy) , 5 , (255,0,253),cv2.FILLED)

        return landMarksList







