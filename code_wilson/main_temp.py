import manage_dB
import machine
import manage_rgb
import utime
import table_db
led = machine.Pin(2, machine.Pin.OUT)
db_value = 0
table_db = table_db.execute_file()

sensor_microphone = machine.ADC(machine.Pin(36))
sensor_microphone.atten(machine.ADC.ATTN_11DB) #11 dB de atenuación. Lectura entre 0.0V y 3.6V
sensor_microphone.width(machine.ADC.WIDTH_11BIT)     # Lectura con precisión de 11 bits
while True:
    led.off()
    for item in ['77,155,0', '100,100,0', '255,69,0', '255,40,0', '255,0,0', '178,34,34', '178,34,34', '0,0,100']:
        rgb_send = item
        manage_rgb.rgb(rgb_send)
        utime.sleep(1)        
        led.on()
    
    
