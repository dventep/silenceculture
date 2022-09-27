import decibeles

def float_return(value:float = 0, max_val:bool = False, min_val:bool = False):
    try:
        value_returned = float(value)
    except:
        if max_val == True:
            value_returned = 0            
        elif min_val == True:
            value_returned = 100000000
    return value_returned
def cal_min_max_manage():
    archivo = open("valores.txt", "a+")
    #archivo.write("Min: 0\nMax: 0")
    values = archivo.readlines()
    if len(values) == 0:
        values = ["10000000:0"]
    values = values[-1].split(":")
    min_val = float_return(value=values[0], min_val=True)
    max_val = float_return(value=values[1], max_val=True)
    archivo.close()

    MIN_TO_CAL = 320
    MAX_TO_CAL = 65535
    print("El cálculo es: ", decibeles.cal_vol_to_decibeles(MAX_TO_CAL, MIN_TO_CAL))
    return [min_val, max_val]
