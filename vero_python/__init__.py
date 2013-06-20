from .client import VeroEventLogger
from .client import VeroEndpoints

VERSION = (1, 0, 1)

__title__ = 'vero_python'
__version__ = '{major}.{minor}.{patch}'.format(
    major=VERSION[0],
    minor=VERSION[1],
    patch=VERSION[2]
)
__author__ = 'Wave Accounting Inc.'
__license__ = 'BSD Simplified'
__copyright__ = 'Copyright 2012 Wave Accounting Inc.'
