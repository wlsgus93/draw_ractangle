#마우스 드래그로 사각형 , 글자크기 ,
import numpy as np
import cv2
drawing =False
def onMouse(event, x, y, flags, param):
##    global img
    global pt1,pt2
    if event == cv2.EVENT_LBUTTONDOWN:
        #global drawing
       # drawing=True
        pt1=x,y
        print(pt1)
    #elif event == cv2.EVENT_MOUSEMOVE:  # 마우스 이동
        #if drawing == True:
         #   cv2.rectangle(param[0], pt1, pt2, (255, 0, 0))
    elif event == cv2.EVENT_LBUTTONUP:
        pt2=x,y
        #drawinging=False
        print(pt2)

        if pt1[0]<pt2[0]: #무조건 왼쪽 위에만 text출력
            ix=pt1[0]
        else:
            ix=pt2[0]
        if pt1[1]<pt2[1]:
            iy=pt1[1]
        else:
            iy=pt2[1]
        cv2.rectangle(param[0], pt1, pt2, (255, 0, 0))
        text='start:{} end:{} '.format(pt1,pt2)
        text= text + 'height:{} width"{}'.format(abs(pt2[0]-pt1[0]),abs(pt2[1]-pt1[1]))
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, text, (ix,iy), font, 0.5, (255, 0, 0), 1)
    cv2.imshow("img", param[0])
img = np.zeros((512,512,3), np.uint8) + 255
cv2.imshow('img', img)
cv2.setMouseCallback('img', onMouse, [img])
cv2.waitKey()
cv2.destroyAllWindows()

