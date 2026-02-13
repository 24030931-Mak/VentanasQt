# ui/main_view.py
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel

class TeacherView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Principal - MVP")
        self.resize(420, 270)
        self._label = QLabel("  (•_•)\n  /|   |\\\n   |___|\n\nBienvenido docente.\nHas iniciado sesión correctamente." , alignment=Qt.AlignCenter)
        self.setCentralWidget(self._label)

    def set_welcome(self, user: str):
        self._label.setText(f"Bienvenido, {user}. ¡Sesión iniciada!")
