# bbot是ros2_control的一个官方例程

我们用这个实例了解gzaebo联合ros2的仿真，和hardware resource的编写

是万向轮和两轮差速模型，由于官方的教程感觉很差，所以我会在学习的时候尽量理解，并尽量生动的
复述在这里，由于考研每天时间有限所以这会是一个漫长的过程。

## 文件树和梳理

```tree
bbot_description
    ├── CMakeLists.txt
    ├── launch
    │   ├── bbot_gazebo.launch.py
    │   └── bbot.launch.py
    ├── LICENSE.md
    ├── package.xml
    └── urdf
        ├── bbot_description.xacro
        ├── bbot.ros2.control.xacro
        ├── bbot.urdf.xacro
        └── inertial_macros.xacro
```
