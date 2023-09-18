import cv2
import numpy as np


def imageofchessboard(chessboard):
    img = np.ones((401, 401, 3), np.uint8)
    img[:] =[0,255,0]
    cv2.line(img, (0, 200), (400, 200), (255, 255, 255), 1)
    cv2.line(img, (200, 0), (200, 400), (255, 255, 255), 1)
    i = 0
    j = 0

    while i <= 8:
        cv2.line(img, (i * 50, 0), (i * 50, 400), (255, 255, 255), 1)
        i += 1
    while j <= 8:
        cv2.line(img, (0, j * 50), (400, j * 50), (255, 255, 255), 1)
        j += 1
    rowindex =0 
    while(rowindex<=7):
        if rowindex % 2 ==0 :
            
            for i in range(50):
                row = rowindex*50 +i
                colindex=0
                while(colindex<=7):
                    if colindex%2 ==0 :
                        
                        for j in range(50):
                            col = colindex*50 + j

                            img[row][col] = [255,255,255]


                    colindex+=1
        rowindex+=1
                
    rowindex =0 


    while(rowindex<=7):
        if rowindex % 2 !=0 :
            
            for i in range(50):
                row = rowindex*50 +i
                colindex=0
                while(colindex<=7):
                    if colindex%2 !=0 :
                        
                        for j in range(50):
                            col = colindex*50 + j

                            img[row][col] = [255,255,255]


                    colindex+=1
        rowindex+=1
    imgknight = cv2.imread("knight.png",cv2.IMREAD_COLOR)
    for r in range(8):
        for c in range(8):
            if(chessboard[r][c]!=-1):
                img[r*50 : r*50+imgknight.shape[0],c*50 : c*50+imgknight.shape[1]] = imgknight
    

    return img


