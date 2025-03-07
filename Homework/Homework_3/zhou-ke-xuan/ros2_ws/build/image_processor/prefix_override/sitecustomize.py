import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/zkx/RM/CLASS_3/ros2_ws/install/image_processor'
