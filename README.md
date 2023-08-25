# pe1-modbus

This project is a work in progress, integrating live data from a Froeling PE1 Heater into Home Assitant via Modbus TCP and MQTT.

Opposite to the Service/App "FrolingConnect" this approach keeps all communication in the local network and is therefore offers adjustable / shorter data refresh interval cycles. 

## Hardware Requirements
The Lambdatronic board offers 2 serial interfaces, which can be configured to Modbus TCP in the settings.
To conveiently integrate the device into the local LAN network, the serial connection needs an adapter to RJ45 (RS232 to Ethernet Converter). This one by Waveshare (Industrial RS232/RS485 to Ethernet Converter) was used and is confiremd to work:
- https://www.waveshare.com/rs232-485-to-eth-for-eu.htm

The RS232 side can be connected to the COM2 port on the Lambdtronic. Ensure you use the proper cable that has the RX TX pins crossed.

More infromation on the hardware setup can be found in this guide:
https://loxwiki.atlassian.net/wiki/spaces/LOX/pages/1704984631/Fr+ling+Pelletskessel+RS232+an+Loxone+Modbus+TCP?focusedCommentId=1705050279


## Modbus TCP
Using python libraries for ModbusTCP, a connection to the waveshare converter can be established fairly easy. Information on Register addresses etc. can be studied in the ModBus Lambdatronic 3200 Modbus Definition Document (google search should provide a link to download). 

## MQTT
Now that we have the data available via network and python script, we need a way to publish this data to the Home Assistant Server in our network. This can be done using the MQTT protocol, which is supported by Home Assistant (there is extensive documentation available on how to do this). Python provides libraries  e.g. (paho-mqtt) to quickly setup a mqtt communication service.

## LINUX service
Lastly we can create a python script like "mqtt.py" in this repo, to automate this pipeline via a linux service that can run on the same host as the Home Assistant server for example. This script aquires the data from the PE1-Heater via Modbus every 30s and then publishes this data via MQTT to the home assistant.

Voila