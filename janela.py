import sys
from PySide import QtGui

class Example(QtGui.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        label = QtGui.QLabel('Hello World 5!', self)
        label_2 = QtGui.QLabel('Tomara que chegue logo a hora da pizza!', self)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Janela')
        self.show()


def main():

    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()