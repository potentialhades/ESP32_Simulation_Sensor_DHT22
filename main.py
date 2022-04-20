import time
import network
from umqtt.simple import MQTTClient
from machine import Pin
import dht

##################################################################################

# MEASURE TEMPERATURE
def sensor_temp():
  sensor.measure() 
  temp = sensor.temperature()
  return round(temp, 1)

##################################################################################

# MEASURE HUMIDITY
def sensor_umidade():
  sensor.measure() 
  umidade = sensor.humidity()
  return round(umidade, 1)

##################################################################################

# MQTT CONFIG
MQTT_BROKER    = "broker.hivemq.com"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC     = "sala306/temp"
MQTT_TOPIC_2   = "sala306/umidade"
MQTT_PORT      = 1883

##################################################################################

# CONNECT WI-FI WOKWI-GUEST
def wifi_connect():
  print("Connecting", end="")

  sta_if = network.WLAN(network.STA_IF)
  sta_if.active(True)
  sta_if.connect('Wokwi-GUEST', '')

  while not sta_if.isconnected():
    print(".", end="")
    time.sleep(0.3)

  print(" Wi-Fi connected!")

##################################################################################

# PUBLISHER
def publish(temp, umidade):
  client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=30)
  client.connect()  # Connection Broker
  print("[OK]")
  
  client.publish(MQTT_TOPIC, str(temp))
  #client.publish("sala306/temp", '{"message": "%s"}' % MESSAGE)

  print("Publishing message Temperature:", temp)
  
  client.publish(MQTT_TOPIC_2, str(umidade))
  #client.publish("sala306/umidade", '{"message": "%s"}' % MESSAGE)

  print("Publishing message Humidity:", umidade)
  client.disconnect()

##################################################################################

# MAIN PROGRAM
wifi_connect()
sensor = dht.DHT22(Pin(14))

while True:
  temp = sensor_temp()
  umidade = sensor_umidade()
  publish(temp, umidade)
  time.sleep(15)