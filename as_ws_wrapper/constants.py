from decouple import config

USERNAME = config("AS_WEBSERVICE_USERNAME", default="")
"""Nome do usuário para autenticação"""

PASSWORD = config("AS_WEBSERVICE_PASSWORD", default="")
"""Token básico para autenticação"""
