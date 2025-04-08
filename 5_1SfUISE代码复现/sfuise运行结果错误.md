 ros2 launch sfuise sfuise_test_isas-walk1.launch 
[INFO] [launch]: All log files can be found below /home/dsh/.ros/log/2025-04-08-02-35-47-916588-dsh-Precision-5680-287805
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [rviz2-1]: process started with pid [287806]
[INFO] [static_transform_publisher-2]: process started with pid [287808]
[INFO] [EstimationInterface-3]: process started with pid [287810]
[INFO] [SplineFusion-4]: process started with pid [287812]
[static_transform_publisher-2] [INFO] [1744050948.058640508] [static_transform_publisher]: Spinning until stopped - publishing transform
[static_transform_publisher-2] translation: ('0.000000', '0.000000', '0.000000')
[static_transform_publisher-2] rotation: ('0.000000', '0.000000', '0.000000', '1.000000')
[static_transform_publisher-2] from 'map' to 'my_frame'
[SplineFusion-4] [INFO] [1744050948.063737215] [SplineFusion]: ----> Starting SplineFusion.
[EstimationInterface-3] [INFO] [1744050948.067357775] [EstimationInterface]: EstimationInterface Initialized.
[EstimationInterface-3] [INFO] [1744050948.067477239] [EstimationInterface]: ----> Starting EstimationInterface.
[rviz2-1] [INFO] [1744050948.413738515] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-1] [INFO] [1744050948.413856691] [rviz2]: OpenGl version: 4.6 (GLSL 4.6)
[rviz2-1] [INFO] [1744050948.439371596] [rviz2]: Stereo is NOT SUPPORTED




dsh@dsh-Precision-5680:~/Documents/work_logs/code/SFUISE/sfuise_ws/src/dataset$ ros2 bag info ros2-walk1

Files:             ros2-walk1.db3
Bag size:          3.1 MiB
Storage id:        sqlite3
Duration:          63.339656084s
Start:             Oct  5 2022 16:47:53.401605086 (1664959673.401605086)
End:               Oct  5 2022 16:48:56.741261170 (1664959736.741261170)
Messages:          10917
Topic information: Topic: /vive/transform/tracker_1_ref | Type: geometry_msgs/msg/TransformStamped | Count: 3168 | Serialization Format: cdr
                   Topic: /waveshare_sense_hat_b | Type: sensor_msgs/msg/Imu | Count: 4839 | Serialization Format: cdr
                   Topic: /rtls_flares | Type: isas_msgs/msg/RTLSStick | Count: 970 | Serialization Format: cdr
                   Topic: /rtls_pose | Type: geometry_msgs/msg/PoseStamped | Count: 970 | Serialization Format: cdr
                   Topic: /anchor_list | Type: isas_msgs/msg/Anchorlist | Count: 970 | Serialization Format: cdr

dsh@dsh-Precision-5680:~/Documents/work_logs/code/SFUISE/sfuise_ws$ ros2 bag play src/dataset/ros2-walk1
[INFO] [1744104312.370102031] [rosbag2_storage]: Opened database 'src/dataset/ros2-walk1/ros2-walk1.db3' for READ_ONLY.
[INFO] [1744104312.370172445] [rosbag2_player]: Set rate to 1
[INFO] [1744104312.376061030] [rosbag2_player]: Adding keyboard callbacks.
[INFO] [1744104312.376102351] [rosbag2_player]: Press SPACE for Pause/Resume
[INFO] [1744104312.376112795] [rosbag2_player]: Press CURSOR_RIGHT for Play Next Message
[INFO] [1744104312.376121344] [rosbag2_player]: Press CURSOR_UP for Increase Rate 10%
[INFO] [1744104312.376128868] [rosbag2_player]: Press CURSOR_DOWN for Decrease Rate 10%
[INFO] [1744104312.376579619] [rosbag2_storage]: Opened database 'src/dataset/ros2-walk1/ros2-walk1.db3' for READ_ONLY.


dsh@dsh-Precision-5680:~/Documents/work_logs/code/SFUISE/sfuise_ws$ ros2 topic list
/EstimationInterface/anchor_list
/EstimationInterface/imu_ds
/EstimationInterface/toa_ds
/SplineFusion/est_window
/SplineFusion/start_time
/SplineFusion/sys_calib
/active_control_points
/anchor_list
/bspline_optimization_old
/bspline_optimization_window
/clicked_point
/default_imu_topic
/est_window
/events/read_split
/goal_pose
/imu_ds
/inactive_control_points
/initialpose
/map
/map_updates
/opt_pose
/parameter_events
/rosout
/rtls_flares
/rtls_pose
/start_time
/sys_calib
/tdoa_data
/tdoa_ds
/tf
/tf_static
/visualization_anchor
/vive/transform/tracker_1_ref
/waveshare_sense_hat_b


dsh@dsh-Precision-5680:~/Documents/work_logs/code/SFUISE/sfuise_ws$ ros2 topic echo /SplineFusion/est_window 
2025-04-08 17:35:10.540 [RTPS_TRANSPORT_SHM Error] Failed init_port fastrtps_port7419: open_and_lock_file failed -> Function open_port_internal
2025-04-08 17:35:10.540 [RTPS_TRANSPORT_SHM Error] Failed init_port fastrtps_port7421: open_and_lock_file failed -> Function open_port_internal
2025-04-08 17:35:10.540 [RTPS_TRANSPORT_SHM Error] Failed init_port fastrtps_port7423: open_and_lock_file failed -> Function open_port_internal
2025-04-08 17:35:10.540 [RTPS_TRANSPORT_SHM Error] Failed init_port fastrtps_port7425: open_and_lock_file failed -> Function open_port_internal
2025-04-08 17:35:10.541 [RTPS_TRANSPORT_SHM Error] Failed init_port fastrtps_port7427: open_and_lock_file failed -> Function open_port_internal
2025-04-08 17:35:10.541 [RTPS_TRANSPORT_SHM Error] Failed init_port fastrtps_port7431: open_and_lock_file failed -> Function open_port_internal
2025-04-08 17:35:10.541 [RTPS_TRANSPORT_SHM Error] Failed init_port fastrtps_port7433: open_and_lock_file failed -> Function open_port_internal
^Z


