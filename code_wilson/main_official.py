import manage_dB
import machine
import manage_rgb
import utime
import table_db
led = machine.Pin(2, machine.Pin.OUT)
db_value = 0
table_db = table_db.execute_file()

sensor_microphone = machine.ADC(machine.Pin(39))
#sensor_microphone.atten(machine.ADC.ATTN_11DB) #11 dB de atenuación. Lectura entre 0.0V y 3.6V # Funciona 1° Parte
sensor_microphone.atten(machine.ADC.ATTN_11DB)
#sensor_microphone.width(machine.ADC.WIDTH_11BIT)     # Lectura con precisión de 11 bits # Funciona 1° Parte
sensor_microphone.width(machine.ADC.WIDTH_11BIT)
while True:
    rgb_send = "127,255,0"
    #led.on()
    db_value = manage_dB.calculate_dB(sensor_microphone, False)
    for index, line_db in enumerate(table_db):        
        if index > 0 and db_value < int(table_db[index]["dB"]):
            rgb_send = table_db[index-1]["rgb"]
            break
    manage_rgb.rgb(rgb_send)
    #$print(dir(sensor_microphone))
    utime.sleep(1)
