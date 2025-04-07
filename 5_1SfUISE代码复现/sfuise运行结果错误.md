            
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp: In member function ‘void SplineFusion::run()’:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:68:39: error: ‘node’ was not declared in this scope; did you mean ‘Node’?
   68 |         rclcpp::Time t_window_start = node->get_clock()->now();  // 获取当前时间
      |                                       ^~~~
      |                                       Node
gmake[2]: *** [CMakeFiles/EstimationInterface.dir/build.make:76: CMakeFiles/EstimationInterface.dir/src/EstimationInterface.cpp.o] Error 1
gmake[1]: *** [CMakeFiles/Makefile2:139: CMakeFiles/EstimationInterface.dir/all] Error 2
gmake[1]: *** Waiting for unfinished jobs....
gmake[2]: *** [CMakeFiles/SplineFusion.dir/build.make:76: CMakeFiles/SplineFusion.dir/src/SplineFusion.cpp.o] Error 1
gmake[1]: *** [CMakeFiles/Makefile2:165: CMakeFiles/SplineFusion.dir/all] Error 2
gmake: *** [Makefile:146: all] Error 2
---
Failed   <<< sfuise [25.3s, exited with code 2]

Summary: 3 packages finished [26.7s]
  1 package failed: sfuise
  1 package had stderr output: sfuise
dsh@dsh-Precision-5680:~/Documents/work_logs/code/SFUISE/sfuise_ws$ 

