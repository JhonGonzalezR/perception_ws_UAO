import rclpy # Python library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import numpy as np
import cv2 # OpenCV library
  
class ColorDetector(Node):
  """
  Create an ImageSubscriber class, which is a subclass of the Node class.
  """
  def __init__(self):
    """
    Class constructor to set up the node
    """
    # Initiate the Node class's constructor and give it a name
    super().__init__('color_detector')
    

    # PARAMETERS
    self.declare_parameter('color', 'red')
    self.color = self.get_parameter('color').value

    # Create the subscriber. This subscriber will receive an Image
    # from the video_frames topic. The queue size is 10 messages.
    self.subscription = self.create_subscription(Image, 'filtered_frames', self.listener_callback, 10)
    self.subscription # prevent unused variable warning

    self.get_logger().info(f'{self.color} detector has been initialize')
       
    # Used to convert between ROS and OpenCV images
    self.br = CvBridge()
    
  def listener_callback(self, data):
    """
    Callback function.
    """
    # Display the message on the console
    self.get_logger().info(f'{self.color}: Receiving video frame')
  
    # Convert ROS Image message to OpenCV image
    img_src = self.br.imgmsg_to_cv2(data)
    hsvFrame = cv2.cvtColor(img_src, cv2.COLOR_BGR2HSV)


    # Define range and mask

    # Case red
    if self.color == 'red':
      self.lower = np.array([136, 87, 111], np.uint8)
      self.upper = np.array([180, 255, 255], np.uint8)
      self.mask = cv2.inRange(hsvFrame, self.lower, self.upper)

      view_color = (0,0,255)
     
    # Case blue
    elif self.color == 'blue':
      self.lower = np.array([94, 80, 2], np.uint8)
      self.upper = np.array([120, 255, 255], np.uint8)
      self.mask = cv2.inRange(hsvFrame, self.lower, self.upper)

      view_color = (255,0,0)

    # Case greeen
    else:
      self.lower = np.array([25, 52, 72], np.uint8)
      self.upper = np.array([102, 255, 255], np.uint8)
      self.mask = cv2.inRange(hsvFrame, self.lower, self.upper)

      view_color = (0,255,0)

    kernal = np.ones((5, 5), "uint8")

    # For red color
    self.mask = cv2.dilate(self.mask, kernal)
    res_color = cv2.bitwise_and(img_src, img_src, 
                              mask = self.mask)
    

    # Creating contour to track red color
    contours, hierarchy = cv2.findContours(self.mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
      
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            img_src = cv2.rectangle(img_src, (x, y), 
                                       (x + w, y + h), 
                                       view_color, 2)
            

              
            cv2.putText(img_src, self.color, (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        view_color)    
    

    # Display image
    cv2.imshow(f"Multiple {self.color} Detection in Real-TIme", img_src)


     
    cv2.waitKey(1)
   
def main(args=None):
   
  # Initialize the rclpy library
  rclpy.init(args=args)
   
  # Create the node
  color_detector = ColorDetector()
   
  # Spin the node so the callback function is called.
  rclpy.spin(color_detector)
   
  # Destroy the node explicitly
  # (optional - otherwise it will be done automatically
  # when the garbage collector destroys the node object)
  color_detector.destroy_node()
   
  # Shutdown the ROS client library for Python
  rclpy.shutdown()
   
if __name__ == '__main__':
  main()
