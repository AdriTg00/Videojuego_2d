# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configuracion.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QSlider,
    QSpacerItem, QWidget)

class Ui_configuracion(object):
    def setupUi(self, configuracion):
        if not configuracion.objectName():
            configuracion.setObjectName(u"configuracion")
        configuracion.resize(479, 330)
        configuracion.setStyleSheet(u"background-color: #faf0d6;")
        self.gridLayout = QGridLayout(configuracion)
        self.gridLayout.setObjectName(u"gridLayout")
        self.TipoDeVisualizacion = QLabel(configuracion)
        self.TipoDeVisualizacion.setObjectName(u"TipoDeVisualizacion")
        self.TipoDeVisualizacion.setStyleSheet(u"QLabel {\n"
"    color: #3C3C3C;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    padding: 6px;\n"
"    letter-spacing: 1px;\n"
"}")

        self.gridLayout.addWidget(self.TipoDeVisualizacion, 5, 2, 1, 1)

        self.volumenSFXSlider = QSlider(configuracion)
        self.volumenSFXSlider.setObjectName(u"volumenSFXSlider")
        self.volumenSFXSlider.setMaximumSize(QSize(300, 70))
        self.volumenSFXSlider.setStyleSheet(u"/* --- QSLIDER HORIZONTAL --- */\n"
"QSlider::groove:horizontal {\n"
"    border: 2px solid #C9A43A;              /* Contorno dorado */\n"
"    height: 10px;\n"
"    background: #F4E29B;                    /* Amarillo suave (igual que botones) */\n"
"    border-radius: 5px;\n"
"    margin: 0px 10px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: 0.4,\n"
"        fx: 0.4, fy: 0.4,\n"
"        radius: 0.6,\n"
"        stop: 0 #FFE873,\n"
"        stop: 1 #C9A43A\n"
"    );\n"
"    border: 2px solid #5A4A00;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 10px;\n"
"    margin: -6px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: 0.4,\n"
"        fx: 0.4, fy: 0.4,\n"
"        radius: 0.6,\n"
"        stop: 0 #FFF3B0,\n"
"        stop: 1 #E5B937\n"
"    );\n"
"}\n"
"\n"
"/* --- PARTE IZQUIERDA (LLENA) --- */\n"
"QSlider::sub-page:horizontal {\n"
"    background: #9BCB43;   "
                        "                 /* Verde suave tipo \u201cCargar datos\u201d */\n"
"    border: 2px solid #5F8A2A;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* --- PARTE DERECHA (VAC\u00cdA) --- */\n"
"QSlider::add-page:horizontal {\n"
"    background: #EDE2AC;                    /* Beige claro */\n"
"    border: 2px solid #C9A43A;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* --- QSLIDER VERTICAL (por si lo usas) --- */\n"
"QSlider::groove:vertical {\n"
"    border: 2px solid #C9A43A;\n"
"    width: 10px;\n"
"    background: #F4E29B;\n"
"    border-radius: 5px;\n"
"    margin: 10px 0px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: 0.4,\n"
"        fx: 0.4, fy: 0.4,\n"
"        radius: 0.6,\n"
"        stop: 0 #FFE873,\n"
"        stop: 1 #C9A43A\n"
"    );\n"
"    border: 2px solid #5A4A00;\n"
"    height: 20px;\n"
"    width: 20px;\n"
"    border-radius: 10px;\n"
"    margin: 0 -6px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: #9BCB43;\n"
"    "
                        "border: 2px solid #5F8A2A;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background: #EDE2AC;\n"
"    border: 2px solid #C9A43A;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.volumenSFXSlider.setMaximum(100)
        self.volumenSFXSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.volumenSFXSlider, 2, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 5, 5, 1, 1)

        self.Resolucion = QLabel(configuracion)
        self.Resolucion.setObjectName(u"Resolucion")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        self.Resolucion.setFont(font)
        self.Resolucion.setStyleSheet(u"QLabel {\n"
"    color: #3C3C3C;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    padding: 6px;\n"
"    letter-spacing: 1px;\n"
"}")

        self.gridLayout.addWidget(self.Resolucion, 4, 2, 1, 1)

        self.guardar = QPushButton(configuracion)
        self.guardar.setObjectName(u"guardar")
        self.guardar.setStyleSheet(u"#guardar {\n"
"    background-color: #7DA23A;          /* Verde oliva oscuro */\n"
"    border: 3px solid #5C7A28;          /* Borde m\u00e1s oscuro para contraste */\n"
"    border-radius: 12px;\n"
"    color: #FDF5C9;                     /* Texto claro, c\u00e1lido */\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    padding: 8px 15px;\n"
"}\n"
"\n"
"#guardar:hover {\n"
"    background-color: #8FBF42;          /* Un verde m\u00e1s vivo al pasar el rat\u00f3n */\n"
"    border: 3px solid #6E9230;\n"
"}\n"
"\n"
"#guardar:pressed {\n"
"    background-color: #6E8D2E;          /* M\u00e1s oscuro al presionar */\n"
"    border: 3px solid #4F6B21;\n"
"}\n"
"\n"
"#guardar:disabled {\n"
"    background-color: #A0A0A0;          /* Gris cuando est\u00e1 desactivado */\n"
"    color: #D8D8D8;\n"
"    border: 3px solid #808080;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.guardar, 6, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.resolucion = QComboBox(configuracion)
        self.resolucion.addItem("")
        self.resolucion.addItem("")
        self.resolucion.addItem("")
        self.resolucion.addItem("")
        self.resolucion.setObjectName(u"resolucion")
        self.resolucion.setMaximumSize(QSize(180, 50))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setBold(True)
        self.resolucion.setFont(font1)
        self.resolucion.setStyleSheet(u"/* --- ComboBox principal --- */\n"
"QComboBox {\n"
"    font-family: \"Arial\";\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"    padding: 6px 30px 6px 12px;\n"
"    min-height: 36px;\n"
"    border-radius: 10px;\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 rgba(246, 226, 143, 255),\n"
"        stop: 1 rgba(236, 198, 70, 255)\n"
"    );\n"
"    color: #2b2b2b;              /* texto oscuro, visible */\n"
"    border: 2px solid rgba(150, 110, 30, 0.6);\n"
"}\n"
"\n"
"/* --- Flecha de desplegable --- */\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 36px;\n"
"    border: none;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    width: 0;\n"
"    height: 0;\n"
"    margin-right: 10px;\n"
"    border-left: 6px solid transparent;\n"
"    border-right: 6px solid transparent;\n"
"    border-top: 8px solid rgba(70, 40, 10, 0.9); /* color de la flecha */\n"
"}\n"
""
                        "\n"
"/* --- Cuando el combo est\u00e1 presionado --- */\n"
"QComboBox:on {\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 0, x2: 0, y2: 1,\n"
"        stop: 0 rgba(240, 210, 110, 255),\n"
"        stop: 1 rgba(230, 180, 60, 255)\n"
"    );\n"
"}\n"
"\n"
"/* --- Lista desplegable --- */\n"
"QComboBox QAbstractItemView {\n"
"    outline: 0;\n"
"    background: #fff9e6; /* tono beige claro */\n"
"    color: #2b2b2b;       /* texto oscuro */\n"
"    border: 1px solid rgba(150, 110, 30, 0.6);\n"
"    padding: 6px;\n"
"    border-radius: 6px;\n"
"    selection-background-color: rgba(245, 234, 180, 255);\n"
"    selection-color: black; /* texto visible al seleccionar */\n"
"}\n"
"\n"
"/* --- Items de la lista --- */\n"
"QComboBox::item {\n"
"    color: #2b2b2b;\n"
"    background: transparent;\n"
"    padding: 4px 10px;\n"
"}\n"
"\n"
"QComboBox::item:selected {\n"
"    background: rgba(245, 234, 180, 255);\n"
"    color: black;\n"
"}\n"
"")
        self.resolucion.setModelColumn(0)

        self.gridLayout.addWidget(self.resolucion, 4, 3, 1, 1)

        self.VolumenSFX = QLabel(configuracion)
        self.VolumenSFX.setObjectName(u"VolumenSFX")
        self.VolumenSFX.setStyleSheet(u"QLabel {\n"
"    color: #3C3C3C;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    padding: 6px;\n"
"    letter-spacing: 1px;\n"
"}")

        self.gridLayout.addWidget(self.VolumenSFX, 2, 2, 1, 1)

        self.volumenGeneralSlider = QSlider(configuracion)
        self.volumenGeneralSlider.setObjectName(u"volumenGeneralSlider")
        self.volumenGeneralSlider.setMaximumSize(QSize(300, 70))
        self.volumenGeneralSlider.setStyleSheet(u"/* --- QSLIDER HORIZONTAL --- */\n"
"QSlider::groove:horizontal {\n"
"    border: 2px solid #C9A43A;              /* Contorno dorado */\n"
"    height: 10px;\n"
"    background: #F4E29B;                    /* Amarillo suave (igual que botones) */\n"
"    border-radius: 5px;\n"
"    margin: 0px 10px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: 0.4,\n"
"        fx: 0.4, fy: 0.4,\n"
"        radius: 0.6,\n"
"        stop: 0 #FFE873,\n"
"        stop: 1 #C9A43A\n"
"    );\n"
"    border: 2px solid #5A4A00;\n"
"    width: 20px;\n"
"    height: 20px;\n"
"    border-radius: 10px;\n"
"    margin: -6px 0;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: 0.4,\n"
"        fx: 0.4, fy: 0.4,\n"
"        radius: 0.6,\n"
"        stop: 0 #FFF3B0,\n"
"        stop: 1 #E5B937\n"
"    );\n"
"}\n"
"\n"
"/* --- PARTE IZQUIERDA (LLENA) --- */\n"
"QSlider::sub-page:horizontal {\n"
"    background: #9BCB43;   "
                        "                 /* Verde suave tipo \u201cCargar datos\u201d */\n"
"    border: 2px solid #5F8A2A;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* --- PARTE DERECHA (VAC\u00cdA) --- */\n"
"QSlider::add-page:horizontal {\n"
"    background: #EDE2AC;                    /* Beige claro */\n"
"    border: 2px solid #C9A43A;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"/* --- QSLIDER VERTICAL (por si lo usas) --- */\n"
"QSlider::groove:vertical {\n"
"    border: 2px solid #C9A43A;\n"
"    width: 10px;\n"
"    background: #F4E29B;\n"
"    border-radius: 5px;\n"
"    margin: 10px 0px;\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background: qradialgradient(\n"
"        cx: 0.4, cy: 0.4,\n"
"        fx: 0.4, fy: 0.4,\n"
"        radius: 0.6,\n"
"        stop: 0 #FFE873,\n"
"        stop: 1 #C9A43A\n"
"    );\n"
"    border: 2px solid #5A4A00;\n"
"    height: 20px;\n"
"    width: 20px;\n"
"    border-radius: 10px;\n"
"    margin: 0 -6px;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: #9BCB43;\n"
"    "
                        "border: 2px solid #5F8A2A;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background: #EDE2AC;\n"
"    border: 2px solid #C9A43A;\n"
"    border-radius: 5px;\n"
"}\n"
"")
        self.volumenGeneralSlider.setMaximum(100)
        self.volumenGeneralSlider.setValue(0)
        self.volumenGeneralSlider.setTracking(True)
        self.volumenGeneralSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.volumenGeneralSlider, 1, 3, 1, 1)

        self.volumenSFX = QLabel(configuracion)
        self.volumenSFX.setObjectName(u"volumenSFX")
        self.volumenSFX.setStyleSheet(u"QLabel {\n"
"    color: #3C3C3C;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    padding: 6px;\n"
"    letter-spacing: 1px;\n"
"}")

        self.gridLayout.addWidget(self.volumenSFX, 2, 4, 1, 1)

        self.volumenGeneral = QLabel(configuracion)
        self.volumenGeneral.setObjectName(u"volumenGeneral")
        self.volumenGeneral.setStyleSheet(u"QLabel {\n"
"    color: #3C3C3C;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    padding: 6px;\n"
"    letter-spacing: 1px;\n"
"}")

        self.gridLayout.addWidget(self.volumenGeneral, 1, 4, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 7, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 4, 0, 1, 1)

        self.VolumenGeneral = QLabel(configuracion)
        self.VolumenGeneral.setObjectName(u"VolumenGeneral")
        self.VolumenGeneral.setFont(font)
        self.VolumenGeneral.setStyleSheet(u"QLabel {\n"
"    color: #3C3C3C;\n"
"    font-size: 11px;\n"
"    font-weight: bold;\n"
"    padding: 6px;\n"
"    letter-spacing: 1px;\n"
"}")

        self.gridLayout.addWidget(self.VolumenGeneral, 1, 2, 1, 1)

        self.completa = QCheckBox(configuracion)
        self.completa.setObjectName(u"completa")
        self.completa.setStyleSheet(u"/* --- ESTILO GENERAL DE QCheckBox --- */\n"
"QCheckBox {\n"
"    spacing: 8px;\n"
"    font-size: 10px;\n"
"    color: #3B2E05;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"/* --- CHECKBOX SIN MARCAR --- */\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 2px solid #C9A43A;        /* Borde dorado */\n"
"    border-radius: 4px;\n"
"    background-color: #F4E29B;        /* Amarillo suave */\n"
"}\n"
"\n"
"/* --- CHECKBOX MARCADO --- */\n"
"QCheckBox::indicator:checked {\n"
"    image: none;\n"
"    background-color: #9BCB43;        /* Verde tipo \u201cCargar datos\u201d */\n"
"    border: 2px solid #5F8A2A;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* --- CHECKBOX AL PASAR EL RAT\u00d3N --- */\n"
"QCheckBox::indicator:hover {\n"
"    background-color: #F9D95C;        /* Amarillo m\u00e1s brillante */\n"
"    border: 2px solid #E5B937;\n"
"}\n"
"\n"
"/* --- CHECKBOX DESHABILITADO --- */\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: #EDE2AC;\n"
"    border: 2px solid "
                        "#B8A34F;\n"
"    opacity: 0.6;\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"    color: #8E8352;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.completa, 5, 4, 1, 1)

        self.ventana = QCheckBox(configuracion)
        self.ventana.setObjectName(u"ventana")
        self.ventana.setStyleSheet(u"/* --- ESTILO GENERAL DE QCheckBox --- */\n"
"QCheckBox {\n"
"    spacing: 8px;\n"
"    font-size: 10px;\n"
"    color: #3B2E05;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"/* --- CHECKBOX SIN MARCAR --- */\n"
"QCheckBox::indicator {\n"
"    width: 16px;\n"
"    height: 16px;\n"
"    border: 2px solid #C9A43A;        /* Borde dorado */\n"
"    border-radius: 4px;\n"
"    background-color: #F4E29B;        /* Amarillo suave */\n"
"}\n"
"\n"
"/* --- CHECKBOX MARCADO --- */\n"
"QCheckBox::indicator:checked {\n"
"    image: none;\n"
"    background-color: #9BCB43;        /* Verde tipo \u201cCargar datos\u201d */\n"
"    border: 2px solid #5F8A2A;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"/* --- CHECKBOX AL PASAR EL RAT\u00d3N --- */\n"
"QCheckBox::indicator:hover {\n"
"    background-color: #F9D95C;        /* Amarillo m\u00e1s brillante */\n"
"    border: 2px solid #E5B937;\n"
"}\n"
"\n"
"/* --- CHECKBOX DESHABILITADO --- */\n"
"QCheckBox::indicator:disabled {\n"
"    background-color: #EDE2AC;\n"
"    border: 2px solid "
                        "#B8A34F;\n"
"    opacity: 0.6;\n"
"}\n"
"\n"
"QCheckBox:disabled {\n"
"    color: #8E8352;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.ventana, 5, 3, 1, 1)


        self.retranslateUi(configuracion)

        self.resolucion.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(configuracion)
    # setupUi

    def retranslateUi(self, configuracion):
        configuracion.setWindowTitle(QCoreApplication.translate("configuracion", u"Configuracion", None))
        self.TipoDeVisualizacion.setText(QCoreApplication.translate("configuracion", u"Tipo de visualizaci\u00f3n:", None))
        self.Resolucion.setText(QCoreApplication.translate("configuracion", u"Resoluci\u00f3n:", None))
        self.guardar.setText(QCoreApplication.translate("configuracion", u"Guardar configuraci\u00f3n", None))
        self.resolucion.setItemText(0, QCoreApplication.translate("configuracion", u"640x480", None))
        self.resolucion.setItemText(1, QCoreApplication.translate("configuracion", u"960x540", None))
        self.resolucion.setItemText(2, QCoreApplication.translate("configuracion", u"1280x720", None))
        self.resolucion.setItemText(3, QCoreApplication.translate("configuracion", u"1920x1080", None))

        self.resolucion.setPlaceholderText("")
        self.VolumenSFX.setText(QCoreApplication.translate("configuracion", u"Volumen SFX:", None))
        self.volumenSFX.setText(QCoreApplication.translate("configuracion", u"TextLabel", None))
        self.volumenGeneral.setText(QCoreApplication.translate("configuracion", u"TextLabel", None))
        self.VolumenGeneral.setText(QCoreApplication.translate("configuracion", u"Volumen general:", None))
        self.completa.setText(QCoreApplication.translate("configuracion", u"Completa", None))
        self.ventana.setText(QCoreApplication.translate("configuracion", u"Ventana ", None))
    # retranslateUi

