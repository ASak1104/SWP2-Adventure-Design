from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QToolButton, QLabel


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
        self.txWindow.setReadOnly(True)
        self.txWindow.setAlignment(Qt.AlignLeft)
        font = self.txWindow.font()
        font.setPointSize(font.pointSize() + 8)
        font.setFamily('Courier New')
        self.txWindow.setFont(font)

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
        pass

    def btnFireClicked(self):
        pass

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    game = CanonGame()
    game.show()
    sys.exit(app.exec_())