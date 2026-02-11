from pymodbus.client import ModbusTcpClient
from time import sleep

IP = "192.168.47.30"
PORT = 502
COIl_relay = 4

client = ModbusTcpClient(IP, port = PORT)

if not client.connect():
    print("No hay conexión")
    exit()

try:
    while True:
        print("\n1 para encender | 0 para apagar | q salir")
        respuesta = input("")
        
        if respuesta.lower() == 'q':
            print("Programa terminado por usuario")
            break
        
        if respuesta not in ["0", "1"]:
            print("Valores fuera de rango")
            continue
        
        valor = bool(int(respuesta))
        client.write_coil(COIl_relay, valor)
        
except KeyboardInterrupt:
    print("Ctrl + c presionado")
    

finally:
    client.write_coil(COIl_relay, False)
    client.close()
    print("Programa finalizado")