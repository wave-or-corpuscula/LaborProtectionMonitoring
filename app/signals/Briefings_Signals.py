from PySide6.QtCore import QObject, Signal


class BriefingsSignals(QObject):
    goto_menu = Signal()