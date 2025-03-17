# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_Publisher2Listener_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED Publisher2Listener_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(Publisher2Listener_FOUND FALSE)
  elseif(NOT Publisher2Listener_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(Publisher2Listener_FOUND FALSE)
  endif()
  return()
endif()
set(_Publisher2Listener_CONFIG_INCLUDED TRUE)

# output package information
if(NOT Publisher2Listener_FIND_QUIETLY)
  message(STATUS "Found Publisher2Listener: 0.0.0 (${Publisher2Listener_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'Publisher2Listener' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${Publisher2Listener_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(Publisher2Listener_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${Publisher2Listener_DIR}/${_extra}")
endforeach()
