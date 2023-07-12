# MASK2YOLO
## Description
This script can be used to convert binary masks images to [yolo format](https://docs.ultralytics.com/datasets/segment/) segmentation files. It may work not so good when segments have "holes". <br/>
In demo.ipynb you can see detailed logic of this script.
## Requirements
Developed and tested on python 3.10 + opencv
## How to use
### Parameters
The script has following params (defaults should work not so bad): <br/>
*EXTENTION* - the extention of binary masks (png/jpg/...) <br/>
*CLASS_ID* - number of class (for binary segmentation: 1/0) <br/>
*MASK_THRES_MIN* & *MASK_THRES_MAX* - limits to detect mask on binary image <br/>
*AREA_THRES* - minimal part of total image area that contour shoud cover not to be ignored <br/>
*CURVE_RATIO* - parameter to decrease the ammount of points 

### Run
Simply run:
```
python3 converter.py PATH_TO_MASKS PATH_TO_YOLO_MASKS
```
