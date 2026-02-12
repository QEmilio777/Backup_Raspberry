from pymodbus.client import ModbusTcpClient
import RPi.GPIO as GPIO
import MCP3008_simple as MCP
from time import sleep

IP = "192.168.47.30"
PORT = 502
Hreg = 0

client = ModbusTcpClient(IP, port=PORT)

if not client.connect():
    print("No hay conexion")
    exit()

try:
    while True:
        
        pot_val = MCP.getResult(0, 12)
        client.write_register(Hreg, pot_val)
        sleep(1)
        
except KeyboardInterrupt:
    print("Ctrl c ejecutado")
finally:
    client.close()
    print("Programa finalizado")