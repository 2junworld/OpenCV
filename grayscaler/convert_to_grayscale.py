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

dirname_of_this_file = os.path.dirname(os.path.realpath(__file__))
# os.path.dirname(): ()안의 파일이 저장된 폴더의 경로
# os.path.realpath(__file__): 현재 실행 파일의 절대경로

# image seed 폴더의 파일 리스트 가져오기
file_list = os.listdir(dirname_of_this_file + '\image seed')

filename_list = [jpgfile.rstrip('.jpg') for jpgfile in file_list] #.rstrip(): ()안의 문자열을 오른쪽부터 지운다.

# 그레이스케일로 이미지 리드한 리스트 생성
readfile_list = []
i=0
while i < len(file_list):
    readfile_list.append(cv2.imread(dirname_of_this_file + '\image seed\\' + file_list[i], cv2.IMREAD_GRAYSCALE))
    i+=1

# 현재 파일의 디렉토리에 gray 폴더 생성
createFolder(dirname_of_this_file + '\gray')

# 그레이스케일로 변환된 이미지 gray 폴더에 저장

i=0
while i < len(file_list):
    cv2.imwrite(dirname_of_this_file + '\gray\\' + filename_list[i] + '_gray'+ str(i) +'.jpg', readfile_list[i])
    i += 1
    # _grayn을 뒤에 붙여 파일 저장