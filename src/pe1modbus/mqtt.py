#!/usr/bin/env python3
from struct import *
from datetime import datetime
import time
import subprocess
import paho.mqtt.client as mqtt
import json
from paho.mqtt import publish
import logging
from register import InputRegisters
from modbusclient import LTModbusClient, RegisterResponse

LOGGER = logging.getLogger(__name__)


# Callback function when the client successfully connects to the MQTT broker
def on_connect(client, userdata, flags, rc):

    interval_in_s = 30
    host_address = "ip_to_host"

    LOGGER.debug("Connected with result code " + str(rc))

    selected_regs = [
        InputRegisters.SYSTEM_STATUS,
        InputRegisters.FURNACE_STATUS,
        InputRegisters.BOILER_TEMPERATURE_TOP,
        InputRegisters.BOILER_PUMP_CONTROL,
        InputRegisters.FILL_LEVEL_PELLETS_CONTAINER,
        InputRegisters.TOTAL_PELLETS_CONSUMPTION,
        InputRegisters.KG_COUNT,
        InputRegisters.HEATING_FLOW_TEMPERATURE_ACTUAL,
        InputRegisters.HEATING_FLOW_TEMPERATURE_TARGET,
        InputRegisters.OUTSIDE_TEMPERATURE,
        InputRegisters.ROOM_TEMPERATURE,
        InputRegisters.BUFFER_TEMPERATURE_TOP,
        InputRegisters.BUFFER_TEMPERATURE_BOTTOM,
        InputRegisters.BUFFER_PUMP_CONTROL,
        InputRegisters.BUFFER_CHARGING_STATE,
        InputRegisters.HEATER_TEMPERATURE,
        #InputRegisters.HOURS_SINCE_LAST_MAINTENANCE,
        #InputRegisters.REMAINING_HOURS_UNTIL_ASH_REMOVAL,
    ]

    while True:

        # TCP auto connect on first modbus request
        lt_client = LTModbusClient(
            host=host_address, 
            port=502, 
            unit_id=2
        )
        status = lt_client.open()

        if status:

            for ir in selected_regs:

                register_response: RegisterResponse = lt_client.get_register_value(ir)
                LOGGER.info(f"{register_response.name}: {register_response.value} {register_response.unit}")
                publish.single(f"homeassistant/pe1/{register_response.name}", payload=json.dumps({"value": register_response.value}), qos=2, hostname="localhost", port=1883)  

        else:
            LOGGER.error("Cannot connect to Lambdatronic via Modbus")
            #raise Exception("Cannot connect to Lambdatronic via Modbus")
        
        lt_client.close()

        time.sleep(interval_in_s)


def main():

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("pymodbus").setLevel(logging.DEBUG)

    user = "some_user"
    pwd = user
    
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set(user, pwd)
    mqtt_client.on_connect = on_connect
    mqtt_client.connect("127.0.0.1", 1883)
    mqtt_client.loop_forever()


if __name__=="__main__":
    main()
