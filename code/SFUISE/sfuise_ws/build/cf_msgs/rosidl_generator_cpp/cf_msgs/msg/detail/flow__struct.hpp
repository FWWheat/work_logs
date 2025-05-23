// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from cf_msgs:msg/Flow.idl
// generated code does not contain a copyright notice

#ifndef CF_MSGS__MSG__DETAIL__FLOW__STRUCT_HPP_
#define CF_MSGS__MSG__DETAIL__FLOW__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__cf_msgs__msg__Flow __attribute__((deprecated))
#else
# define DEPRECATED__cf_msgs__msg__Flow __declspec(deprecated)
#endif

namespace cf_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Flow_
{
  using Type = Flow_<ContainerAllocator>;

  explicit Flow_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->delta_x = 0l;
      this->delta_y = 0l;
    }
  }

  explicit Flow_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->delta_x = 0l;
      this->delta_y = 0l;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _delta_x_type =
    int32_t;
  _delta_x_type delta_x;
  using _delta_y_type =
    int32_t;
  _delta_y_type delta_y;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__delta_x(
    const int32_t & _arg)
  {
    this->delta_x = _arg;
    return *this;
  }
  Type & set__delta_y(
    const int32_t & _arg)
  {
    this->delta_y = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    cf_msgs::msg::Flow_<ContainerAllocator> *;
  using ConstRawPtr =
    const cf_msgs::msg::Flow_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<cf_msgs::msg::Flow_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<cf_msgs::msg::Flow_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      cf_msgs::msg::Flow_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<cf_msgs::msg::Flow_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      cf_msgs::msg::Flow_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<cf_msgs::msg::Flow_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<cf_msgs::msg::Flow_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<cf_msgs::msg::Flow_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__cf_msgs__msg__Flow
    std::shared_ptr<cf_msgs::msg::Flow_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__cf_msgs__msg__Flow
    std::shared_ptr<cf_msgs::msg::Flow_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Flow_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->delta_x != other.delta_x) {
      return false;
    }
    if (this->delta_y != other.delta_y) {
      return false;
    }
    return true;
  }
  bool operator!=(const Flow_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Flow_

// alias to use template instance with default allocator
using Flow =
  cf_msgs::msg::Flow_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace cf_msgs

#endif  // CF_MSGS__MSG__DETAIL__FLOW__STRUCT_HPP_
