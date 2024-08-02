import cv2
from cvlib.object_detection import detect_common_objects
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound, PlaysoundException


def speech(text):
    print(text)
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)
    output.save("C:/Users/USER/Desktop/ALL MY TASKS/TSI DATA SCIENCE/Machine Learning/Deep Learning/DeepLearning/sounds/output.mp3")
    try:
        playsound("C:/Users/USER/Desktop/ALL MY TASKS/TSI DATA SCIENCE/Machine Learning/Deep Learning/DeepLearning/sounds/output.mp3")
    except PlaysoundException as e:
        print("Error:", e)


video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Error: Could not open webcam.")
    exit()

items = []

while True:
    ret, frame = video.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    bbox, label, conf = detect_common_objects(frame)  # dataset

    if not label:
        print("No objects detected.")
    else:
        output_image = draw_bbox(frame, bbox, label, conf)
        cv2.imshow("Object Detection", output_image)

        for item in label:
            if item not in items:
                items.append(item)

    if cv2.waitKey(1) & 0xFF == ord(" "):
        break

video.release()
cv2.destroyAllWindows()

i = 0
new_sentence = []

for label in items:
    if i == 0:
        new_sentence.append(f"A CCTV footage behind the principal's office has captured the student as a {label}, and, carrying")
    else:
        new_sentence.append(f"a {label}")

    i = i + 1

speech(" ".join(new_sentence))
