import cv2
import serial
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade.xml')
lower_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_lowerbody.xml')
upper_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_upperbody.xml')
i = 0
ser = serial.Serial()
ser.baudrate = 9600
ser.port = '/dev/ttyUSB0'
ser.open()
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = tuple(face_cascade.detectMultiScale(gray, 1.3, 1))
    lower = tuple(lower_cascade.detectMultiScale(gray, 1.3, 1))
    upper = tuple(upper_cascade.detectMultiScale(gray, 1.3, 1))
    if(len(faces) == 0 and len(lower) == 0  and len(upper) == 0):
      ser.write(b'1')
      print("No humans " + str(i))
    else:
        ser.write(b'0')
        print("Humans present")
        #  for (x,y,w,h) in humans:
             #  cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
ser.write(b'0')
ser.close()
