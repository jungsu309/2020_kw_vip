#!/usr/bin/env python
# coding: utf-8

# In[16]:


import cv2

#open image 이미지 열기
img = cv2.imread('fruits.png')
#이미지 좌우반전
img_reverse = cv2.flip(img,1)


#이미지 회전을 위해 해당 이미지의 높이 너비 채널값을 저장한다.
height, width, channel = img.shape

#cv2.getRotationMatrix2D((중심점 X좌표, 중심점 Y좌표), 각도, 스케일)를 이용하여 사진을 돌린다
#사진 돌리기
matrix = cv2.getRotationMatrix2D((width/2, height/2), 180, 1)
#위의 회전함수 적용하기
img_180 = cv2.warpAffine(img, matrix, (width, height))


#사진을 두배 작게 만드는 함수
img_small = cv2.pyrDown(img);


#사진들을 화면에 띄운다.
cv2.imshow('furits_show',img)
cv2.imshow('furits_reverse_show',img_reverse)
cv2.imshow('furits_180turn_show',img_180)
cv2.imshow('furits_small_show',img_small)

cv2.waitKey(0)
cv2.destroyAllWindows()


# In[ ]:




