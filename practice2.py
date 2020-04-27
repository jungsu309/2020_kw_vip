import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
import numpy as np
import qimage2ndarray

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("practice2.ui")[0]


#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    
    def __init__(self) :
        super().__init__()
        
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda : self.Imageshow())
        self.pushButton_flip.clicked.connect(lambda : self.Imageflip())

    def Imageshow(self):
        FileName, _ = QFileDialog.getOpenFileName(self, "Open File", ".")
        
        if FileName:
            image = QImage(FileName)
            
            if image.isNull():
                QMessgeBox.information(self, "Image Viewer", "Cannot load %s" %fileName)
                return ""
            
            qPixmapVar = QPixmap.fromImage(image)
            qPixmapVar = qPixmapVar.scaled(256,256)
            
            self.label.setPixmap(qPixmapVar)
            self.show()
            
            self.count = 0 #횟수 리셋.
            #return FileName
            self.filename = FileName
            
            
    def Imageflip(self):
        
        if self.filename == "":
            print("Please load image first.")
            return

        self.flipimage = QImage(self.filename)

        image_array = qimage2ndarray.rgb_view(self.flipimage)
        
        self.count += 1
        #회전
        #홀수일때 거꾸로 돌리기
        if(self.count % 2 == 1):
            image_array = np.flip(image_array,0)#상하 반전 주는 함수
        #짝수일때 원래 사진 출력하게...아무일도 하지 않게 한다.
        
        self.flipimage = qimage2ndarray.array2qimage(image_array, normalize = False)
        qPixmapVar = QPixmap.fromImage(self.flipimage)
        qPixmapVar = qPixmapVar.scaled(256,256)
        self.label.setPixmap(qPixmapVar)
        self.show()

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()
    yourWindow=WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()
    yourWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
