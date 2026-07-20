import os
class Config:
    """
    Konfigurasi aplikasi Flask
    """

  # Konfigurasi Database MySQL
    HOST = os.environ.get("DB_HOST", "localhost")
    PORT = int(os.environ.get("DB_PORT", 3306))
    USER = os.environ.get("DB_USER", "root")
    PASSWORD = os.environ.get("DB_PASSWORD", "root")
    DATABASE = os.environ.get("DB_NAME", "db_akademik")

    # Secret Key Flask
    SECRET_KEY = os.environ.get("SECRET_KEY", "praktikum-flask-2026")

    # Konfigurasi Flask
    # Diubah default ke False -- DEBUG=True di production membocorkan
    # traceback lengkap (termasuk kredensial DB) ke publik kalau error.
    DEBUG = os.environ.get("FLASK_DEBUG", "False") == "True"