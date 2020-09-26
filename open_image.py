""" Implementation of Dialog Widget which displays an Image.
"""
from PyQt5 import QtCore, QtGui, QtWidgets


class OpenImageWindow(QtWidgets.QDialog):
    """ This class has been extended by QDialog Widget, which displays an
        image on top of it.

        Extends:
            QtWidgets.QDialog
        """
    def __init__(self, image_path, parent=None):
        """ Initialization of application.

            Args:
                image_path (str): Full path of an Image.
        """
        super(OpenImageWindow, self).__init__(parent)
        self.image_path = image_path
        self.open_image_window()

    def open_image_window(self):
        """ Creates a label, adds an Image on top of it and displays the dialog box.
        """
        horizontal_layout = QtWidgets.QHBoxLayout(self)
        img_label = QtWidgets.QLabel()
        img_label.setAlignment(QtCore.Qt.AlignCenter)
        image_pixmap = QtGui.QPixmap(self.image_path)
        image_pixmap = image_pixmap.scaled(QtCore.QSize(500, 500), QtCore.Qt.KeepAspectRatio,
                                           QtCore.Qt.SmoothTransformation)
        img_label.setPixmap(image_pixmap)
        horizontal_layout.addWidget(img_label)

        self.setLayout(horizontal_layout)
        self.setWindowTitle('Image Dialog')
        self.setFixedSize(image_pixmap.width(), image_pixmap.height())
