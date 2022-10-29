from machine import PWM, Pin # Importar la función PWM y  Pin del módulo machine
from time import *

pin27 = Pin(27, Pin.OUT)
pin14 = Pin(14, Pin.OUT)
pin12 = Pin(12, Pin.OUT)

#red = PWM(pin27) # Original
red = PWM(pin12) 
#rojo.duty(0)

#green = PWM(pin12) #original
green = PWM(pin27)
#verde.duty(1023)

#blue = PWM(pin14) # original
blue = PWM(pin14) 
#azul.duty(1023)

def calculateNum(num:int):
    return int(511.5*num/127.5)
    #return int(round(1023 - (511.5*num/127.5), 0))
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
    #red.duty(255)
    #green.duty(0)
    #blue.duty(0)
     
    red.freq(100)  
    green.freq(100) 
    blue.freq(100)
    red.duty(calculateNum(int(rgb_string[0])))
    green.duty(calculateNum(int(rgb_string[1])))
    blue.duty(calculateNum(int(rgb_string[2])))
rgb("255,0,0")
#rgb("178,34,34")

