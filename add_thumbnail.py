""" Implementation of a Widget, which creates a Thumbnail of it, and adds into a layout.
"""
from PyQt5 import QtWidgets, QtGui, QtCore
from open_image import OpenImageWindow


class GenerateThumbnail(QtWidgets.QWidget):
    """ This class has been extended by QWidget, which displays an thumbnail on top of label
        and adds a line, which display the status of the SKU id

        Extends:
            QtWidgets.QWidget
    """
    def __init__(self, image_path, color, parent=None):
        """ Initialization of application.

            Args:
                image_path: Full path of an Image.
                color: Color to be set on the line.
        """
        super(GenerateThumbnail, self).__init__(parent)
        self.image_path = image_path
        self.color = color
        self.parent = parent
        self.create_image()

    def create_image(self):
        """ Label is created adding an image on top of it, also adding Line below the
            image with a color as per the status.
        """
        image_label = QtWidgets.QLabel()
        image_label.setAlignment(QtCore.Qt.AlignCenter)
        image_label.mousePressEvent = lambda x: self.open_image(self.image_path)

        pixmap_image = QtGui.QPixmap(self.image_path)
        pixmap_image = pixmap_image.scaled(QtCore.QSize(100, 100), QtCore.Qt.KeepAspectRatio,
                                           QtCore.Qt.SmoothTransformation)

        image_label.setPixmap(pixmap_image)

        thumbnail = QtWidgets.QBoxLayout(QtWidgets.QBoxLayout.TopToBottom)
        thumbnail.addWidget(image_label)

        color = QtGui.QColor(self.color)
        color_palette = QtGui.QPalette()
        color_palette.setColor(QtGui.QPalette.WindowText, color)

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setLineWidth(15)
        line.setPalette(color_palette)
        if self.color == "green":
            image_label.setToolTip("This is a Good Product")
            line.setToolTip("This is a Good Product")
        else:
            image_label.setToolTip("This is a Bad Product")
            line.setToolTip("This is a Bad Product")

        thumbnail.addWidget(line)
        self.setLayout(thumbnail)

    def open_image(self, image_path):
        """ On click on image thumbnail, a new window is pop-ed up showing the image on it.

            Args:
                image_path (str): Full path of an image.
        """
        image = OpenImageWindow(image_path, self)
        image.show()
