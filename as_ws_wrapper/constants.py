from decouple import config

USERNAME = config("username", default="")
"""Token básico para autenticação"""

PASSWORD = config("password", default="")
"""developer_application_key"""
