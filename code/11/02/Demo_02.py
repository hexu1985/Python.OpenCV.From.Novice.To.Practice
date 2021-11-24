import cv2

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW) # 打开笔记本内置摄像头
while (capture.isOpened()): # 笔记本内置摄像头被打开后
    retval, image = capture.read() # 从摄像头中实时读取视频
    # 把彩色视频转换为灰度视频
    image_Gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    if retval == True: # 读取到摄像头视频后
        cv2.imshow("Video", image) # 在窗口中显示彩色视频
        cv2.imshow("Video_Gray", image_Gray) # 在窗口中显示灰度视频
    key = cv2.waitKey(1) # 窗口的图像刷新时间为1毫秒
    if key == 32: # 如果按下空格键
        break
capture.release() # 关闭笔记本内置摄像头
cv2.destroyAllWindows() # 销毁显示摄像头视频的窗口
