# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(612, 490)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(622, 490))
        MainWindow.setMaximumSize(QtCore.QSize(622, 490))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../VideoAutoSplitter/icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWhatsThis(_fromUtf8(""))
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.splitimagefolderLabel = QtWidgets.QLabel(self.centralwidget)
        self.splitimagefolderLabel.setGeometry(QtCore.QRect(90, 13, 91, 16))
        self.splitimagefolderLabel.setObjectName(_fromUtf8("splitimagefolderLabel"))
        self.splitimagefolderLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.splitimagefolderLineEdit.setGeometry(QtCore.QRect(187, 11, 247, 20))
        self.splitimagefolderLineEdit.setReadOnly(True)
        self.splitimagefolderLineEdit.setObjectName(_fromUtf8("splitimagefolderLineEdit"))
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(443, 9, 75, 24))
        self.browseButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.browseButton.setObjectName(_fromUtf8("browseButton"))
        self.xLabel = QtWidgets.QLabel(self.centralwidget)
        self.xLabel.setGeometry(QtCore.QRect(25, 139, 7, 16))
        self.xLabel.setObjectName(_fromUtf8("xLabel"))
        self.liveimageCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.liveimageCheckBox.setEnabled(True)
        self.liveimageCheckBox.setGeometry(QtCore.QRect(125, 253, 121, 17))
        self.liveimageCheckBox.setChecked(True)
        self.liveimageCheckBox.setTristate(False)
        self.liveimageCheckBox.setObjectName(_fromUtf8("liveimageCheckBox"))
        self.loopCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.loopCheckBox.setEnabled(True)
        self.loopCheckBox.setGeometry(QtCore.QRect(500, 314, 121, 17))
        self.loopCheckBox.setChecked(False)
        self.loopCheckBox.setTristate(False)
        self.loopCheckBox.setObjectName(_fromUtf8("loopCheckBox"))
        self.autostartonresetCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.autostartonresetCheckBox.setEnabled(True)
        self.autostartonresetCheckBox.setGeometry(QtCore.QRect(500, 344, 121, 17))
        self.autostartonresetCheckBox.setChecked(False)
        self.autostartonresetCheckBox.setTristate(False)
        self.autostartonresetCheckBox.setObjectName(_fromUtf8("autostartonresetCheckBox"))
        self.selectregionButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectregionButton.setGeometry(QtCore.QRect(5, 67, 101, 23))
        self.selectregionButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.selectregionButton.setObjectName(_fromUtf8("selectregionButton"))
        self.similaritythresholdLabel = QtWidgets.QLabel(self.centralwidget)
        self.similaritythresholdLabel.setGeometry(QtCore.QRect(10, 378, 91, 16))
        self.similaritythresholdLabel.setObjectName(_fromUtf8("similaritythresholdLabel"))
        self.similaritythresholdDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.similaritythresholdDoubleSpinBox.setGeometry(QtCore.QRect(160, 383, 64, 22))
        self.similaritythresholdDoubleSpinBox.setMaximum(1.0)
        self.similaritythresholdDoubleSpinBox.setSingleStep(0.01)
        self.similaritythresholdDoubleSpinBox.setProperty("value", 0.9)
        self.similaritythresholdDoubleSpinBox.setObjectName(_fromUtf8("similaritythresholdDoubleSpinBox"))
        self.startautosplitterButton = QtWidgets.QPushButton(self.centralwidget)
        self.startautosplitterButton.setGeometry(QtCore.QRect(506, 425, 101, 31))
        self.startautosplitterButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.startautosplitterButton.setObjectName(_fromUtf8("startautosplitterButton"))
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setGeometry(QtCore.QRect(506, 385, 101, 31))
        self.resetButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.resetButton.setObjectName(_fromUtf8("resetButton"))
        self.undosplitButton = QtWidgets.QPushButton(self.centralwidget)
        self.undosplitButton.setGeometry(QtCore.QRect(477, 251, 61, 21))
        self.undosplitButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.undosplitButton.setObjectName(_fromUtf8("undosplitButton"))
        self.skipsplitButton = QtWidgets.QPushButton(self.centralwidget)
        self.skipsplitButton.setGeometry(QtCore.QRect(541, 251, 61, 21))
        self.skipsplitButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.skipsplitButton.setObjectName(_fromUtf8("skipsplitButton"))
        self.pauseLabel = QtWidgets.QLabel(self.centralwidget)
        self.pauseLabel.setGeometry(QtCore.QRect(10, 420, 140, 16))
        self.pauseLabel.setObjectName(_fromUtf8("pauseLabel"))
        self.checkfpsButton = QtWidgets.QPushButton(self.centralwidget)
        self.checkfpsButton.setGeometry(QtCore.QRect(5, 225, 51, 21))
        self.checkfpsButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.checkfpsButton.setObjectName(_fromUtf8("checkfpsButton"))
        self.fpsLabel = QtWidgets.QLabel(self.centralwidget)
        self.fpsLabel.setGeometry(QtCore.QRect(87, 225, 20, 20))
        self.fpsLabel.setObjectName(_fromUtf8("fpsLabel"))
        self.showlivesimilarityCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.showlivesimilarityCheckBox.setEnabled(True)
        self.showlivesimilarityCheckBox.setGeometry(QtCore.QRect(10, 330, 111, 17))
        self.showlivesimilarityCheckBox.setChecked(True)
        self.showlivesimilarityCheckBox.setTristate(False)
        self.showlivesimilarityCheckBox.setObjectName(_fromUtf8("showlivesimilarityCheckBox"))
        self.showhighestsimilarityCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.showhighestsimilarityCheckBox.setEnabled(True)
        self.showhighestsimilarityCheckBox.setGeometry(QtCore.QRect(10, 351, 131, 17))
        self.showhighestsimilarityCheckBox.setChecked(True)
        self.showhighestsimilarityCheckBox.setTristate(False)
        self.showhighestsimilarityCheckBox.setObjectName(_fromUtf8("showhighestsimilarityCheckBox"))
        self.livesimilarityLabel = QtWidgets.QLabel(self.centralwidget)
        self.livesimilarityLabel.setGeometry(QtCore.QRect(160, 332, 46, 13))
        self.livesimilarityLabel.setText(_fromUtf8(""))
        self.livesimilarityLabel.setObjectName(_fromUtf8("livesimilarityLabel"))
        self.highestsimilarityLabel = QtWidgets.QLabel(self.centralwidget)
        self.highestsimilarityLabel.setGeometry(QtCore.QRect(160, 353, 46, 13))
        self.highestsimilarityLabel.setText(_fromUtf8(""))
        self.highestsimilarityLabel.setObjectName(_fromUtf8("highestsimilarityLabel"))
        self.splitLabel = QtWidgets.QLabel(self.centralwidget)
        self.splitLabel.setGeometry(QtCore.QRect(249, 317, 61, 16))
        self.splitLabel.setObjectName(_fromUtf8("splitLabel"))
        self.resetLabel = QtWidgets.QLabel(self.centralwidget)
        self.resetLabel.setGeometry(QtCore.QRect(249, 341, 61, 16))
        self.resetLabel.setObjectName(_fromUtf8("resetLabel"))
        self.skiptsplitLabel = QtWidgets.QLabel(self.centralwidget)
        self.skiptsplitLabel.setGeometry(QtCore.QRect(249, 367, 50, 16))
        self.skiptsplitLabel.setObjectName(_fromUtf8("skiptsplitLabel"))
        self.undosplitLabel = QtWidgets.QLabel(self.centralwidget)
        self.undosplitLabel.setGeometry(QtCore.QRect(249, 393, 61, 16))
        self.undosplitLabel.setObjectName(_fromUtf8("undosplitLabel"))
        self.pausehotkeyLabel = QtWidgets.QLabel(self.centralwidget)
        self.pausehotkeyLabel.setGeometry(QtCore.QRect(249, 418, 61, 16))
        self.pausehotkeyLabel.setObjectName(_fromUtf8("undosplitLabel"))
        self.splitLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.splitLineEdit.setGeometry(QtCore.QRect(316, 314, 81, 20))
        self.splitLineEdit.setReadOnly(True)
        self.splitLineEdit.setObjectName(_fromUtf8("splitLineEdit"))
        self.undosplitLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.undosplitLineEdit.setGeometry(QtCore.QRect(316, 391, 81, 20))
        self.undosplitLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.undosplitLineEdit.setReadOnly(True)
        self.undosplitLineEdit.setObjectName(_fromUtf8("undosplitLineEdit"))
        self.skipsplitLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.skipsplitLineEdit.setGeometry(QtCore.QRect(316, 365, 81, 20))
        self.skipsplitLineEdit.setReadOnly(True)
        self.skipsplitLineEdit.setObjectName(_fromUtf8("skipsplitLineEdit"))
        self.resetLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.resetLineEdit.setGeometry(QtCore.QRect(316, 339, 81, 20))
        self.resetLineEdit.setReadOnly(True)
        self.resetLineEdit.setObjectName(_fromUtf8("resetLineEdit"))
        self.pausehotkeyLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pausehotkeyLineEdit.setGeometry(QtCore.QRect(316, 416, 81, 20))
        self.pausehotkeyLineEdit.setReadOnly(True)
        self.pausehotkeyLineEdit.setObjectName(_fromUtf8("pausehotkeyLineEdit"))
        self.setsplithotkeyButton = QtWidgets.QPushButton(self.centralwidget)
        self.setsplithotkeyButton.setGeometry(QtCore.QRect(409, 314, 71, 21))
        self.setsplithotkeyButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setsplithotkeyButton.setObjectName(_fromUtf8("setsplithotkeyButton"))
        self.setresethotkeyButton = QtWidgets.QPushButton(self.centralwidget)
        self.setresethotkeyButton.setGeometry(QtCore.QRect(410, 339, 71, 21))
        self.setresethotkeyButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setresethotkeyButton.setObjectName(_fromUtf8("setresethotkeyButton"))
        self.setskipsplithotkeyButton = QtWidgets.QPushButton(self.centralwidget)
        self.setskipsplithotkeyButton.setGeometry(QtCore.QRect(410, 365, 71, 21))
        self.setskipsplithotkeyButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setskipsplithotkeyButton.setObjectName(_fromUtf8("setskipsplithotkeyButton"))
        self.setundosplithotkeyButton = QtWidgets.QPushButton(self.centralwidget)
        self.setundosplithotkeyButton.setGeometry(QtCore.QRect(410, 391, 71, 21))
        self.setundosplithotkeyButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setundosplithotkeyButton.setObjectName(_fromUtf8("setundosplithotkeyButton"))
        self.setpausehotkeyButton = QtWidgets.QPushButton(self.centralwidget)
        self.setpausehotkeyButton.setGeometry(QtCore.QRect(410, 416, 71, 21))
        self.setpausehotkeyButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.setpausehotkeyButton.setObjectName(_fromUtf8("setpausehotkeyButton"))
        self.line_live_bottom = QtWidgets.QFrame(self.centralwidget)
        self.line_live_bottom.setGeometry(QtCore.QRect(111, 247, 240, 2))
        self.line_live_bottom.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_live_bottom.setLineWidth(1)
        self.line_live_bottom.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_live_bottom.setObjectName(_fromUtf8("line_live_bottom"))
        self.line_live_top = QtWidgets.QFrame(self.centralwidget)
        self.line_live_top.setGeometry(QtCore.QRect(111, 68, 240, 2))
        self.line_live_top.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_live_top.setLineWidth(1)
        self.line_live_top.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_live_top.setObjectName(_fromUtf8("line_live_top"))
        self.line_live_right = QtWidgets.QFrame(self.centralwidget)
        self.line_live_right.setGeometry(QtCore.QRect(349, 69, 2, 180))
        self.line_live_right.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_live_right.setLineWidth(1)
        self.line_live_right.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_live_right.setObjectName(_fromUtf8("line_live_right"))
        self.line_left = QtWidgets.QFrame(self.centralwidget)
        self.line_left.setGeometry(QtCore.QRect(234, 296, 2, 163))
        self.line_left.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_left.setLineWidth(1)
        self.line_left.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_left.setObjectName(_fromUtf8("line_left"))
        self.line_live_left = QtWidgets.QFrame(self.centralwidget)
        self.line_live_left.setGeometry(QtCore.QRect(110, 69, 2, 180))
        self.line_live_left.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_live_left.setLineWidth(1)
        self.line_live_left.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_live_left.setObjectName(_fromUtf8("line_live_left"))
        self.line_split_left = QtWidgets.QFrame(self.centralwidget)
        self.line_split_left.setGeometry(QtCore.QRect(360, 69, 2, 180))
        self.line_split_left.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_split_left.setLineWidth(1)
        self.line_split_left.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_split_left.setObjectName(_fromUtf8("line_split_left"))
        self.line_split_right = QtWidgets.QFrame(self.centralwidget)
        self.line_split_right.setGeometry(QtCore.QRect(599, 69, 2, 180))
        self.line_split_right.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_split_right.setLineWidth(1)
        self.line_split_right.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_split_right.setObjectName(_fromUtf8("line_split_right"))
        self.line_split_top = QtWidgets.QFrame(self.centralwidget)
        self.line_split_top.setGeometry(QtCore.QRect(361, 68, 240, 2))
        self.line_split_top.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_split_top.setLineWidth(1)
        self.line_split_top.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_split_top.setObjectName(_fromUtf8("line_split_top"))
        self.line_split_bottom = QtWidgets.QFrame(self.centralwidget)
        self.line_split_bottom.setGeometry(QtCore.QRect(361, 247, 240, 2))
        self.line_split_bottom.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_split_bottom.setLineWidth(1)
        self.line_split_bottom.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_split_bottom.setObjectName(_fromUtf8("line_split_bottom"))
        self.timerglobalhotkeysLabel = QtWidgets.QLabel(self.centralwidget)
        self.timerglobalhotkeysLabel.setGeometry(QtCore.QRect(313, 293, 101, 20))
        self.timerglobalhotkeysLabel.setObjectName(_fromUtf8("timerglobalhotkeysLabel"))
        self.line_right = QtWidgets.QFrame(self.centralwidget)
        self.line_right.setGeometry(QtCore.QRect(489, 296, 2, 163))
        self.line_right.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_right.setLineWidth(1)
        self.line_right.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_right.setObjectName(_fromUtf8("line_right"))
        self.liveImage = QtWidgets.QLabel(self.centralwidget)
        self.liveImage.setGeometry(QtCore.QRect(111, 69, 240, 180))
        self.liveImage.setText(_fromUtf8(""))
        self.liveImage.setObjectName(_fromUtf8("liveImage"))
        self.currentSplitImage = QtWidgets.QLabel(self.centralwidget)
        self.currentSplitImage.setGeometry(QtCore.QRect(361, 69, 240, 180))
        self.currentSplitImage.setText(_fromUtf8(""))
        self.currentSplitImage.setObjectName(_fromUtf8("currentSplitImage"))
        self.currentsplitimageLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentsplitimageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentsplitimageLabel.setGeometry(QtCore.QRect(370, 50, 221, 20))
        self.currentsplitimageLabel.setObjectName(_fromUtf8("currentsplitimageLabel"))
        self.imageloopLabel = QtWidgets.QLabel(self.centralwidget)
        self.imageloopLabel.setGeometry(QtCore.QRect(362, 251, 108, 20))
        self.imageloopLabel.setObjectName(_fromUtf8("Image Loop #:"))
        self.widthLabel = QtWidgets.QLabel(self.centralwidget)
        self.widthLabel.setGeometry(QtCore.QRect(14, 177, 31, 16))
        self.widthLabel.setObjectName(_fromUtf8("widthLabel"))
        self.heightLabel = QtWidgets.QLabel(self.centralwidget)
        self.heightLabel.setGeometry(QtCore.QRect(68, 177, 31, 16))
        self.heightLabel.setObjectName(_fromUtf8("heightLabel"))
        self.fpsvalueLabel = QtWidgets.QLabel(self.centralwidget)
        self.fpsvalueLabel.setGeometry(QtCore.QRect(58, 225, 26, 20))
        self.fpsvalueLabel.setText(_fromUtf8(""))
        self.fpsvalueLabel.setObjectName(_fromUtf8("fpsvalueLabel"))
        self.widthSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.widthSpinBox.setGeometry(QtCore.QRect(6, 193, 44, 22))
        self.widthSpinBox.setMinimum(1)
        self.widthSpinBox.setMaximum(10000)
        self.widthSpinBox.setProperty("value", 640)
        self.widthSpinBox.setObjectName(_fromUtf8("widthSpinBox"))
        self.heightSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.heightSpinBox.setGeometry(QtCore.QRect(62, 193, 44, 22))
        self.heightSpinBox.setMinimum(1)
        self.heightSpinBox.setMaximum(10000)
        self.heightSpinBox.setProperty("value", 480)
        self.heightSpinBox.setObjectName(_fromUtf8("heightSpinBox"))
        self.captureregionLabel = QtWidgets.QLabel(self.centralwidget)
        self.captureregionLabel.setGeometry(QtCore.QRect(192, 50, 81, 16))
        self.captureregionLabel.setObjectName(_fromUtf8("captureregionLabel"))
        self.fpslimitLabel = QtWidgets.QLabel(self.centralwidget)
        self.fpslimitLabel.setGeometry(QtCore.QRect(8, 251, 51, 16))
        self.fpslimitLabel.setObjectName(_fromUtf8("fpslimitLabel"))
        self.fpslimitSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.fpslimitSpinBox.setGeometry(QtCore.QRect(62, 248, 44, 22))
        self.fpslimitSpinBox.setPrefix(_fromUtf8(""))
        self.fpslimitSpinBox.setDecimals(0)
        self.fpslimitSpinBox.setMinimum(30.0)
        self.fpslimitSpinBox.setMaximum(5000.0)
        self.fpslimitSpinBox.setSingleStep(1.0)
        self.fpslimitSpinBox.setProperty("value", 60.0)
        self.fpslimitSpinBox.setObjectName(_fromUtf8("fpslimitSpinBox"))
        self.currentsplitimagefileLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentsplitimagefileLabel.setGeometry(QtCore.QRect(362, 271, 237, 20))
        self.currentsplitimagefileLabel.setText(_fromUtf8(""))
        self.currentsplitimagefileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.currentsplitimagefileLabel.setObjectName(_fromUtf8("currentsplitimagefileLabel"))
        self.takescreenshotButton = QtWidgets.QPushButton(self.centralwidget)
        self.takescreenshotButton.setGeometry(QtCore.QRect(250, 251, 91, 21))
        self.takescreenshotButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.takescreenshotButton.setObjectName(_fromUtf8("takescreenshotButton"))
        self.xSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.xSpinBox.setGeometry(QtCore.QRect(6, 154, 44, 22))
        self.xSpinBox.setReadOnly(False)
        self.xSpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.xSpinBox.setMinimum(0)
        self.xSpinBox.setMaximum(999999999)
        self.xSpinBox.setSingleStep(1)
        self.xSpinBox.setProperty("value", 0)
        self.xSpinBox.setObjectName(_fromUtf8("xSpinBox"))
        self.ySpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.ySpinBox.setGeometry(QtCore.QRect(62, 154, 44, 22))
        self.ySpinBox.setReadOnly(False)
        self.ySpinBox.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.ySpinBox.setMinimum(0)
        self.ySpinBox.setMaximum(999999999)
        self.ySpinBox.setProperty("value", 0)
        self.ySpinBox.setObjectName(_fromUtf8("ySpinBox"))
        self.yLabel = QtWidgets.QLabel(self.centralwidget)
        self.yLabel.setGeometry(QtCore.QRect(81, 139, 7, 16))
        self.yLabel.setObjectName(_fromUtf8("yLabel"))
        self.comparisonmethodComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comparisonmethodComboBox.setGeometry(QtCore.QRect(143, 299, 81, 22))
        self.comparisonmethodComboBox.setObjectName(_fromUtf8("comparisonmethodComboBox"))
        self.comparisonmethodComboBox.addItem(_fromUtf8(""))
        self.comparisonmethodComboBox.addItem(_fromUtf8(""))
        self.comparisonmethodComboBox.addItem(_fromUtf8(""))
        self.pauseDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.pauseDoubleSpinBox.setGeometry(QtCore.QRect(160, 425, 64, 22))
        self.pauseDoubleSpinBox.setMaximum(999999999.0)
        self.pauseDoubleSpinBox.setSingleStep(1.0)
        self.pauseDoubleSpinBox.setProperty("value", 10.0)
        self.pauseDoubleSpinBox.setObjectName(_fromUtf8("pauseDoubleSpinBox"))
        self.custompausetimesCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.custompausetimesCheckBox.setEnabled(True)
        self.custompausetimesCheckBox.setGeometry(QtCore.QRect(10, 435, 121, 17))
        self.custompausetimesCheckBox.setWhatsThis(_fromUtf8(""))
        self.custompausetimesCheckBox.setChecked(False)
        self.custompausetimesCheckBox.setTristate(False)
        self.custompausetimesCheckBox.setObjectName(_fromUtf8("custompausetimesCheckBox"))
        self.customthresholdsCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.customthresholdsCheckBox.setEnabled(True)
        self.customthresholdsCheckBox.setGeometry(QtCore.QRect(10, 394, 111, 17))
        self.customthresholdsCheckBox.setWhatsThis(_fromUtf8(""))
        self.customthresholdsCheckBox.setChecked(False)
        self.customthresholdsCheckBox.setTristate(False)
        self.customthresholdsCheckBox.setObjectName(_fromUtf8("customthresholdsCheckBox"))
        self.comparisonmethodLabel = QtWidgets.QLabel(self.centralwidget)
        self.comparisonmethodLabel.setGeometry(QtCore.QRect(10, 300, 101, 16))
        self.comparisonmethodLabel.setObjectName(_fromUtf8("comparisonmethodLabel"))
        self.alignregionButton = QtWidgets.QPushButton(self.centralwidget)
        self.alignregionButton.setGeometry(QtCore.QRect(5, 92, 101, 23))
        self.alignregionButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.alignregionButton.setObjectName(_fromUtf8("alignregionButton"))
        self.groupDummySplitsCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.groupDummySplitsCheckBox.setGeometry(QtCore.QRect(252, 440, 230, 17))
        self.groupDummySplitsCheckBox.setChecked(False)
        self.groupDummySplitsCheckBox.setObjectName(_fromUtf8("groupDummySplitsCheckBox"))
        self.selectwindowButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectwindowButton.setGeometry(QtCore.QRect(5, 117, 101, 23))
        self.selectwindowButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.selectwindowButton.setObjectName(_fromUtf8("selectwindowButton"))
        self.splitimagefolderLabel.raise_()
        self.splitimagefolderLineEdit.raise_()
        self.browseButton.raise_()
        self.xLabel.raise_()
        self.liveimageCheckBox.raise_()
        self.loopCheckBox.raise_()
        self.autostartonresetCheckBox.raise_()
        self.selectregionButton.raise_()
        self.similaritythresholdLabel.raise_()
        self.similaritythresholdDoubleSpinBox.raise_()
        self.startautosplitterButton.raise_()
        self.resetButton.raise_()
        self.undosplitButton.raise_()
        self.skipsplitButton.raise_()
        self.pauseLabel.raise_()
        self.checkfpsButton.raise_()
        self.fpsLabel.raise_()
        self.showlivesimilarityCheckBox.raise_()
        self.showhighestsimilarityCheckBox.raise_()
        self.livesimilarityLabel.raise_()
        self.highestsimilarityLabel.raise_()
        self.splitLabel.raise_()
        self.resetLabel.raise_()
        self.skiptsplitLabel.raise_()
        self.undosplitLabel.raise_()
        self.pausehotkeyLabel.raise_()
        self.splitLineEdit.raise_()
        self.undosplitLineEdit.raise_()
        self.skipsplitLineEdit.raise_()
        self.resetLineEdit.raise_()
        self.pausehotkeyLineEdit.raise_()
        self.setsplithotkeyButton.raise_()
        self.setresethotkeyButton.raise_()
        self.setskipsplithotkeyButton.raise_()
        self.setundosplithotkeyButton.raise_()
        self.setpausehotkeyButton.raise_()
        self.line_live_bottom.raise_()
        self.line_live_top.raise_()
        self.line_live_right.raise_()
        self.line_left.raise_()
        self.line_live_left.raise_()
        self.line_split_left.raise_()
        self.line_split_right.raise_()
        self.line_split_top.raise_()
        self.line_split_bottom.raise_()
        self.timerglobalhotkeysLabel.raise_()
        self.line_right.raise_()
        self.currentsplitimageLabel.raise_()
        self.imageloopLabel.raise_()
        self.liveImage.raise_()
        self.currentSplitImage.raise_()
        self.widthLabel.raise_()
        self.heightLabel.raise_()
        self.fpsvalueLabel.raise_()
        self.widthSpinBox.raise_()
        self.heightSpinBox.raise_()
        self.captureregionLabel.raise_()
        self.fpslimitLabel.raise_()
        self.fpslimitSpinBox.raise_()
        self.currentsplitimagefileLabel.raise_()
        self.takescreenshotButton.raise_()
        self.xSpinBox.raise_()
        self.ySpinBox.raise_()
        self.yLabel.raise_()
        self.comparisonmethodComboBox.raise_()
        self.pauseDoubleSpinBox.raise_()
        self.custompausetimesCheckBox.raise_()
        self.customthresholdsCheckBox.raise_()
        self.comparisonmethodLabel.raise_()
        self.alignregionButton.raise_()
        self.groupDummySplitsCheckBox.raise_()
        self.selectwindowButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 612, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionView_Help = QtWidgets.QAction(MainWindow)
        self.actionView_Help.setObjectName(_fromUtf8("actionView_Help"))
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionSave_Settings = QtWidgets.QAction(MainWindow)
        self.actionSave_Settings.setObjectName(_fromUtf8("actionSave_Settings"))
        self.actionSave_Settings_As = QtWidgets.QAction(MainWindow)
        self.actionSave_Settings_As.setObjectName(_fromUtf8("actionSave_Settings_As"))
        self.actionLoad_Settings = QtWidgets.QAction(MainWindow)
        self.actionLoad_Settings.setObjectName(_fromUtf8("actionLoad_Settings"))
        self.menuHelp.addAction(self.actionView_Help)
        self.menuHelp.addAction(self.actionAbout)
        self.menuFile.addAction(self.actionSave_Settings)
        self.menuFile.addAction(self.actionSave_Settings_As)
        self.menuFile.addAction(self.actionLoad_Settings)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.splitimagefolderLineEdit, self.xSpinBox)
        MainWindow.setTabOrder(self.xSpinBox, self.ySpinBox)
        MainWindow.setTabOrder(self.ySpinBox, self.widthSpinBox)
        MainWindow.setTabOrder(self.widthSpinBox, self.heightSpinBox)
        MainWindow.setTabOrder(self.heightSpinBox, self.fpslimitSpinBox)
        MainWindow.setTabOrder(self.fpslimitSpinBox, self.liveimageCheckBox)
        MainWindow.setTabOrder(self.liveimageCheckBox, self.comparisonmethodComboBox)
        MainWindow.setTabOrder(self.comparisonmethodComboBox, self.showlivesimilarityCheckBox)
        MainWindow.setTabOrder(self.showlivesimilarityCheckBox, self.showhighestsimilarityCheckBox)
        MainWindow.setTabOrder(self.showhighestsimilarityCheckBox, self.customthresholdsCheckBox)
        MainWindow.setTabOrder(self.customthresholdsCheckBox, self.similaritythresholdDoubleSpinBox)
        MainWindow.setTabOrder(self.similaritythresholdDoubleSpinBox, self.custompausetimesCheckBox)
        MainWindow.setTabOrder(self.custompausetimesCheckBox, self.pauseDoubleSpinBox)
        MainWindow.setTabOrder(self.pauseDoubleSpinBox, self.splitLineEdit)
        MainWindow.setTabOrder(self.splitLineEdit, self.resetLineEdit)
        MainWindow.setTabOrder(self.resetLineEdit, self.skipsplitLineEdit)
        MainWindow.setTabOrder(self.skipsplitLineEdit, self.undosplitLineEdit)
        MainWindow.setTabOrder(self.undosplitLineEdit, self.pausehotkeyLineEdit)
        MainWindow.setTabOrder(self.pausehotkeyLineEdit, self.groupDummySplitsCheckBox)
        MainWindow.setTabOrder(self.groupDummySplitsCheckBox, self.loopCheckBox)
        MainWindow.setTabOrder(self.loopCheckBox, self.autostartonresetCheckBox)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "AutoSplit", None))
        self.splitimagefolderLabel.setText(_translate("MainWindow", "Split Image Folder:", None))
        self.browseButton.setText(_translate("MainWindow", "Browse..", None))
        self.xLabel.setText(_translate("MainWindow", "X", None))
        self.liveimageCheckBox.setText(_translate("MainWindow", "Live Capture Region", None))
        self.loopCheckBox.setText(_translate("MainWindow", "Loop Split Images", None))
        self.autostartonresetCheckBox.setText(_translate("MainWindow", "Auto Start On Reset", None))
        self.selectregionButton.setText(_translate("MainWindow", "Select Region", None))
        self.similaritythresholdLabel.setText(_translate("MainWindow", "Similarity threshold", None))
        self.startautosplitterButton.setText(_translate("MainWindow", "Start Auto Splitter", None))
        self.resetButton.setText(_translate("MainWindow", "Reset", None))
        self.undosplitButton.setText(_translate("MainWindow", "Undo Split", None))
        self.skipsplitButton.setText(_translate("MainWindow", "Skip Split", None))
        self.pauseLabel.setText(_translate("MainWindow", "Pause time after split (sec)", None))
        self.checkfpsButton.setText(_translate("MainWindow", "Max FPS", None))
        self.fpsLabel.setText(_translate("MainWindow", "FPS", None))
        self.showlivesimilarityCheckBox.setText(_translate("MainWindow", "Show live similarity", None))
        self.showhighestsimilarityCheckBox.setText(_translate("MainWindow", "Show highest similarity", None))
        self.splitLabel.setText(_translate("MainWindow", "Start / Split", None))
        self.resetLabel.setText(_translate("MainWindow", "Reset", None))
        self.skiptsplitLabel.setText(_translate("MainWindow", "Skip Split", None))
        self.undosplitLabel.setText(_translate("MainWindow", "Undo Split", None))
        self.pausehotkeyLabel.setText(_translate("MainWindow", "Pause", None))
        self.setsplithotkeyButton.setText(_translate("MainWindow", "Set Hotkey", None))
        self.setresethotkeyButton.setText(_translate("MainWindow", "Set Hotkey", None))
        self.setskipsplithotkeyButton.setText(_translate("MainWindow", "Set Hotkey", None))
        self.setundosplithotkeyButton.setText(_translate("MainWindow", "Set Hotkey", None))
        self.setpausehotkeyButton.setText(_translate("MainWindow", "Set Hotkey", None))
        self.timerglobalhotkeysLabel.setText(_translate("MainWindow", "Timer Global Hotkeys", None))
        self.currentsplitimageLabel.setText(_translate("MainWindow", "Current Split Image", None))
        self.imageloopLabel.setText(_translate("MainWindow", "Image Loop #:", None))
        self.widthLabel.setText(_translate("MainWindow", "Width", None))
        self.heightLabel.setText(_translate("MainWindow", "Height", None))
        self.captureregionLabel.setText(_translate("MainWindow", "Capture Region", None))
        self.fpslimitLabel.setText(_translate("MainWindow", "FPS Limit:", None))
        self.takescreenshotButton.setText(_translate("MainWindow", "Take Screenshot", None))
        self.yLabel.setText(_translate("MainWindow", "Y", None))
        self.comparisonmethodComboBox.setItemText(0, _translate("MainWindow", "L2 Norm", None))
        self.comparisonmethodComboBox.setItemText(1, _translate("MainWindow", "Histograms", None))
        self.comparisonmethodComboBox.setItemText(2, _translate("MainWindow", "pHash", None))
        self.custompausetimesCheckBox.setText(_translate("MainWindow", "Custom pause times", None))
        self.customthresholdsCheckBox.setText(_translate("MainWindow", "Custom thresholds", None))
        self.comparisonmethodLabel.setText(_translate("MainWindow", "Comparison Method", None))
        self.alignregionButton.setText(_translate("MainWindow", "Align Region", None))
        self.groupDummySplitsCheckBox.setText(_translate("MainWindow", "Group dummy splits when undoing/skipping", None))
        self.selectwindowButton.setText(_translate("MainWindow", "Select Window", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionView_Help.setText(_translate("MainWindow", "View Help", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionSave_Settings.setText(_translate("MainWindow", "Save Settings", None))
        self.actionSave_Settings_As.setText(_translate("MainWindow", "Save Settings As...", None))
        self.actionLoad_Settings.setText(_translate("MainWindow", "Load Settings", None))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
