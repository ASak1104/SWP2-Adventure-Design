from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel, QSlider
from PyQt5.QtCore import QEventLoop, QTimer

import random

from fire import Fire
from cannon import Cannon


class CanonGame(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Button Widget
        self.btnNewGame = QToolButton()
        self.btnNewGame.setText('New Game!')
        self.btnNewGame.clicked.connect(self.btnNewGameClicked)

        self.btnFire = QToolButton()
        self.btnFire.setText('Fire!')
        self.btnFire.clicked.connect(self.btnFireClicked)

        # Label Widget
        self.lbResult = QLabel('Status:')

        self.lbAngle = QLabel('Angle(40 ~ 70):')

        self.lbPower = QLabel('Power(30 ~ 50):')

        self.lbBullet = QLabel('Bullet: ')

        # LineEdit Widget
        self.lnResult = QLineEdit()
        self.lnResult.setReadOnly(True)
        self.lnResult.setAlignment(Qt.AlignCenter)

        self.lnBullet = QLineEdit()
        self.lnBullet.setReadOnly(True)
        self.lnBullet.setAlignment(Qt.AlignCenter)

        # QSlider Widget
        self.slAngle = QSlider(Qt.Horizontal)
        self.slAngle.setMinimum(40)
        self.slAngle.setMaximum(70)
        self.slAngle.setValue(55)
        self.slAngle.setTickPosition(QSlider.TicksBelow)
        self.slAngle.setTickInterval(5)
        self.slAngle.setFixedWidth(200)

        self.slPower = QSlider(Qt.Horizontal)
        self.slPower.setMinimum(30)
        self.slPower.setMaximum(50)
        self.slPower.setValue(55)
        self.slPower.setTickPosition(QSlider.TicksBelow)
        self.slPower.setTickInterval(5)
        self.slPower.setFixedWidth(200)

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
        hLayout1.addWidget(self.btnNewGame)
        hLayout1.addStretch(1)
        hLayout1.addWidget(self.lbBullet)
        hLayout1.addWidget(self.lnBullet)
        hLayout1.addWidget(self.lbResult)
        hLayout1.addWidget(self.lnResult)
        hLayout2.addWidget(self.lbAngle)
        hLayout2.addWidget(self.slAngle)
        hLayout2.addWidget(self.lbPower)
        hLayout2.addWidget(self.slPower)
        hLayout2.addStretch(1)
        hLayout2.addWidget(self.btnFire)

        mainLayout = QVBoxLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)
        mainLayout.addLayout(hLayout1)
        mainLayout.addWidget(self.txWindow)
        mainLayout.addLayout(hLayout2)

        self.setLayout(mainLayout)
        self.setWindowTitle('Cannon Game')

        # Start Game
        self.btnNewGameClicked()

    def btnNewGameClicked(self):
        # target 위치 지정
        self.targetColumn = random.randint(40, 60)
        self.targetRow = random.randint(18, 21)
        self.target = (self.targetRow, self.targetColumn)

        # 게임 시작시 초기화
        self.cannon = Cannon(self.target)
        self.fire = Fire()
        self.gameOver = False
        self.bullet = 5

        self.txWindow.setText(self.cannon.initialMap())
        self.lnResult.setText('Start!')
        self.lnBullet.setText(str(self.bullet))
        self.slAngle.setValue(55)
        self.slPower.setValue(40)


    def btnFireClicked(self):
        self.cannon = Cannon(self.target)

        # 각도 와 파워 설정
        try:
            angle = int(self.slAngle.value())
            power = int(self.slPower.value())
        except:
            self.lnResult.setText('Not integer')
            return

        # 게임 완료 시
        if self.gameOver == True:
            self.lnResult.setText('Game Over')
            return

        # 현재 맵 출력
        for point in self.fire.parabola(angle, power):
            shape = self.cannon.currentMap(point)[0]
            hit = self.cannon.currentMap(point)[1]
            self.txWindow.setText(shape)
            if hit:
                self.lnResult.setText('Hit!')
                self.gameOver = True
                break
            else:
                self.lnResult.setText('Miss!')
            # Text animation effect
            loop = QEventLoop()
            QTimer.singleShot(100, loop.quit)
            loop.exec_()
        self.bullet -= 1
        self.lnBullet.setText(str(self.bullet))
        if self.bullet == 0:
            self.gameOver = True

    # 단축키 설정
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_N:
            self.btnNewGameClicked()
        elif e.key() == Qt.Key_Enter or Qt.Key_Return:
            self.btnFireClicked()


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = CanonGame()
    game.show()
    sys.exit(app.exec_())