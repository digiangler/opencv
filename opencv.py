import cv2

# 画像の読み込み
img = cv2.imread("sample.jpg")

# グレースケール変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 画像の保存
cv2.imwrite("gray.jpg", gray)
