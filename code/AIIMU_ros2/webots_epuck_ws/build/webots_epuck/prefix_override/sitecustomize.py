import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/dsh/Documents/work_logs/code/AIIMU_ros2/webots_epuck_ws/install/webots_epuck'
