# IoT_Simulation
Temperature (°C) and Humidity (%) microcontroller ESP32 on Python (Wokwi Simulation + Hivemq Broker Client)

Run the simulation on Wokwi and see the messages on Hivemq Broker

Project on Wokwi (Micropython on ESP32): https://wokwi.com/projects/328777740948865619

Link Broker -> Hivemq Broker Client: http://www.hivemq.com/demos/websocket-client/

Or install the app MQTT DASH on Google Play Store

Language: Portuguese

# Hivemq Broker website
# Connection
- Host -> broker.mqttdashboard.com
- Port -> 8000
- KeepAlive -> 60
- Click on 'Connect'

# Subscriptions - Add new Topic
- Topic: sala306/#
- QoS: 0
- Click on 'Subscribe'

# App MQTT Dash on Smartphone
# Config the Broker
- Click on '+' button (upper right corner of the screen)
- Name the broker
- Address: broker.hivemq.com
- Port: 1883
- Click on diskette button (upper right corner of the screen) to save
- Click on Broker

# Subscritions
# Temperature
-  Click on '+' button (upper right corner of the screen)
-  Choose type: 'Text'
-  Name: Temperature
-  Topic: sala306/temp
-  Postfix: °C
- Click on diskette button (upper right corner of the screen) to save

# Humidity
-  Click on '+' button (upper right corner of the screen)
-  Choose type: 'Text'
-  Name: Humidity
-  Topic: sala306/umidade
-  Postfix: %
- Click on diskette button (upper right corner of the screen) to save
