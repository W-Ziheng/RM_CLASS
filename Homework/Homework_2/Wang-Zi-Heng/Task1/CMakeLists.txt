cmake_minimum_required(VERSION 3.11)

project(Task1)

include_directories(./includes)

aux_source_directory(./tools TOOLS)


### 1 ###
add_executable(cmake_exe src/cmake.cpp tools/hello.cpp)


### 2 ###
add_executable(cmake_exe src/cmake.cpp ${TOOLS})

message(${TOOLS})


