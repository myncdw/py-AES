# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(561, 353)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.input_lb = QLabel(self.centralwidget)
        self.input_lb.setObjectName(u"input_lb")

        self.verticalLayout_2.addWidget(self.input_lb)

        self.input_box = QTextEdit(self.centralwidget)
        self.input_box.setObjectName(u"input_box")

        self.verticalLayout_2.addWidget(self.input_box)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.key_box = QLineEdit(self.centralwidget)
        self.key_box.setObjectName(u"key_box")

        self.gridLayout.addWidget(self.key_box, 2, 0, 1, 1)

        self.key_lb = QLabel(self.centralwidget)
        self.key_lb.setObjectName(u"key_lb")

        self.gridLayout.addWidget(self.key_lb, 1, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)

        self.output_lb = QLabel(self.centralwidget)
        self.output_lb.setObjectName(u"output_lb")

        self.verticalLayout_2.addWidget(self.output_lb)

        self.output_box = QTextEdit(self.centralwidget)
        self.output_box.setObjectName(u"output_box")
        self.output_box.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.output_box)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.info = QLabel(self.centralwidget)
        self.info.setObjectName(u"info")

        self.verticalLayout.addWidget(self.info)

        self.clear_btn = QPushButton(self.centralwidget)
        self.clear_btn.setObjectName(u"clear_btn")

        self.verticalLayout.addWidget(self.clear_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.encrypt_btn = QPushButton(self.centralwidget)
        self.encrypt_btn.setObjectName(u"encrypt_btn")

        self.verticalLayout.addWidget(self.encrypt_btn)

        self.decrypt_btn = QPushButton(self.centralwidget)
        self.decrypt_btn.setObjectName(u"decrypt_btn")

        self.verticalLayout.addWidget(self.decrypt_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.copy_key_btn = QPushButton(self.centralwidget)
        self.copy_key_btn.setObjectName(u"copy_key_btn")

        self.verticalLayout.addWidget(self.copy_key_btn)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.copy_result_btn = QPushButton(self.centralwidget)
        self.copy_result_btn.setObjectName(u"copy_result_btn")

        self.verticalLayout.addWidget(self.copy_result_btn)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_5)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.input_lb.setText(QCoreApplication.translate("MainWindow", u"\u539f\u59cb\u5185\u5bb9", None))
        self.input_box.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.key_lb.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.output_lb.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u8f93\u51fa", None))
        self.info.setText(QCoreApplication.translate("MainWindow", u"AES\u52a0\u5bc6", None))
        self.clear_btn.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u5168\u90e8", None))
        self.encrypt_btn.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u5bc6", None))
        self.decrypt_btn.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u5bc6", None))
        self.copy_key_btn.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236\u5bc6\u7801", None))
        self.copy_result_btn.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236\u7ed3\u679c", None))
    # retranslateUi

