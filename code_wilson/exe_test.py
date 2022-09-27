from machine import PWM, Pin # Importar la función PWM y  Pin del módulo machine
from time import *

pin27 = Pin(27, Pin.OUT)
pin14 = Pin(14, Pin.OUT)
pin12 = Pin(12, Pin.OUT)

rojo = PWM(pin27)
#rojo.duty(0)

verde = PWM(pin12)
#verde.duty(1023)

azul = PWM(pin14)
#azul.duty(1023)

def calculateNum(num:int):
    return int(round(1023 - (511.5*num/127.5), 0))
def rgb (rgb_string): # Función para controlar RGB
    try:
        value_test = int(rgb_string.replace(",",""))
    except:
        return None
    rgb_string = rgb_string.replace("\n", "").split(",")    
    print("rgb:", rgb_string)
    #rojo.freq(500)    
    #verde.freq(500)    
    #azul.freq(500)
    rojo.freq(100)    
    verde.freq(100)    
    azul.freq(100)
    
    rojo.duty(calculateNum(int(rgb_string[0])))
    verde.duty(calculateNum(int(rgb_string[1])))
    azul.duty(calculateNum(int(rgb_string[2])))
#rgb(0,0,255)
