from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_inference_preview_win(object):
    def setupUi(self, inference_preview_win, width, height):
        inference_preview_win.setObjectName("inference_preview_wind")
        inference_preview_win.resize(width, height)
        inference_preview_win.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        inference_preview_win.setWindowTitle("Inference Preview")
        inference_preview_win.setLocale(QtCore.QLocale(QtCore.QLocale.Language.English, QtCore.QLocale.Country.Germany))
        inference_preview_win.setWindowIcon(QtGui.QIcon("resources/img/window_icons/GRS_mainWindow_icon.png"))
        self.inference_img = QtWidgets.QLabel(parent=inference_preview_win)
        self.inference_img.setGeometry(QtCore.QRect(0, 0, width, height))
        self.inference_img.setScaledContents(True)
        self.inference_img.setText("")
        self.inference_img.setObjectName("inference_img")

        self.retranslateUi(inference_preview_win)
        QtCore.QMetaObject.connectSlotsByName(inference_preview_win)

    def retranslateUi(self, inference_preview_window):
        pass

    def update_inference_img(self, updated_frame):
        self.inference_img.setPixmap(QtGui.QPixmap.fromImage(updated_frame))