# 图像拼接(目前效果不好)
import cv2 as cv
import numpy as np


def detectAndDescribe(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    sift = cv.SIFT_create()
    kps, des = sift.detectAndCompute(gray, None)
    # kps = np.float([kp.pt for kp in kps])
    return (kps, des)


imageA = cv.imread("./img/pj2.png")

imageB = cv.imread("./img/pj1.png")

kpsA, featuresA = detectAndDescribe(imageA)
kpsB, featuresB = detectAndDescribe(imageB)
# 将结果转换成NumPy数组
kpsA = np.float32([kpA.pt for kpA in kpsA])
kpsB = np.float32([kpB.pt for kpB in kpsB])
# 建立暴力匹配器
matcher = cv.BFMatcher()
# 使用KNN检测来自A、B图的SIFT特征匹配对，K=2
rawMatches = matcher.knnMatch(featuresA, featuresB, k=2)
print(np.array(rawMatches).shape)
matches = []
for m, n in rawMatches:
    if m.distance < 0.5 * n.distance:
        matches.append((m.trainIdx, m.queryIdx))
print(np.array(matches).shape)
print("zj")
print(len(matches))

if len(matches) > 4:
    # 获取匹配对的点坐标
    ptsA = np.float32([kpsA[i] for (_, i) in matches])
    print(ptsA.shape)
    ptsB = np.float32([kpsB[i] for (i, _) in matches])
    # 计算视角变换矩阵
    H, status = cv.findHomography(ptsA, ptsB, cv.RANSAC, 4.0)
    print(H.shape)
    print(status.shape)

# 将图片A进行视角变换，result是变换后图片
hA, wA = imageA.shape[:2]
print((hA, wA))
hB, wB = imageB.shape[:2]
print((hB, wB))

result = cv.warpPerspective(imageA, H, (wA+wB, hA))
cv.imshow('result1', result)
cv.waitKey(0)
# 将图片B传入result图片最左端
result[:hB, :wB] = imageB

# result[0:imageB.shape[0], 0:imageB.shape[1]] = imageB

cv.imshow('result2', result)
cv.waitKey(0)

# 可视化
vis = np.zeros((hA, wA+wB, 3), dtype=np.uint8)
vis[0:hA, 0:wA] = imageA
vis[0:hB, wA:] = imageB
# 联合遍历，画出匹配对
for ((trainIdx, queryIdx), s) in zip(matches, status):
    # 当点对匹配成功时，画到可视化图上
    if s == 1:
        # 画出匹配对
        ptA = (int(kpsA[queryIdx][0]), int(kpsA[queryIdx][1]))
        ptB = (int(kpsB[trainIdx][0]) + wA, int(kpsB[trainIdx][1]))
        cv.line(vis, ptA, ptB, (0, 255, 0), 1)
cv.imshow("Keypoint Matches", vis)
cv.waitKey(0)
