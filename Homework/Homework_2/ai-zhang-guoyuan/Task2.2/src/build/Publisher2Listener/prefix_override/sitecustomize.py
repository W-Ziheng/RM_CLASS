import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ggbond/CLASS_2/Task2.2/src/install/Publisher2Listener'
