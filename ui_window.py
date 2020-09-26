""" Adding a Analytics Tab and Image Gallery Tab are processed here.
"""
from PyQt5 import QtWidgets
from analytics_tab import AnalyticsTab
from image_gallery_tab import ImageGallery


class SwitchOnUI(QtWidgets.QWidget):
    """ This is an UI based application which shows graphical representation of data
        in Bar Chart and having an image gallery to browse set of Images.

        Extends:
            QtWidgets.QMainWindow
    """
    def __init__(self, parent):
        """ Initialization of application.
        """
        super(SwitchOnUI, self).__init__(parent)
        self.tab_widget = QtWidgets.QTabWidget()
        self.analytics_tab = AnalyticsTab()
        self.image_gallery_tab = ImageGallery()
        self.tab_widget.addTab(self.analytics_tab, "Analytics")
        self.tab_widget.addTab(self.image_gallery_tab, "Image Gallery")
        main_layout = QtWidgets.QHBoxLayout(self)
        main_layout.addWidget(self.tab_widget)
        self.setLayout(main_layout)
