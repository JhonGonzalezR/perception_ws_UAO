import rclpy # Python Client Library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library

import tkinter as tk
from tkinter import filedialog
  
class FramesPublisher(Node):
  """
  Create an ImagePublisher class, which is a subclass of the Node class.
  """
  def __init__(self):
    """
    Class constructor to set up the node
    """
    # Initiate the Node class's constructor and give it a name
    super().__init__('frames_publisher')

    # Setting parameters
    self.declare_parameter('use_webcam', True)
    self.use_webcam = self.get_parameter('use_webcam').value
       
    # Create the publisher. This publisher will publish an Image
    # to the video_frames topic. The queue size is 10 messages.
    self.publisher_ = self.create_publisher(Image, 'video_frames', 10)

    # We will publish a message every 0.1 seconds
    timer_period = 0.001  # seconds
       
    # Create the timer
    self.timer = self.create_timer(timer_period, self.timer_callback)

    # Select the video
    if not(self.use_webcam):
      
        # Select the video
        root = tk.Tk()
        root.withdraw()
        video_source = filedialog.askopenfile().name

        self.cap = cv2.VideoCapture(video_source)
    else:
               
        # Create a VideoCapture object
        # The argument '0' gets the default webcam.
        self.cap = cv2.VideoCapture(0)
          
    # Used to convert between ROS and OpenCV images
    self.br = CvBridge()
    
  def timer_callback(self):
    """
    Callback function.
    This function gets called every 0.1 seconds.
    """
    # Capture frame-by-frame
    # This method returns True/False as well
    # as the video frame.

    ret, frame = self.cap.read()
           
    if ret == True:
      
      # Publish the image.
      # The 'cv2_to_imgmsg' method converts an OpenCV
      # image to a ROS 2 image message
      self.publisher_.publish(self.br.cv2_to_imgmsg(frame))
  
    # Display the message on the console
    self.get_logger().info('Publishing video frame')
   
def main(args=None):
   
  # Initialize the rclpy library
  rclpy.init(args=args)
   
  # Create the node
  frames_Publisher = FramesPublisher()
   
  # Spin the node so the callback function is called.
  rclpy.spin(frames_Publisher)
   
  # Destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  frames_Publisher.destroy_node()
   
  # Shutdown the ROS client library for Python
  rclpy.shutdown()
   
if __name__ == '__main__':
  main()
