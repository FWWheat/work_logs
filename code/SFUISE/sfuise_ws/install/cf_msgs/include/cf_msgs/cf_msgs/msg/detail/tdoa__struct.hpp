// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from cf_msgs:msg/Tdoa.idl
// generated code does not contain a copyright notice

#ifndef CF_MSGS__MSG__DETAIL__TDOA__STRUCT_HPP_
#define CF_MSGS__MSG__DETAIL__TDOA__STRUCT_HPP_

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
# define DEPRECATED__cf_msgs__msg__Tdoa __attribute__((deprecated))
#else
# define DEPRECATED__cf_msgs__msg__Tdoa __declspec(deprecated)
#endif

namespace cf_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct Tdoa_
{
  using Type = Tdoa_<ContainerAllocator>;

  explicit Tdoa_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id_a = 0l;
      this->id_b = 0l;
      this->data = 0.0f;
    }
  }

  explicit Tdoa_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->id_a = 0l;
      this->id_b = 0l;
      this->data = 0.0f;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _id_a_type =
    int32_t;
  _id_a_type id_a;
  using _id_b_type =
    int32_t;
  _id_b_type id_b;
  using _data_type =
    float;
  _data_type data;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__id_a(
    const int32_t & _arg)
  {
    this->id_a = _arg;
    return *this;
  }
  Type & set__id_b(
    const int32_t & _arg)
  {
    this->id_b = _arg;
    return *this;
  }
  Type & set__data(
    const float & _arg)
  {
    this->data = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    cf_msgs::msg::Tdoa_<ContainerAllocator> *;
  using ConstRawPtr =
    const cf_msgs::msg::Tdoa_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<cf_msgs::msg::Tdoa_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<cf_msgs::msg::Tdoa_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      cf_msgs::msg::Tdoa_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<cf_msgs::msg::Tdoa_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      cf_msgs::msg::Tdoa_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<cf_msgs::msg::Tdoa_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<cf_msgs::msg::Tdoa_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<cf_msgs::msg::Tdoa_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__cf_msgs__msg__Tdoa
    std::shared_ptr<cf_msgs::msg::Tdoa_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__cf_msgs__msg__Tdoa
    std::shared_ptr<cf_msgs::msg::Tdoa_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const Tdoa_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->id_a != other.id_a) {
      return false;
    }
    if (this->id_b != other.id_b) {
      return false;
    }
    if (this->data != other.data) {
      return false;
    }
    return true;
  }
  bool operator!=(const Tdoa_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct Tdoa_

// alias to use template instance with default allocator
using Tdoa =
  cf_msgs::msg::Tdoa_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace cf_msgs

#endif  // CF_MSGS__MSG__DETAIL__TDOA__STRUCT_HPP_
