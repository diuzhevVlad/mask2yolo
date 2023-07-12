import cv2
import sys
import glob
import os

CLASS_ID = 0
CURVE_RATIO = 0.005
AREA_THRES = 0.005
MASK_THRES_MIN, MASK_THRES_MAX = 127,255

def generate_yolo_mask_txt(mask):
    height, width = mask.shape
    _, thresh = cv2.threshold(mask,MASK_THRES_MIN, MASK_THRES_MAX ,0)
    contours, _ = cv2.findContours(thresh, 1, 2)
    new_contours = []
    for cnt in contours:
        if cv2.contourArea(cnt) > AREA_THRES*height*width:
            new_contours.append(cnt)
    
    approx = []
    for cnt in new_contours:
        epsilon = CURVE_RATIO*cv2.arcLength(cnt,True)
        approx.append(cv2.approxPolyDP(cnt,epsilon,True))


    file_s = ""

    for i, app in enumerate(approx):
        file_s += f"{CLASS_ID} "
        for point in app:
            p = point.reshape(-1)
            file_s += f"{p[0]/width} {p[1]/height} "
        if i + 1 != len(approx):
            file_s += "\n"

    return file_s

if __name__ == "__main__":
    file_arr = glob.glob(sys.argv[1]+"/*.png")
    if not os.path.exists(sys.argv[2]):
        os.makedirs(sys.argv[2])
    for file in file_arr:
        s = generate_yolo_mask_txt(cv2.imread(file, cv2.IMREAD_GRAYSCALE))
        filename = file.split('/')[-1]
        with open(sys.argv[2] + "/" + ''.join(filename.split('.')[:-1]+[".txt"]),"w") as f:
            f.writelines(s)
    
            