import cv2

kamera = cv2.VideoCapture(0)
kamera.set(3, 640)
kamera.set(4, 480)
face_detector = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')
MAXFOTOSAY = 50
face_id = 1
print("\n Kayıtlar başlıyor. Kameraya bak ve bekle ...")

say = 0

while (True):
    ret, img = kamera.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    yuzler = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in yuzler:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        say += 1
        cv2.imwrite("veriseti/" + str(face_id) + '.' + str(say) + ".jpg", gray[y:y + h, x:x + w])
        cv2.imshow('imaj', img)
        print("Kayıt no: ", say)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
    elif say >= MAXFOTOSAY:
        break

print("\n Program sonlanıyor.")
kamera.release()
cv2.destroyAllWindows()