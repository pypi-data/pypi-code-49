import matplotlib.pyplot as plt
import numpy as np
import datetime as dt  # Importamos el módulo datetime


prima = 600 + np.random.randn(5) * 10  # Valores inventados para la prima de riesgo
fechas = (dt.date.today() - dt.timedelta(5)) + dt.timedelta(1) * np.arange(5) # generamos las fechas de los últimos cinco días
plt.axes((0.1, 0.3, 0.8, 0.6))  # Definimos la posición de los ejes
plt.bar(np.arange(5), prima)  # Dibujamos el gráfico de barras
plt.ylim(550,650)  # Limitamos los valores del eje y al range definido [450, 550]
plt.title('prima de riesgo')  # Colocamos el título
plt.xticks(np.arange(5), fechas, rotation = 45)  # Colocamos las etiquetas del eje x, en este caso, las fechas