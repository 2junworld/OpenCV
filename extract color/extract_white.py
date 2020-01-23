import os
import cv2
import numpy as np

directoryRoot = os.path.dirname(os.path.realpath(__file__))

img = cv2.imread(directoryRoot+ '/image seed/roadimage1.jpg')
mark = np.copy(img) #이미지 복사

#  BGR 제한 값 설정
blue_threshold = 200
green_threshold = 200
red_threshold = 200
bgr_threshold = [blue_threshold, green_threshold, red_threshold]

# BGR 제한 값보다 작으면 검은색으로
thresholds = (img[:,:,0] < bgr_threshold[0])\
           | (img[:,:,1] < bgr_threshold[1])\
           | (img[:,:,2] < bgr_threshold[2])
            
mark[thresholds] = [0,0,0]

cv2.imshow('white',mark) # 흰색 추출 이미지 출력
cv2.imshow('result',img) # 이미지 출력
cv2.waitKey(0) 
