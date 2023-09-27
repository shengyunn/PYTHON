import cv2

# 載入 YOLOv7 模型
#net = cv2.dnn.readNet('yolov7.pt', 'yolov7-custom.yaml')  # 替換成你的權重檔和配置文件路徑
net = cv2.dnn.readNet("C:\\Users\\ryan0\\Desktop\\yolov7_Custom\\yolov7-custom\\yolov7_custom.pt", "C:\\Users\\ryan0\Desktop\\yolov7_Custom\\yolov7-custom\\cfg\\training\\yolov7-custom.yaml")

# 載入類別名稱
with open("C:\\Users\\ryan0\Desktop\\yolov7_Custom\\yolov7-custom\\data\\custom_data.yaml", 'r') as f:  # 替換成你的類別名稱文件路徑
    classes = f.read().strip().split('\n')

# 讀取圖片
image = cv2.imread("C:\\Users\\ryan0\\OneDrive\\For GitHub\\PYTHON\\images\\02.jpg")  # 替換成你的圖片路徑
height, width, channels = image.shape

# 將圖片轉換為 blob 格式
blob = cv2.dnn.blobFromImage(image, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(net.getUnconnectedOutLayersNames())

# 顯示辨識結果
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = int(cv2.dnn.NMSBoxes([detection], 0.5, 0.4)[0][0])
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)
            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(image, classes[class_id], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

# 顯示辨識結果
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
