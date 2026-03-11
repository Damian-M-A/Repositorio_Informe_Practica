# This Python file uses the following encoding: utf-8
## Todo esto desde el ejemplo del video con conversion de C++ a python
from PySide6.QtCore import QObject, Property, Signal, Slot, QTimer, QDateTime


class System(QObject):
    carLockedChanged = Signal()
    usernameChanged = Signal()
    outTempChanged = Signal()
    timeChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._carLocked = False
        self._outdoorTemp = 30
        self._userName = "test_name"
        self._time = ""

        ## Configuracion de Qtimer para actualizar la hora
        self._timerCurrentTime = QTimer(self)
        self._timerCurrentTime.setInterval(1000)
        self._timerCurrentTime.timeout.connect(self._updateTime)
        self._timerCurrentTime.start()

        ## aqui se llama a la funcion
        self._updateTime()

        ## este es el que se encarga de obtener y actualizar la hora
    def _updateTime(self):
        self._time = QDateTime.currentDateTime().toString("HH:mm:ss AP")
        self.timeChanged.emit()
    def getCurrentTime(self):
        return self._time


    def getOutdoorTemp(self):
        return self._outdoorTemp
    def getUserName(self):
        return self._userName




    @Slot(str)
    def setUserName(self, value):
        if self._userName == value:
            return
        self._userName = value
        self.usernameChanged.emit()

    @Slot(int)
    def setOutdoorTemp(self,value):
        if self._outdoorTemp == value:
            return
        self._outdoorTemp = value
        self.outTempChanged.emit()

    def getCarLocked(self):
        return self._carLocked


    @Slot(bool)
    def setCarLocked(self,value):
        if self._carLocked == value:
            return
        self._carLocked = value
        self.carLockedChanged.emit()

## Se crea un property por componente a utilizar
    carLocked = Property(
        bool,
        getCarLocked,
        setCarLocked,
        notify= carLockedChanged
    )
    outTemp = Property(
        int,
        getOutdoorTemp,
        setOutdoorTemp,
        notify = outTempChanged
    )
    userName = Property(
        str,
        getUserName,
        setUserName,
        notify = usernameChanged
    )
    currentTime = Property (
        str,
        getCurrentTime,
        notify = timeChanged
    )
