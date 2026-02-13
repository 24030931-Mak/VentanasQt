# services/auth_service.py
from dataclasses import dataclass

@dataclass(frozen=True)
class AuthResult:
    ok: bool
    message: str = ""
    role: str=""

class AuthService:
    """
    Servicio de autenticación. Hoy: validación estática.
    Mañana: cambiar por BD/API.
    """
    def __init__(self, valid_user: str = "admin", valid_password: str = "1234"):
        self._user = valid_user
        self._password = valid_password

    ##########   Se cambió de solo validar a validar y especificar el tipo de usuario
    def login(self, username: str, password: str) -> AuthResult:
        if not username or not password:
            return AuthResult(False, "Usuario y contraseña son requeridos.")

        if username == "admin" and password == "1234":                    # ADMIN
            return AuthResult(True, "Autenticación exitosa.", "admin")

        if username == "estudiante" and password == "1234":                # ESTUDIANTE
            return AuthResult(True, "Autenticación exitosa.", "student")

        if username == "maestro" and password == "1234":                  # DOCENTE
            return AuthResult(True, "Autenticación exitosa.", "teacher")

        return AuthResult(False, "Usuario o contraseña incorrectos.")
   
"""    
    def login(self, username: str, password: str) -> AuthResult:
        if not username or not password:
            return AuthResult(False, "Usuario y contraseña son requeridos.")
        if username == self._user and password == self._password:
            return AuthResult(True, "Autenticación exitosa.")
        return AuthResult(False, "Usuario o contraseña incorrectos.")
"""
