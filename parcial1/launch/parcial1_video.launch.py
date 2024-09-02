from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    LaunchDescription()

    redColor = Node(
        package="parcial1",
        executable="color",
        name="redColor",
        parameters=[
            {'color': 'red'},
        ]

    )
    blueColor = Node(
        package="parcial1",
        executable="color",
        name="blueColor",
        parameters=[
            {'color': 'blue'},
        ]
    )
    greenColor = Node(
        package="parcial1",
        executable="color",
        name="greenColor",
        parameters=[
            {'color': 'green'},
        ]
    )
    
    current_frame = Node(
        package="parcial1",
        executable = "frames",
        parameters=[
            {'use_webcam': False},
        ]
    )
    show_frame = Node(
        package="parcial1",
        executable = "suscriber"
        
    )
    person = Node(
        package="parcial1",
        executable = "person"
        
    )
    filter = Node(
        package="parcial1",
        executable = "filter"
        
    )
  

    return LaunchDescription([redColor,
                              blueColor,
                              greenColor,                              
                              current_frame,
                              show_frame,
                              person,
                              filter])  