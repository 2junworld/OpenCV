import os
import cv2
import numpy as np

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

# 변환된 이미지 파일을 원래 이미지 파일명 뒤에 _folder를 추가해 folder에 저장
def save_img(img, img_name, folder_name):
    cv2.imwrite(this_dirname + '/' + folder_name + '/' \
    + img_name[:-4] + '_' + folder_name + img_name[-4:], img)

this_dirname = os.path.dirname(os.path.realpath(__file__))

flname_list = os.listdir(this_dirname + '/image seed') # image seed 폴더의 파일 리스트 가져오기

createFolder(this_dirname + '/mirror') # 현재 파일의 디렉토리에 mirror 폴더 생성

# 그레이스케일로 이미지 읽고 좌우반전 후 mirror 폴더에 저장
i=0
while i < len(flname_list):
    img = this_dirname + '/image seed/' + flname_list[i]
    img = read_grayscale(img)
    img = cv2.flip(img, 1) # 1이면 좌우반전, 0이면 상하반전
    save_img(img, flname_list[i], 'mirror')
    print('complete to save image: ' + str(flname_list[i]))
    i += 1