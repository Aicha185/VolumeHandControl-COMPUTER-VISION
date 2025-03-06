import cv2
import time
import  VolumeHandControl


class Main:
       
                

        def main(self):


            
##############################################################
#       Webcam configuration
#################################################################
            wCam , hCam = 640 ,480
            cap = cv2.VideoCapture(0)
            
            cap.set(3,wCam)
            cap.set(4,hCam)
            pTime =0
            cTime = time.time()
            fps = 1/(cTime - pTime)

            while True:
               
                
                success , img = cap.read()
                if not success:
                    print("Erreur lors de la capture de l'image.")
                    break


                
                img =VolumeHandControl.start_hand_tracking(img)
                cv2.putText(img , f'FPS: {int(fps)}' , (20 , 40) , cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),3)
                cv2.imshow('Img' , img)
                
                

                if cv2.waitKey(1) & 0xFF == ord('q'):
                            break

            cap.release()  
            cv2.destroyAllWindows() 

main = Main()
main.main()