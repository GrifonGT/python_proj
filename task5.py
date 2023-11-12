import sys
from PyQt5.QtWidgets import *
from ArrayAggregation import *

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
    def setupUi(self):
        self.setWindowTitle("Thomas Anderson")
        self.move(300, 300)
        self.resize(400, 500)

        self.label = QLabel('input array', self)
        self.label.move(30, 30)

        self.text_field = QLineEdit(self)
        self.text_field.move(30, 70)

        self.max_button = QPushButton("Max value", self)
        self.max_button.move(30, 110)
        self.max_button.clicked.connect(self.on_max_button_clicked)

        self.min_button = QPushButton("Min value", self)
        self.min_button.move(30, 150)
        self.min_button.clicked.connect(self.on_min_button_clicked)

        self.sum_button = QPushButton("Summary", self)
        self.sum_button.move(30, 190)
        self.sum_button.clicked.connect(self.on_sum_button_clicked)

        self.product_button = QPushButton("Product", self)
        self.product_button.move(30, 230)
        self.product_button.clicked.connect(self.on_product_button_clicked)

        self.average_button = QPushButton("Average", self)
        self.average_button.move(30, 270)
        self.average_button.clicked.connect(self.on_average_button_clicked)

    def show_dialog(self, value):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("Result")
        dialog.setText(value)
        button = dialog.exec()

        if button == QMessageBox.Ok:
            print("Ok")

    def create_array_aggregation(self):
        raw = self.text_field.text()
        array = list(map(int, raw.split(' ')))
        return ArrayAggregation(array)

    def on_max_button_clicked(self):
        sample = self.create_array_aggregation()
        self.show_dialog(f"Max: {sample.max()}")

    def on_min_button_clicked(self):
        sample = self.create_array_aggregation()
        self.show_dialog(f"Min: {sample.min()}")

    def on_sum_button_clicked(self):
        sample = self.create_array_aggregation()
        self.show_dialog(f"Max: {sample.sum()}")

    def on_product_button_clicked(self):
        sample = self.create_array_aggregation()
        self.show_dialog(f"Max: {sample.product()}")

    def on_average_button_clicked(self):
        sample = self.create_array_aggregation()
        self.show_dialog(f"Max: {sample.average()}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())