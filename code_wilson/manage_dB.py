import machine
import utime
import math
import decibeles
import cal_min_max
from machine import Pin, SoftI2C
from ds3231_port import DS3231
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)
rtc = DS3231(i2c)

##led = machine.Pin(2, machine.Pin.OUT)
##factor_16 = 3.3 / (65535) # Cantidad de bits que puede procesar (65545) . valor universal

#--------------------------------------------------------------
def take_typical_date(tuple_data):
    value_data = int("".join([str(tuple_data[0]), str(tuple_data[1]), str(tuple_data[2])]))
    return value_data
def get_date():
    try:
        if take_typical_date(utime.localtime()) > take_typical_date(rtc.get_time()):
            data_utime = utime.localtime()
            rtc.save_time()
            current_date = utime.localtime()
        elif take_typical_date(utime.localtime()) <= take_typical_date(rtc.get_time()):
            current_date = rtc.get_time()
    except:
        current_date = utime.localtime()
    return current_date

def calculate_dB(sensor_microphone, led=False):
    ##sensor_microphone = machine.ADC(machine.Pin(36))
    ##sensor_microphone.atten(machine.ADC.ATTN_11DB) #6 dB de atenuación. Lectura entre 0.0V y 3.6V
    ##sensor_microphone.width(machine.ADC.WIDTH_11BIT)     # Lectura con precisión de 9 bits
    voltaje = decibeles.bin_to_vol(sensor_microphone.read_u16())
    db_value = decibeles.cal_decibeles(signalIn=voltaje, signalOut=5)
    if db_value > 0:
        current_date = get_date() #Dormido, encender
        #current_date = utime.localtime()
        #date_to_save = "archivo"
        print(current_date)
        date_to_save = "{:02d}/{:02d}/{:4d} {:02d}:{:02d}:{:02d}" .format(current_date[2], current_date[1], current_date[0], current_date[3], current_date[4], current_date[5])
        #archivo = open(f"basedata/registro_db.txt", "a+")
        archivo = open("basedata/{:02d}-{:02d}-{:4d}_WilsonData.csv" .format(current_date[2], current_date[1], current_date[0]), "a+")
        archivo.write(f"{db_value}\t{date_to_save}\n")
        archivo.close()
    print(f"{sensor_microphone.read_u16()} - voltaje: {round(voltaje,2)}v - cálculo: {db_value}dB")
    return db_value
    ##while True:
        #voltaje = sensor_sound.read_u16() * factor_16
        #if sensor_sound.read_u16() > 50000:
        ##voltaje = decibeles.bin_to_vol(sensor_microphone.read_u16())
        ##db_value = decibeles.cal_decibeles(signalIn=voltaje, signalOut=5)
        ##print(f"{sensor_microphone.read_u16()} - voltaje: {round(voltaje,2)}v - cálculo: {db_value}dB")
        ##if float(db_value) >= 30:   
            ##led.value(1)
            ##utime.sleep(1)  
            ##led.value(0)
        #voltaje = sensor_sound.read_u16() * factor_16

