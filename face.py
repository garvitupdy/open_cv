import cv2
import mediapipe as mp
import time

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()
p_time = 0

eye_cascade = cv2.CascadeClassifier(r"C:\Users\Manisha\OneDrive\Documents\Desktop\open_cv\blurring\haarcascade_eye.xml")
face_cascade = cv2.CascadeClassifier(r"C:\Users\Manisha\OneDrive\Documents\Desktop\open_cv\blurring\haarcascade_frontalface_default.xml")
smile_cascade = cv2.CascadeClassifier(r"C:\Users\Manisha\OneDrive\Documents\Desktop\open_cv\blurring\haarcascade_smile.xml")

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
        if len(eyes) > 0:
            cv2.putText(frame, "Eyes Detected", (x, y-30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

        
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.7, 20)
        if len(smiles) > 0:
            cv2.putText(frame, "Smiling", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)
        else:
            cv2.putText(frame, "No smile", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

    
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            
    results1 = pose.process(frame_rgb)
    
    if results1.pose_landmarks:
        mp_draw.draw_landmarks(frame,results1.pose_landmarks, mpPose.POSE_CONNECTIONS)


    c_time = time.time()
    fps = 1/(c_time - p_time)
    p_time = c_time

    cv2.putText(frame,str(int(fps)), (70,50), cv2.FONT_HERSHEY_PLAIN,3, (255,0,255),3)

    cv2.imshow("Smart Face Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
