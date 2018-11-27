from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel
from text import Text

import random

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
        self.lbResult = QLabel('Result:')

        self.lbAngle = QLabel('Angle:')

        self.lbPower = QLabel('Power:')

        # LineEdit Widget
        self.lnResult = QLineEdit()
        self.lnResult.setReadOnly(True)
        self.lnResult.setAlignment(Qt.AlignCenter)

        self.lnAngle = QLineEdit()

        self.lnPower = QLineEdit()

        # TextEdit Widget
        self.txWindow = QTextEdit()
        self.txWindow.setFixedSize(650, 650)
        self.txWindow.setReadOnly(True)
        self.txWindow.setAlignment(Qt.AlignLeft)
        font = self.txWindow.font()
        font.setPointSize(font.pointSize() + 4)
        font.setFamily('Courier New')
        self.txWindow.setFont(font)
        self.txWindow.setText(Text().initialShape())

        # Layout
        hLayout1 = QHBoxLayout()
        hLayout2 = QHBoxLayout()
        hLayout1.addWidget(self.btnStart)
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
        # 게임 시작시 초기화
        self.text = Text()
        self.fire = Fire()
        self.gameOver = False

        self.txWindow.setPlaceholderText(self.text.)
        self.lnResult.setText("Start!")
        self.lnAngle.clear()
        self.lnPower.clear()

        # target 위치 지정
        self.targetX = random.randrange(40, 60)
        self.targetY = random.randrange(18, 21)
        self.target = (self.targetX, self.targetY)

    def btnFireClicked(self):
        # 각도 와 힘 설정
        angle = self.lnAngle.text()
        power = self.lnPower.text()

        # 게임 완료 시
        if self.gameOver == True:
            self.lnResult.setText("Game Over")
            return

        # 범위에서 벗어난 값을 받았을 경우
        if self.lnAngle < 30 or self.lnAngle > 50 or self.lnPower < 30 or self.lnPower > 50:
            self.lnResult.setText("Not in the range")
            return

        # 타깃이 맞았을 경우
        for t in self.fire.parabola(angle, power):
            if self.target == t:
                self.lnResult.setText("Hit!")
                self.gameOver = True

        # 윈도우에 대포상태 출력
        self.txWindow.setText(text.)



if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = CanonGame()
    game.show()
    sys.exit(app.exec_())