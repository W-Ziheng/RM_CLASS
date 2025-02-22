import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/zjy/桌面/Task2/hw_py/install/Publisher2Listener'
