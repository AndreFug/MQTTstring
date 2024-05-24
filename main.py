## Main program to run mqtt parsing
import paho.mqtt.client as mqtt

# Define the callback for when a message is received
def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode('utf-8')
    
    # Split the payload into separate values
    values = payload.split(', ')
    
    # Define the new topics to publish based on the received topic
    new_topics = {
        'cabot/output/targetmotorspeed': ['cabot/targetpos/targetmotorspeed{}'.format(i) for i in range(1, 9)],
        'cabot/output/actualmotorspeed': ['cabot/targetpos/actualmotorspeed{}'.format(i) for i in range(1, 9)],
        'cabot/output/targetposition': ['cabot/targetpos/targetmotorposition{}'.format(i) for i in range(1, 4)],
        'cabot/output/actualposition': ['cabot/targetpos/actualmotorposition{}'.format(i) for i in range(1, 4)]
    }
    
    # Publish each value to the corresponding new topic
    if topic in new_topics:
        for i, new_topic in enumerate(new_topics[topic]):
            if i < len(values):
                client.publish(new_topic, values[i])

# Set up the MQTT client
client = mqtt.Client()
client.on_message = on_message

# Connect to the MQTT broker
client.connect("127.0.0.1", 1883, 60)

# Subscribe to the original topics
client.subscribe("cabot/output/targetmotorspeed")
client.subscribe("cabot/output/actualmotorspeed")
client.subscribe("cabot/output/targetposition")
client.subscribe("cabot/output/actualposition")

# Start the loop to process received messages
client.loop_forever()
