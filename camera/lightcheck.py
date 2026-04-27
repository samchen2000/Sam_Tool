# 匯入必要的模組
import cv2  # 用於影像處理
import numpy as np  # 用於數值運算

# 定義函數來計算影像某範圍內的平均亮度
def calculate_brightness(image, x1, y1, x2, y2):
    """
    計算影像在特定範圍內的平均亮度
    :param image: 輸入影像 (OpenCV 影像格式)
    :param x1, y1: 範圍的左上角座標
    :param x2, y2: 範圍的右下角座標
    :return: 範圍內的平均亮度
    """
    # 確保範圍在影像尺寸內
    if x1 < 0 or y1 < 0 or x2 > image.shape[1] or y2 > image.shape[0]:
        raise ValueError("選取範圍超出影像範圍")

    # 裁剪選取範圍內的影像
    region = image[y1:y2, x1:x2]

    # 將影像轉換為灰階（單通道）
    gray_region = cv2.cvtColor(region, cv2.COLOR_BGR2GRAY)

    # 計算灰階範圍內的平均亮度
    brightness = np.mean(gray_region)

    return brightness

# 主程式
if __name__ == "__main__":
    # 讀取影像
    image_path = "example.jpg"  # 修改為您的影像檔案路徑
    image = cv2.imread(image_path)

    # 檢查影像是否成功讀取
    if image is None:
        print("無法讀取影像，請檢查路徑或檔案名稱")
    else:
        # 定義選取範圍 (左上角和右下角座標)
        x1, y1 = 50, 50  # 左上角
        x2, y2 = 150, 150  # 右下角

        # 計算該範圍的平均亮度
        brightness = calculate_brightness(image, x1, y1, x2, y2)

        # 印出結果
        print(f"選取範圍的平均亮度為: {brightness}")