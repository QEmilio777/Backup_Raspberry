from pymodbus.client import ModbusTcpClient
import time

IP = "192.168.47.30"
PORT = 502
REG_NUM = 0

client = ModbusTcpClient(IP, port=PORT)

if not client.connect():
    print("No hay conexión")
    exit()

print("Conexión establecida")

try:
    while True:
        print("Velocidad del '0 - 100' || q para salir")
        velocidad = input("")
        if velocidad.lower() == "q":
            break
        
        if not velocidad.isdigit():
            print("No ingresaste una opción valida")
            continue
        
        potencia = int(velocidad)
        if  0 <= potencia <= 100:
            potencia = int((4095/100) * potencia)
            client.write_register(REG_NUM, potencia)
            print(f"La velocidad es: {potencia}")
        else:
            print("Potencia fuera de los limites")

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    client.close()
    client.write_register(REG_NUM, 0)
    print("Programa finalizado")