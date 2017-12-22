from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QGridLayout, QLineEdit, QPushButton, QWidget


class GridFrame(QWidget):

    def __init__(self):
        super().__init__()
        self.grid()

    def grid(self):
        grid = QGridLayout()
        self.setLayout(grid)

        self.display = QLineEdit("0")
        self.display.setFont(QFont("Times", 18))
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(30)
        grid.addWidget(self.display, 0, 0, 1, 4)

        names = ['Clear', 'Back', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+', ]
        for name in names:
            button = QPushButton(name)
            grid.addWidget(button)
            button.clicked.connect(self.buttonClicked)  # 给每个按钮设置信号/槽


            # positions = [(i, j) for i in range(1, 6) for j in range(4)]
            #
            # for position, name in zip(positions, names):
            #
            #     if name == '':
            #         continue
            #     button = QPushButton(name)
            #     grid.addWidget(button, *position)
            #     button.clicked.connect(self.buttonClicked)  # 给每个按钮设置信号/槽









