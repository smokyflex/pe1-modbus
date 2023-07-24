#!/usr/bin/env python3
from struct import *
from datetime import datetime
import time
import subprocess
import paho.mqtt.client as mqtt

#mqtt_username = "smoky"
#mqtt_password =  "smoky"
mqtt_host = "192.168.0.99"
mqtt_port = 1883

#******************************************
# Callback function when the client successfully connects to the MQTT broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    while True:
      item1 = 1000
      item2 = 2000
      
      # Publish config??
      config_payload = {
          "name": "Power Use General",
          "state_topic": "homeassistant/sensor/house/power_use1/state",
          "state_class": "measurement",
          "unit_of_measurement": "kWh",
          "device_class": "energy",
          "value_template": "{{ value }}",
          "unique_id": "power_use",
          "device": {
            "identifiers": [
               "thesensor"
            ],
            "name": "Power Use Sensors",
            "model": "None",
            "manufacturer": "None"
          },
          "icon": "mdi:home-lightning-bolt-outline",
          "platform": "mqtt"
      }
      #client.publish(topic="homeassistant/sensor/house/power_use1/config", payload=str(config_payload), qos=2, retain=False)

      # Publish State1
      topic1 = "homeassistant/sensor/house/power_use1/state"
      client.publish(topic=topic1, payload=str(item1), qos=2, retain=False)

      # Publish State2
      #topic2 = "homeassistant/sensor/house/power_use2/state"
      #client.publish(topic=topic2, payload=str(item2), qos=2, retain=False)
      
      
      #print("Published    '{0}' to '{1}'          Published '{2}' to '{3}'".format(str(item1), topic1, str(item2), topic2))
      print("PAck sent")
      time.sleep(2)
#******************************************

#-------------------------------------------------------------------------------------------------------
# main function
def main():
    client = mqtt.Client()
    #client.username_pw_set(mqtt_username, mqtt_password)
    client.on_connect = on_connect
    client.connect(mqtt_host, mqtt_port)
    client.loop_forever()

#---------------------------------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    main()
#---------------------------------------------------------------------------------------------------------------------------------
