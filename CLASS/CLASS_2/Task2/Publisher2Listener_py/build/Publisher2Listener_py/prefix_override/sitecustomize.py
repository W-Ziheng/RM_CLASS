import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/whaltze/rm/RM_CLASS/CLASS/CLASS_2/Task2/Publisher2Listener_py/install/Publisher2Listener_py'
