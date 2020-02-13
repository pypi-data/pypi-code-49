#   ПРИМЕР РАБОТЫ С КНОПКОЙ ЭНКОДЕРА:
# В stdout выводится состояние кнопки
# энкодера на момент запуска сценария

# Подключаем библиотеку для работы с энкодером I2C-flash.
from pyiArduinoI2Cencoder import *
# Инстанциируем объект, указывая адрес модуля на шине I2C.
enc = pyiArduinoI2Cencoder(0x09)

# Считываем состояние кнопки энкодера в переменную f.
f = enc.getButton(KEY_PRESSED)

if not f:
    print("OFF")
else:
    print("ON")
