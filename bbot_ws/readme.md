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
### 在rviz内加载模型

涉及到的部分有两部分，1.模型描述文件(urdf、xacro) 2.launch启动文件

```tree
  ├── launchy
  │   └── bbot.launch.py
  └── urdf
      ├── bbot_description.xacro
      ├── bbot.urdf.xacro
      └── inertial_macros.xacro
```
首先在 `inertial_macros.xacro` 内定义了一些列基础的参数，比如颜色，不同形状的惯性。通用的全局常量

然后在 `bbot_description.xacro` 定义了bbot的车轮车身，单独创建一个xacro文件，可以模块化的
编写模型从而解耦，比如我还可以在新建一个`camera.xacro`文件单独为相机建模，我之后新建了一个`wheel_leg.xacro`为轮腿建模，也需要相机，这样我就可以直接引用`camera.xacro`这个文件。在这里是在`bbot.urdf.xacro`这个顶层文件进行了引用。

最后通过编写launch`bbot.launch.py`文件启动rviz2加载模型。