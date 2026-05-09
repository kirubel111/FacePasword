import cv2
import face_recognition
import hashlib

scanned_face_id = None 
is_done = False
user_password = input("inter uer password: ")
cap = cv2.VideoCapture(0)           
print("face scaning...")

while not is_done:
    ret, frame = cap.read()
    if not ret: break

    face_locations = face_recognition.face_locations(frame)
    
    if len(face_locations) > 0:
        face_encodings = face_recognition.face_encodings(frame, face_locations)
        
        if len(face_encodings) > 0:
            scanned_face_id = face_encodings[0] 
            is_done = True 
            print("scan !")

    cv2.imshow('Scanning Face ID...', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

INTERNAL_SECRET = "HG@#61Hdash54#_Kirubel" 

strengthened_data = scanned_face_id + user_password + INTERNAL_SECRET


final_secure_hash = hashlib.sha256(strengthened_data.encode()).hexdigest()

print("\n---Securet---")
print(f"sef pasword : {final_secure_hash}")
