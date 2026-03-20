import cv2 as cv
import numpy as np

# 이미지 로드
img = cv.imread('img.jpg')

# 흑백 전환
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 블러 처리
gray = cv.medianBlur(gray, 9)
#외곽선 검출
edges = cv.Canny(gray, 0,150)
#팽창으로 외곽선을 더 굵게
kernel = np.ones((2, 2), np.uint8)
edges = cv.dilate(edges, kernel, iterations=2)
#외곽선 반전
edges=cv.bitwise_not(edges)


result=img.copy()
n_iteration=10
kernel_size=9
sigma_color=100
sigma_space=2
#뭉개기
for itr in range(n_iteration):
    result = cv.bilateralFilter(result, kernel_size, sigma_color, sigma_space)

cartoon = cv.bitwise_and(result, result, mask=edges)

# 출력
cv.imshow("Cartoon Rendering", cartoon)
cv.waitKey(0)
cv.destroyAllWindows()