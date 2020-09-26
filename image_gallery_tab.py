""" This is the file where Image Gallery is created and Initialized.
    It displays random images from the resources directory, displaying if the SKU is faulty or not.
    Also, there is an filter options to display All, Good and Bad Images.
"""
import os
import random
import constants
import database_queries
from add_thumbnail import GenerateThumbnail
from PyQt5 import QtWidgets, QtCore


class ImageGallery(QtWidgets.QWidget):
    """ Class that creates an Image Gallery Tab with filtering options.

        Extends:
            QtWidgets.QWidget
    """
    def __init__(self):
        """ Initialization of application.
        """
        super(ImageGallery, self).__init__()
        self.gallery_layout = QtWidgets.QGridLayout()
        self.image_sku = []

        self.button_box = QtWidgets.QHBoxLayout()
        button_all = QtWidgets.QPushButton("All")
        button_all.setToolTip("Clicking this button displays all the images having bad and good products")
        button_good = QtWidgets.QPushButton("Good")
        button_good.setToolTip("Clicking this button displays the images having good products")
        button_bad = QtWidgets.QPushButton("Bad")
        button_bad.setToolTip("Clicking this button displays the images having bad products")
        button_all.clicked.connect(self.display_all)
        button_good.clicked.connect(lambda: self.display_status_selected("Good"))
        button_bad.clicked.connect(lambda: self.display_status_selected("Bad"))
        self.button_box.addWidget(button_all)
        self.button_box.addWidget(button_good)
        self.button_box.addWidget(button_bad)

        self.gallery_layout.addLayout(self.button_box, 0, 4)
        self.setLayout(self.gallery_layout)

        for i in range(1, 5):
            for j in range(1, 5):
                thumbnail = self.generate_random_image()
                self.gallery_layout.addWidget(thumbnail, i, j, QtCore.Qt.AlignCenter)

    def generate_random_image(self):
        """ Picks a random image from the resources directory and display it as a thumbnail.
        """
        image_file = random.choice(os.listdir(constants.RESOURCES_PATH))
        sku_id, _ = os.path.splitext(image_file)
        self.image_sku.append(sku_id)
        status = database_queries.get_status_of_id(sku_id)
        display_color = constants.STATUS_COLOR_CHECK[status]
        full_path = os.path.join(constants.RESOURCES_PATH, image_file)
        thumbnail = GenerateThumbnail(full_path, display_color, self)
        return thumbnail

    def clear_images(self):
        """ Clears layout before filtering
        """
        for item in reversed(range(self.gallery_layout.count())):
            if self.gallery_layout.itemAt(item).widget():
                self.gallery_layout.itemAt(item).widget().setParent(None)

    def display_all(self):
        """ Functionality to display all status SKU images
        """
        all_skus = self.image_sku.copy()

        for i in range(1, 5):
            for j in range(1, 5):
                if all_skus:
                    full_path = os.path.join(constants.RESOURCES_PATH, "%s.jpg" % all_skus[0])
                    status = database_queries.get_status_of_id(all_skus[0])
                    thumbnail = GenerateThumbnail(full_path, constants.STATUS_COLOR_CHECK[status], self)
                    self.gallery_layout.addWidget(thumbnail, i, j, QtCore.Qt.AlignCenter)
                    all_skus.pop(0)

    def display_status_selected(self, status):
        """ Functionality to filter selected SKU status

            Args:
                status (str): Status of SKU product.
        """
        self.clear_images()
        status_skus = database_queries.get_status_skus(self.image_sku, status)

        for i in range(1, 5):
            for j in range(1, 5):
                if status_skus:
                    full_path = os.path.join(constants.RESOURCES_PATH, "%s.jpg" % status_skus[0])
                    thumbnail = GenerateThumbnail(full_path, constants.STATUS_COLOR_CHECK[status], self)
                    self.gallery_layout.addWidget(thumbnail, i, j, QtCore.Qt.AlignCenter)
                    status_skus.pop(0)
        vertical_spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                QtWidgets.QSizePolicy.Expanding)
        self.gallery_layout.addItem(vertical_spacer)
