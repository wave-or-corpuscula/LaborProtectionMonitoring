from PySide6.QtCore import QObject, Signal

from app.utils import User


class MenuSignals(QObject):
    user_logout = Signal()
    goto_data_change = Signal()
    goto_briefing = Signal()
