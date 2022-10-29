import network
import utime
import esp
import gc
import machine
import socket
import webpage
import html_webpage
#import traceback
led_2 = machine.Pin(22,machine.Pin.OUT)
led_2.value(1)
print("Encendido")
esp.osdebug(None)
gc.collect()
#network.WLAN(tipo) _ tipo puede ser network.STA_IF o network.AP_IF
wf = network.WLAN(network.STA_IF)
wf.active(True) # False desactivar
#print(wf.scan()) # Escanea las redes disponibles - Devuelve una lista
# 0° item:Nombre red o ssid - 1° item: Mac - 2° item: Canal - 3° item:la potencia - 4° item:tipo de encriptación - 5° item: si es libre o no (contraseña o no)
lista = wf.scan()
print(lista)
name_wifi = "Destructor "
password_wifi = "david222"
#name_wifi = "emcali_1652"
#password_wifi = "3381900222##"
try:
    wf.connect(name_wifi,password_wifi)
except:
    if wf.isconnected():
        wf.disconnect()
    try:
        wf.connect(name_wifi,password_wifi)
    except Exception as e:
        print(e)
try:
    while not wf.isconnected():
        print(".")
        utime.sleep(1)
    # wf.ifconfig nos devulve la 0:IP - 1:Máscara - 2:El gateway - 3:DNS
    print(wf.ifconfig())
    led = machine.Pin(2,machine.Pin.OUT)
    #addr = socket.getaddrinfo("0.0.0.0", 80)[0][-1]
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("", 80))
    s.listen(5)
    #print("listening on", addr)
    
    back_led = True
    name_button, color_button = "Encender", "ButtonB_green"
    while True:
        cl, addr = s.accept()
        print("client connected from ",addr)
        #cl_file = cl.makefile("rwb",0)
        request = cl.recv(1024)
        request= str(request)
        led_active = request.find('/?led')
        if led_active == 6:
            if back_led:
                back_led = False
                led.on()
                name_button = "Apagar"
                color_button = "ButtonB_red"
            else:
                back_led = True
                led.off()
                name_button = "Encender"
                color_button = "ButtonB_green"
        print(led_active)
        
        #while True:
        #    line = cl_file.readline()
        #   if not line or line == b"\r\n":
        #        break
        response = html_webpage.web_page(name_button, color_button)
        cl.send("HTTP/1.0 200 OK\n")
        cl.send("Content-type:text/html\n")
        cl.send("Connection:close\n")
        cl.sendall(response)
        cl.close()
    
    
    wf.disconnect()
except Exception as e:
    if wf.isconnected():
        wf.disconnect()
    print(e)


