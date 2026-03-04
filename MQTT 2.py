import cv2
import mediapipe as mp
import paho.mqtt.client as mqtt

mqttbroker = "mqtt-dashboard.com"
client = mqtt.Client()
client.connect (mqttbroker)
client.loop_start()
kirim = "aselole"

cap = cv2.VideoCapture(0)
mphand = mp.solutions.hands
hands = mphand.Hands()
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    if result.multi_hand_landmarks:
        client.publish(kirim, "ada tangan")
        print ("ada tangan")
    else :
        client.publish(kirim, "tidak ada tangan")
        print ("tidak ada tangan")
    cv2.imshow("Deteksi",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break