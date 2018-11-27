from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel

import random
import time

from AD_Project.fire import Fire
from AD_Project.text import Text


class CanonGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Button Widget
        self.btnStart = QToolButton()
        self.btnStart.setText('Start!')
        self.btnStart.clicked.connect(self.btnStartClicked)

        self.btnFire = QToolButton()
        self.btnFire.setText('Fire!')
        self.btnFire.clicked.connect(self.btnFireClicked)

        # Label Widget
        self.lbResult = QLabel('Status:')

        self.lbAngle = QLabel('Angle(40 ~ 70):')

        self.lbPower = QLabel('Power(30 ~ 50):')

        # LineEdit Widget
        self.lnResult = QLineEdit()
        self.lnResult.setReadOnly(True)
        self.lnResult.setAlignment(Qt.AlignCenter)

        self.lnAngle = QLineEdit()

        self.lnPower = QLineEdit()

        # TextEdit Widget
        self.txWindow = QTextEdit()
        self.txWindow.setFixedSize(850, 670)
        self.txWindow.setReadOnly(True)
        self.txWindow.setAlignment(Qt.AlignLeft)
        font = self.txWindow.font()
        font.setPointSize(font.pointSize() + 4)
        font.setFamily('Courier New')
        self.txWindow.setFont(font)

        # Layout
        hLayout1 = QHBoxLayout()
        hLayout2 = QHBoxLayout()
        hLayout1.addWidget(self.btnStart)
        hLayout1.addStretch(1)
        hLayout1.addWidget(self.lbResult)
        hLayout1.addWidget(self.lnResult)
        hLayout2.addWidget(self.lbAngle)
        hLayout2.addWidget(self.lnAngle)
        hLayout2.addWidget(self.lbPower)
        hLayout2.addWidget(self.lnPower)
        hLayout2.addStretch(1)
        hLayout2.addWidget(self.btnFire)

        mainLayout = QVBoxLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(hLayout1)
        mainLayout.addWidget(self.txWindow)
        mainLayout.addLayout(hLayout2)

        self.setLayout(mainLayout)
        self.setWindowTitle('Canon Game')

        # Start Game
        self.btnStartClicked()

    def btnStartClicked(self):
        # target 위치 지정
        self.targetColumn = random.randint(40, 60)
        self.targetRow = random.randint(18, 21)
        self.target = (self.targetRow, self.targetColumn)

        # 게임 시작시 초기화
        self.text = Text()
        self.fire = Fire()
        self.gameOver = False

        self.txWindow.setText(self.text.initialMap(self.target))
        self.lnResult.setText("Start!")
        self.lnAngle.clear()
        self.lnPower.clear()

    def btnFireClicked(self):
        self.text = Text()

        # 각도 와 파 설정
        try:
            angle = int(self.lnAngle.text())
            power = int(self.lnPower.text())
        except:
            self.lnResult.setText("Not integer")

        # 게임 완료 시
        if self.gameOver == True:
            self.lnResult.setText("Game Over")
            return
        # 범위에서 벗어난 값을 받았을 경우
        if int(self.lnAngle.text()) < 40 or int(self.lnAngle.text()) > 70 or int(self.lnPower.text()) < 30 or int(self.lnPower.text()) > 50:
            self.lnResult.setText("Not in the range")
            return

        # 현재 맵 출력
        for point in self.fire.parabola(angle, power):
            shape = self.text.currentMap(self.target, point)[0]
            hit = self.text.currentMap(self.target, point)[1]
            self.txWindow.setText(shape)
            if hit:
                self.lnResult.setText("Hit!")
                self.gameOver = True
            else:
                self.lnResult.setText("Miss!")


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = CanonGame()
    game.show()
    sys.exit(app.exec_())