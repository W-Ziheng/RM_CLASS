# 指定CMake的最低版本要求
cmake_minimum_required(VERSION 3.11)

# 定义项目名称
project(CLASS_2)

# 添加头文件目录
include_directories(./includes)

aux_source_directory(./tools TOOLS)

# 添加可执行文件，并指定源文件
add_executable(cmake_exe src/cmake.cpp ${TOOLS})

message(${TOOLS})