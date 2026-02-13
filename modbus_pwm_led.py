from pymodbus.client import ModbusTcpClient
# import RPi.GPIO as GPIO
import MCP3008_simple as MCP
# from time import sleep

IP = "192.168.47.30"
PORT = 502
HREG_LED = 0

client = ModbusTcpClient(IP, port=PORT)

pwm = None

try:
    
    while True:
        pwm = MCP.getResult(0, 12)
        client.write_register(HREG_LED, pwm)
        
        
except KeyboardInterrupt:
    print("Ctrl c ejecutado")
finally:
    client.write_register(HREG_LED, 0)
    client.close()
    print("Programa finalizado")