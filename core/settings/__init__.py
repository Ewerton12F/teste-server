from .base import *

if base.DEBUG:
    from .local import *
else:
    from .production import *
