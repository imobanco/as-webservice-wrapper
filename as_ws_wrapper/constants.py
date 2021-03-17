from decouple import config

USERNAME = config("username", default="")
"""Token básico para autenticação"""

PASSWORD = config("password", default="")
"""Token básico para autenticação"""
