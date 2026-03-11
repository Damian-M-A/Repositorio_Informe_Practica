from PySide6.QtCore import QObject, Property, Signal, Slot


class HVACHandler(QObject):

    targetTempChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._targetTemp = 25


    def getTargetTemp(self):
        return self._targetTemp


    @Slot(int)
    def setTargetTemp(self, value):
        if self._targetTemp == value:
            return
        self._targetTemp = value
        self.targetTempChanged.emit()


    @Slot()
    def incrementTemp(self):
        self.setTargetTemp(self._targetTemp + 1)

    @Slot()
    def decrementTemp(self):
        self.setTargetTemp(self._targetTemp - 1)

    targetTemp = Property(
        int,
        getTargetTemp,
        setTargetTemp,
        incrementTemp,
        decrementTemp,
        notify=targetTempChanged
    )
