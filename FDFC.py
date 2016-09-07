from PySide import QtCore, QtGui
class Ui_FDFC(object):
    def setupUi(self, FDFC):
        FDFC.setObjectName("FDFC")
        FDFC.setWindowModality(QtCore.Qt.NonModal)
        FDFC.setEnabled(True)
        FDFC.resize(400, 250)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FDFC.sizePolicy().hasHeightForWidth())
        FDFC.setSizePolicy(sizePolicy)
        FDFC.setMinimumSize(QtCore.QSize(400, 250))
        FDFC.setMaximumSize(QtCore.QSize(400, 250))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(98, 98, 98))
        gradient.setColorAt(1.0, QtGui.QColor(91, 91, 91))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(98, 98, 98))
        gradient.setColorAt(1.0, QtGui.QColor(91, 91, 91))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(98, 98, 98))
        gradient.setColorAt(1.0, QtGui.QColor(91, 91, 91))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(98, 98, 98))
        gradient.setColorAt(1.0, QtGui.QColor(91, 91, 91))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(98, 98, 98))
        gradient.setColorAt(1.0, QtGui.QColor(91, 91, 91))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(98, 98, 98))
        gradient.setColorAt(1.0, QtGui.QColor(91, 91, 91))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(98, 98, 98))
        gradient.setColorAt(1.0, QtGui.QColor(91, 91, 91))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(217, 217, 217))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(98, 98, 98))
        gradient.setColorAt(1.0, QtGui.QColor(91, 91, 91))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(1.0, 0.0, 1.0, 1.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(98, 98, 98))
        gradient.setColorAt(1.0, QtGui.QColor(91, 91, 91))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        FDFC.setPalette(palette)
        FDFC.setCursor(QtCore.Qt.ArrowCursor)
        FDFC.setMouseTracking(False)
        FDFC.setFocusPolicy(QtCore.Qt.NoFocus)
        FDFC.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        FDFC.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Freepik-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FDFC.setWindowIcon(icon)
        FDFC.setWindowOpacity(0.97)
        FDFC.setToolTip("")
        #FDFC.setToolTipDuration(0)
        FDFC.setLayoutDirection(QtCore.Qt.LeftToRight)
        FDFC.setAutoFillBackground(False)
        FDFC.setStyleSheet("background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(98, 98, 98, 255), stop:1 rgba(91, 91, 91, 255));\n"
"\n"
"color: rgb(217, 217, 217);\n"
"\n"
"")
        FDFC.setWindowFilePath("")
        self.MainBox = QtGui.QGroupBox(FDFC)
        self.MainBox.setGeometry(QtCore.QRect(10, 30, 161, 111))
        self.MainBox.setObjectName("MainBox")
        self.left_btn = QtGui.QPushButton(self.MainBox)
        self.left_btn.setGeometry(QtCore.QRect(10, 20, 71, 21))
        self.left_btn.setObjectName("left_btn")
        self.right_btn = QtGui.QPushButton(self.MainBox)
        self.right_btn.setGeometry(QtCore.QRect(80, 20, 71, 21))
        self.right_btn.setObjectName("right_btn")
        self.top_btn = QtGui.QPushButton(self.MainBox)
        self.top_btn.setGeometry(QtCore.QRect(10, 40, 71, 21))
        self.top_btn.setObjectName("top_btn")
        self.front_btn = QtGui.QPushButton(self.MainBox)
        self.front_btn.setGeometry(QtCore.QRect(10, 60, 71, 21))
        self.front_btn.setObjectName("front_btn")
        self.bottom_btn = QtGui.QPushButton(self.MainBox)
        self.bottom_btn.setGeometry(QtCore.QRect(80, 40, 71, 21))
        self.bottom_btn.setObjectName("bottom_btn")
        self.back_btn = QtGui.QPushButton(self.MainBox)
        self.back_btn.setGeometry(QtCore.QRect(80, 60, 71, 21))
        self.back_btn.setObjectName("back_btn")
        self.autocrate_btn = QtGui.QPushButton(self.MainBox)
        self.autocrate_btn.setGeometry(QtCore.QRect(10, 80, 141, 21))
        self.autocrate_btn.setObjectName("autocrate_btn")
        self.AutomaticBox = QtGui.QGroupBox(FDFC)
        self.AutomaticBox.setEnabled(True)
        self.AutomaticBox.setGeometry(QtCore.QRect(10, 150, 161, 91))
        self.AutomaticBox.setStyleSheet("")
        self.AutomaticBox.setFlat(False)
        self.AutomaticBox.setCheckable(False)
        self.AutomaticBox.setChecked(False)
        self.AutomaticBox.setObjectName("AutomaticBox")
        self.stitch_btn = QtGui.QPushButton(self.AutomaticBox)
        self.stitch_btn.setGeometry(QtCore.QRect(10, 20, 141, 21))
        self.stitch_btn.setObjectName("stitch_btn")
        self.custom_btn = QtGui.QPushButton(self.AutomaticBox)
        self.custom_btn.setGeometry(QtCore.QRect(10, 40, 141, 21))
        self.custom_btn.setObjectName("custom_btn")
        self.custom_line = QtGui.QLineEdit(self.AutomaticBox)
        self.custom_line.setPlaceholderText("Custom")
        self.custom_line.setGeometry(QtCore.QRect(10, 60, 141, 21))
        self.custom_line.setStyleSheet("background-color: rgb(235, 235, 235);\n"
"color: rgb(31, 104, 131);")
        self.custom_line.setDragEnabled(False)
        #self.custom_line.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        #self.custom_line.setClearButtonEnabled(True)
        self.custom_line.setObjectName("custom_line")
        self.setPath_btn = QtGui.QToolButton(FDFC)
        self.setPath_btn.setGeometry(QtCore.QRect(10, 10, 161, 21))
        self.setPath_btn.setAutoFillBackground(False)
        self.setPath_btn.setStyleSheet("")
        self.setPath_btn.setIconSize(QtCore.QSize(64, 64))
        self.setPath_btn.setAutoRaise(False)
        self.setPath_btn.setObjectName("setPath_btn")
        self.terminal = QtGui.QTextEdit(FDFC)
        self.terminal.setGeometry(QtCore.QRect(180, 10, 211, 231))
        self.terminal.setStyleSheet("QFrame{\n"
"background-color: rgb(26, 26, 26);\n"
"color: rgb(29, 158, 37);\n"
"}\n"
"")
        self.terminal.setFrameShape(QtGui.QFrame.StyledPanel)
        self.terminal.setFrameShadow(QtGui.QFrame.Sunken)
        self.terminal.setLineWidth(5)
        self.terminal.setMidLineWidth(0)
        self.terminal.setTabChangesFocus(False)
        self.terminal.setDocumentTitle("")
        #self.terminal.setPlaceholderText("")
        self.terminal.setObjectName("terminal")

        self.retranslateUi(FDFC)
        QtCore.QMetaObject.connectSlotsByName(FDFC)

    def retranslateUi(self, FDFC):
        FDFC.setWindowTitle(QtGui.QApplication.translate("FDFC", "FDFC", None, QtGui.QApplication.UnicodeUTF8))
        FDFC.setWhatsThis(QtGui.QApplication.translate("FDFC", "This App for creating Fulldome folders \n"
"\n"
"", None, QtGui.QApplication.UnicodeUTF8))
        self.MainBox.setTitle(QtGui.QApplication.translate("FDFC", "Main camera", None, QtGui.QApplication.UnicodeUTF8))
        self.left_btn.setText(QtGui.QApplication.translate("FDFC", "Left", None, QtGui.QApplication.UnicodeUTF8))
        self.right_btn.setText(QtGui.QApplication.translate("FDFC", "Right", None, QtGui.QApplication.UnicodeUTF8))
        self.top_btn.setText(QtGui.QApplication.translate("FDFC", "Top", None, QtGui.QApplication.UnicodeUTF8))
        self.front_btn.setText(QtGui.QApplication.translate("FDFC", "Front", None, QtGui.QApplication.UnicodeUTF8))
        self.bottom_btn.setText(QtGui.QApplication.translate("FDFC", "Bottom", None, QtGui.QApplication.UnicodeUTF8))
        self.back_btn.setText(QtGui.QApplication.translate("FDFC", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.autocrate_btn.setText(QtGui.QApplication.translate("FDFC", "Auto Create", None, QtGui.QApplication.UnicodeUTF8))
        self.AutomaticBox.setTitle(QtGui.QApplication.translate("FDFC", "Extra", None, QtGui.QApplication.UnicodeUTF8))
        self.stitch_btn.setText(QtGui.QApplication.translate("FDFC", "Stitch", None, QtGui.QApplication.UnicodeUTF8))
        self.custom_btn.setText(QtGui.QApplication.translate("FDFC", "Custom", None, QtGui.QApplication.UnicodeUTF8))
        self.setPath_btn.setToolTip(QtGui.QApplication.translate("FDFC", "Select your location", None, QtGui.QApplication.UnicodeUTF8))
        self.setPath_btn.setText(QtGui.QApplication.translate("FDFC", "Create Project", None, QtGui.QApplication.UnicodeUTF8))
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    FDFC = QtGui.QWidget()
    ui = Ui_FDFC()
    ui.setupUi(FDFC)
    FDFC.show()
    sys.exit(app.exec_())
