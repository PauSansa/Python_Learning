import time
current_hour = int(time.strftime("%H"))
if current_hour >= 19:
    print("Vete a casa")
else:
    calculo = 19 - current_hour
    print("Quedan {} horas para volver a casa".format(calculo))