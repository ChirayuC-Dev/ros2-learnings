cmake_minimum_required(VERSION 3.5)
project(ros2_basics)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

install(
  DIRECTORY ros2_basics
  DESTINATION lib/python3.10.12/site-packages
)

ament_package()
