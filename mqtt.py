import time
import paho.mqtt.client as paho

broker = "broker.shiftr.io"


# define callback
def on_message(client, userdata, message):
    time.sleep(1)
    print("received message =", str(message.payload.decode("utf-8")))


def mqtt(dev_id, message):
    client = paho.Client(dev_id)
    # create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port)
    ######Bind function to callback
    client.username_pw_set("try", "try")
    client.on_message = on_message
    #####
    print("connecting to broker ", broker)
    client.connect(broker)  # connect
    # client.loop_start() #start loop to process received messages
    # print("subscribing ")
    # client.subscribe("house/bulb1")#subscribe
    time.sleep(1)
    print("publishing ")
    client.publish(dev_id+"/strange/pin", message)  # publish
    time.sleep(2)
    client.disconnect()  # disconnect
    # client.loop_stop() #stop loop
    return True
