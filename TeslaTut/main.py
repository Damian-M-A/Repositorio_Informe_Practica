import sys
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtLocation import QGeoServiceProvider
## Importar para imagenes, se debe crear el archivo resources.qrc y poner las imagenes
import rc_resources
## archivo creado para controlar diversos componentes (igual que en el video)
from Controllers import System
from Controllers import HVACHandler

app = QGuiApplication(sys.argv)

engine = QQmlApplicationEngine()

def on_warnings(warnings):
    for w in warnings:
        print("QML WARNING:", w.toString())

engine.warnings.connect(on_warnings)


system = System.System()
engine.rootContext().setContextProperty("system",system)
hvadriver = HVACHandler.HVACHandler()
engine.rootContext().setContextProperty("hvadriver",hvadriver)
hvapass = HVACHandler.HVACHandler()
engine.rootContext().setContextProperty("hvapass",hvapass)
engine.load("main.qml")

if not engine.rootObjects():
    print("ERROR: No se pudo cargar main.qml")
    sys.exit(-1)

sys.exit(app.exec())
