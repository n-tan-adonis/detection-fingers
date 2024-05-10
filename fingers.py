import cv2
import mediapipe as mp
import time

mp_drawing = mp.solutions.drawing_utils
mp_hand = mp.solutions.hands
hands = mp_hand.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

cap = cv2.VideoCapture(0)
pTime=0
while cap.isOpened():
    ret, img = cap.read()


    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    dem = 0

    # Vẽ bàn tay
    if result.multi_hand_landmarks:
        myHand = []
        dem = 0
        for idx, hand in enumerate(result.multi_hand_landmarks):
            mp_drawing.draw_landmarks(img, hand, mp_hand.HAND_CONNECTIONS)
            for id, lm in enumerate(hand.landmark):
                h, w, c = img.shape
                myHand.append([int(lm.x * w), int(lm.y * h)])   # x=0, y=1
            if myHand[8][1] < myHand[5][1]:
                dem = dem + 1
            if myHand[12][1] < myHand[9][1]:
                dem = dem + 1
            if myHand[16][1] < myHand[13][1]:
                dem = dem + 1
            if myHand[20][1] < myHand[17][1]:
                dem = dem + 1
            if myHand[4][0] < myHand[2][0]:
                dem = dem + 1

    #cv2.putText(img, str(dem), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cTime = time.time()  # trả về số giây, tính từ 0:0:00 ngày 1/1/1970 theo giờ  utc , gọi là(thời điểm bắt đầu thời gian)
    fps = 1 / (cTime - pTime)  # tính fps Frames per second - đây là  chỉ số khung hình trên mỗi giây
    pTime = cTime
    # show fps lên màn hình, fps hiện đang là kiểu float , ktra print(type(fps))
    cv2.putText(img, f"FPS: {int(fps)}", (0, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)


    cv2.putText(img, f"So ngon tay: {dem}", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    print(dem)

    # Hiển thị
    cv2.imshow("Cua so hien thi", img)
    key = cv2.waitKey(1)
    if key == ord("e"):
        break

cap.release()
cv2.destroyAllWindows()
