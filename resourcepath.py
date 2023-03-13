import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def get_config_path(name):
    if hasattr(sys, "_MEIPASS"):
        abs_home = os.path.abspath(os.path.expanduser("~"))
        abs_dir_app = os.path.join(abs_home, f".pyqtplanner")
        if not os.path.exists(abs_dir_app):
            os.mkdir(abs_dir_app)
        cfg_path = os.path.join(abs_dir_app, name)
    else:
        cfg_path = os.path.abspath(f".%s{name}" % os.sep)
    return cfg_path
