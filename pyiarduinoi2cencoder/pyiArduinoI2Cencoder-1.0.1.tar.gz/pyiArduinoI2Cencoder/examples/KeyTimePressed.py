#   ДАННЫЙ ПРИМЕР ФИКСИРУЕТ УДЕРЖАНИЕ КНОПКИ:
# В stdout будет вывоится время удержания кнопки

from time import sleep
# Подключаем библиотеку для работы с энкодером I2C-flash.
from pyiArduinoI2Cencoder import *

# Инстанциируем объект, указывая адрес модуля на шине I2C.
enc = pyiArduinoI2Cencoder(0x09)

print("Удерживайте вал нажатым")

while True:
    # Считываем время удержания кнопки (в миллисекундах)
    # Максимально фиксируемое время удержания: 25,5 секунд.
    t = enc.getButton(KEY_TIME_PRESSED)

    if t is not 0:
        print(t)
    sleep(.1)
