import os
import cv2
import numpy as np

'''
image seed 폴더의 이미지를 그레이스케일로 변환하여 gray 폴더에 저장하는 코드
'''

# 디렉토리가 존재하지 않으면 디렉토리 생성하는 함수
def createFolder(directory): 
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory.', + directory)

# 그레이스케일로 이미지 리드
def read_grayscale(img): #img는 img파일의 경로를 입력해야함
    return cv2.imread(img, cv2.IMREAD_GRAYSCALE)

this_dirname = os.path.dirname(os.path.realpath(__file__))
# os.path.dirname(): ()안의 파일이 저장된 폴더의 경로
# os.path.realpath(__file__): 현재 실행 파일의 절대경로

# image seed 폴더의 파일 리스트 가져오기
file_list = os.listdir(this_dirname + '/image seed')

# 현재 파일의 디렉토리에 gray 폴더 생성
createFolder(this_dirname + '/gray')

# 그레이스케일로 이미지 읽고 gray 폴더에 저장
i=0
while i < len(file_list):
    img = this_dirname + '/image seed/' + file_list[i]
    gray_img = read_grayscale(img)
    cv2.imwrite(this_dirname + '/gray/' + file_list[i].rstrip('.jpg') + '_gray.jpg', gray_img)
    i += 1
