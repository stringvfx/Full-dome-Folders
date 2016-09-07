from PySide.QtGui import *
from PySide.QtCore import *
import sys, os, FDFC, time
class FDFC(QDialog, FDFC.Ui_FDFC):
    def __init__(self):
        QDialog.__init__(self)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.setupUi(self)
        # Connections
        self.top_btn.clicked.connect(self.top)
        self.front_btn.clicked.connect(self.front)
        self.back_btn.clicked.connect(self.back)
        self.autocrate_btn.clicked.connect(self.Auto)
        self.left_btn.clicked.connect(self.left)
        self.right_btn.clicked.connect(self.right)
        self.stitch_btn.clicked.connect(self.stitch)
        self.custom_btn.clicked.connect(self.custom)
        self.bottom_btn.clicked.connect(self.bottom)
        self.custom_line.textChanged.connect(self.ctl)
        self.terminal.setReadOnly(True)
        self.left_btn.clicked.connect(self.settermleft)
        self.right_btn.clicked.connect(self.settermright)
        self.top_btn.clicked.connect(self.settermtop)
        self.back_btn.clicked.connect(self.settermback)
        self.bottom_btn.clicked.connect(self.settermbottom)
        self.stitch_btn.clicked.connect(self.settermstitch)
        self.custom_btn.clicked.connect(self.settermcustom)
        self.front_btn.clicked.connect(self.settermfront)
        self.autocrate_btn.clicked.connect(self.settermauto)
        self.setWindowTitle("FullDome Project | Developed by: Ahmed Abdelnaby")
        self.setPath_btn.clicked.connect(self.path)
        self.setWindowIcon(QIcon("icon.ct"))


    def path(self):
        os.chdir(QFileDialog.getExistingDirectory(self, "Select your project path"))
# Connect terminal
    def settermright(self):
        self.terminal.setText(self.right_btn.text())
    def settermleft(self):
        self.terminal.setText(self.left_btn.text())
    def settermtop(self):
        self.terminal.setText(self.top_btn.text())
    def settermback(self):
        self.terminal.setText(self.back_btn.text())
    def settermbottom(self):
        self.terminal.setText(self.bottom_btn.text())
    def settermcustom(self):
        self.terminal.setText(self.custom_btn.text())
    def settermstitch(self):
        self.terminal.setText(self.stitch_btn.text())
    def settermfront(self):
        self.terminal.setText(self.stitch_btn.text())
    def settermfront(self):
        self.terminal.setText(self.front_btn.text())
    def settermauto(self):
        a = ("Front \nBack \nTop \nBottom \nRight \nLeft")
        self.terminal.setText(a)
# Manual Create
    def ctl(self, text):
        ctm = self.custom_btn.setText(text)
    def bottom(self):
        if os.path.isdir(self.bottom_btn.text()):
            self.terminal.setText(self.bottom_btn.text())
            QMessageBox.warning(self, "Wrong ", "Folder is exist, Called Bottom")
            print "Folder is exist, Called {}".format(self.bottom_btn.text())
        else:
            os.makedirs(self.bottom_btn.text())
            QMessageBox.information(self, "Created ", "Folder is created now called Bottom")
            self.terminal.setText(self.bottom_btn.text())
            print"Folder is not exist. Created now Called {}".format(self.bottom_btn.text())
    def custom(self):
        if os.path.isdir(self.custom_btn.text()):
            QMessageBox.warning(self, "Wrong ", "Folder is exist. Called {}".format(self.custom_btn.text()))
            print "Folder is exist, Called {}".format(self.custom_btn.text())
        else:
            os.makedirs(self.custom_btn.text())
            QMessageBox.information(self, "Created ", "Folder is not exist. Created now Called {}".format(self.custom_btn.text()))
            print "Folder is not exist. Created now Called {}".format(self.custom_btn.text())
    def stitch(self):
        if os.path.isdir(self.stitch_btn.text()):
            QMessageBox.warning(self, "Wrong ", "Folder is exist, Called Stitch")
            print "Folder is exist, Called {}".format(self.stitch_btn.text())
        else:
            os.makedirs(self.stitch_btn.text())
            QMessageBox.information(self, "Created ", "Folder is created now called Stitch")
            print "Folder is not exist. Created now Called {}".format(self.stitch_btn.text())
    def top(self):
        if os.path.isdir(self.top_btn.text()):
            QMessageBox.warning(self, "Wrong ", "Folder is exist, Called Top")
            print "Folder is exist, Called {}".format(self.top_btn.text())
        else:
            os.makedirs(self.top_btn.text())
            QMessageBox.information(self, "Created ", "Folder is not exist. Created now Called Top")
            print "Folder is not exist. Created now Called {}".format(self.top_btn.text())
    def front(self):
        if os.path.isdir(self.front_btn.text()):
            QMessageBox.warning(self, "Wrong ", "Folder is exist, Called Front")
            print "Folder is exist, Called {}".format(self.front_btn.text())
        else:
            os.makedirs("Front")
            QMessageBox.information(self, "Created ", "Folder is not exist. Created now Called Front")
            print "Folder is not exist. Created now Called {}".format(self.front_btn.text())
    def back(self):
        if os.path.isdir(self.back_btn.text()):
            QMessageBox.warning(self, "Wrong ", "Folder is exist, Called Back")
            print "Folder is exist, Called {}".format(self.back_btn.text())
        else:
            os.makedirs(self.back_btn.text())
            QMessageBox.information(self, "Created ", "Folder is not exist. Created now Called Back")
            print "Folder is not exist. Created now Called {}".format(self.back_btn.text())
    def left(self):
        if os.path.isdir(self.left_btn.text()):
            QMessageBox.warning(self, "Wrong ", "Folder is exist, Called Left")
            #print "Folder is exist, Called {}".format(self.left_btn.text())
        else:
            os.makedirs(self.left_btn.text())
            QMessageBox.information(self, "Created ", "Folder is not exist. Created now Called Left")
            print "Folder is not exist. Created now Called {}".format(self.left_btn.text())
    def right(self):
        if os.path.isdir(self.right_btn.text()):
            QMessageBox.warning(self, "Wrong ", "Folder is exist, Called Right")
            print "Folder is exist, Called {}".format(self.right_btn.text())
        else:
            os.makedirs(self.right_btn.text())
            QMessageBox.information(self, "Created ", "Folder is not exist. Created now Called Right")
            print "Folder is not exist. Created now Called {}".format(self.right_btn.text())
# Automatic task
    def Auto(self):
        cameras = ("Front", "Back", "Right", "Left", "Top", "Bottom")
        for c in cameras:
            if os.path.isdir(c):
                QMessageBox.warning(self, "Wrong ", "Folder is exist. Called %s" %c)
                print "Folder is exist called %s" % c
            else:
                os.makedirs(c)
                print "Folder exist. Created now %s" % c
app = QApplication(sys.argv)
dialog = FDFC()
splash_img = QPixmap("splash.ct")
splash = QSplashScreen(splash_img)
splash.show()
time.sleep(2)
dialog.show()
splash.finish(dialog)
sys.exit(app.exec_())
