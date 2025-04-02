colcon build --packages-select sfuise
Starting >>> sfuise  
--- stderr: sfuise                               
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp: In constructor ‘EstimationInterface::EstimationInterface()’:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:42:118: error: no match for ‘operator=’ (operand types are ‘rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > >::SharedPtr’ {aka ‘std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > > >’} and ‘std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Int64_<std::allocator<void> >, std::allocator<void>, std_msgs::msg::Int64_<std::allocator<void> >, std_msgs::msg::Int64_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<std_msgs::msg::Int64_<std::allocator<void> >, std::allocator<void> > > >’)
   42 |  1000, std::bind(&EstimationInterface::startCallBack, this, std::placeholders::_1));
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:363:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<const std::shared_ptr<_Yp>&> std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Yp>&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > >]’
  363 |         operator=(const shared_ptr<_Yp>& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:363:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = const std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Int64_<std::allocator<void> >, std::allocator<void>, std_msgs::msg::Int64_<std::allocator<void> >, std_msgs::msg::Int64_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<std_msgs::msg::Int64_<std::allocator<void> >, std::allocator<void> > > >&; _Tp = rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:363:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > > >::_Assignable<const std::shared_ptr<_Tp>&> std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > > >::operator=<_Yp>(const std::shared_ptr<_Tp>&) [with _Yp = rclcpp::Subscription<std_msgs::msg::Int64_<std::allocator<void> >, std::allocator<void>, std_msgs::msg::Int64_<std::allocator<void> >, std_msgs::msg::Int64_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<std_msgs::msg::Int64_<std::allocator<void> >, std::allocator<void> > >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:42:118:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::auto_ptr<_Up> > std::shared_ptr<_Tp>::operator=(std::auto_ptr<_Up>&&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > >]’
  374 |         operator=(auto_ptr<_Yp>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:42:118: note:   ‘std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Int64_<std::allocator<void> >, std::allocator<void>, std_msgs::msg::Int64_<std::allocator<void> >, std_msgs::msg::Int64_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<std_msgs::msg::Int64_<std::allocator<void> >, std::allocator<void> > > >’ is not derived from ‘std::auto_ptr<_Up>’
   42 |  1000, std::bind(&EstimationInterface::startCallBack, this, std::placeholders::_1));
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:391:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::shared_ptr<_Yp> > std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Yp>&&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > >]’
  391 |         operator=(shared_ptr<_Yp>&& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:391:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Int64_<std::allocator<void> >, std::allocator<void>, std_msgs::msg::Int64_<std::allocator<void> >, std_msgs::msg::Int64_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<std_msgs::msg::Int64_<std::allocator<void> >, std::allocator<void> > > >; _Tp = rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:391:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > > >::_Assignable<std::shared_ptr<_Tp> > std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > > >::operator=<_Yp>(std::shared_ptr<_Tp>&&) [with _Yp = rclcpp::Subscription<std_msgs::msg::Int64_<std::allocator<void> >, std::allocator<void>, std_msgs::msg::Int64_<std::allocator<void> >, std_msgs::msg::Int64_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<std_msgs::msg::Int64_<std::allocator<void> >, std::allocator<void> > >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:42:118:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note: candidate: ‘template<class _Yp, class _Del> std::shared_ptr<_Tp>::_Assignable<std::unique_ptr<_Up, _Ep> > std::shared_ptr<_Tp>::operator=(std::unique_ptr<_Up, _Ep>&&) [with _Yp = _Yp; _Del = _Del; _Tp = rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > >]’
  399 |         operator=(unique_ptr<_Yp, _Del>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:42:118: note:   ‘std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Int64_<std::allocator<void> >, std::allocator<void>, std_msgs::msg::Int64_<std::allocator<void> >, std_msgs::msg::Int64_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<std_msgs::msg::Int64_<std::allocator<void> >, std::allocator<void> > > >’ is not derived from ‘std::unique_ptr<_Tp, _Dp>’
   42 |  1000, std::bind(&EstimationInterface::startCallBack, this, std::placeholders::_1));
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:359:19: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Tp>&) [with _Tp = rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > >]’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                   ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:359:29: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Int64_<std::allocator<void> >, std::allocator<void>, std_msgs::msg::Int64_<std::allocator<void> >, std_msgs::msg::Int64_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<std_msgs::msg::Int64_<std::allocator<void> >, std::allocator<void> > > >’ to ‘const std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > > >&’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                             ^~~~~~~~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:7: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Tp>&&) [with _Tp = rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > >]’
  383 |       operator=(shared_ptr&& __r) noexcept
      |       ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:30: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Int64_<std::allocator<void> >, std::allocator<void>, std_msgs::msg::Int64_<std::allocator<void> >, std_msgs::msg::Int64_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<std_msgs::msg::Int64_<std::allocator<void> >, std::allocator<void> > > >’ to ‘std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > > >&&’
  383 |       operator=(shared_ptr&& __r) noexcept
      |                 ~~~~~~~~~~~~~^~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:55:113: error: no match for ‘operator=’ (operand types are ‘rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >::SharedPtr’ {aka ‘std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >’} and ‘std::shared_ptr<rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void>, cf_msgs::msg::Tdoa_<std::allocator<void> >, cf_msgs::msg::Tdoa_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void> > > >’)
   55 |  std::bind(&EstimationInterface::getTdoaUTILCallback, this, std::placeholders::_1));
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:363:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<const std::shared_ptr<_Yp>&> std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Yp>&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  363 |         operator=(const shared_ptr<_Yp>& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:363:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = const std::shared_ptr<rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void>, cf_msgs::msg::Tdoa_<std::allocator<void> >, cf_msgs::msg::Tdoa_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void> > > >&; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:363:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >::_Assignable<const std::shared_ptr<_Tp>&> std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >::operator=<_Yp>(const std::shared_ptr<_Tp>&) [with _Yp = rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void>, cf_msgs::msg::Tdoa_<std::allocator<void> >, cf_msgs::msg::Tdoa_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void> > >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:55:113:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::auto_ptr<_Up> > std::shared_ptr<_Tp>::operator=(std::auto_ptr<_Up>&&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  374 |         operator=(auto_ptr<_Yp>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:55:113: note:   ‘std::shared_ptr<rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void>, cf_msgs::msg::Tdoa_<std::allocator<void> >, cf_msgs::msg::Tdoa_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void> > > >’ is not derived from ‘std::auto_ptr<_Up>’
   55 |  std::bind(&EstimationInterface::getTdoaUTILCallback, this, std::placeholders::_1));
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:391:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::shared_ptr<_Yp> > std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Yp>&&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  391 |         operator=(shared_ptr<_Yp>&& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:391:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = std::shared_ptr<rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void>, cf_msgs::msg::Tdoa_<std::allocator<void> >, cf_msgs::msg::Tdoa_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void> > > >; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:391:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >::_Assignable<std::shared_ptr<_Tp> > std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >::operator=<_Yp>(std::shared_ptr<_Tp>&&) [with _Yp = rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void>, cf_msgs::msg::Tdoa_<std::allocator<void> >, cf_msgs::msg::Tdoa_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void> > >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:55:113:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note: candidate: ‘template<class _Yp, class _Del> std::shared_ptr<_Tp>::_Assignable<std::unique_ptr<_Up, _Ep> > std::shared_ptr<_Tp>::operator=(std::unique_ptr<_Up, _Ep>&&) [with _Yp = _Yp; _Del = _Del; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  399 |         operator=(unique_ptr<_Yp, _Del>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:55:113: note:   ‘std::shared_ptr<rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void>, cf_msgs::msg::Tdoa_<std::allocator<void> >, cf_msgs::msg::Tdoa_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void> > > >’ is not derived from ‘std::unique_ptr<_Tp, _Dp>’
   55 |  std::bind(&EstimationInterface::getTdoaUTILCallback, this, std::placeholders::_1));
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:359:19: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Tp>&) [with _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                   ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:359:29: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void>, cf_msgs::msg::Tdoa_<std::allocator<void> >, cf_msgs::msg::Tdoa_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void> > > >’ to ‘const std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >&’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                             ^~~~~~~~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:7: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Tp>&&) [with _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  383 |       operator=(shared_ptr&& __r) noexcept
      |       ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:30: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void>, cf_msgs::msg::Tdoa_<std::allocator<void> >, cf_msgs::msg::Tdoa_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void> > > >’ to ‘std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >&&’
  383 |       operator=(shared_ptr&& __r) noexcept
      |                 ~~~~~~~~~~~~~^~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:56:80: error: no match for ‘operator=’ (operand types are ‘rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >::SharedPtr’ {aka ‘std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >’} and ‘std::shared_ptr<rclcpp::Publisher<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void> > >’)
   56 |             pub_uwb = this->create_publisher<cf_msgs::msg::Tdoa>("tdoa_ds", 400);
      |                                                                                ^
In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:363:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<const std::shared_ptr<_Yp>&> std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Yp>&) [with _Yp = _Yp; _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’
  363 |         operator=(const shared_ptr<_Yp>& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:363:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = const std::shared_ptr<rclcpp::Publisher<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void> > >&; _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:363:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >::_Assignable<const std::shared_ptr<_Tp>&> std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >::operator=<_Yp>(const std::shared_ptr<_Tp>&) [with _Yp = rclcpp::Publisher<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void> >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:56:80:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::auto_ptr<_Up> > std::shared_ptr<_Tp>::operator=(std::auto_ptr<_Up>&&) [with _Yp = _Yp; _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’
  374 |         operator=(auto_ptr<_Yp>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:56:80: note:   ‘std::shared_ptr<rclcpp::Publisher<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void> > >’ is not derived from ‘std::auto_ptr<_Up>’
   56 |             pub_uwb = this->create_publisher<cf_msgs::msg::Tdoa>("tdoa_ds", 400);
      |                                                                                ^
In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:391:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::shared_ptr<_Yp> > std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Yp>&&) [with _Yp = _Yp; _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’
  391 |         operator=(shared_ptr<_Yp>&& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:391:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = std::shared_ptr<rclcpp::Publisher<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void> > >; _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:391:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >::_Assignable<std::shared_ptr<_Tp> > std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >::operator=<_Yp>(std::shared_ptr<_Tp>&&) [with _Yp = rclcpp::Publisher<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void> >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:56:80:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note: candidate: ‘template<class _Yp, class _Del> std::shared_ptr<_Tp>::_Assignable<std::unique_ptr<_Up, _Ep> > std::shared_ptr<_Tp>::operator=(std::unique_ptr<_Up, _Ep>&&) [with _Yp = _Yp; _Del = _Del; _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’
  399 |         operator=(unique_ptr<_Yp, _Del>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:56:80: note:   ‘std::shared_ptr<rclcpp::Publisher<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void> > >’ is not derived from ‘std::unique_ptr<_Tp, _Dp>’
   56 |             pub_uwb = this->create_publisher<cf_msgs::msg::Tdoa>("tdoa_ds", 400);
      |                                                                                ^
In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:359:19: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Tp>&) [with _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                   ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:359:29: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Publisher<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void> > >’ to ‘const std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >&’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                             ^~~~~~~~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:7: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Tp>&&) [with _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’
  383 |       operator=(shared_ptr&& __r) noexcept
      |       ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:30: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Publisher<cf_msgs::msg::Tdoa_<std::allocator<void> >, std::allocator<void> > >’ to ‘std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >&&’
  383 |       operator=(shared_ptr&& __r) noexcept
      |                 ~~~~~~~~~~~~~^~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:59:112: error: no match for ‘operator=’ (operand types are ‘rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >::SharedPtr’ {aka ‘std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >’} and ‘std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::RTLSStick_<std::allocator<void> >, isas_msgs::msg::RTLSStick_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > > >’)
   59 | , std::bind(&EstimationInterface::getToaISASCallback, this, std::placeholders::_1));
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:363:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<const std::shared_ptr<_Yp>&> std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Yp>&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  363 |         operator=(const shared_ptr<_Yp>& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:363:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = const std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::RTLSStick_<std::allocator<void> >, isas_msgs::msg::RTLSStick_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > > >&; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:363:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >::_Assignable<const std::shared_ptr<_Tp>&> std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >::operator=<_Yp>(const std::shared_ptr<_Tp>&) [with _Yp = rclcpp::Subscription<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::RTLSStick_<std::allocator<void> >, isas_msgs::msg::RTLSStick_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:59:112:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::auto_ptr<_Up> > std::shared_ptr<_Tp>::operator=(std::auto_ptr<_Up>&&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  374 |         operator=(auto_ptr<_Yp>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:59:112: note:   ‘std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::RTLSStick_<std::allocator<void> >, isas_msgs::msg::RTLSStick_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > > >’ is not derived from ‘std::auto_ptr<_Up>’
   59 | , std::bind(&EstimationInterface::getToaISASCallback, this, std::placeholders::_1));
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:391:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::shared_ptr<_Yp> > std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Yp>&&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  391 |         operator=(shared_ptr<_Yp>&& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:391:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::RTLSStick_<std::allocator<void> >, isas_msgs::msg::RTLSStick_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > > >; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:391:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >::_Assignable<std::shared_ptr<_Tp> > std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >::operator=<_Yp>(std::shared_ptr<_Tp>&&) [with _Yp = rclcpp::Subscription<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::RTLSStick_<std::allocator<void> >, isas_msgs::msg::RTLSStick_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:59:112:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note: candidate: ‘template<class _Yp, class _Del> std::shared_ptr<_Tp>::_Assignable<std::unique_ptr<_Up, _Ep> > std::shared_ptr<_Tp>::operator=(std::unique_ptr<_Up, _Ep>&&) [with _Yp = _Yp; _Del = _Del; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  399 |         operator=(unique_ptr<_Yp, _Del>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:59:112: note:   ‘std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::RTLSStick_<std::allocator<void> >, isas_msgs::msg::RTLSStick_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > > >’ is not derived from ‘std::unique_ptr<_Tp, _Dp>’
   59 | , std::bind(&EstimationInterface::getToaISASCallback, this, std::placeholders::_1));
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:359:19: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Tp>&) [with _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                   ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:359:29: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::RTLSStick_<std::allocator<void> >, isas_msgs::msg::RTLSStick_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > > >’ to ‘const std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >&’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                             ^~~~~~~~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:7: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Tp>&&) [with _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  383 |       operator=(shared_ptr&& __r) noexcept
      |       ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:30: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::RTLSStick_<std::allocator<void> >, isas_msgs::msg::RTLSStick_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > > >’ to ‘std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >&&’
  383 |       operator=(shared_ptr&& __r) noexcept
      |                 ~~~~~~~~~~~~~^~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:60:86: error: no match for ‘operator=’ (operand types are ‘rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >::SharedPtr’ {aka ‘std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >’} and ‘std::shared_ptr<rclcpp::Publisher<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > >’)
   60 |          pub_uwb = this->create_publisher<isas_msgs::msg::RTLSStick>("toa_ds", 400);
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:363:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<const std::shared_ptr<_Yp>&> std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Yp>&) [with _Yp = _Yp; _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’
  363 |         operator=(const shared_ptr<_Yp>& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:363:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = const std::shared_ptr<rclcpp::Publisher<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > >&; _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:363:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >::_Assignable<const std::shared_ptr<_Tp>&> std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >::operator=<_Yp>(const std::shared_ptr<_Tp>&) [with _Yp = rclcpp::Publisher<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:60:86:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::auto_ptr<_Up> > std::shared_ptr<_Tp>::operator=(std::auto_ptr<_Up>&&) [with _Yp = _Yp; _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’
  374 |         operator=(auto_ptr<_Yp>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:60:86: note:   ‘std::shared_ptr<rclcpp::Publisher<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > >’ is not derived from ‘std::auto_ptr<_Up>’
   60 |          pub_uwb = this->create_publisher<isas_msgs::msg::RTLSStick>("toa_ds", 400);
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:391:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::shared_ptr<_Yp> > std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Yp>&&) [with _Yp = _Yp; _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’
  391 |         operator=(shared_ptr<_Yp>&& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:391:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = std::shared_ptr<rclcpp::Publisher<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > >; _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:391:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >::_Assignable<std::shared_ptr<_Tp> > std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >::operator=<_Yp>(std::shared_ptr<_Tp>&&) [with _Yp = rclcpp::Publisher<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:60:86:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note: candidate: ‘template<class _Yp, class _Del> std::shared_ptr<_Tp>::_Assignable<std::unique_ptr<_Up, _Ep> > std::shared_ptr<_Tp>::operator=(std::unique_ptr<_Up, _Ep>&&) [with _Yp = _Yp; _Del = _Del; _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’
  399 |         operator=(unique_ptr<_Yp, _Del>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:60:86: note:   ‘std::shared_ptr<rclcpp::Publisher<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > >’ is not derived from ‘std::unique_ptr<_Tp, _Dp>’
   60 |          pub_uwb = this->create_publisher<isas_msgs::msg::RTLSStick>("toa_ds", 400);
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:359:19: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Tp>&) [with _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                   ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:359:29: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Publisher<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > >’ to ‘const std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >&’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                             ^~~~~~~~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:7: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Tp>&&) [with _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’
  383 |       operator=(shared_ptr&& __r) noexcept
      |       ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:30: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Publisher<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > >’ to ‘std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >&&’
  383 |       operator=(shared_ptr&& __r) noexcept
      |                 ~~~~~~~~~~~~~^~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:69:126: error: no match for ‘operator=’ (operand types are ‘rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >::SharedPtr’ {aka ‘std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >’} and ‘std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::Anchorlist_<std::allocator<void> >, isas_msgs::msg::Anchorlist_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void> > > >’)
   69 | (&EstimationInterface::getAnchorListFromISASCallback, this, std::placeholders::_1));
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:363:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<const std::shared_ptr<_Yp>&> std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Yp>&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  363 |         operator=(const shared_ptr<_Yp>& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:363:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = const std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::Anchorlist_<std::allocator<void> >, isas_msgs::msg::Anchorlist_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void> > > >&; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:363:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >::_Assignable<const std::shared_ptr<_Tp>&> std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >::operator=<_Yp>(const std::shared_ptr<_Tp>&) [with _Yp = rclcpp::Subscription<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::Anchorlist_<std::allocator<void> >, isas_msgs::msg::Anchorlist_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void> > >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:69:126:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::auto_ptr<_Up> > std::shared_ptr<_Tp>::operator=(std::auto_ptr<_Up>&&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  374 |         operator=(auto_ptr<_Yp>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:69:126: note:   ‘std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::Anchorlist_<std::allocator<void> >, isas_msgs::msg::Anchorlist_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void> > > >’ is not derived from ‘std::auto_ptr<_Up>’
   69 | (&EstimationInterface::getAnchorListFromISASCallback, this, std::placeholders::_1));
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:391:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::shared_ptr<_Yp> > std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Yp>&&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  391 |         operator=(shared_ptr<_Yp>&& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:391:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::Anchorlist_<std::allocator<void> >, isas_msgs::msg::Anchorlist_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void> > > >; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:391:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >::_Assignable<std::shared_ptr<_Tp> > std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >::operator=<_Yp>(std::shared_ptr<_Tp>&&) [with _Yp = rclcpp::Subscription<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::Anchorlist_<std::allocator<void> >, isas_msgs::msg::Anchorlist_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void> > >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:69:126:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note: candidate: ‘template<class _Yp, class _Del> std::shared_ptr<_Tp>::_Assignable<std::unique_ptr<_Up, _Ep> > std::shared_ptr<_Tp>::operator=(std::unique_ptr<_Up, _Ep>&&) [with _Yp = _Yp; _Del = _Del; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  399 |         operator=(unique_ptr<_Yp, _Del>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:69:126: note:   ‘std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::Anchorlist_<std::allocator<void> >, isas_msgs::msg::Anchorlist_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void> > > >’ is not derived from ‘std::unique_ptr<_Tp, _Dp>’
   69 | (&EstimationInterface::getAnchorListFromISASCallback, this, std::placeholders::_1));
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:359:19: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Tp>&) [with _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                   ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:359:29: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::Anchorlist_<std::allocator<void> >, isas_msgs::msg::Anchorlist_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void> > > >’ to ‘const std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >&’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                             ^~~~~~~~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:7: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Tp>&&) [with _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  383 |       operator=(shared_ptr&& __r) noexcept
      |       ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:30: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::Anchorlist_<std::allocator<void> >, isas_msgs::msg::Anchorlist_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void> > > >’ to ‘std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >&&’
  383 |       operator=(shared_ptr&& __r) noexcept
      |                 ~~~~~~~~~~~~~^~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:76:92: error: no match for ‘operator=’ (operand types are ‘rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >::SharedPtr’ {aka ‘std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >’} and ‘std::shared_ptr<rclcpp::Publisher<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void> > >’)
   76 | nchor_pub = this->create_publisher<isas_msgs::msg::Anchorlist>("anchor_list", 1000);
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:363:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<const std::shared_ptr<_Yp>&> std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Yp>&) [with _Yp = _Yp; _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’
  363 |         operator=(const shared_ptr<_Yp>& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:363:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = const std::shared_ptr<rclcpp::Publisher<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void> > >&; _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:363:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >::_Assignable<const std::shared_ptr<_Tp>&> std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >::operator=<_Yp>(const std::shared_ptr<_Tp>&) [with _Yp = rclcpp::Publisher<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void> >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:76:92:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::auto_ptr<_Up> > std::shared_ptr<_Tp>::operator=(std::auto_ptr<_Up>&&) [with _Yp = _Yp; _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’
  374 |         operator=(auto_ptr<_Yp>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:76:92: note:   ‘std::shared_ptr<rclcpp::Publisher<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void> > >’ is not derived from ‘std::auto_ptr<_Up>’
   76 | nchor_pub = this->create_publisher<isas_msgs::msg::Anchorlist>("anchor_list", 1000);
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:391:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::shared_ptr<_Yp> > std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Yp>&&) [with _Yp = _Yp; _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’
  391 |         operator=(shared_ptr<_Yp>&& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:391:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = std::shared_ptr<rclcpp::Publisher<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void> > >; _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:391:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >::_Assignable<std::shared_ptr<_Tp> > std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >::operator=<_Yp>(std::shared_ptr<_Tp>&&) [with _Yp = rclcpp::Publisher<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void> >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:76:92:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note: candidate: ‘template<class _Yp, class _Del> std::shared_ptr<_Tp>::_Assignable<std::unique_ptr<_Up, _Ep> > std::shared_ptr<_Tp>::operator=(std::unique_ptr<_Up, _Ep>&&) [with _Yp = _Yp; _Del = _Del; _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’
  399 |         operator=(unique_ptr<_Yp, _Del>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:76:92: note:   ‘std::shared_ptr<rclcpp::Publisher<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void> > >’ is not derived from ‘std::unique_ptr<_Tp, _Dp>’
   76 | nchor_pub = this->create_publisher<isas_msgs::msg::Anchorlist>("anchor_list", 1000);
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:359:19: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Tp>&) [with _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                   ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:359:29: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Publisher<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void> > >’ to ‘const std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >&’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                             ^~~~~~~~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:7: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Tp>&&) [with _Tp = rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >]’
  383 |       operator=(shared_ptr&& __r) noexcept
      |       ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:30: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Publisher<isas_msgs::msg::Anchorlist_<std::allocator<void> >, std::allocator<void> > >’ to ‘std::shared_ptr<rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > > >&&’
  383 |       operator=(shared_ptr&& __r) noexcept
      |                 ~~~~~~~~~~~~~^~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:86:115: error: no match for ‘operator=’ (operand types are ‘rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > >::SharedPtr’ {aka ‘std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > > >’} and ‘std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::TransformStamped_<std::allocator<void> >, std::allocator<void>, geometry_msgs::msg::TransformStamped_<std::allocator<void> >, geometry_msgs::msg::TransformStamped_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<geometry_msgs::msg::TransformStamped_<std::allocator<void> >, std::allocator<void> > > >’)
   86 | td::bind(&EstimationInterface::getGtFromISASCallback, this, std::placeholders::_1));
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:363:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<const std::shared_ptr<_Yp>&> std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Yp>&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > >]’
  363 |         operator=(const shared_ptr<_Yp>& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:363:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = const std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::TransformStamped_<std::allocator<void> >, std::allocator<void>, geometry_msgs::msg::TransformStamped_<std::allocator<void> >, geometry_msgs::msg::TransformStamped_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<geometry_msgs::msg::TransformStamped_<std::allocator<void> >, std::allocator<void> > > >&; _Tp = rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:363:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > > >::_Assignable<const std::shared_ptr<_Tp>&> std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > > >::operator=<_Yp>(const std::shared_ptr<_Tp>&) [with _Yp = rclcpp::Subscription<geometry_msgs::msg::TransformStamped_<std::allocator<void> >, std::allocator<void>, geometry_msgs::msg::TransformStamped_<std::allocator<void> >, geometry_msgs::msg::TransformStamped_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<geometry_msgs::msg::TransformStamped_<std::allocator<void> >, std::allocator<void> > >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:86:115:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::auto_ptr<_Up> > std::shared_ptr<_Tp>::operator=(std::auto_ptr<_Up>&&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > >]’
  374 |         operator=(auto_ptr<_Yp>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:86:115: note:   ‘std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::TransformStamped_<std::allocator<void> >, std::allocator<void>, geometry_msgs::msg::TransformStamped_<std::allocator<void> >, geometry_msgs::msg::TransformStamped_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<geometry_msgs::msg::TransformStamped_<std::allocator<void> >, std::allocator<void> > > >’ is not derived from ‘std::auto_ptr<_Up>’
   86 | td::bind(&EstimationInterface::getGtFromISASCallback, this, std::placeholders::_1));
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:391:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::shared_ptr<_Yp> > std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Yp>&&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > >]’
  391 |         operator=(shared_ptr<_Yp>&& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:391:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::TransformStamped_<std::allocator<void> >, std::allocator<void>, geometry_msgs::msg::TransformStamped_<std::allocator<void> >, geometry_msgs::msg::TransformStamped_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<geometry_msgs::msg::TransformStamped_<std::allocator<void> >, std::allocator<void> > > >; _Tp = rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:391:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > > >::_Assignable<std::shared_ptr<_Tp> > std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > > >::operator=<_Yp>(std::shared_ptr<_Tp>&&) [with _Yp = rclcpp::Subscription<geometry_msgs::msg::TransformStamped_<std::allocator<void> >, std::allocator<void>, geometry_msgs::msg::TransformStamped_<std::allocator<void> >, geometry_msgs::msg::TransformStamped_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<geometry_msgs::msg::TransformStamped_<std::allocator<void> >, std::allocator<void> > >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:86:115:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note: candidate: ‘template<class _Yp, class _Del> std::shared_ptr<_Tp>::_Assignable<std::unique_ptr<_Up, _Ep> > std::shared_ptr<_Tp>::operator=(std::unique_ptr<_Up, _Ep>&&) [with _Yp = _Yp; _Del = _Del; _Tp = rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > >]’
  399 |         operator=(unique_ptr<_Yp, _Del>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:86:115: note:   ‘std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::TransformStamped_<std::allocator<void> >, std::allocator<void>, geometry_msgs::msg::TransformStamped_<std::allocator<void> >, geometry_msgs::msg::TransformStamped_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<geometry_msgs::msg::TransformStamped_<std::allocator<void> >, std::allocator<void> > > >’ is not derived from ‘std::unique_ptr<_Tp, _Dp>’
   86 | td::bind(&EstimationInterface::getGtFromISASCallback, this, std::placeholders::_1));
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:359:19: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Tp>&) [with _Tp = rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > >]’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                   ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:359:29: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::TransformStamped_<std::allocator<void> >, std::allocator<void>, geometry_msgs::msg::TransformStamped_<std::allocator<void> >, geometry_msgs::msg::TransformStamped_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<geometry_msgs::msg::TransformStamped_<std::allocator<void> >, std::allocator<void> > > >’ to ‘const std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > > >&’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                             ^~~~~~~~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:7: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Tp>&&) [with _Tp = rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > >]’
  383 |       operator=(shared_ptr&& __r) noexcept
      |       ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:30: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::TransformStamped_<std::allocator<void> >, std::allocator<void>, geometry_msgs::msg::TransformStamped_<std::allocator<void> >, geometry_msgs::msg::TransformStamped_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<geometry_msgs::msg::TransformStamped_<std::allocator<void> >, std::allocator<void> > > >’ to ‘std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > > >&&’
  383 |       operator=(shared_ptr&& __r) noexcept
      |                 ~~~~~~~~~~~~~^~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:89:115: error: no match for ‘operator=’ (operand types are ‘rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > >::SharedPtr’ {aka ‘std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > > >’} and ‘std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, std::allocator<void>, geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, std::allocator<void> > > >’)
   89 | td::bind(&EstimationInterface::getGtFromUTILCallback, this, std::placeholders::_1));
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:363:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<const std::shared_ptr<_Yp>&> std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Yp>&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > >]’
  363 |         operator=(const shared_ptr<_Yp>& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:363:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = const std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, std::allocator<void>, geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, std::allocator<void> > > >&; _Tp = rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:363:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > > >::_Assignable<const std::shared_ptr<_Tp>&> std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > > >::operator=<_Yp>(const std::shared_ptr<_Tp>&) [with _Yp = rclcpp::Subscription<geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, std::allocator<void>, geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, std::allocator<void> > >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:89:115:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::auto_ptr<_Up> > std::shared_ptr<_Tp>::operator=(std::auto_ptr<_Up>&&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > >]’
  374 |         operator=(auto_ptr<_Yp>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:89:115: note:   ‘std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, std::allocator<void>, geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, std::allocator<void> > > >’ is not derived from ‘std::auto_ptr<_Up>’
   89 | td::bind(&EstimationInterface::getGtFromUTILCallback, this, std::placeholders::_1));
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:391:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::shared_ptr<_Yp> > std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Yp>&&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > >]’
  391 |         operator=(shared_ptr<_Yp>&& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:391:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, std::allocator<void>, geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, std::allocator<void> > > >; _Tp = rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:391:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > > >::_Assignable<std::shared_ptr<_Tp> > std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > > >::operator=<_Yp>(std::shared_ptr<_Tp>&&) [with _Yp = rclcpp::Subscription<geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, std::allocator<void>, geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, std::allocator<void> > >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:89:115:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note: candidate: ‘template<class _Yp, class _Del> std::shared_ptr<_Tp>::_Assignable<std::unique_ptr<_Up, _Ep> > std::shared_ptr<_Tp>::operator=(std::unique_ptr<_Up, _Ep>&&) [with _Yp = _Yp; _Del = _Del; _Tp = rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > >]’
  399 |         operator=(unique_ptr<_Yp, _Del>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:89:115: note:   ‘std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, std::allocator<void>, geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, std::allocator<void> > > >’ is not derived from ‘std::unique_ptr<_Tp, _Dp>’
   89 | td::bind(&EstimationInterface::getGtFromUTILCallback, this, std::placeholders::_1));
      |                                                                                   ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:359:19: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Tp>&) [with _Tp = rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > >]’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                   ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:359:29: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, std::allocator<void>, geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, std::allocator<void> > > >’ to ‘const std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > > >&’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                             ^~~~~~~~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:7: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Tp>&&) [with _Tp = rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > >]’
  383 |       operator=(shared_ptr&& __r) noexcept
      |       ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:30: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, std::allocator<void>, geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<geometry_msgs::msg::PoseWithCovarianceStamped_<std::allocator<void> >, std::allocator<void> > > >’ to ‘std::shared_ptr<rclcpp::Subscription<geometry_msgs::msg::PoseStamped_<std::allocator<void> > > >&&’
  383 |       operator=(shared_ptr&& __r) noexcept
      |                 ~~~~~~~~~~~~~^~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:96:123: error: no match for ‘operator=’ (operand types are ‘rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > >::SharedPtr’ {aka ‘std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > > >’} and ‘std::shared_ptr<rclcpp::Subscription<sfuise_msgs::msg::Calib_<std::allocator<void> >, std::allocator<void>, sfuise_msgs::msg::Calib_<std::allocator<void> >, sfuise_msgs::msg::Calib_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<sfuise_msgs::msg::Calib_<std::allocator<void> >, std::allocator<void> > > >’)
   96 | bind(&EstimationInterface::getCalibCallback, this, std::placeholders::_1));// 订阅系统标定数据
      |                                                                          ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:363:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<const std::shared_ptr<_Yp>&> std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Yp>&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > >]’
  363 |         operator=(const shared_ptr<_Yp>& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:363:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = const std::shared_ptr<rclcpp::Subscription<sfuise_msgs::msg::Calib_<std::allocator<void> >, std::allocator<void>, sfuise_msgs::msg::Calib_<std::allocator<void> >, sfuise_msgs::msg::Calib_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<sfuise_msgs::msg::Calib_<std::allocator<void> >, std::allocator<void> > > >&; _Tp = rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:363:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > > >::_Assignable<const std::shared_ptr<_Tp>&> std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > > >::operator=<_Yp>(const std::shared_ptr<_Tp>&) [with _Yp = rclcpp::Subscription<sfuise_msgs::msg::Calib_<std::allocator<void> >, std::allocator<void>, sfuise_msgs::msg::Calib_<std::allocator<void> >, sfuise_msgs::msg::Calib_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<sfuise_msgs::msg::Calib_<std::allocator<void> >, std::allocator<void> > >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:96:123:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::auto_ptr<_Up> > std::shared_ptr<_Tp>::operator=(std::auto_ptr<_Up>&&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > >]’
  374 |         operator=(auto_ptr<_Yp>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:96:123: note:   ‘std::shared_ptr<rclcpp::Subscription<sfuise_msgs::msg::Calib_<std::allocator<void> >, std::allocator<void>, sfuise_msgs::msg::Calib_<std::allocator<void> >, sfuise_msgs::msg::Calib_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<sfuise_msgs::msg::Calib_<std::allocator<void> >, std::allocator<void> > > >’ is not derived from ‘std::auto_ptr<_Up>’
   96 | bind(&EstimationInterface::getCalibCallback, this, std::placeholders::_1));// 订阅系统标定数据
      |                                                                          ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:391:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::shared_ptr<_Yp> > std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Yp>&&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > >]’
  391 |         operator=(shared_ptr<_Yp>&& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:391:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = std::shared_ptr<rclcpp::Subscription<sfuise_msgs::msg::Calib_<std::allocator<void> >, std::allocator<void>, sfuise_msgs::msg::Calib_<std::allocator<void> >, sfuise_msgs::msg::Calib_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<sfuise_msgs::msg::Calib_<std::allocator<void> >, std::allocator<void> > > >; _Tp = rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:391:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > > >::_Assignable<std::shared_ptr<_Tp> > std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > > >::operator=<_Yp>(std::shared_ptr<_Tp>&&) [with _Yp = rclcpp::Subscription<sfuise_msgs::msg::Calib_<std::allocator<void> >, std::allocator<void>, sfuise_msgs::msg::Calib_<std::allocator<void> >, sfuise_msgs::msg::Calib_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<sfuise_msgs::msg::Calib_<std::allocator<void> >, std::allocator<void> > >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:96:123:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note: candidate: ‘template<class _Yp, class _Del> std::shared_ptr<_Tp>::_Assignable<std::unique_ptr<_Up, _Ep> > std::shared_ptr<_Tp>::operator=(std::unique_ptr<_Up, _Ep>&&) [with _Yp = _Yp; _Del = _Del; _Tp = rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > >]’
  399 |         operator=(unique_ptr<_Yp, _Del>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:96:123: note:   ‘std::shared_ptr<rclcpp::Subscription<sfuise_msgs::msg::Calib_<std::allocator<void> >, std::allocator<void>, sfuise_msgs::msg::Calib_<std::allocator<void> >, sfuise_msgs::msg::Calib_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<sfuise_msgs::msg::Calib_<std::allocator<void> >, std::allocator<void> > > >’ is not derived from ‘std::unique_ptr<_Tp, _Dp>’
   96 | bind(&EstimationInterface::getCalibCallback, this, std::placeholders::_1));// 订阅系统标定数据
      |                                                                          ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:359:19: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Tp>&) [with _Tp = rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > >]’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                   ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:359:29: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Subscription<sfuise_msgs::msg::Calib_<std::allocator<void> >, std::allocator<void>, sfuise_msgs::msg::Calib_<std::allocator<void> >, sfuise_msgs::msg::Calib_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<sfuise_msgs::msg::Calib_<std::allocator<void> >, std::allocator<void> > > >’ to ‘const std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > > >&’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                             ^~~~~~~~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:7: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Tp>&&) [with _Tp = rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > >]’
  383 |       operator=(shared_ptr&& __r) noexcept
      |       ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:30: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Subscription<sfuise_msgs::msg::Calib_<std::allocator<void> >, std::allocator<void>, sfuise_msgs::msg::Calib_<std::allocator<void> >, sfuise_msgs::msg::Calib_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<sfuise_msgs::msg::Calib_<std::allocator<void> >, std::allocator<void> > > >’ to ‘std::shared_ptr<rclcpp::Subscription<std_msgs::msg::Bool_<std::allocator<void> > > >&&’
  383 |       operator=(shared_ptr&& __r) noexcept
      |                 ~~~~~~~~~~~~~^~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:98:122: error: no match for ‘operator=’ (operand types are ‘rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >::SharedPtr’ {aka ‘std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >’} and ‘std::shared_ptr<rclcpp::Subscription<sfuise_msgs::msg::Estimate_<std::allocator<void> >, std::allocator<void>, sfuise_msgs::msg::Estimate_<std::allocator<void> >, sfuise_msgs::msg::Estimate_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<sfuise_msgs::msg::Estimate_<std::allocator<void> >, std::allocator<void> > > >’)
   98 | ::bind(&EstimationInterface::getEstCallback, this, std::placeholders::_1));// 订阅估计窗口数据
      |                                                                          ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:363:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<const std::shared_ptr<_Yp>&> std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Yp>&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  363 |         operator=(const shared_ptr<_Yp>& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:363:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = const std::shared_ptr<rclcpp::Subscription<sfuise_msgs::msg::Estimate_<std::allocator<void> >, std::allocator<void>, sfuise_msgs::msg::Estimate_<std::allocator<void> >, sfuise_msgs::msg::Estimate_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<sfuise_msgs::msg::Estimate_<std::allocator<void> >, std::allocator<void> > > >&; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:363:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >::_Assignable<const std::shared_ptr<_Tp>&> std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >::operator=<_Yp>(const std::shared_ptr<_Tp>&) [with _Yp = rclcpp::Subscription<sfuise_msgs::msg::Estimate_<std::allocator<void> >, std::allocator<void>, sfuise_msgs::msg::Estimate_<std::allocator<void> >, sfuise_msgs::msg::Estimate_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<sfuise_msgs::msg::Estimate_<std::allocator<void> >, std::allocator<void> > >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:98:122:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::auto_ptr<_Up> > std::shared_ptr<_Tp>::operator=(std::auto_ptr<_Up>&&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  374 |         operator=(auto_ptr<_Yp>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:98:122: note:   ‘std::shared_ptr<rclcpp::Subscription<sfuise_msgs::msg::Estimate_<std::allocator<void> >, std::allocator<void>, sfuise_msgs::msg::Estimate_<std::allocator<void> >, sfuise_msgs::msg::Estimate_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<sfuise_msgs::msg::Estimate_<std::allocator<void> >, std::allocator<void> > > >’ is not derived from ‘std::auto_ptr<_Up>’
   98 | ::bind(&EstimationInterface::getEstCallback, this, std::placeholders::_1));// 订阅估计窗口数据
      |                                                                          ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:391:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::shared_ptr<_Yp> > std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Yp>&&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  391 |         operator=(shared_ptr<_Yp>&& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:391:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = std::shared_ptr<rclcpp::Subscription<sfuise_msgs::msg::Estimate_<std::allocator<void> >, std::allocator<void>, sfuise_msgs::msg::Estimate_<std::allocator<void> >, sfuise_msgs::msg::Estimate_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<sfuise_msgs::msg::Estimate_<std::allocator<void> >, std::allocator<void> > > >; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:391:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >::_Assignable<std::shared_ptr<_Tp> > std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >::operator=<_Yp>(std::shared_ptr<_Tp>&&) [with _Yp = rclcpp::Subscription<sfuise_msgs::msg::Estimate_<std::allocator<void> >, std::allocator<void>, sfuise_msgs::msg::Estimate_<std::allocator<void> >, sfuise_msgs::msg::Estimate_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<sfuise_msgs::msg::Estimate_<std::allocator<void> >, std::allocator<void> > >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:98:122:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note: candidate: ‘template<class _Yp, class _Del> std::shared_ptr<_Tp>::_Assignable<std::unique_ptr<_Up, _Ep> > std::shared_ptr<_Tp>::operator=(std::unique_ptr<_Up, _Ep>&&) [with _Yp = _Yp; _Del = _Del; _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  399 |         operator=(unique_ptr<_Yp, _Del>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:98:122: note:   ‘std::shared_ptr<rclcpp::Subscription<sfuise_msgs::msg::Estimate_<std::allocator<void> >, std::allocator<void>, sfuise_msgs::msg::Estimate_<std::allocator<void> >, sfuise_msgs::msg::Estimate_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<sfuise_msgs::msg::Estimate_<std::allocator<void> >, std::allocator<void> > > >’ is not derived from ‘std::unique_ptr<_Tp, _Dp>’
   98 | ::bind(&EstimationInterface::getEstCallback, this, std::placeholders::_1));// 订阅估计窗口数据
      |                                                                          ^

In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:359:19: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Tp>&) [with _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                   ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:359:29: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Subscription<sfuise_msgs::msg::Estimate_<std::allocator<void> >, std::allocator<void>, sfuise_msgs::msg::Estimate_<std::allocator<void> >, sfuise_msgs::msg::Estimate_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<sfuise_msgs::msg::Estimate_<std::allocator<void> >, std::allocator<void> > > >’ to ‘const std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >&’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                             ^~~~~~~~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:7: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Tp>&&) [with _Tp = rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > >]’
  383 |       operator=(shared_ptr&& __r) noexcept
      |       ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:30: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Subscription<sfuise_msgs::msg::Estimate_<std::allocator<void> >, std::allocator<void>, sfuise_msgs::msg::Estimate_<std::allocator<void> >, sfuise_msgs::msg::Estimate_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<sfuise_msgs::msg::Estimate_<std::allocator<void> >, std::allocator<void> > > >’ to ‘std::shared_ptr<rclcpp::Subscription<std_msgs::msg::String_<std::allocator<void> > > >&&’
  383 |       operator=(shared_ptr&& __r) noexcept
      |                 ~~~~~~~~~~~~~^~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp: In member function ‘void EstimationInterface::getToaISASCallback(isas_msgs::msg::RTLSStick_<std::allocator<void> >::SharedPtr)’:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:308:29: error: no matching function for call to ‘rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >::publish(std::__shared_ptr_access<isas_msgs::msg::RTLSStick_<std::allocator<void> >, __gnu_cxx::_S_atomic, false, false>::element_type&)’
  308 |             pub_uwb->publish(*uwb_msg); // 发布UWB数据
      |             ~~~~~~~~~~~~~~~~^~~~~~~~~~
In file included from /opt/ros/humble/include/rclcpp/rclcpp/topic_statistics/subscription_topic_statistics.hpp:31,
                 from /opt/ros/humble/include/rclcpp/rclcpp/subscription.hpp:50,
                 from /opt/ros/humble/include/rclcpp/rclcpp/any_executable.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/memory_strategy.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/memory_strategies.hpp:18,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executor_options.hpp:20,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executor.hpp:37,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors/multi_threaded_executor.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors.hpp:21,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:155,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:251:3: note: candidate: ‘template<class T> std::enable_if_t<(rosidl_generator_traits::is_message<T>::value && std::is_same<T, typename rclcpp::TypeAdapter<MessageT>::ros_message_type>::value)> rclcpp::Publisher<MessageT, AllocatorT>::publish(std::unique_ptr<T, typename std::conditional<std::is_same<typename std::allocator_traits<typename std::allocator_traits<_Allocator>::rebind_traits<typename rclcpp::TypeAdapter<MessageT, void, void>::ros_message_type>::allocator_type>::rebind_alloc<typename rclcpp::TypeAdapter<MessageT, void, void>::ros_message_type>, std::allocator<typename rclcpp::TypeAdapter<MessageT>::ros_message_type> >::value, std::default_delete<typename rclcpp::TypeAdapter<MessageT>::ros_message_type>, rclcpp::allocator::AllocatorDeleter<typename std::allocator_traits<_Allocator>::rebind_traits<typename rclcpp::TypeAdapter<MessageT, void, void>::ros_message_type>::allocator_type> >::type>) [with T = T; MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>]’
  251 |   publish(std::unique_ptr<T, ROSMessageTypeDeleter> msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:251:3: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:308:29: note:   ‘isas_msgs::msg::RTLSStick_<std::allocator<void> >’ is not derived from ‘std::unique_ptr<T, std::default_delete<std_msgs::msg::String_<std::allocator<void> > > >’
  308 |             pub_uwb->publish(*uwb_msg); // 发布UWB数据
      |             ~~~~~~~~~~~~~~~~^~~~~~~~~~
In file included from /opt/ros/humble/include/rclcpp/rclcpp/topic_statistics/subscription_topic_statistics.hpp:31,
                 from /opt/ros/humble/include/rclcpp/rclcpp/subscription.hpp:50,
                 from /opt/ros/humble/include/rclcpp/rclcpp/any_executable.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/memory_strategy.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/memory_strategies.hpp:18,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executor_options.hpp:20,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executor.hpp:37,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors/multi_threaded_executor.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors.hpp:21,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:155,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:292:3: note: candidate: ‘template<class T> std::enable_if_t<(rosidl_generator_traits::is_message<T>::value && std::is_same<T, typename rclcpp::TypeAdapter<MessageT>::ros_message_type>::value)> rclcpp::Publisher<MessageT, AllocatorT>::publish(const T&) [with T = T; MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>]’
  292 |   publish(const T & msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:292:3: note:   template argument deduction/substitution failed:
In file included from /usr/include/c++/11/bits/move.h:57,
                 from /usr/include/c++/11/bits/stl_pair.h:59,
                 from /usr/include/c++/11/bits/stl_algobase.h:64,
                 from /usr/include/c++/11/memory:63,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/usr/include/c++/11/type_traits: In substitution of ‘template<bool _Cond, class _Tp> using enable_if_t = typename std::enable_if::type [with bool _Cond = false; _Tp = void]’:
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:292:3:   required by substitution of ‘template<class T> std::enable_if_t<(rosidl_generator_traits::is_message<T>::value && std::is_same<T, std_msgs::msg::String_<std::allocator<void> > >::value), void> rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >::publish<T>(const T&) [with T = isas_msgs::msg::RTLSStick_<std::allocator<void> >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:308:29:   required from here
/usr/include/c++/11/type_traits:2579:11: error: no type named ‘type’ in ‘struct std::enable_if<false, void>’
 2579 |     using enable_if_t = typename enable_if<_Cond, _Tp>::type;
      |           ^~~~~~~~~~~
In file included from /opt/ros/humble/include/rclcpp/rclcpp/topic_statistics/subscription_topic_statistics.hpp:31,
                 from /opt/ros/humble/include/rclcpp/rclcpp/subscription.hpp:50,
                 from /opt/ros/humble/include/rclcpp/rclcpp/any_executable.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/memory_strategy.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/memory_strategies.hpp:18,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executor_options.hpp:20,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executor.hpp:37,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors/multi_threaded_executor.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors.hpp:21,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:155,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:322:3: note: candidate: ‘template<class T> std::enable_if_t<(typename rclcpp::TypeAdapter<MessageT>::is_specialized::value && std::is_same<T, typename rclcpp::TypeAdapter<MessageT>::custom_type>::value)> rclcpp::Publisher<MessageT, AllocatorT>::publish(std::unique_ptr<T, typename std::conditional<std::is_same<typename std::allocator_traits<typename std::allocator_traits<_Allocator>::rebind_traits<typename rclcpp::TypeAdapter<MessageT, void, void>::custom_type>::allocator_type>::rebind_alloc<typename rclcpp::TypeAdapter<MessageT, void, void>::custom_type>, std::allocator<typename rclcpp::TypeAdapter<MessageT>::custom_type> >::value, std::default_delete<typename rclcpp::TypeAdapter<MessageT>::custom_type>, rclcpp::allocator::AllocatorDeleter<typename std::allocator_traits<_Allocator>::rebind_traits<typename rclcpp::TypeAdapter<MessageT, void, void>::custom_type>::allocator_type> >::type>) [with T = T; MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>]’
  322 |   publish(std::unique_ptr<T, PublishedTypeDeleter> msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:322:3: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:308:29: note:   ‘isas_msgs::msg::RTLSStick_<std::allocator<void> >’ is not derived from ‘std::unique_ptr<T, std::default_delete<std_msgs::msg::String_<std::allocator<void> > > >’
  308 |             pub_uwb->publish(*uwb_msg); // 发布UWB数据
      |             ~~~~~~~~~~~~~~~~^~~~~~~~~~
In file included from /opt/ros/humble/include/rclcpp/rclcpp/topic_statistics/subscription_topic_statistics.hpp:31,
                 from /opt/ros/humble/include/rclcpp/rclcpp/subscription.hpp:50,
                 from /opt/ros/humble/include/rclcpp/rclcpp/any_executable.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/memory_strategy.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/memory_strategies.hpp:18,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executor_options.hpp:20,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executor.hpp:37,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors/multi_threaded_executor.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors.hpp:21,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:155,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:364:3: note: candidate: ‘template<class T> std::enable_if_t<(typename rclcpp::TypeAdapter<MessageT>::is_specialized::value && std::is_same<T, typename rclcpp::TypeAdapter<MessageT>::custom_type>::value)> rclcpp::Publisher<MessageT, AllocatorT>::publish(const T&) [with T = T; MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>]’
  364 |   publish(const T & msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:364:3: note:   template argument deduction/substitution failed:
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:383:3: note: candidate: ‘void rclcpp::Publisher<MessageT, AllocatorT>::publish(const rcl_serialized_message_t&) [with MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>; rcl_serialized_message_t = rcutils_uint8_array_s]’
  383 |   publish(const rcl_serialized_message_t & serialized_msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:383:44: note:   no known conversion for argument 1 from ‘std::__shared_ptr_access<isas_msgs::msg::RTLSStick_<std::allocator<void> >, __gnu_cxx::_S_atomic, false, false>::element_type’ {aka ‘isas_msgs::msg::RTLSStick_<std::allocator<void> >’} to ‘const rcl_serialized_message_t&’ {aka ‘const rcutils_uint8_array_s&’}
  383 |   publish(const rcl_serialized_message_t & serialized_msg)
      |           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:389:3: note: candidate: ‘void rclcpp::Publisher<MessageT, AllocatorT>::publish(const rclcpp::SerializedMessage&) [with MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>]’
  389 |   publish(const SerializedMessage & serialized_msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:389:37: note:   no known conversion for argument 1 from ‘std::__shared_ptr_access<isas_msgs::msg::RTLSStick_<std::allocator<void> >, __gnu_cxx::_S_atomic, false, false>::element_type’ {aka ‘isas_msgs::msg::RTLSStick_<std::allocator<void> >’} to ‘const rclcpp::SerializedMessage&’
  389 |   publish(const SerializedMessage & serialized_msg)
      |           ~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:403:3: note: candidate: ‘void rclcpp::Publisher<MessageT, AllocatorT>::publish(rclcpp::LoanedMessage<typename rclcpp::TypeAdapter<MessageT>::ros_message_type, AllocatorT>&&) [with MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>; typename rclcpp::TypeAdapter<MessageT>::ros_message_type = std_msgs::msg::String_<std::allocator<void> >]’
  403 |   publish(rclcpp::LoanedMessage<ROSMessageType, AllocatorT> && loaned_msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:403:64: note:   no known conversion for argument 1 from ‘std::__shared_ptr_access<isas_msgs::msg::RTLSStick_<std::allocator<void> >, __gnu_cxx::_S_atomic, false, false>::element_type’ {aka ‘isas_msgs::msg::RTLSStick_<std::allocator<void> >’} to ‘rclcpp::LoanedMessage<std_msgs::msg::String_<std::allocator<void> >, std::allocator<void> >&&’
  403 |   publish(rclcpp::LoanedMessage<ROSMessageType, AllocatorT> && loaned_msg)
      |           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp: In member function ‘void EstimationInterface::getTdoaUTILCallback(cf_msgs::msg::Tdoa_<std::allocator<void> >::SharedPtr)’:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:321:42: error: no matching function for call to ‘rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >::publish(std::__shared_ptr_access<cf_msgs::msg::Tdoa_<std::allocator<void> >, __gnu_cxx::_S_atomic, false, false>::element_type&)’
  321 |             if (pub_uwb) pub_uwb->publish(*msg); // 发布TDOA数据
      |                          ~~~~~~~~~~~~~~~~^~~~~~
In file included from /opt/ros/humble/include/rclcpp/rclcpp/topic_statistics/subscription_topic_statistics.hpp:31,
                 from /opt/ros/humble/include/rclcpp/rclcpp/subscription.hpp:50,
                 from /opt/ros/humble/include/rclcpp/rclcpp/any_executable.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/memory_strategy.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/memory_strategies.hpp:18,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executor_options.hpp:20,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executor.hpp:37,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors/multi_threaded_executor.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors.hpp:21,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:155,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:251:3: note: candidate: ‘template<class T> std::enable_if_t<(rosidl_generator_traits::is_message<T>::value && std::is_same<T, typename rclcpp::TypeAdapter<MessageT>::ros_message_type>::value)> rclcpp::Publisher<MessageT, AllocatorT>::publish(std::unique_ptr<T, typename std::conditional<std::is_same<typename std::allocator_traits<typename std::allocator_traits<_Allocator>::rebind_traits<typename rclcpp::TypeAdapter<MessageT, void, void>::ros_message_type>::allocator_type>::rebind_alloc<typename rclcpp::TypeAdapter<MessageT, void, void>::ros_message_type>, std::allocator<typename rclcpp::TypeAdapter<MessageT>::ros_message_type> >::value, std::default_delete<typename rclcpp::TypeAdapter<MessageT>::ros_message_type>, rclcpp::allocator::AllocatorDeleter<typename std::allocator_traits<_Allocator>::rebind_traits<typename rclcpp::TypeAdapter<MessageT, void, void>::ros_message_type>::allocator_type> >::type>) [with T = T; MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>]’
  251 |   publish(std::unique_ptr<T, ROSMessageTypeDeleter> msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:251:3: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:321:42: note:   ‘cf_msgs::msg::Tdoa_<std::allocator<void> >’ is not derived from ‘std::unique_ptr<T, std::default_delete<std_msgs::msg::String_<std::allocator<void> > > >’
  321 |             if (pub_uwb) pub_uwb->publish(*msg); // 发布TDOA数据
      |                          ~~~~~~~~~~~~~~~~^~~~~~
In file included from /opt/ros/humble/include/rclcpp/rclcpp/topic_statistics/subscription_topic_statistics.hpp:31,
                 from /opt/ros/humble/include/rclcpp/rclcpp/subscription.hpp:50,
                 from /opt/ros/humble/include/rclcpp/rclcpp/any_executable.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/memory_strategy.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/memory_strategies.hpp:18,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executor_options.hpp:20,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executor.hpp:37,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors/multi_threaded_executor.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors.hpp:21,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:155,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:292:3: note: candidate: ‘template<class T> std::enable_if_t<(rosidl_generator_traits::is_message<T>::value && std::is_same<T, typename rclcpp::TypeAdapter<MessageT>::ros_message_type>::value)> rclcpp::Publisher<MessageT, AllocatorT>::publish(const T&) [with T = T; MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>]’
  292 |   publish(const T & msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:292:3: note:   template argument deduction/substitution failed:
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:322:3: note: candidate: ‘template<class T> std::enable_if_t<(typename rclcpp::TypeAdapter<MessageT>::is_specialized::value && std::is_same<T, typename rclcpp::TypeAdapter<MessageT>::custom_type>::value)> rclcpp::Publisher<MessageT, AllocatorT>::publish(std::unique_ptr<T, typename std::conditional<std::is_same<typename std::allocator_traits<typename std::allocator_traits<_Allocator>::rebind_traits<typename rclcpp::TypeAdapter<MessageT, void, void>::custom_type>::allocator_type>::rebind_alloc<typename rclcpp::TypeAdapter<MessageT, void, void>::custom_type>, std::allocator<typename rclcpp::TypeAdapter<MessageT>::custom_type> >::value, std::default_delete<typename rclcpp::TypeAdapter<MessageT>::custom_type>, rclcpp::allocator::AllocatorDeleter<typename std::allocator_traits<_Allocator>::rebind_traits<typename rclcpp::TypeAdapter<MessageT, void, void>::custom_type>::allocator_type> >::type>) [with T = T; MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>]’
  322 |   publish(std::unique_ptr<T, PublishedTypeDeleter> msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:322:3: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:321:42: note:   ‘cf_msgs::msg::Tdoa_<std::allocator<void> >’ is not derived from ‘std::unique_ptr<T, std::default_delete<std_msgs::msg::String_<std::allocator<void> > > >’
  321 |             if (pub_uwb) pub_uwb->publish(*msg); // 发布TDOA数据
      |                          ~~~~~~~~~~~~~~~~^~~~~~
In file included from /opt/ros/humble/include/rclcpp/rclcpp/topic_statistics/subscription_topic_statistics.hpp:31,
                 from /opt/ros/humble/include/rclcpp/rclcpp/subscription.hpp:50,
                 from /opt/ros/humble/include/rclcpp/rclcpp/any_executable.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/memory_strategy.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/memory_strategies.hpp:18,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executor_options.hpp:20,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executor.hpp:37,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors/multi_threaded_executor.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors.hpp:21,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:155,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:364:3: note: candidate: ‘template<class T> std::enable_if_t<(typename rclcpp::TypeAdapter<MessageT>::is_specialized::value && std::is_same<T, typename rclcpp::TypeAdapter<MessageT>::custom_type>::value)> rclcpp::Publisher<MessageT, AllocatorT>::publish(const T&) [with T = T; MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>]’
  364 |   publish(const T & msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:364:3: note:   template argument deduction/substitution failed:
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:383:3: note: candidate: ‘void rclcpp::Publisher<MessageT, AllocatorT>::publish(const rcl_serialized_message_t&) [with MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>; rcl_serialized_message_t = rcutils_uint8_array_s]’
  383 |   publish(const rcl_serialized_message_t & serialized_msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:383:44: note:   no known conversion for argument 1 from ‘std::__shared_ptr_access<cf_msgs::msg::Tdoa_<std::allocator<void> >, __gnu_cxx::_S_atomic, false, false>::element_type’ {aka ‘cf_msgs::msg::Tdoa_<std::allocator<void> >’} to ‘const rcl_serialized_message_t&’ {aka ‘const rcutils_uint8_array_s&’}
  383 |   publish(const rcl_serialized_message_t & serialized_msg)
      |           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:389:3: note: candidate: ‘void rclcpp::Publisher<MessageT, AllocatorT>::publish(const rclcpp::SerializedMessage&) [with MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>]’
  389 |   publish(const SerializedMessage & serialized_msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:389:37: note:   no known conversion for argument 1 from ‘std::__shared_ptr_access<cf_msgs::msg::Tdoa_<std::allocator<void> >, __gnu_cxx::_S_atomic, false, false>::element_type’ {aka ‘cf_msgs::msg::Tdoa_<std::allocator<void> >’} to ‘const rclcpp::SerializedMessage&’
  389 |   publish(const SerializedMessage & serialized_msg)
      |           ~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:403:3: note: candidate: ‘void rclcpp::Publisher<MessageT, AllocatorT>::publish(rclcpp::LoanedMessage<typename rclcpp::TypeAdapter<MessageT>::ros_message_type, AllocatorT>&&) [with MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>; typename rclcpp::TypeAdapter<MessageT>::ros_message_type = std_msgs::msg::String_<std::allocator<void> >]’
  403 |   publish(rclcpp::LoanedMessage<ROSMessageType, AllocatorT> && loaned_msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:403:64: note:   no known conversion for argument 1 from ‘std::__shared_ptr_access<cf_msgs::msg::Tdoa_<std::allocator<void> >, __gnu_cxx::_S_atomic, false, false>::element_type’ {aka ‘cf_msgs::msg::Tdoa_<std::allocator<void> >’} to ‘rclcpp::LoanedMessage<std_msgs::msg::String_<std::allocator<void> >, std::allocator<void> >&&’
  403 |   publish(rclcpp::LoanedMessage<ROSMessageType, AllocatorT> && loaned_msg)
      |           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp: In member function ‘void EstimationInterface::publishAnchor()’:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:415:28: error: no matching function for call to ‘rclcpp::Publisher<std_msgs::msg::String_<std::allocator<void> > >::publish(isas_msgs::msg::Anchorlist_<std::allocator<void> >&)’
  415 |         anchor_pub->publish(anchor_list_msg);
      |         ~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~
In file included from /opt/ros/humble/include/rclcpp/rclcpp/topic_statistics/subscription_topic_statistics.hpp:31,
                 from /opt/ros/humble/include/rclcpp/rclcpp/subscription.hpp:50,
                 from /opt/ros/humble/include/rclcpp/rclcpp/any_executable.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/memory_strategy.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/memory_strategies.hpp:18,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executor_options.hpp:20,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executor.hpp:37,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors/multi_threaded_executor.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors.hpp:21,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:155,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:251:3: note: candidate: ‘template<class T> std::enable_if_t<(rosidl_generator_traits::is_message<T>::value && std::is_same<T, typename rclcpp::TypeAdapter<MessageT>::ros_message_type>::value)> rclcpp::Publisher<MessageT, AllocatorT>::publish(std::unique_ptr<T, typename std::conditional<std::is_same<typename std::allocator_traits<typename std::allocator_traits<_Allocator>::rebind_traits<typename rclcpp::TypeAdapter<MessageT, void, void>::ros_message_type>::allocator_type>::rebind_alloc<typename rclcpp::TypeAdapter<MessageT, void, void>::ros_message_type>, std::allocator<typename rclcpp::TypeAdapter<MessageT>::ros_message_type> >::value, std::default_delete<typename rclcpp::TypeAdapter<MessageT>::ros_message_type>, rclcpp::allocator::AllocatorDeleter<typename std::allocator_traits<_Allocator>::rebind_traits<typename rclcpp::TypeAdapter<MessageT, void, void>::ros_message_type>::allocator_type> >::type>) [with T = T; MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>]’
  251 |   publish(std::unique_ptr<T, ROSMessageTypeDeleter> msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:251:3: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:415:28: note:   ‘isas_msgs::msg::Anchorlist_<std::allocator<void> >’ is not derived from ‘std::unique_ptr<T, std::default_delete<std_msgs::msg::String_<std::allocator<void> > > >’
  415 |         anchor_pub->publish(anchor_list_msg);
      |         ~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~
In file included from /opt/ros/humble/include/rclcpp/rclcpp/topic_statistics/subscription_topic_statistics.hpp:31,
                 from /opt/ros/humble/include/rclcpp/rclcpp/subscription.hpp:50,
                 from /opt/ros/humble/include/rclcpp/rclcpp/any_executable.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/memory_strategy.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/memory_strategies.hpp:18,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executor_options.hpp:20,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executor.hpp:37,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors/multi_threaded_executor.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors.hpp:21,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:155,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:292:3: note: candidate: ‘template<class T> std::enable_if_t<(rosidl_generator_traits::is_message<T>::value && std::is_same<T, typename rclcpp::TypeAdapter<MessageT>::ros_message_type>::value)> rclcpp::Publisher<MessageT, AllocatorT>::publish(const T&) [with T = T; MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>]’
  292 |   publish(const T & msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:292:3: note:   template argument deduction/substitution failed:
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:322:3: note: candidate: ‘template<class T> std::enable_if_t<(typename rclcpp::TypeAdapter<MessageT>::is_specialized::value && std::is_same<T, typename rclcpp::TypeAdapter<MessageT>::custom_type>::value)> rclcpp::Publisher<MessageT, AllocatorT>::publish(std::unique_ptr<T, typename std::conditional<std::is_same<typename std::allocator_traits<typename std::allocator_traits<_Allocator>::rebind_traits<typename rclcpp::TypeAdapter<MessageT, void, void>::custom_type>::allocator_type>::rebind_alloc<typename rclcpp::TypeAdapter<MessageT, void, void>::custom_type>, std::allocator<typename rclcpp::TypeAdapter<MessageT>::custom_type> >::value, std::default_delete<typename rclcpp::TypeAdapter<MessageT>::custom_type>, rclcpp::allocator::AllocatorDeleter<typename std::allocator_traits<_Allocator>::rebind_traits<typename rclcpp::TypeAdapter<MessageT, void, void>::custom_type>::allocator_type> >::type>) [with T = T; MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>]’
  322 |   publish(std::unique_ptr<T, PublishedTypeDeleter> msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:322:3: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:415:28: note:   ‘isas_msgs::msg::Anchorlist_<std::allocator<void> >’ is not derived from ‘std::unique_ptr<T, std::default_delete<std_msgs::msg::String_<std::allocator<void> > > >’
  415 |         anchor_pub->publish(anchor_list_msg);
      |         ~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~
In file included from /opt/ros/humble/include/rclcpp/rclcpp/topic_statistics/subscription_topic_statistics.hpp:31,
                 from /opt/ros/humble/include/rclcpp/rclcpp/subscription.hpp:50,
                 from /opt/ros/humble/include/rclcpp/rclcpp/any_executable.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/memory_strategy.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/memory_strategies.hpp:18,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executor_options.hpp:20,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executor.hpp:37,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors/multi_threaded_executor.hpp:25,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors.hpp:21,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:155,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/EstimationInterface.cpp:1:
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:364:3: note: candidate: ‘template<class T> std::enable_if_t<(typename rclcpp::TypeAdapter<MessageT>::is_specialized::value && std::is_same<T, typename rclcpp::TypeAdapter<MessageT>::custom_type>::value)> rclcpp::Publisher<MessageT, AllocatorT>::publish(const T&) [with T = T; MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>]’
  364 |   publish(const T & msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:364:3: note:   template argument deduction/substitution failed:
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:383:3: note: candidate: ‘void rclcpp::Publisher<MessageT, AllocatorT>::publish(const rcl_serialized_message_t&) [with MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>; rcl_serialized_message_t = rcutils_uint8_array_s]’
  383 |   publish(const rcl_serialized_message_t & serialized_msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:383:44: note:   no known conversion for argument 1 from ‘isas_msgs::msg::Anchorlist_<std::allocator<void> >’ to ‘const rcl_serialized_message_t&’ {aka ‘const rcutils_uint8_array_s&’}
  383 |   publish(const rcl_serialized_message_t & serialized_msg)
      |           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:389:3: note: candidate: ‘void rclcpp::Publisher<MessageT, AllocatorT>::publish(const rclcpp::SerializedMessage&) [with MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>]’
  389 |   publish(const SerializedMessage & serialized_msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:389:37: note:   no known conversion for argument 1 from ‘isas_msgs::msg::Anchorlist_<std::allocator<void> >’ to ‘const rclcpp::SerializedMessage&’
  389 |   publish(const SerializedMessage & serialized_msg)
      |           ~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:403:3: note: candidate: ‘void rclcpp::Publisher<MessageT, AllocatorT>::publish(rclcpp::LoanedMessage<typename rclcpp::TypeAdapter<MessageT>::ros_message_type, AllocatorT>&&) [with MessageT = std_msgs::msg::String_<std::allocator<void> >; AllocatorT = std::allocator<void>; typename rclcpp::TypeAdapter<MessageT>::ros_message_type = std_msgs::msg::String_<std::allocator<void> >]’
  403 |   publish(rclcpp::LoanedMessage<ROSMessageType, AllocatorT> && loaned_msg)
      |   ^~~~~~~
/opt/ros/humble/include/rclcpp/rclcpp/publisher.hpp:403:64: note:   no known conversion for argument 1 from ‘isas_msgs::msg::Anchorlist_<std::allocator<void> >’ to ‘rclcpp::LoanedMessage<std_msgs::msg::String_<std::allocator<void> >, std::allocator<void> >&&’
  403 |   publish(rclcpp::LoanedMessage<ROSMessageType, AllocatorT> && loaned_msg)
      |           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp: In constructor ‘SplineFusion::SplineFusion(std::shared_ptr<rclcpp::Node>)’:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:25:5: error: no matching function for call to ‘rclcpp::Node::Node()’
   25 |     {
      |     ^
In file included from /opt/ros/humble/include/rclcpp/rclcpp/executors/single_threaded_executor.hpp:28,
                 from /opt/ros/humble/include/rclcpp/rclcpp/executors.hpp:22,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:155,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:1:
/opt/ros/humble/include/rclcpp/rclcpp/node.hpp:1294:3: note: candidate: ‘rclcpp::Node::Node(const rclcpp::Node&, const string&)’
 1294 |   Node(
      |   ^~~~
/opt/ros/humble/include/rclcpp/rclcpp/node.hpp:1294:3: note:   candidate expects 2 arguments, 0 provided
/opt/ros/humble/include/rclcpp/rclcpp/node.hpp:101:12: note: candidate: ‘rclcpp::Node::Node(const string&, const string&, const rclcpp::NodeOptions&)’
  101 |   explicit Node(
      |            ^~~~
/opt/ros/humble/include/rclcpp/rclcpp/node.hpp:101:12: note:   candidate expects 3 arguments, 0 provided
/opt/ros/humble/include/rclcpp/rclcpp/node.hpp:89:12: note: candidate: ‘rclcpp::Node::Node(const string&, const rclcpp::NodeOptions&)’
   89 |   explicit Node(
      |            ^~~~
/opt/ros/humble/include/rclcpp/rclcpp/node.hpp:89:12: note:   candidate expects 2 arguments, 0 provided
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:29:23: error: ‘INITIAL’ was not declared in this scope
   29 |         solver_flag = INITIAL;  // 初始化求解器标志
      |                       ^~~~~~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:45:136: error: no match for ‘operator=’ (operand types are ‘rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> > >::SharedPtr’ {aka ‘std::shared_ptr<rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> > > >’} and ‘std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::RTLSStick_<std::allocator<void> >, isas_msgs::msg::RTLSStick_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > > >’)
   45 |                 "/EstimationInterface/toa_ds", rclcpp::QoS(1000), std::bind(&SplineFusion::getToaCallback, this, std::placeholders::_1));
      |                                                                                                                                        ^
In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:363:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<const std::shared_ptr<_Yp>&> std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Yp>&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> > >]’
  363 |         operator=(const shared_ptr<_Yp>& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:363:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = const std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::RTLSStick_<std::allocator<void> >, isas_msgs::msg::RTLSStick_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > > >&; _Tp = rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:363:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> > > >::_Assignable<const std::shared_ptr<_Tp>&> std::shared_ptr<rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> > > >::operator=<_Yp>(const std::shared_ptr<_Tp>&) [with _Yp = rclcpp::Subscription<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::RTLSStick_<std::allocator<void> >, isas_msgs::msg::RTLSStick_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:45:136:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::auto_ptr<_Up> > std::shared_ptr<_Tp>::operator=(std::auto_ptr<_Up>&&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> > >]’
  374 |         operator=(auto_ptr<_Yp>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:374:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:45:136: note:   ‘std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::RTLSStick_<std::allocator<void> >, isas_msgs::msg::RTLSStick_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > > >’ is not derived from ‘std::auto_ptr<_Up>’
   45 |                 "/EstimationInterface/toa_ds", rclcpp::QoS(1000), std::bind(&SplineFusion::getToaCallback, this, std::placeholders::_1));
      |                                                                                                                                        ^
In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:391:9: note: candidate: ‘template<class _Yp> std::shared_ptr<_Tp>::_Assignable<std::shared_ptr<_Yp> > std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Yp>&&) [with _Yp = _Yp; _Tp = rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> > >]’
  391 |         operator=(shared_ptr<_Yp>&& __r) noexcept
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:391:9: note:   template argument deduction/substitution failed:
/usr/include/c++/11/bits/shared_ptr.h: In substitution of ‘template<class _Tp> template<class _Arg> using _Assignable = typename std::enable_if<std::is_assignable<std::__shared_ptr<_Tp>&, _Arg>::value, std::shared_ptr<_Tp>&>::type [with _Arg = std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::RTLSStick_<std::allocator<void> >, isas_msgs::msg::RTLSStick_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > > >; _Tp = rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> > >]’:
/usr/include/c++/11/bits/shared_ptr.h:391:2:   required by substitution of ‘template<class _Yp> std::shared_ptr<rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> > > >::_Assignable<std::shared_ptr<_Tp> > std::shared_ptr<rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> > > >::operator=<_Yp>(std::shared_ptr<_Tp>&&) [with _Yp = rclcpp::Subscription<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::RTLSStick_<std::allocator<void> >, isas_msgs::msg::RTLSStick_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > >]’
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:45:136:   required from here
/usr/include/c++/11/bits/shared_ptr.h:130:15: error: no type named ‘type’ in ‘struct std::enable_if<false, std::shared_ptr<rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> > > >&>’
  130 |         using _Assignable = typename enable_if<
      |               ^~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note: candidate: ‘template<class _Yp, class _Del> std::shared_ptr<_Tp>::_Assignable<std::unique_ptr<_Up, _Ep> > std::shared_ptr<_Tp>::operator=(std::unique_ptr<_Up, _Ep>&&) [with _Yp = _Yp; _Del = _Del; _Tp = rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> > >]’
  399 |         operator=(unique_ptr<_Yp, _Del>&& __r)
      |         ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:399:9: note:   template argument deduction/substitution failed:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:45:136: note:   ‘std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::RTLSStick_<std::allocator<void> >, isas_msgs::msg::RTLSStick_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > > >’ is not derived from ‘std::unique_ptr<_Tp, _Dp>’
   45 |                 "/EstimationInterface/toa_ds", rclcpp::QoS(1000), std::bind(&SplineFusion::getToaCallback, this, std::placeholders::_1));
      |                                                                                                                                        ^
In file included from /usr/include/c++/11/memory:77,
                 from /opt/ros/humble/include/rclcpp/rclcpp/rclcpp.hpp:153,
                 from /home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:1:
/usr/include/c++/11/bits/shared_ptr.h:359:19: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(const std::shared_ptr<_Tp>&) [with _Tp = rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> > >]’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                   ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:359:29: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::RTLSStick_<std::allocator<void> >, isas_msgs::msg::RTLSStick_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > > >’ to ‘const std::shared_ptr<rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> > > >&’
  359 |       shared_ptr& operator=(const shared_ptr&) noexcept = default;
      |                             ^~~~~~~~~~~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:7: note: candidate: ‘std::shared_ptr<_Tp>& std::shared_ptr<_Tp>::operator=(std::shared_ptr<_Tp>&&) [with _Tp = rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> > >]’
  383 |       operator=(shared_ptr&& __r) noexcept
      |       ^~~~~~~~
/usr/include/c++/11/bits/shared_ptr.h:383:30: note:   no known conversion for argument 1 from ‘std::shared_ptr<rclcpp::Subscription<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void>, isas_msgs::msg::RTLSStick_<std::allocator<void> >, isas_msgs::msg::RTLSStick_<std::allocator<void> >, rclcpp::message_memory_strategy::MessageMemoryStrategy<isas_msgs::msg::RTLSStick_<std::allocator<void> >, std::allocator<void> > > >’ to ‘std::shared_ptr<rclcpp::Subscription<cf_msgs::msg::Tdoa_<std::allocator<void> > > >&&’
  383 |       operator=(shared_ptr&& __r) noexcept
      |                 ~~~~~~~~~~~~~^~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp: In member function ‘void SplineFusion::run()’:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:68:39: error: ‘node’ was not declared in this scope; did you mean ‘Node’?
   68 |         rclcpp::Time t_window_start = node->get_clock()->now();  // 获取当前时间
      |                                       ^~~~
      |                                       Node
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:95:17: error: ‘pub_calib_’ was not declared in this scope; did you mean ‘pub_calib’?
   95 |                 pub_calib_->publish(calib_msg);  // 发布校准消息
      |                 ^~~~~~~~~~
      |                 pub_calib
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:100:36: error: ‘INITIAL’ was not declared in this scope
  100 |                 if (solver_flag == INITIAL) {  // 如果求解器标志为初始状态
      |                                    ^~~~~~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:101:35: error: ‘FULLSIZE’ was not declared in this scope
  101 |                     solver_flag = FULLSIZE;  // 设置为全尺寸状态
      |                                   ^~~~~~~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:110:59: error: ‘INITIAL’ was not declared in this scope
  110 |             est_msg.if_full_window.data = (solver_flag != INITIAL);  // 设置是否为全窗口
      |                                                           ^~~~~~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:113:13: error: ‘pub_est_’ was not declared in this scope; did you mean ‘pub_est’?
  113 |             pub_est_->publish(est_msg);  // 发布估计消息
      |             ^~~~~~~~
      |             pub_est
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:116:32: error: ‘FULLSIZE’ was not declared in this scope
  116 |             if (solver_flag == FULLSIZE) {
      |                                ^~~~~~~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp: In member function ‘bool SplineFusion::initialization()’:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:329:33: error: ‘next_knot_TimeNs’ was not declared in this scope; did you mean ‘next_knot_time_ns’?
  329 |                     integration(next_knot_TimeNs, q_ini, pos_ini); // 执行积分
      |                                 ^~~~~~~~~~~~~~~~
      |                                 next_knot_time_ns
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:332:55: error: ‘next_knot_TimeNs’ was not declared in this scope; did you mean ‘next_knot_time_ns’?
  332 |                         pos_ini = tdoaMultilateration(next_knot_TimeNs * NS_TO_S); // 执行TDOA多边定位
      |                                                       ^~~~~~~~~~~~~~~~
      |                                                       next_knot_time_ns
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:341:17: error: ‘next_knot_TimeNs’ was not declared in this scope; did you mean ‘next_knot_time_ns’?
  341 |                 next_knot_TimeNs += dt_ns; // 更新下一个节点时间
      |                 ^~~~~~~~~~~~~~~~
      |                 next_knot_time_ns
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:351:17: error: ‘pub_start_time_’ was not declared in this scope; did you mean ‘pub_start_time’?
  351 |                 pub_start_time_->publish(start_time); // 发布启动时间
      |                 ^~~~~~~~~~~~~~~
      |                 pub_start_time
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:374:21: error: ‘next_knot_TimeNs’ was not declared in this scope; did you mean ‘next_knot_time_ns’?
  374 |                     next_knot_TimeNs += dt_ns; // 更新下一个节点时间
      |                     ^~~~~~~~~~~~~~~~
      |                     next_knot_time_ns
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp: In member function ‘Eigen::Vector3d SplineFusion::tdoaMultilateration(double) const’:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:406:14: error: ‘set_origin’ was not declared in this scope; did you mean ‘setlogin’?
  406 |         if (!set_origin) { // 如果未设置原点
      |              ^~~~~~~~~~
      |              setlogin
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp: In member function ‘bool SplineFusion::optimization()’:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:446:32: error: ‘INITIAL’ was not declared in this scope
  446 |             if (solver_flag == INITIAL && spline_local.numKnots() < int(param.reject_uwb_window_width * window_size))
      |                                ^~~~~~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:470:28: error: ‘INITIAL’ was not declared in this scope
  470 |         if (solver_flag == INITIAL) {
      |                            ^~~~~~~
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp: In member function ‘bool SplineFusion::setParameters()’:
/home/dsh/Documents/work_logs/code/SFUISE/sfuise_ws/src/sfuise/src/SplineFusion.cpp:499:9: error: ‘next_knot_TimeNs’ was not declared in this scope; did you mean ‘next_knot_time_ns’?
  499 |         next_knot_TimeNs = bag_start_time; // 设置下一个节点时间
      |         ^~~~~~~~~~~~~~~~
      |         next_knot_time_ns
gmake[2]: *** [CMakeFiles/EstimationInterface.dir/build.make:76: CMakeFiles/EstimationInterface.dir/src/EstimationInterface.cpp.o] Error 1
gmake[1]: *** [CMakeFiles/Makefile2:139: CMakeFiles/EstimationInterface.dir/all] Error 2
gmake[1]: *** Waiting for unfinished jobs....
gmake[2]: *** [CMakeFiles/SplineFusion.dir/build.make:76: CMakeFiles/SplineFusion.dir/src/SplineFusion.cpp.o] Error 1
gmake[1]: *** [CMakeFiles/Makefile2:165: CMakeFiles/SplineFusion.dir/all] Error 2
gmake: *** [Makefile:146: all] Error 2
---
Failed   <<< sfuise [26.6s, exited with code 2]
                                 
Summary: 0 packages finished [27.0s]
  1 package failed: sfuise
  1 package had stderr output: sfuise
dsh@dsh-Precision-5680:~/Documents/work_logs/code/SFUISE/sfuise_ws$ ^C
dsh@dsh-Precision-5680:~/Documents/work_logs/code/SFUISE/sfuise_ws$ 

