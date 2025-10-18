from PySide6.QtCore import QObject, QTimer, Signal  # type: ignore

class Poller(QObject):
    tick = Signal()

    def __init__(self, interval_ms: int):
        super().__init__()
        self._timer = QTimer(self)
        self._timer.setInterval(interval_ms)
        self._timer.timeout.connect(self.tick.emit)

    def start(self):
        if not self._timer.isActive():
            self._timer.start()

    def stop(self):
        if self._timer.isActive():
            self._timer.stop()
