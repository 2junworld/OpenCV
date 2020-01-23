import os
import cv2
import numpy as np
import shutil

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

# 이미지 밝기 변환
def lux_control(img, value):
    U = np.ones(img.shape, dtype = 'uint8')
    value = int(value)
    if (value >= 0): 
        img = cv2.add(img, U*value)
    else: 
        value = value * (-1)
        img = cv2.subtract(img, U*value)

    return img
    '''
    함수 설명
    U = np.ones(img.shape, dtype = "uint8") 
    pixel unit 정의: img의 픽셀만큼의 공간(행렬)을 만들고, 
    0~255 범위의 데이터타입 지정(픽셀 값의 범위가 0~255이기 때문)
    ones는 각 행렬의 값을 1로 초기화한다.
    '''
# 변환된 이미지 파일을 원래 이미지 파일명 뒤에 _folder를 추가해 folder에 저장
def save_img(img, img_name, folder_name):
    cv2.imwrite(this_dirname + '/' + folder_name + '/' \
    + img_name[:-4] + '_' + folder_name + img_name[-4:], img)

this_dirname = os.path.dirname(os.path.realpath(__file__))

flname_list = os.listdir(this_dirname + '/image seed') # image seed 폴더의 파일 리스트 가져오기

createFolder(this_dirname + '/dark') # 현재 파일의 디렉토리에 mirror 폴더 생성

img = this_dirname + '/image seed/' + flname_list[0]

# 그레이스케일로 이미지 읽고 밝기 50 증가 후 bright 폴더에 저장
i=0
while i < len(flname_list):
    img = this_dirname + '/image seed/' + flname_list[i]
    img = read_grayscale(img)
    img = lux_control(img, -80)
    save_img(img, flname_list[i], 'dark')
    print('complete saving image: ' + str(flname_list[i]))
    i += 1

print("File convert finish!")
os.system("pause")