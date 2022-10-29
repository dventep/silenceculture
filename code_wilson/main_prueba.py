import manage_dB
import machine
import utime
import decibeles
led = machine.Pin(2, machine.Pin.OUT)

sensor_microphone = machine.ADC(machine.Pin(39))
#sensor_microphone.atten(machine.ADC.ATTN_11DB) #11 dB de atenuación. Lectura entre 0.0V y 3.6V # Funciona 1° Parte
sensor_microphone.atten(machine.ADC.ATTN_6DB)
#sensor_microphone.width(machine.ADC.WIDTH_11BIT)     # Lectura con precisión de 11 bits # Funciona 1° Parte
sensor_microphone.width(machine.ADC.WIDTH_9BIT)
db_value = 0
print(dir(sensor_microphone))
while True:
    #db_value = manage_dB.calculate_dB(sensor_microphone, False)
    #voltaje = decibeles.bin_to_vol(sensor_microphone.read_u16())
    #db_value = decibeles.cal_decibeles(signalIn=voltaje, signalOut=3.3)
    #print(f"- {sensor_microphone.read_u16()} - voltaje: {round(voltaje,2)}v - cálculo: {db_value}dB")
    utime.sleep(0.5)
    print(sensor_microphone.read_u16(), '--', sensor_microphone.read_u16()/65535/2)