"""TeleNotif - Simple Telegram Notification Framework"""

from telenotif.__version__ import __version__
from telenotif.server.app import create_app
from telenotif.core.interfaces import IFormatter, IPlugin

__all__ = ["__version__", "create_app", "IFormatter", "IPlugin"]
