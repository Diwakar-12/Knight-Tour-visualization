

import cv2

from display import *


def safe(i,j,chessboard):
    if (i<0 or i>=8 or j<0 or j>=8 or chessboard[i][j]!=-1):
        return False
    return True

def filling(i,j,chessboard,jumpnumber):
    chessboard[i][j]= jumpnumber
    image= imageofchessboard(chessboard)
    cv2.imshow("Chessboard",image)
    cv2.waitKey(10)

    if (jumpnumber==63):
        return True
    
    dx=[2,2,-2,-2,1,-1,1,-1]
    dy=[1,-1,1,-1,2,2,-2,-2]
    for dir in range(8):
        newi = i+dx[dir]
        newj = j+dy[dir]


        if(safe(newi,newj,chessboard)==True):

            if(filling(newi,newj,chessboard,jumpnumber+1)==True):
                return True
        
    chessboard[i][j]=-1
    image= imageofchessboard(chessboard)
    cv2.imshow("Chessboard",image)
    cv2.waitKey(10)
    return False

if __name__ == '__main__':
    cv2.namedWindow("Chessboard", cv2.WINDOW_AUTOSIZE)

    chessboard =[[-1 for i in range(8)]for j in range(8)]
    filling(0,0,chessboard,0)


    img = imageofchessboard(chessboard)
    cv2.imshow("Chessboard", img)
    for i in range(8):
        print(chessboard[i])
    cv2.waitKey()
    cv2.destroyAllWindows()
    