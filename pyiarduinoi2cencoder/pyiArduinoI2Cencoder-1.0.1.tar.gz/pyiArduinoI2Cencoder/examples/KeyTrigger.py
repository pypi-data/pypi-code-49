#   ПРИМЕР РАБОТЫ С КНОПОЧНЫМ ПЕРЕКЛЮЧАТЕЛЕМ:
# При каждом нажатии на кнопку булева переменная
# будет менять своё значение на противоположное

from time import sleep
# Подключаем библиотеку для работы с энкодером I2C-flash.
from pyiArduinoI2Cencoder import *
# Инстанциируем объект, указывая адрес модуля на шине I2C.
enc = pyiArduinoI2Cencoder(0x09)

while True:
    # Считываем состояние кнопочного переключателя энкодера
    t = bool(enc.getButton(KEY_TRIGGER))
    print(t)
    sleep(.1)
