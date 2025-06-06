// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from sfuise_msgs:msg/Spline.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "sfuise_msgs/msg/detail/spline__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace sfuise_msgs
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void Spline_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) sfuise_msgs::msg::Spline(_init);
}

void Spline_fini_function(void * message_memory)
{
  auto typed_message = static_cast<sfuise_msgs::msg::Spline *>(message_memory);
  typed_message->~Spline();
}

size_t size_function__Spline__knots(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<sfuise_msgs::msg::Knot> *>(untyped_member);
  return member->size();
}

const void * get_const_function__Spline__knots(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<sfuise_msgs::msg::Knot> *>(untyped_member);
  return &member[index];
}

void * get_function__Spline__knots(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<sfuise_msgs::msg::Knot> *>(untyped_member);
  return &member[index];
}

void fetch_function__Spline__knots(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const sfuise_msgs::msg::Knot *>(
    get_const_function__Spline__knots(untyped_member, index));
  auto & value = *reinterpret_cast<sfuise_msgs::msg::Knot *>(untyped_value);
  value = item;
}

void assign_function__Spline__knots(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<sfuise_msgs::msg::Knot *>(
    get_function__Spline__knots(untyped_member, index));
  const auto & value = *reinterpret_cast<const sfuise_msgs::msg::Knot *>(untyped_value);
  item = value;
}

void resize_function__Spline__knots(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<sfuise_msgs::msg::Knot> *>(untyped_member);
  member->resize(size);
}

size_t size_function__Spline__idles(const void * untyped_member)
{
  const auto * member = reinterpret_cast<const std::vector<sfuise_msgs::msg::Knot> *>(untyped_member);
  return member->size();
}

const void * get_const_function__Spline__idles(const void * untyped_member, size_t index)
{
  const auto & member =
    *reinterpret_cast<const std::vector<sfuise_msgs::msg::Knot> *>(untyped_member);
  return &member[index];
}

void * get_function__Spline__idles(void * untyped_member, size_t index)
{
  auto & member =
    *reinterpret_cast<std::vector<sfuise_msgs::msg::Knot> *>(untyped_member);
  return &member[index];
}

void fetch_function__Spline__idles(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const auto & item = *reinterpret_cast<const sfuise_msgs::msg::Knot *>(
    get_const_function__Spline__idles(untyped_member, index));
  auto & value = *reinterpret_cast<sfuise_msgs::msg::Knot *>(untyped_value);
  value = item;
}

void assign_function__Spline__idles(
  void * untyped_member, size_t index, const void * untyped_value)
{
  auto & item = *reinterpret_cast<sfuise_msgs::msg::Knot *>(
    get_function__Spline__idles(untyped_member, index));
  const auto & value = *reinterpret_cast<const sfuise_msgs::msg::Knot *>(untyped_value);
  item = value;
}

void resize_function__Spline__idles(void * untyped_member, size_t size)
{
  auto * member =
    reinterpret_cast<std::vector<sfuise_msgs::msg::Knot> *>(untyped_member);
  member->resize(size);
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember Spline_message_member_array[5] = {
  {
    "start_idx",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_UINT64,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sfuise_msgs::msg::Spline, start_idx),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "dt",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sfuise_msgs::msg::Spline, dt),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "start_t",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_INT64,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sfuise_msgs::msg::Spline, start_t),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr,  // fetch(index, &value) function pointer
    nullptr,  // assign(index, value) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "knots",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<sfuise_msgs::msg::Knot>(),  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sfuise_msgs::msg::Spline, knots),  // bytes offset in struct
    nullptr,  // default value
    size_function__Spline__knots,  // size() function pointer
    get_const_function__Spline__knots,  // get_const(index) function pointer
    get_function__Spline__knots,  // get(index) function pointer
    fetch_function__Spline__knots,  // fetch(index, &value) function pointer
    assign_function__Spline__knots,  // assign(index, value) function pointer
    resize_function__Spline__knots  // resize(index) function pointer
  },
  {
    "idles",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    ::rosidl_typesupport_introspection_cpp::get_message_type_support_handle<sfuise_msgs::msg::Knot>(),  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(sfuise_msgs::msg::Spline, idles),  // bytes offset in struct
    nullptr,  // default value
    size_function__Spline__idles,  // size() function pointer
    get_const_function__Spline__idles,  // get_const(index) function pointer
    get_function__Spline__idles,  // get(index) function pointer
    fetch_function__Spline__idles,  // fetch(index, &value) function pointer
    assign_function__Spline__idles,  // assign(index, value) function pointer
    resize_function__Spline__idles  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers Spline_message_members = {
  "sfuise_msgs::msg",  // message namespace
  "Spline",  // message name
  5,  // number of fields
  sizeof(sfuise_msgs::msg::Spline),
  Spline_message_member_array,  // message members
  Spline_init_function,  // function to initialize message memory (memory has to be allocated)
  Spline_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t Spline_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &Spline_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace sfuise_msgs


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<sfuise_msgs::msg::Spline>()
{
  return &::sfuise_msgs::msg::rosidl_typesupport_introspection_cpp::Spline_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, sfuise_msgs, msg, Spline)() {
  return &::sfuise_msgs::msg::rosidl_typesupport_introspection_cpp::Spline_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
