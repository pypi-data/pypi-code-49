# ПРИМЕР ЧТЕНИЯ ТАКТОВ ПОВОРОТА ЭНКОДЕРА:
# В данном примере считываются такты поворотов энкодера,
# отдельно вправо и отдельно влево.

from time import sleep

# Подключаем библиотеку для работы с энкодером I2C-flash.
from pyiArduinoI2Cencoder import *
# Инстанциируем объект, указывая адрес модуля на шине I2C.
enc = pyiArduinoI2Cencoder(0x09)

print("Вращайте барабан!")

while True:

    # Определяем переменные для чтения количества тактов поворота энкодера.
    turnL, turnR = 0, 0

    # Считываем такты поворота энкодера:
    turnL=enc.getEncoder(ENC_TURN_LEFT)   # Считываем количество влево
    turnR=enc.getEncoder(ENC_TURN_RIGHT)  # Считываем количество вправо

    # Выводим считанные данные:
    if turnL:
        print("-",
             turnL)

    if turnR:
        print("+",
             turnR)

    sleep(.1)
