from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
import sys


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.operation = None
        self.initUI()
        self.mu_input = []
        self.operand_1 = 0
        self.operand_2 = 0

    def initUI(self):
        self.setGeometry(300, 300, 225, 425)
        self.setWindowTitle("калькулятор")

        self.label = QLabel(self)
        self.label.setText('0')
        self.label.resize(225, 95)
        self.move(0, 0)

        self.nun_1 = QPushButton('1', self)
        self.nun_1.resize(50, 50)
        self.nun_1.move(5, 100)

        self.nun_2 = QPushButton('2', self)
        self.nun_2.resize(50, 50)
        self.nun_2.move(60, 100)

        self.nun_3 = QPushButton('3', self)
        self.nun_3.resize(50, 50)
        self.nun_3.move(115, 100)

        self.div = QPushButton('/', self)
        self.div.resize(50, 50)
        self.div.move(170, 100)

        self.nun_4 = QPushButton('4', self)
        self.nun_4.resize(50, 50)
        self.nun_4.move(5, 155)
        # self.nun_1.clicked.connect()

        self.nun_5 = QPushButton('5', self)
        self.nun_5.resize(50, 50)
        self.nun_5.move(60, 155)

        self.nun_6 = QPushButton('6', self)
        self.nun_6.resize(50, 50)
        self.nun_6.move(115, 155)

        self.mul = QPushButton('*', self)
        self.mul.resize(50, 50)
        self.mul.move(170, 155)

        self.nun_7 = QPushButton('7', self)
        self.nun_7.resize(50, 50)
        self.nun_7.move(5, 210)

        self.nun_8 = QPushButton('8', self)
        self.nun_8.resize(50, 50)
        self.nun_8.move(60, 210)

        self.nun_9 = QPushButton('9', self)
        self.nun_9.resize(50, 50)
        self.nun_9.move(115, 210)

        self.plus = QPushButton('+', self)
        self.plus.resize(50, 50)
        self.plus.move(170, 210)

        self.nun_0 = QPushButton('0', self)
        self.nun_0.resize(50, 50)
        self.nun_0.move(5, 265)

        self.minus = QPushButton('-', self)
        self.minus.resize(50, 50)
        self.minus.move(60, 265)

        self.step = QPushButton('^()', self)
        self.step.resize(50, 50)
        self.step.move(115, 265)

        self.sqrt = QPushButton('√', self)
        self.sqrt.resize(50, 50)
        self.sqrt.move(170, 265)

        self.proc = QPushButton('%', self)
        self.proc.resize(66, 50)
        self.proc.move(5, 320)

        self.cel = QPushButton('//', self)
        self.cel.resize(66, 50)
        self.cel.move(79, 320)

        self.kvad = QPushButton('^2', self)
        self.kvad.resize(66, 50)
        self.kvad.move(154, 320)

        self.ravn = QPushButton('=', self)
        self.ravn.resize(155, 50)
        self.ravn.move(5, 375)

        self.c = QPushButton('c', self)
        self.c.resize(50, 50)
        self.c.move(170, 375)

        self.nun_1.clicked.connect(self.one)
        self.nun_2.clicked.connect(self.two)
        self.nun_3.clicked.connect(self.tree)
        self.nun_4.clicked.connect(self.four)
        self.nun_5.clicked.connect(self.five)
        self.nun_6.clicked.connect(self.six)
        self.nun_7.clicked.connect(self.seven)
        self.nun_8.clicked.connect(self.eight)
        self.nun_9.clicked.connect(self.nine)
        self.nun_0.clicked.connect(self.zero)
        self.plus.clicked.connect(self.plus_1)
        self.minus.clicked.connect(self.minus_1)
        self.div.clicked.connect(self.div_1)
        self.mul.clicked.connect(self.mul_1)
        self.step.clicked.connect(self.step_1)
        self.sqrt.clicked.connect(self.sqrt_1)
        self.proc.clicked.connect(self.proc_1)
        self.cel.clicked.connect(self.cel_1)
        self.kvad.clicked.connect(self.kvad_1)
        self.ravn.clicked.connect(self.ravno)
        self.c.clicked.connect(self.clear)

    def enterValue(self):
        if self.label.text() == '0':
            self.label.setText("")
        self.label.setText(self.label.text() + self.my_input)

    def one(self):
        self.my_input = '1'
        self.enterValue()

    def two(self):
        self.my_input = '2'
        self.enterValue()

    def tree(self):
        self.my_input = '3'
        self.enterValue()

    def four(self):
        self.my_input = '4'
        self.enterValue()

    def five(self):
        self.my_input = '5'
        self.enterValue()

    def six(self):
        self.my_input = '6'
        self.enterValue()

    def seven(self):
        self.my_input = '7'
        self.enterValue()

    def eight(self):
        self.my_input = '8'
        self.enterValue()

    def nine(self):
        self.my_input = '9'
        self.enterValue()

    def zero(self):
        self.my_input = '0'
        self.enterValue()

    def plus_1(self):
        self.operation = '+'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def minus_1(self):
        self.operation = '-'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def div_1(self):
        self.operation = '/'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def mul_1(self):
        self.operation = '*'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def step_1(self):
        self.operation = '^()'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def sqrt_1(self):
        self.operation = '√'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def proc_1(self):
        self.operation = '%'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def cel_1(self):
        self.operation = '//'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def kvad_1(self):
        self.operation = '^2'
        self.operand_1 = float(self.label.text())
        self.label.setText('')
        self.ravno()
        # if self.operation == '^2':
        #     self.rezult = self.operand_1 * self.operand_1
        #     self.label.setText(str(self.rezult))

    def ravno(self):
        if self.operation != '^2':
            self.operand_2 = float(self.label.text())
            if self.operation == '+':
                self.rezult = self.operand_1 + self.operand_2
            if self.operation == '-':
                self.rezult = self.operand_1 - self.operand_2
            if self.operation == '*':
                self.rezult = self.operand_1 * self.operand_2
            if self.operation == '^()':
                self.rezult = self.operand_1 ** self.operand_2
            if self.operation == '/':
                if self.operand_2 == 0:
                    self.rezult = 'error'
                else:
                    self.rezult = self.operand_1 / self.operand_2
            if self.operation == '//':
                if self.operand_2 == 0:
                    self.rezult = 'error'
                else:
                    self.rezult = self.operand_1 // self.operand_2
            if self.operation == '√':
                self.rezult = self.operand_1 ** (1 / self.operand_2)
            if self.operation == '%':
                self.rezult = (self.operand_1 / self.operand_2) * 100
            self.label.setText(str(self.rezult))
        else:
            self.rezult = self.operand_1 * self.operand_1
        self.label.setText(str(self.rezult))

    def clear(self):
        self.label.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
