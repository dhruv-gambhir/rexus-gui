import rospy
from std_msgs.msg import String
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class MyGui(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize ROS node
        rospy.init_node('my_gui_node', anonymous=True)

        # Create ROS subscriber
        rospy.Subscriber('my_topic_name', String, self.callback_function)

        # Create ROS publisher
        self.pub = rospy.Publisher('my_topic_name', String, queue_size=10)

        # Set up GUI widgets
        self.label = QLabel('Hello, ROS!', self)
        self.label.move(50, 50)
        self.button = QPushButton('Publish', self)
        self.button.move(50, 100)
        self.button.clicked.connect(self.publish_function)

        # Show the GUI window
        self.setGeometry(100, 100, 200, 150)
        self.show()

    def callback_function(self, data):
        # Handle incoming messages from ROS topic
        self.label.setText(data.data)

    def publish_function(self):
        # Handle button click event and publish message to ROS topic
        msg = String()
        msg.data = "Button clicked!"
        self.pub.publish(msg)

if __name__ == '__main__':
    app = QApplication([])
    gui = MyGui()
    rospy.spin()