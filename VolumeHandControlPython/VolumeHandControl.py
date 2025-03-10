import cv2
import mediapipe as mp
import time
import numpy as np
import math
import tkinter as tk
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import HandTrackingModule





def  start_hand_tracking(image):
    ##############################################################
#       Audio configuration
#################################################################
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)
    volRange = volume.GetVolumeRange() #-65,25db -- 0.0 db
    minVol, maxVol = volRange[0],volRange[1]
    volBar , volPer = 400 , 0
    detector = HandTrackingModule.HandDetector(detectionCon = 0.8)
    
    img = detector.findHands(image)
    lmList = detector.findPositionHand(img , draw=False)

    if len(lmList) != 0:

        x1 ,y1 = lmList[4][1] , lmList[4][2]
        x2 ,y2 = lmList[8][1] , lmList[8][2]

        cx ,cy = (x1+x2)//2 , (y1+y2)//2

        cv2.circle(img , (x1 , y1) ,15 ,(255,0,255) ,cv2.FILLED)
        cv2.circle(img , (x2, y2) ,15 ,(255,0,255) ,cv2.FILLED)
        #create a line between them
        cv2.line(img , (x1,y1),(x2,y2),(255 ,0,255),3)
        cv2.circle(img , (cx , cy) ,5 ,(255,0,255) ,cv2.FILLED)
        
        length = math.hypot(x2-x1 , y2-y1)
        #HandRange 50-300
        #volume range -65 to 0


        vol =  vol = np.interp(length ,[50,300],[minVol , maxVol])
        volBar = np.interp(length ,[50,300],[400 , 150])
        volPer = np.interp(length ,[50,300],[0 , 100])
        print(int(length),vol)
        print(int(length),vol)
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
                cv2.circle(img , (cx , cy) ,4 ,(0,255,0),cv2.FILLED)
                volume.SetMasterVolumeLevel(minVol, None)  
                cv2.putText(img, "MUTE", (200, 450), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)

    cv2.rectangle(img ,(50,150) , (85,400), (0,255 ,0) )
    cv2.rectangle(img ,(50,int(volBar)) , (85,400), (0,255 ,0) ,cv2.FILLED)
    cv2.putText(img , f'{int(volPer)}%' , (40,450) , cv2.FONT_HERSHEY_COMPLEX ,2,(255,0,0),3)
    return img







            

    



