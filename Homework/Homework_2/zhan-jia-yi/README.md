# zhan-jia-yi Homework_2

## 项目概述

本项目是算法组培训的第二次作业，包含了两个任务：Task1和Task2。Task1是一个简单的C++程序，用于打印"Hello RM!"。Task2是一个ROS2包，包含发布者和监听者节点，用于在ROS2环境中进行消息发布和订阅。

## 目录结构

├── 阐述.md
├── README.md
├── ros2.md
├── Task1
│   └── CLASS_2
│       ├── build
│       │   ├── CMakeCache.txt
│       │   ├── cmake_exe
│       │   ├── CMakeFiles
│       │   │   ├── 3.22.1
│       │   │   │   ├── CMakeCCompiler.cmake
│       │   │   │   ├── CMakeCXXCompiler.cmake
│       │   │   │   ├── CMakeDetermineCompilerABI_C.bin
│       │   │   │   ├── CMakeDetermineCompilerABI_CXX.bin
│       │   │   │   ├── CMakeSystem.cmake
│       │   │   │   ├── CompilerIdC
│       │   │   │   │   ├── a.out
│       │   │   │   │   ├── CMakeCCompilerId.c
│       │   │   │   │   └── tmp
│       │   │   │   └── CompilerIdCXX
│       │   │   │       ├── a.out
│       │   │   │       ├── CMakeCXXCompilerId.cpp
│       │   │   │       └── tmp
│       │   │   ├── cmake.check_cache
│       │   │   ├── CMakeDirectoryInformation.cmake
│       │   │   ├── cmake_exe.dir
│       │   │   │   ├── build.make
│       │   │   │   ├── cmake_clean.cmake
│       │   │   │   ├── compiler_depend.make
│       │   │   │   ├── compiler_depend.ts
│       │   │   │   ├── DependInfo.cmake
│       │   │   │   ├── depend.make
│       │   │   │   ├── flags.make
│       │   │   │   ├── link.txt
│       │   │   │   ├── progress.make
│       │   │   │   ├── src
│       │   │   │   │   ├── cmake.cpp.o
│       │   │   │   │   └── cmake.cpp.o.d
│       │   │   │   └── tools
│       │   │   │       ├── hello.cpp.o
│       │   │   │       └── hello.cpp.o.d
│       │   │   ├── CMakeOutput.log
│       │   │   ├── CMakeTmp
│       │   │   ├── Makefile2
│       │   │   ├── Makefile.cmake
│       │   │   ├── progress.marks
│       │   │   └── TargetDirectories.txt
│       │   ├── cmake_install.cmake
│       │   └── Makefile
│       ├── cmake_exe
│       ├── CMakeLists.txt
│       ├── includes
│       │   └── hello.hpp
│       ├── src
│       │   └── cmake.cpp
│       └── tools
│           └── hello.cpp
└── Task2
    ├── hw
    │   ├── build
    │   │   ├── COLCON_IGNORE
    │   │   └── Publisher2Listener
    │   │       ├── ament_cmake_core
    │   │       │   ├── package.cmake
    │   │       │   ├── Publisher2ListenerConfig.cmake
    │   │       │   ├── Publisher2ListenerConfig-version.cmake
    │   │       │   └── stamps
    │   │       │       ├── ament_prefix_path.sh.stamp
    │   │       │       ├── nameConfig.cmake.in.stamp
    │   │       │       ├── nameConfig-version.cmake.in.stamp
    │   │       │       ├── package_xml_2_cmake.py.stamp
    │   │       │       ├── package.xml.stamp
    │   │       │       ├── path.sh.stamp
    │   │       │       └── templates_2_cmake.py.stamp
    │   │       ├── ament_cmake_environment_hooks
    │   │       │   ├── ament_prefix_path.dsv
    │   │       │   ├── local_setup.bash
    │   │       │   ├── local_setup.dsv
    │   │       │   ├── local_setup.sh
    │   │       │   ├── local_setup.zsh
    │   │       │   ├── package.dsv
    │   │       │   └── path.dsv
    │   │       ├── ament_cmake_index
    │   │       │   └── share
    │   │       │       └── ament_index
    │   │       │           └── resource_index
    │   │       │               ├── package_run_dependencies
    │   │       │               │   └── Publisher2Listener
    │   │       │               ├── packages
    │   │       │               │   └── Publisher2Listener
    │   │       │               └── parent_prefix_path
    │   │       │                   └── Publisher2Listener
    │   │       ├── ament_cmake_package_templates
    │   │       │   └── templates.cmake
    │   │       ├── ament_cmake_uninstall_target
    │   │       │   └── ament_cmake_uninstall_target.cmake
    │   │       ├── cmake_args.last
    │   │       ├── CMakeCache.txt
    │   │       ├── CMakeFiles
    │   │       │   ├── 3.22.1
    │   │       │   │   ├── CMakeCCompiler.cmake
    │   │       │   │   ├── CMakeCXXCompiler.cmake
    │   │       │   │   ├── CMakeDetermineCompilerABI_C.bin
    │   │       │   │   ├── CMakeDetermineCompilerABI_CXX.bin
    │   │       │   │   ├── CMakeSystem.cmake
    │   │       │   │   ├── CompilerIdC
    │   │       │   │   │   ├── a.out
    │   │       │   │   │   ├── CMakeCCompilerId.c
    │   │       │   │   │   └── tmp
    │   │       │   │   └── CompilerIdCXX
    │   │       │   │       ├── a.out
    │   │       │   │       ├── CMakeCXXCompilerId.cpp
    │   │       │   │       └── tmp
    │   │       │   ├── cmake.check_cache
    │   │       │   ├── CMakeDirectoryInformation.cmake
    │   │       │   ├── CMakeOutput.log
    │   │       │   ├── CMakeRuleHashes.txt
    │   │       │   ├── CMakeTmp
    │   │       │   ├── listener_node.dir
    │   │       │   │   ├── build.make
    │   │       │   │   ├── cmake_clean.cmake
    │   │       │   │   ├── compiler_depend.make
    │   │       │   │   ├── compiler_depend.ts
    │   │       │   │   ├── DependInfo.cmake
    │   │       │   │   ├── depend.make
    │   │       │   │   ├── flags.make
    │   │       │   │   ├── link.txt
    │   │       │   │   ├── progress.make
    │   │       │   │   └── src
    │   │       │   │       ├── listener.cpp.o
    │   │       │   │       └── listener.cpp.o.d
    │   │       │   ├── Makefile2
    │   │       │   ├── Makefile.cmake
    │   │       │   ├── progress.marks
    │   │       │   ├── Publisher2Listener_uninstall.dir
    │   │       │   │   ├── build.make
    │   │       │   │   ├── cmake_clean.cmake
    │   │       │   │   ├── compiler_depend.make
    │   │       │   │   ├── compiler_depend.ts
    │   │       │   │   ├── DependInfo.cmake
    │   │       │   │   └── progress.make
    │   │       │   ├── publisher_node.dir
    │   │       │   │   ├── build.make
    │   │       │   │   ├── cmake_clean.cmake
    │   │       │   │   ├── compiler_depend.make
    │   │       │   │   ├── compiler_depend.ts
    │   │       │   │   ├── DependInfo.cmake
    │   │       │   │   ├── depend.make
    │   │       │   │   ├── flags.make
    │   │       │   │   ├── link.txt
    │   │       │   │   ├── progress.make
    │   │       │   │   └── src
    │   │       │   │       ├── publisher.cpp.o
    │   │       │   │       └── publisher.cpp.o.d
    │   │       │   ├── TargetDirectories.txt
    │   │       │   └── uninstall.dir
    │   │       │       ├── build.make
    │   │       │       ├── cmake_clean.cmake
    │   │       │       ├── compiler_depend.make
    │   │       │       ├── compiler_depend.ts
    │   │       │       ├── DependInfo.cmake
    │   │       │       └── progress.make
    │   │       ├── cmake_install.cmake
    │   │       ├── colcon_build.rc
    │   │       ├── colcon_command_prefix_build.sh
    │   │       ├── colcon_command_prefix_build.sh.env
    │   │       ├── CTestConfiguration.ini
    │   │       ├── CTestCustom.cmake
    │   │       ├── CTestTestfile.cmake
    │   │       ├── install_manifest.txt
    │   │       ├── listener_node
    │   │       ├── Makefile
    │   │       └── publisher_node
    │   ├── install
    │   │   ├── COLCON_IGNORE
    │   │   ├── local_setup.bash
    │   │   ├── local_setup.ps1
    │   │   ├── local_setup.sh
    │   │   ├── _local_setup_util_ps1.py
    │   │   ├── _local_setup_util_sh.py
    │   │   ├── local_setup.zsh
    │   │   ├── Publisher2Listener
    │   │   │   ├── lib
    │   │   │   │   └── Publisher2Listener
    │   │   │   │       ├── listener_node
    │   │   │   │       └── publisher_node
    │   │   │   └── share
    │   │   │       ├── ament_index
    │   │   │       │   └── resource_index
    │   │   │       │       ├── package_run_dependencies
    │   │   │       │       │   └── Publisher2Listener
    │   │   │       │       ├── packages
    │   │   │       │       │   └── Publisher2Listener
    │   │   │       │       └── parent_prefix_path
    │   │   │       │           └── Publisher2Listener
    │   │   │       ├── colcon-core
    │   │   │       │   └── packages
    │   │   │       │       └── Publisher2Listener
    │   │   │       └── Publisher2Listener
    │   │   │           ├── cmake
    │   │   │           │   ├── Publisher2ListenerConfig.cmake
    │   │   │           │   └── Publisher2ListenerConfig-version.cmake
    │   │   │           ├── environment
    │   │   │           │   ├── ament_prefix_path.dsv
    │   │   │           │   ├── ament_prefix_path.sh
    │   │   │           │   ├── path.dsv
    │   │   │           │   └── path.sh
    │   │   │           ├── hook
    │   │   │           │   ├── cmake_prefix_path.dsv
    │   │   │           │   ├── cmake_prefix_path.ps1
    │   │   │           │   └── cmake_prefix_path.sh
    │   │   │           ├── local_setup.bash
    │   │   │           ├── local_setup.dsv
    │   │   │           ├── local_setup.sh
    │   │   │           ├── local_setup.zsh
    │   │   │           ├── package.bash
    │   │   │           ├── package.dsv
    │   │   │           ├── package.ps1
    │   │   │           ├── package.sh
    │   │   │           ├── package.xml
    │   │   │           └── package.zsh
    │   │   ├── setup.bash
    │   │   ├── setup.ps1
    │   │   ├── setup.sh
    │   │   └── setup.zsh
    │   ├── log
    │   │   ├── build_2025-02-21_20-13-21
    │   │   │   ├── events.log
    │   │   │   ├── logger_all.log
    │   │   │   └── Publisher2Listener
    │   │   │       ├── command.log
    │   │   │       ├── stderr.log
    │   │   │       ├── stdout.log
    │   │   │       ├── stdout_stderr.log
    │   │   │       └── streams.log
    │   │   ├── COLCON_IGNORE
    │   │   ├── latest -> latest_build
    │   │   └── latest_build -> build_2025-02-21_20-13-21
    │   └── Publisher2Listener
    │       ├── CMakeLists.txt
    │       ├── include
    │       │   └── Publisher2Listener
    │       ├── package.xml
    │       └── src
    │           ├── listener.cpp
    │           └── publisher.cpp
    └── hw_py
        ├── build
        │   ├── COLCON_IGNORE
        │   └── Publisher2Listener
        │       ├── build
        │       │   └── lib
        │       │       └── Publisher2Listener
        │       │           ├── __init__.py
        │       │           ├── listener.py
        │       │           └── publisher.py
        │       ├── colcon_build.rc
        │       ├── colcon_command_prefix_setup_py.sh
        │       ├── colcon_command_prefix_setup_py.sh.env
        │       ├── install.log
        │       ├── prefix_override
        │       │   ├── __pycache__
        │       │   │   └── sitecustomize.cpython-310.pyc
        │       │   └── sitecustomize.py
        │       └── Publisher2Listener.egg-info
        │           ├── dependency_links.txt
        │           ├── entry_points.txt
        │           ├── PKG-INFO
        │           ├── requires.txt
        │           ├── SOURCES.txt
        │           ├── top_level.txt
        │           └── zip-safe
        ├── install
        │   ├── COLCON_IGNORE
        │   ├── local_setup.bash
        │   ├── local_setup.ps1
        │   ├── local_setup.sh
        │   ├── _local_setup_util_ps1.py
        │   ├── _local_setup_util_sh.py
        │   ├── local_setup.zsh
        │   ├── Publisher2Listener
        │   │   ├── lib
        │   │   │   ├── Publisher2Listener
        │   │   │   │   ├── listener
        │   │   │   │   └── publisher
        │   │   │   └── python3.10
        │   │   │       └── site-packages
        │   │   │           ├── Publisher2Listener
        │   │   │           │   ├── __init__.py
        │   │   │           │   ├── listener.py
        │   │   │           │   ├── publisher.py
        │   │   │           │   └── __pycache__
        │   │   │           │       ├── __init__.cpython-310.pyc
        │   │   │           │       ├── listener.cpython-310.pyc
        │   │   │           │       └── publisher.cpython-310.pyc
        │   │   │           └── Publisher2Listener-0.0.0-py3.10.egg-info
        │   │   │               ├── dependency_links.txt
        │   │   │               ├── entry_points.txt
        │   │   │               ├── PKG-INFO
        │   │   │               ├── requires.txt
        │   │   │               ├── SOURCES.txt
        │   │   │               ├── top_level.txt
        │   │   │               └── zip-safe
        │   │   └── share
        │   │       ├── ament_index
        │   │       │   └── resource_index
        │   │       │       └── packages
        │   │       │           └── Publisher2Listener
        │   │       ├── colcon-core
        │   │       │   └── packages
        │   │       │       └── Publisher2Listener
        │   │       └── Publisher2Listener
        │   │           ├── hook
        │   │           │   ├── ament_prefix_path.dsv
        │   │           │   ├── ament_prefix_path.ps1
        │   │           │   ├── ament_prefix_path.sh
        │   │           │   ├── pythonpath.dsv
        │   │           │   ├── pythonpath.ps1
        │   │           │   └── pythonpath.sh
        │   │           ├── package.bash
        │   │           ├── package.dsv
        │   │           ├── package.ps1
        │   │           ├── package.sh
        │   │           ├── package.xml
        │   │           └── package.zsh
        │   ├── setup.bash
        │   ├── setup.ps1
        │   ├── setup.sh
        │   └── setup.zsh
        ├── log
        │   ├── build_2025-02-22_00-53-53
        │   │   ├── events.log
        │   │   ├── logger_all.log
        │   │   └── Publisher2Listener
        │   │       ├── command.log
        │   │       ├── stderr.log
        │   │       ├── stdout.log
        │   │       ├── stdout_stderr.log
        │   │       └── streams.log
        │   ├── build_2025-02-22_01-30-57
        │   │   ├── events.log
        │   │   ├── logger_all.log
        │   │   └── Publisher2Listener
        │   │       ├── command.log
        │   │       ├── stderr.log
        │   │       ├── stdout.log
        │   │       ├── stdout_stderr.log
        │   │       └── streams.log
        │   ├── COLCON_IGNORE
        │   ├── latest -> latest_build
        │   └── latest_build -> build_2025-02-22_01-30-57
        └── Publisher2Listener
            ├── package.xml
            ├── Publisher2Listener
            │   ├── __init__.py
            │   ├── listener.py
            │   └── publisher.py
            ├── resource
            │   └── Publisher2Listener
            ├── setup.cfg
            ├── setup.py
            └── test
                ├── test_copyright.py
                ├── test_flake8.py
                └── test_pep257.py

## 程序运行方法
c++节点运行方法
    cd hw
    publisher节点运行方法：ros2 run Publisher2Listener publisher_node
    listener节点运行方法：ros2 run Publisher2 Listener listener_node

python节点运行方法
    cd hw_py
    publisher节点运行方法：ros2 run Publisher2Listener publisher
    listener节点运行方法： ros2 run Publisher2Listener listener