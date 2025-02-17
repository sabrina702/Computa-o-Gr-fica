import cv2

source_video = "C:/Users/Lenovo/Downloads/Prova I/Imagens/video_cachorro.mp4"
cap = cv2.VideoCapture(source_video)

if __name__ == "__main__":
     
    img_carro = cv2.imread("C:/Users/Lenovo/Downloads/Prova I/Imagens/Imagen_cachorro.jpg")
    cv2.imshow("img", img_carro)

    box = cv2.selectROI("select roi", img_carro, fromCenter=False)

    #(674, 249, 225, 183)
    tracker = cv2.TrackerCSRT_create()
    tracker.init(img_carro, box)

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        sucesso, box = tracker.update(frame)

        if sucesso:
            pt1 = (box[0], box[1])
            pt2 = ((box[0] + box[2]), (box[1] + box[3]))
            cv2.rectangle(frame, pt1, pt2, (255, 0, 0), 2, 1)
        else:
            print("FALHOU")

        cv2.imshow("Tracking", frame)

        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
