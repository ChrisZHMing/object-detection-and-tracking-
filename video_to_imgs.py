import cv2
vidcap = cv2.VideoCapture('challenge_video.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
    success,image = vidcap.read()
    count_str = "{}".format(count).zfill(5)
    filename = "//{}.jpg".format(count_str)
    cv2.imwrite(filename, image)
    print(filename)
    count += 1

print("done")

