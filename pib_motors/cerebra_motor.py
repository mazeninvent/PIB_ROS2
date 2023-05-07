#!/usr/bin/env python3
import json
from std_msgs.msg import String
import tinkerforge
import rclpy
from rclpy.node import Node
from rosbridge_library import RosbridgeWebSocket

class cerebra_motor(Node):

    def __init__(self):
        super().__init__('cerebra_motor')
        self.websocket = RosbridgeWebSocket('http://h2879304.stratoserver.net/hand/left', 9090)
        self.websocket.connect()
        self.create_subscription(
            msg_type=str,
            topic='/motor_settings',
            callback=self.handle_message,
            qos_profile=rclpy.qos.qos_profile_sensor_data
        )

    def handle_message(self, msg):
        data = json.loads(msg.data)
        motor = data["data"][0]["motor"]
        value = data["data"][1]["value"]
        self.get_logger().info("Received message: motor={}, value={}".format(motor, value))

        # Define the IP address and port number of your Tinkerforge Master Brick
        HOST = 'localhost'
        PORT = 4223
        # Define the UID of your Tinkerforge Servo Bricklet
        SERVO_UID = 'XYZ'  # Replace with your own UID

        # Connect to the Tinkerforge hat Brick and instantiate a Servo Bricklet object
        servo = tinkerforge.BrickletServo(SERVO_UID, tinkerforge.IPConnection(HOST, PORT))

        # Convert the "motor" field from the incoming message into a servo channel number (0-9)
        # Define the mapping of servo motor names to channel numbers
        motor_channel_map = {
            'ring_left_stretch': 0,
            'pinky_left_stretch': 1,
            'index_left_stretch': 2,
            'middle_left_stretch': 3,
            'thumb_left_stretch': 4,
            'thumb_left_stretch': 5,
            'thumb_left_opposition': 6,
            }

            # Map the incoming motor name to the corresponding channel number
        channel = motor_channel_map.get(motor, None)
        servo.set_position(channel, value)
        # Clean up
        servo.disable()
        IPConnection.disconnect()


    def shutdown(self):
        self.websocket.close()
        super().shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = cerebra_motor()
    rclpy.spin(node)
    node.shutdown()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
