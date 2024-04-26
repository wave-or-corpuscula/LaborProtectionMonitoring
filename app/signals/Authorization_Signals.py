from PySide6.QtCore import QObject, Signal

from app.utils import User


class AuthorizationSignals(QObject):
    user_authorized = Signal(User)
