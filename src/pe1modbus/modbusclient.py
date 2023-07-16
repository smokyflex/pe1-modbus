from pyModbusTCP.client import ModbusClient
from typing import Union

from register import InputRegisters

class RegisterOperation:

    def __init__(self, address: int, offset: int, scaling_factor: int, decimals: int, unit: str, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.address = address
        self.offset = offset
        self.scaling_factor = scaling_factor
        self.decimals = decimals
        self.unit = unit
        self.relative_address = self.address - self.offset


class RegisterResponse:

    def __init__(self, name: str, value: Union[int, float], unit: str) -> None:
        self.name = name
        self.value = value
        self.unit = unit
    


class LTModbusClient(ModbusClient):

    def __init__(self, host='localhost', port=502, unit_id=1, timeout=30, debug=False, auto_open=True, auto_close=False):
        super().__init__(host, port, unit_id, timeout, debug, auto_open, auto_close)


    def get_register_value(self, input_register: InputRegisters) -> RegisterResponse:

        register_operation = RegisterOperation(*input_register.value)
        response_value = self.read_input_registers(register_operation.relative_address)[0]
        response_value_scaled = round(response_value / register_operation.scaling_factor, register_operation.decimals)
        register_response = RegisterResponse(register_operation.name, response_value_scaled, register_operation.unit) 

        return register_response
    