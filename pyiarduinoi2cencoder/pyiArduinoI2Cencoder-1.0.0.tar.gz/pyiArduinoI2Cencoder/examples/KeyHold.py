#   ДАННЫЙ ПРИМЕР ФИКСИРУЕТ УДЕРЖАНИЕ КНОПКИ:
# Если кнопка удерживается дольше фиксированного времени,
# в stdout выводится "ON".

from time import sleep

# Подключаем библиотеку для работы с энкодером I2C-flash.
from pyiArduinoI2Cencoder import *
# Инстанциируем объект, указывая адрес модуля на шине I2C.
enc = pyiArduinoI2Cencoder(0x09)

print("Удерживайте кноку вала")

while True:
    # f = enc.getButton(KEY_HOLD_05)  # Считываем удержание дольше 0,5 сек
    f = enc.getButton(KEY_HOLD_10)    # Считываем удержание дольше 1,0 сек
    # f = enc.getButton(KEY_HOLD_20)  # Считываем удержание дольше 2,0 сек

    if f:
        print("ON")
        sleep(1)

    sleep(.1)
