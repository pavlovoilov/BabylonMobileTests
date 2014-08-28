import os
from settings import APPIUM_PATH, APP_PACKAGE, APP_START_ACTIVITY, APP_WAIT_ACTIVITY, PLATFORM_VERSION
from subprocess import call

run_params = ""
run_params += "cd %s\n" % APPIUM_PATH
run_params += "start node node_modules\\appium\\bin\\appium.js "
run_params += "--app-pkg %s " % APP_PACKAGE
run_params += "--app-activity %s " % APP_START_ACTIVITY
run_params += "--app-wait-activity %s " % APP_WAIT_ACTIVITY
run_params += "--platform-version %s " % PLATFORM_VERSION

bat_file = file('../batch_scripts/start_appium_server.bat', 'w')
bat_file.write(run_params)
bat_file.close()

os.system('call ../batch_scripts/start_appium_server.bat')
