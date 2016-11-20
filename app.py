
# coding: utf-8
import sys
import logging
from core import Core

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    if not sys.platform.startswith('win'):
        import coloredlogs
        coloredlogs.install(level='DEBUG')

    webwx = Core()
    webwx.start()
