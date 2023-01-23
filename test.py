import cv2
import requests
from PIL import Image
url = "http://localhost:8000/image-to-json"
payload={}
headers = {}
print("start")


cap=cv2.VideoCapture(0)
process_this_frame=10
while True:
    # Grab a single frame of video
    ret, frame = cap.read()
    if process_this_frame == 10:
        process_this_frame=0
        # Resize frame of video to 1/4 size for faster face recognition processing
        im = Image.fromarray(frame)
        im.save("your_file.jpeg")
        files = [
            ('file', ('your_file.jpeg', open('your_file.jpeg', 'rb'), 'image/jpeg'))
        ]
        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        print(response.text)
    process_this_frame+=1
    # ind_time = datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
    # print(face_names,ind_time[11:19])
    # for (top, right, bottom, left), name in zip(face_locations, face_names):
    #     # Scale back up face locations since the frame we detected in was scaled to 1/4 size
    #     top *= 4
    #     right *= 4
    #     bottom *= 4
    #     left *= 4
    #
    #     # Draw a box around the face
    #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        # cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        # font = cv2.FONT_HERSHEY_DUPLEX
        # cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # cv2.imshow('webcam',img)
    # cv2.waitKey(1)