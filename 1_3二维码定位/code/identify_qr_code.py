import cv2
import numpy as np
from PIL import Image
from pyzbar.pyzbar import decode

def identify_qr_code(image_path):
    try:
        pil_img = Image.open(image_path)  # 获取PIL图像
        cv_img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)  # 转换为OpenCV格式

        width, height = pil_img.size  # 获取图像尺寸
        centerpoint = width / 2, height / 2  # 计算中心点
        cp_size = 10  # 中心点大小
        matches = decode(pil_img)  # 扫描传入图像，识别其中的二维码
        print(matches)
        count=0
# ####
# matches 变量存储的是 decode 函数返回的一个列表，其中每个元素都是一个 Decoded 对象，代表识别到的 QR 码。每个 Decoded 对象包含以下几个重要属性：
# 1. data：这是识别到的 QR 码中存储的实际数据，通常是一个字符串。例如，可能是一个 URL 或其他文本信息。
# 2. polygon：这是一个包含 QR 码四个角点坐标的列表，通常是一个包含四个点的多边形（如果 QR 码是矩形的）。这些点可以用来绘制 QR 码的轮廓。
# 3. rect：这是一个矩形对象，表示 QR 码在图像中的位置和大小，通常包含 x, y, width, height 属性。
# 4. type：表示识别到的条形码或 QR 码的类型。
# ####
        if matches:
            for match in matches:
                count=count+1
                tl, bl, br, tr = match.polygon  # 获取QR码的四个角点
                match_cp = ((tl.x + bl.x + br.x + tr.x) / 4, (tl.y + bl.y + br.y + tr.y) / 4)  # 计算中心点

                centerpoint_dist = np.linalg.norm(np.array(match_cp) - np.array(centerpoint))  # 计算中心点距离
                outline_color = (0, 0, 255)  # 默认轮廓颜色
                if centerpoint_dist < 10:
                    outline_color = (0, 255, 0)  # 如果距离小于10，改变颜色

                # 绘制轮廓
                cv2.line(cv_img, (tl.x, tl.y), (bl.x, bl.y), outline_color, 3)
                cv2.line(cv_img, (bl.x, bl.y), (br.x, br.y), outline_color, 3)
                cv2.line(cv_img, (br.x, br.y), (tr.x, tr.y), outline_color, 3)
                cv2.line(cv_img, (tr.x, tr.y), (tl.x, tl.y), outline_color, 3)

                # 绘制中心点
                cv2.line(cv_img, (int(match_cp[0] - cp_size), int(match_cp[1] - cp_size)), (int(match_cp[0] + cp_size), int(match_cp[1] + cp_size)), (0, 0, 255), 2)
                cv2.line(cv_img, (int(match_cp[0] - cp_size), int(match_cp[1] + cp_size)), (int(match_cp[0] + cp_size), int(match_cp[1] - cp_size)), (0, 0, 255), 2)

                # 绘制图像中心
                cv2.line(cv_img, (int(centerpoint[0] - cp_size), int(centerpoint[1] - cp_size)), (int(centerpoint[0] + cp_size), int(centerpoint[1] + cp_size)), (255, 0, 0), 2)
                cv2.line(cv_img, (int(centerpoint[0] - cp_size), int(centerpoint[1] + cp_size)), (int(centerpoint[0] + cp_size), int(centerpoint[1] - cp_size)), (255, 0, 0), 2)

                # 绘制文本
                cv2.putText(cv_img, f'{count}code content:{match.data.decode("utf-8")}', (tl.x, tl.y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                
                # 显示二维码中心点坐标
                cv2.putText(cv_img, f'{count}{match_cp}', (int(match_cp[0]), int(match_cp[1] - 20)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                # 在中心点旁边标注坐标（0,0）
                cv2.putText(cv_img, '(0,0)', (int(centerpoint[0] + 10), int(centerpoint[1] - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                print(f'{count}二维码位置: {match_cp}, 编码: {match.data.decode("utf-8")}')  # 同时打印出结果


        cv2.imshow('QR Code Detection', cv_img)  # 显示图像
        cv2.imwrite('output_image.png', cv_img)  # 保存最后的图片
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    except Exception as exc:
        print('Error: %s' % exc)  # 错误日志

if __name__ == '__main__':
    identify_qr_code('test2.png')  # 替换为你的图像路径