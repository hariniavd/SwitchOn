""" Analytics Tab has the functionalities to generate the Bar Graph for the selected
SKU's and display its Good and Bad count in an Graphical representation.
"""
import database_queries
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5 import QtChart
import constants


class AnalyticsTab(QtWidgets.QWidget):
    """ Class that creates an Bar Chart for selected SKU's.

        Extends:
            QtWidgets.QWidget
    """
    def __init__(self):
        """ Initialization of application.
        """
        super(AnalyticsTab, self).__init__()
        self.show_graph = False
        self.analytics_h_layout = QtWidgets.QHBoxLayout()
        self.update_analytic_tab()

    def update_analytic_tab(self):
        """ Adds Combobox for user selection and updates the Bar Chart of any SKU
            is selected.
        """
        self.sku_combobox = QtWidgets.QComboBox(self)
        self.sku_combobox.addItems(["Please select SKU"])
        self.sku_combobox.addItems(database_queries.get_all_skus())
        self.sku_combobox.setFixedSize(250, 20)
        self.sku_combobox.setToolTip("Please select any SKU to display graphical representation of "
                                     "Good and Bad products")
        self.sku_combobox.currentIndexChanged.connect(self.update_sku_value)
        horizontal_spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Expanding,
                                                  QtWidgets.QSizePolicy.Minimum)
        self.analytics_h_layout.addWidget(self.sku_combobox)
        self.analytics_h_layout.addItem(horizontal_spacer)
        self.analytics_v_layout = QtWidgets.QVBoxLayout()
        self.analytics_v_layout.addLayout(self.analytics_h_layout)

        bar_graph = self.add_bar_graph()
        if not bar_graph:
            self.add_vertical_layout()

        self.setLayout(self.analytics_v_layout)

    def update_sku_value(self, value):
        """ When combobox text is changed, it removed the default value and
            updated the selected SKU's Graph
        """
        if self.sku_combobox.currentText() != "Please select SKU":
            index = self.sku_combobox.findText("Please select SKU")
            self.sku_combobox.removeItem(index)
            self.show_graph = True
            self.clear_layout()
            self.add_bar_graph()

    def add_bar_graph(self):
        """ Adds the bar graph into the layout.
        """
        chart_view = self.calculate_graph()
        if chart_view:
            self.analytics_v_layout.addWidget(chart_view)
            return True
        return False

    def add_vertical_layout(self):
        """ Add vertical spaces when no bar chart is selected for UI representation.
        """
        vertical_spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum,
                                                QtWidgets.QSizePolicy.Expanding)
        self.analytics_v_layout.addItem(vertical_spacer)

    def clear_layout(self):
        """ Clear the layout before adding a new graph to the UI.
        """
        for i in reversed(range(self.analytics_v_layout.count())):
            if self.analytics_v_layout.itemAt(i).widget():
                self.analytics_v_layout.itemAt(i).widget().setParent(None)
            elif self.analytics_v_layout.itemAt(i).spacerItem():
                self.analytics_v_layout.removeItem(self.analytics_v_layout.itemAt(i).spacerItem())

    def calculate_graph(self):
        """ Calculate the Bar graph for the selected SKU's from database.
        """
        if self.show_graph:
            bar_set_1, bar_set_2 = self.get_graph_point()

            series = QtChart.QStackedBarSeries()
            series.append(bar_set_1)
            series.append(bar_set_2)

            chart = QtChart.QChart()
            chart.setTitle("Good and Bad")
            chart.addSeries(series)
            chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)

            x_axis = QtChart.QBarCategoryAxis()
            x_axis.append(constants.TIME_VALUES[:-1])
            chart.addAxis(x_axis, QtCore.Qt.AlignBottom)
            series.attachAxis(x_axis)

            y_axis = QtChart.QValueAxis()
            chart.addAxis(y_axis, QtCore.Qt.AlignLeft)
            series.attachAxis(y_axis)

            chart.legend().setVisible(True)
            chart.legend().setAlignment(QtCore.Qt.AlignBottom)

            chart_view = QtChart.QChartView(chart)
            chart_view.setRenderHint(QtGui.QPainter.Antialiasing)

            return chart_view

    def get_graph_point(self):
        """ Get the required data from database to generate the graph points.
        """
        bar_set_1 = QtChart.QBarSet("Good")
        color = QtGui.QColor("green")
        bar_set_1.setColor(color)
        bar_set_2 = QtChart.QBarSet("Bad")
        color = QtGui.QColor(255, 60, 60)
        bar_set_2.setColor(color)

        selected_sku = str(self.sku_combobox.currentText())

        for index in range(len(constants.TIME_VALUES) - 1):
            good_value = len(database_queries.get_sku_id(selected_sku, "Good", constants.TIME_VALUES[index],
                                                         constants.TIME_VALUES[index + 1]))
            bad_value = len(database_queries.get_sku_id(selected_sku, "Bad", constants.TIME_VALUES[index],
                                                        constants.TIME_VALUES[index + 1]))
            bar_set_1.append(good_value)
            bar_set_2.append(bad_value)

        return bar_set_1, bar_set_2
