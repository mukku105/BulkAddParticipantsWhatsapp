# Form implementation generated from reading ui file 'd:\PROJECTS_WORKSPACE\Python_WS\BulkAddParticipantsWhatsapp\main.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(509, 541)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 20, 471, 201))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.l_csvpath = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.l_csvpath.setObjectName("l_csvpath")
        self.gridLayout.addWidget(self.l_csvpath, 5, 0, 1, 3, QtCore.Qt.AlignmentFlag.AlignHCenter|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.pb_savetoken = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_savetoken.sizePolicy().hasHeightForWidth())
        self.pb_savetoken.setSizePolicy(sizePolicy)
        self.pb_savetoken.setMinimumSize(QtCore.QSize(0, 40))
        self.pb_savetoken.setStyleSheet("QPushButton {\n"
"    background-color: black;\n"
"    border-radius: 10px;\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"    padding: 0 0 5px 0;\n"
"    color:white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 255, 255);\n"
"}\n"
"")
        self.pb_savetoken.setObjectName("pb_savetoken")
        self.gridLayout.addWidget(self.pb_savetoken, 0, 1, 1, 1)
        self.le_watoken = QtWidgets.QLineEdit(parent=self.gridLayoutWidget)
        self.le_watoken.setMinimumSize(QtCore.QSize(0, 30))
        self.le_watoken.setObjectName("le_watoken")
        self.gridLayout.addWidget(self.le_watoken, 1, 1, 1, 1)
        self.pb_import = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.pb_import.setMinimumSize(QtCore.QSize(0, 40))
        self.pb_import.setStyleSheet("")
        self.pb_import.setObjectName("pb_import")
        self.gridLayout.addWidget(self.pb_import, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.cb_grouplist = QtWidgets.QComboBox(parent=self.gridLayoutWidget)
        self.cb_grouplist.setMinimumSize(QtCore.QSize(0, 30))
        self.cb_grouplist.setObjectName("cb_grouplist")
        self.gridLayout.addWidget(self.cb_grouplist, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.l_req_left = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.l_req_left.setFont(font)
        self.l_req_left.setObjectName("l_req_left")
        self.gridLayout.addWidget(self.l_req_left, 0, 2, 1, 1, QtCore.Qt.AlignmentFlag.AlignRight)
        self.pb_sync = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_sync.sizePolicy().hasHeightForWidth())
        self.pb_sync.setSizePolicy(sizePolicy)
        self.pb_sync.setMinimumSize(QtCore.QSize(100, 40))
        self.pb_sync.setMouseTracking(False)
        self.pb_sync.setAcceptDrops(False)
        self.pb_sync.setAutoFillBackground(False)
        self.pb_sync.setStyleSheet("QPushButton {\n"
"    background-color: rgb(0, 212, 0);\n"
"    border-radius: 10px;\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"    padding: 0 0 5px 0;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 255, 127);\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: rgb(85, 255, 255);\n"
"}\n"
"")
        self.pb_sync.setAutoDefault(False)
        self.pb_sync.setDefault(False)
        self.pb_sync.setFlat(False)
        self.pb_sync.setObjectName("pb_sync")
        self.gridLayout.addWidget(self.pb_sync, 1, 2, 1, 1)
        self.pb_add = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_add.sizePolicy().hasHeightForWidth())
        self.pb_add.setSizePolicy(sizePolicy)
        self.pb_add.setMinimumSize(QtCore.QSize(100, 40))
        self.pb_add.setMouseTracking(False)
        self.pb_add.setAcceptDrops(False)
        self.pb_add.setAutoFillBackground(False)
        self.pb_add.setStyleSheet("QPushButton {\n"
"    background-color: rgb(70, 175, 255);\n"
"    border-radius: 10px;\n"
"    font-weight: bold;\n"
"    font-size: 16px;\n"
"    padding: 0 0 4px 0;\n"
"    color: white;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 255, 127);\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: rgb(85, 255, 255);\n"
"}\n"
"")
        self.pb_add.setAutoDefault(False)
        self.pb_add.setDefault(False)
        self.pb_add.setFlat(False)
        self.pb_add.setObjectName("pb_add")
        self.gridLayout.addWidget(self.pb_add, 4, 2, 1, 1)
        self.pb_instruct = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_instruct.sizePolicy().hasHeightForWidth())
        self.pb_instruct.setSizePolicy(sizePolicy)
        self.pb_instruct.setMinimumSize(QtCore.QSize(100, 40))
        self.pb_instruct.setMouseTracking(False)
        self.pb_instruct.setAcceptDrops(False)
        self.pb_instruct.setAutoFillBackground(False)
        self.pb_instruct.setStyleSheet("QPushButton {\n"
"    background-color: rgb(255, 170, 255);\n"
"    border-radius: 10px;\n"
"    font-weight: bold;\n"
"    font-size: 12px;\n"
"    padding: 8px;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: rgb(0, 255, 127);\n"
"}")
        self.pb_instruct.setAutoDefault(False)
        self.pb_instruct.setDefault(False)
        self.pb_instruct.setFlat(False)
        self.pb_instruct.setObjectName("pb_instruct")
        self.gridLayout.addWidget(self.pb_instruct, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignHCenter)
        self.tv_csv = QtWidgets.QTableView(parent=Form)
        self.tv_csv.setGeometry(QtCore.QRect(25, 240, 461, 251))
        self.tv_csv.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.tv_csv.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tv_csv.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tv_csv.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.tv_csv.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.tv_csv.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tv_csv.setAlternatingRowColors(True)
        self.tv_csv.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.ExtendedSelection)
        self.tv_csv.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        self.tv_csv.setGridStyle(QtCore.Qt.PenStyle.SolidLine)
        self.tv_csv.setSortingEnabled(True)
        self.tv_csv.setWordWrap(False)
        self.tv_csv.setObjectName("tv_csv")
        self.tv_csv.horizontalHeader().setCascadingSectionResizes(True)
        self.tv_csv.horizontalHeader().setStretchLastSection(True)
        self.tv_csv.verticalHeader().setCascadingSectionResizes(False)
        self.tv_csv.verticalHeader().setStretchLastSection(False)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(140, 510, 251, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(True)
        font.setUnderline(False)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.TextFormat.AutoText)
        self.label_3.setOpenExternalLinks(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.l_csvpath.setText(_translate("Form", "Import CSV file containing contact numbers."))
        self.pb_savetoken.setText(_translate("Form", "Save Current Token"))
        self.pb_import.setText(_translate("Form", "Import CSV"))
        self.label_2.setText(_translate("Form", "Group List"))
        self.label.setText(_translate("Form", "Whapi.cloud Token"))
        self.l_req_left.setText(_translate("Form", "Req. left: -"))
        self.pb_sync.setText(_translate("Form", "Sync"))
        self.pb_add.setText(_translate("Form", "Add"))
        self.pb_instruct.setText(_translate("Form", "Get API Token"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>Developed by Muksam Limboo, <a href=\"https://github.com/mukku105\"><span style=\" text-decoration: underline; color:#0000ff;\">mukku105</span></a></p></body></html>"))
