from decouple import config

USERNAME = config("username", default="")
"""Nome do usuário para autenticação"""

PASSWORD = config("password", default="")
"""Token básico para autenticação"""
