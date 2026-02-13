# core/app_shell.py
from PyQt5.QtWidgets import QStackedWidget
from ui.login_view import LoginView
from ui.main_view import MainView
from ui.student_view import StudentView                    #Vista de estudiante
from ui.teacher_view import TeacherView                    #Vista de profesor
from services.auth_service import AuthService
from presenters.login_presenter import LoginPresenter

class AppShell(QStackedWidget):
    PAGE_LOGIN = 0
    PAGE_ADMIN = 1
    PAGE_STUDENT = 2                        #Nuevas ventanas        
    PAGE_TEACHER = 3


    def __init__(self):
        super().__init__()

        self.login_view = LoginView()
        self.main_view = MainView()
        self.student_view = StudentView()                        #Nuevas vistas    
        self.teacher_view = TeacherView()



        self.auth_service = AuthService()
        
        self.login_presenter = LoginPresenter(
            view=self.login_view,
            auth=self.auth_service,
            on_success=self._go_main
        )
        
        self.addWidget(self.login_view)
        self.addWidget(self.main_view)
        self.addWidget(self.student_view)                        #Nuevas vistas
        self.addWidget(self.teacher_view)

        
        self.setCurrentIndex(self.PAGE_LOGIN)
        self.setWindowTitle("PyQt5 - MVP - Rivera Ramírez María Magdalena")
        self.resize(400, 300)

    def _go_main(self, username: str, role: str):              # Antes se mandaba a la vista main, ahora se direcciona segun el rol de usuario

        if role == "admin":
            self.main_view.set_welcome(username)
            self.setCurrentIndex(self.PAGE_ADMIN)

        elif role == "student":
            self.setCurrentIndex(self.PAGE_STUDENT)

        elif role == "teacher":
            self.setCurrentIndex(self.PAGE_TEACHER)

"""
    def _go_main(self, username: str):
        self.main_view.set_welcome(username)
        self.setCurrentIndex(self.PAGE_MAIN)
"""
