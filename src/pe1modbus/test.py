#from pymodbus.client import ModbusTcpClient
import logging

from pyModbusTCP.client import ModbusClient

from register import InputRegisters
from modbusclient import LTModbusClient, RegisterResponse

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("pymodbus").setLevel(logging.DEBUG)

# TCP auto connect on first modbus request
client = LTModbusClient(
    host="192.168.0.222", 
    port=502, 
    unit_id=2
)

print(client)

status = client.open()

if status:

    for ir in InputRegisters:
        
        #print(ir.value)
        register_response: RegisterResponse = client.get_register_value(ir)

        print(f"{register_response.name}: {register_response.value} {register_response.unit}")


client.close()

exit()
