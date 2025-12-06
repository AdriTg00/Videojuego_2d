# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'partidasGuardadas.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHeaderView, QLabel, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_partidasGuardadas(object):
    def setupUi(self, partidasGuardadas):
        if not partidasGuardadas.objectName():
            partidasGuardadas.setObjectName(u"partidasGuardadas")
        partidasGuardadas.resize(575, 359)
        partidasGuardadas.setStyleSheet(u"background-color: #faf0d6;")
        self.gridLayout_3 = QGridLayout(partidasGuardadas)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame_2 = QFrame(partidasGuardadas)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.partidasGuardadas_2 = QLabel(self.frame_2)
        self.partidasGuardadas_2.setObjectName(u"partidasGuardadas_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.partidasGuardadas_2.sizePolicy().hasHeightForWidth())
        self.partidasGuardadas_2.setSizePolicy(sizePolicy)
        self.partidasGuardadas_2.setMaximumSize(QSize(500, 300))
        self.partidasGuardadas_2.setStyleSheet(u"QLabel {\n"
"    color: #3C3C3C;\n"
"    font-size: 30px;\n"
"    font-weight: bold;\n"
"}")
        self.partidasGuardadas_2.setTextFormat(Qt.TextFormat.AutoText)
        self.partidasGuardadas_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.partidasGuardadas_2.setWordWrap(False)
        self.partidasGuardadas_2.setOpenExternalLinks(False)

        self.gridLayout_2.addWidget(self.partidasGuardadas_2, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 0, 1, 1)

        self.frame = QFrame(partidasGuardadas)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tablaGuardados = QTableWidget(self.frame)
        if (self.tablaGuardados.columnCount() < 7):
            self.tablaGuardados.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tablaGuardados.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tablaGuardados.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tablaGuardados.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tablaGuardados.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tablaGuardados.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tablaGuardados.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tablaGuardados.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tablaGuardados.setObjectName(u"tablaGuardados")
        self.tablaGuardados.setMaximumSize(QSize(500, 500))
        self.tablaGuardados.setStyleSheet(u"/* --- Tabla general --- */\n"
"QTableWidget, QTableView {\n"
"    background-color: #F5E8C7;      /* pergamino */\n"
"    color: #5C3A1E;                 /* marr\u00f3n texto */\n"
"    border: 3px solid #7A4E28;      /* borde pixel marr\u00f3n */\n"
"    gridline-color: #D2B48C;        /* l\u00edneas internas suaves */\n"
"    font-size: 14px;\n"
"    selection-background-color: #F1D7A3; \n"
"    selection-color: #3B2614;\n"
"}\n"
"\n"
"/* --- Cabecera horizontal --- */\n"
"QHeaderView::section {\n"
"    background-color: #EED9B6; \n"
"    color: #4A2E1A;\n"
"    padding: 6px;\n"
"    border: 2px solid #7A4E28;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* --- Filas alternas --- */\n"
"QTableWidget::item:alternate,\n"
"QTableView::item:alternate {\n"
"    background-color: #F9EED3; \n"
"}\n"
"\n"
"/* --- Filas normales --- */\n"
"QTableWidget::item,\n"
"QTableView::item {\n"
"    padding: 4px;\n"
"}\n"
"\n"
"/* --- Hover sobre filas --- */\n"
"QTableWidget::item:hover,\n"
"QTableView::item:hover {\n"
"    bac"
                        "kground-color: #FFF5DD;\n"
"    color: #3B2614;\n"
"}\n"
"\n"
"/* --- Barra de scroll horizontal --- */\n"
"QScrollBar:horizontal {\n"
"    background: #EED9B6;\n"
"    height: 14px;\n"
"    border: 2px solid #7A4E28;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: #C7A272;\n"
"    min-width: 30px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"    background: #B89262;\n"
"    width: 14px;\n"
"}\n"
"\n"
"/* --- Scroll vertical (si existiera) --- */\n"
"QScrollBar:vertical {\n"
"    background: #EED9B6;\n"
"    width: 14px;\n"
"    border: 2px solid #7A4E28;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #C7A272;\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical {\n"
"    background: #B89262;\n"
"    height: 14px;\n"
"}\n"
"")
        self.tablaGuardados.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tablaGuardados.setAlternatingRowColors(True)
        self.tablaGuardados.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tablaGuardados.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tablaGuardados.setSortingEnabled(True)
        self.tablaGuardados.setColumnCount(7)

        self.gridLayout.addWidget(self.tablaGuardados, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 3, 0, 1, 1)


        self.retranslateUi(partidasGuardadas)

        QMetaObject.connectSlotsByName(partidasGuardadas)
    # setupUi

    def retranslateUi(self, partidasGuardadas):
        partidasGuardadas.setWindowTitle(QCoreApplication.translate("partidasGuardadas", u"Form", None))
        self.partidasGuardadas_2.setText(QCoreApplication.translate("partidasGuardadas", u"Partidas guardadas:", None))
        ___qtablewidgetitem = self.tablaGuardados.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("partidasGuardadas", u"Jugador", None));
        ___qtablewidgetitem1 = self.tablaGuardados.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("partidasGuardadas", u"Nivel", None));
        ___qtablewidgetitem2 = self.tablaGuardados.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("partidasGuardadas", u"Muertes", None));
        ___qtablewidgetitem3 = self.tablaGuardados.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("partidasGuardadas", u"Puntuacion", None));
        ___qtablewidgetitem4 = self.tablaGuardados.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("partidasGuardadas", u"Tiempo", None));
        ___qtablewidgetitem5 = self.tablaGuardados.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("partidasGuardadas", u"Fecha", None));
        ___qtablewidgetitem6 = self.tablaGuardados.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("partidasGuardadas", u"ID", None));
    # retranslateUi

