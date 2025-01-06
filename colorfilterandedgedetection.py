import cv2
import numpy as np

def apply_filter(image, filter_type):
    filtered_img=image.copy
    if filter_type=="red tint":
        filtered_img[:,:,1]=0
        filtered_img[:,:0]=0
    elif filter_type=="green tint":
        filtered_img[:,:,0]=0
        filtered_img[:,:2]=0
    elif filter_type=="blue tint":
        filtered_img[:,:,1]=0
        filtered_img[:,:2]=0
    elif filter_type =="canny":
        gray_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        edges=cv2.Canny(gray_img,100,200)
        return cv2.cvtColor(edges, cv2.COLOR_GRAY2BG)
    elif filter_type=="sobel":
        gray_img=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        sobelx=cv2.Sobel(gray_img,cv2.CV_64F,1,0,ksize=3)
        sobely=cv2.Sobel(gray_img,cv2.CV_64F,0,1,ksize=3)
        combined_sobel=cv2.bitwise_or(sobelx.astype("uint8"),sobely.astype("uint8"))
        filtered_img=cv2.cvtColor(combined_sobel,cv2.COLOR_GRAY2BGR)

    imgpath="3x3 logo.png"
    image=cv2.imread(imgpath)
    if image is None:
        print("Error: Image not found")
    else:
        print("press the following keys to apply filters:")
        print("R = Red tint")
        print("B = Blue tint")
        print("G = Green tint")
        print("S = Sobel edge detection")
        print("C = Canny edge detection")
        print("q = Quit")
        while True:
            filteredimg_path=apply_filter(image,filter_type)
            cv2.imshow("Filtered Image",filteredimg_path)
            key=cv2.waitKey(0) & 0xFF
            if key==ord("G"):
                   filter_type="green tint"
            elif key==ord("c"):
                   filter_type="canny"
            elif key==ord("s"):
                   filter_type="sobel"
            elif key==ord("r"):
                   filter_type="red tint"
            elif key==ord("b"):
                   filter_type="blue tint"
            elif key==ord("q"):
                   print("EXITING...")
                   break
            else:print("Invalid Key")
            
cv2.destroyAllWindows()


        
    