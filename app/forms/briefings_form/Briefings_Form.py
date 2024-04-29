from PySide6.QtWidgets import QMainWindow

from .BriefingsUi import Ui_BriefingsWindow


class BriefingsForm(QMainWindow):

    def __init__(self, parent=None):
        super(BriefingsForm, self).__init__(parent)
        self.ui = Ui_BriefingsWindow()
        self.ui.setupUi(self)