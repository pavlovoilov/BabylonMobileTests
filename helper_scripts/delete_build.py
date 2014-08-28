import os
from settings import APP_PACKAGE

os.system('adb uninstall {}'.format(APP_PACKAGE))