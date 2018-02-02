try:
    from settings_local import *  # NOQA
except ImportError:
    from d21.settings.base import *  # NOQA
