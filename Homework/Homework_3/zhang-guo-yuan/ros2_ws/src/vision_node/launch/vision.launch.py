from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='vision_node',
            executable='image_processor_node',
            name='image_processor',
            parameters=[{'debug_mode': True}],
            remappings=[
                ('input_image', '/camera/image_raw'),
                ('output_image', '/vision/processed_image')
            ]
        )
    ])
    
