import machine
import utime
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

led = machine.Pin(25, machine.Pin.OUT)

# Dirección del I2C y tamaño del LCD
sda = machine.Pin(0)
scl = machine.Pin(1)
I2C_ADDR = 0x27
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16
i2c = machine.I2C(0, scl=scl, sda=sda, freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

# Conocer la temperatura en la que estoy
sensor_temp = machine.ADC(4) # Sensor interno de temperatura
factor_16 = 3.3 / (65535) # Cantidad de bits que puede procesar (65545) . valor universal

# Funcionar Ultrasonido
trig = machine.Pin(2, machine.Pin.OUT)
echo = machine.Pin(3, machine.Pin.IN)
trig.value(0)
print("Hola")
while True:
    # empezar Ultrasonido
    led.value(1)
    trig.value(1)
    utime.sleep_us(10)
    trig.value(0)
    t1 = utime.ticks_us()
    print("Hola 1")
    
    while echo.value() == 0:
        print("Hola 2")
        led.value(0)
        t1 = utime.ticks_us()
    while echo.value() == 1:
        led.value(1)
        t2 = utime.ticks_us()
    led.value(0)
    t = t2-t1
    d = 17*t/1000
    lcd.putstr("Distancia: {} cms" .format(d))
    
    # Empezar sensor de temperatura de rapsberry PI PICO
    voltaje = sensor_temp.read_u16() * factor_16
    temperatura = 27 - (voltaje - 0.706)/0.001721
    led.value(1)
    print(round(temperatura, 2))
    temperatura_lista = "{}" .format(round(temperatura, 2))
    led.value(0)
    # Impresiones en display LCD
    #lcd.clear()
    #lcd.putstr(temperatura_lista)
    utime.sleep(2)
    lcd.clear()