""" Entry point for Implementation of SwitchOn Application.
"""
import sys
from PyQt5 import QtWidgets
from ui_window import SwitchOnUI


class SwitchOnApp(QtWidgets.QMainWindow):
    """ This is an UI based application which shows graphical representation of data
        in Bar Chart and having an image gallery to browse set of Images.

        Extends:
            QtWidgets.QMainWindow
    """
    def __init__(self):
        """ Initialization of application.
        """
        super(SwitchOnApp, self).__init__()
        self.setWindowTitle("SwitchOn Window Application!")

        # Class having QtWidget that displays Analytics and Image Gallery Tabs.
        switch_on_ui = SwitchOnUI(self)
        self.setCentralWidget(switch_on_ui)
        self.setFixedSize(800, 600)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    run_app = SwitchOnApp()
    run_app.show()
    sys.exit(app.exec_())
