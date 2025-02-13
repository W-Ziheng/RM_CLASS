cmake_minimum_required(VERSION 3.11)

project(Task_2)

include_directories(./includes)

aux_source_directory(./tools TOOLS)
# 保存至TOOLS变量

add_executable(cmake_exe src/cmake.cpp ${TOOLS} )

#查看一下变量里面有什么
message(${TOOLS})

