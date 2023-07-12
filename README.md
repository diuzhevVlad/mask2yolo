# MASK2YOLO
## Description
This script can be used to convert binary masks images to [yolo format](https://docs.ultralytics.com/datasets/segment/) segmentation files. It may work not so good when segments have "holes".
In demo.ipynb you can see detailed logic of this script.
## Requirements
Developed and tested on python 3.10 + opencv
## How to use
### Parameters
The script has 5 params:
*CLASS_ID* - number of class (for binary segmentation: 1/0)
*MASK_THRES_MIN* & *MASK_THRES_MAX* - limits to detect mask on binary image
*AREA_THRES* - minimal part of total image area that contour shoud cover not to be ignored
*CURVE_RATIO* - parameter to decrease the ammount of points
### Run
Simply run:
```
python3 converter.py PATH_TO_MASKS PATH_TO_YOLO_MASKS
```
