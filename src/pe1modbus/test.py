from pymodbus.client import ModbusTcpClient

client = ModbusTcpClient('192.168.0.7')
client.connect()
client.write_coil(1, True)
result = client.read_coils(1,1)
print(result.bits[0])
client.close()