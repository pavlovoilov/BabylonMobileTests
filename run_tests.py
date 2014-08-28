import os

os.system('py.test tests --alluredir reports')
os.system('allure report generate reports -o reports')
