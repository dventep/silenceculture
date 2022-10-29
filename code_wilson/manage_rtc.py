from machine import Pin, SoftI2C
from ds3231_port import DS3231
import utime
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)
rtc = DS3231(i2c)

#rtc.set_time()
print(dir(i2c))
print(Pin(22).value())
print(i2c)
def take_typical_date(tuple_data):
    print("Tuple_data", tuple_data)
    value_data = int("".join([str(tuple_data[0]), str(tuple_data[1]), str(tuple_data[2])]))
    return value_data
def get_date():
    if take_typical_date(utime.localtime()) > take_typical_date(rtc.get_time()):
        data_utime = utime.localtime()
        rtc.save_time(data_utime[0], data_utime[1], data_utime[2], data_utime[3], data_utime[4], data_utime[5], data_utime[6])
        current_date = utime.localtime()
    elif take_typical_date(utime.localtime()) <= take_typical_date(rtc.get_time()):
        current_date = rtc.get_time()
    return current_date    

