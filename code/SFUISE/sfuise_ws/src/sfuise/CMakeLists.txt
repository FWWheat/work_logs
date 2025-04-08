cmake_minimum_required(VERSION 3.8)
project(sfuise)  

# 设置C++标准
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
add_compile_options(-O3)

# 配置CMake模块路径（用于FindSuiteSparse）
list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}/cmake_modules")

# 查找依赖包
# ROS2核心依赖
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
find_package(nav_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(visualization_msgs REQUIRED)


# 自定义消息依赖
find_package(cf_msgs REQUIRED)
find_package(isas_msgs REQUIRED)
find_package(sfuise_msgs REQUIRED)

# 第三方数学库
find_package(Eigen3 REQUIRED)
find_package(SuiteSparse REQUIRED)  # 依赖stuise/cmake_modules/FindSuiteSparse.cmake


include_directories(
  include
  ${EIGEN3_INCLUDE_DIRS}
  ${BOOST_INCLUDE_DIR}
  ${SUITESPARSE_INCLUDE_DIRS}
)

add_executable(EstimationInterface src/EstimationInterface.cpp)
ament_target_dependencies(EstimationInterface
  rclcpp
  std_msgs
  sensor_msgs
  geometry_msgs
  nav_msgs
  cf_msgs
  isas_msgs
  sfuise_msgs
  visualization_msgs
)

add_executable(SplineFusion src/SplineFusion.cpp)
ament_target_dependencies(SplineFusion
  rclcpp
  std_msgs
  sensor_msgs
  geometry_msgs
  nav_msgs
  cf_msgs
  isas_msgs
  sfuise_msgs
  visualization_msgs
)

install(TARGETS
  EstimationInterface
  SplineFusion
  DESTINATION lib/${PROJECT_NAME})

# 查找 SuiteSparse 库
find_package(SuiteSparse REQUIRED COMPONENTS cholmod)

# 添加头文件路径
include_directories(${SUITESPARSE_INCLUDE_DIRS})

# 链接到目标（如 SplineFusion）
target_link_libraries(SplineFusion
  ${SUITESPARSE_LIBRARIES}
)
# Install launch files.
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()