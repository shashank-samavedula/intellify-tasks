import cv2 
   
vid = cv2.VideoCapture(0) 
  
while(True): 
      
    ret, frame = vid.read() 
    
    font = cv2.FONT_HERSHEY_SIMPLEX 
    cv2.putText(frame,  
                'BOOYAH!',  
                (50, 50),  
                font, 3,  
                (250, 252, 255),  
                2,  
                cv2.LINE_4)
    cv2.imshow('frame', frame) 

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
vid.release()  
cv2.destroyAllWindows() 
