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
    LOGGER.debug("Connected with result code " + str(rc))

    selected_regs = [
        InputRegisters.BOILER_TEMPERATURE_TOP,
        InputRegisters.FILL_LEVEL_PELLETS_CONTAINER,
        InputRegisters.TOTAL_PELLETS_CONSUMPTION,
        InputRegisters.HEATING_FLOW_TEMPERATURE_ACTUAL,
        InputRegisters.HEATING_FLOW_TEMPERATURE_TARGET,
        InputRegisters.BUFFER_TEMPERATURE_TOP,
        InputRegisters.BUFFER_TEMPERATURE_BOTTOM,
        InputRegisters.BUFFER_CHARGING_STATE
    ]

    while True:

        # TCP auto connect on first modbus request
        lt_client = LTModbusClient(
            host="192.168.0.222", 
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

        time.sleep(30)


def main():

    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("pymodbus").setLevel(logging.DEBUG)
    
    mqtt_client = mqtt.Client()
    mqtt_client.username_pw_set("smoky", "smoky")
    mqtt_client.on_connect = on_connect
    mqtt_client.connect("127.0.0.1", 1883)
    mqtt_client.loop_forever()


if __name__=="__main__":
    main()
