import save_tests
import machine
import exe_test
import utime
import table_db
led = machine.Pin(2, machine.Pin.OUT)
db_value = 0
table_db = table_db.execute_file()

sensor_microphone = machine.ADC(machine.Pin(36))
sensor_microphone.atten(machine.ADC.ATTN_11DB) #11 dB de atenuación. Lectura entre 0.0V y 3.6V
sensor_microphone.width(machine.ADC.WIDTH_11BIT)     # Lectura con precisión de 11 bits
while True:
    rgb_send = "127,255,0"
    utime.sleep(1)
    for index, line_db in enumerate(table_db):        
        if index > 0 and db_value < int(table_db[index]["dB"]):
            print("Valor RGB es", table_db[index-1]["rgb"], "con index", index)
            #rgb_send = table_db[index-1]["rgb"]
            break
            
    #exe_test.rgb(rgb_send)
    led.on()
    db_value = save_tests.calculate_dB(sensor_microphone, led)
    
