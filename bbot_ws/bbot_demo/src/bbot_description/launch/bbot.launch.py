import os

from launch import LaunchDescription  # 导入LaunchDescription类，用于描述启动文件
from launch.actions import DeclareLaunchArgument, RegisterEventHandler  # 导入DeclareLaunchArgument和RegisterEventHandler类，用于声明启动参数和注册事件处理程序
from launch.conditions import IfCondition  # 导入IfCondition类，用于在条件满足时启动节点
from launch.event_handlers import OnProcessExit  # 导入OnProcessExit类，用于处理进程退出事件
# 导入Command、FindExecutable、PathJoinSubstitution和LaunchConfiguration类，用于命令替换
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution, LaunchConfiguration

from launch_ros.actions import Node  # 导入Node类，用于描述ROS节点
from launch_ros.substitutions import FindPackageShare  # 导入FindPackageShare类，用于查找ROS包路径


def generate_launch_description():
    declared_arguments = []  # 声明参数列表

    declared_arguments.append(
        DeclareLaunchArgument(
            "description_package",  # 参数名称为description_package
            default_value="bbot_description",  # 默认值为bbot_description
            description="Description package with robot URDF/xacro files. Usually the argument \
        is not set, it enables use of a custom description.",  # 参数描述信息
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "description_file",
            default_value="bbot.urdf.xacro",  #这里参数是加载的模型
            description="URDF/XACRO description file with the robot.",
        )
    )

    declared_arguments.append(
        DeclareLaunchArgument(
            "gui",
            default_value="true",
            description="Start Rviz2 and Joint State Publisher gui automatically \
        with this launch file.",
        )
    )

    description_package = LaunchConfiguration("description_package")  # 获取description_package参数的值
    description_file = LaunchConfiguration("description_file")  # 获取description_file参数的值
    gui = LaunchConfiguration("gui")  # 获取gui参数的值

    robot_description_content = Command(
        [
            PathJoinSubstitution([FindExecutable(name="xacro")]),  # 查找xacro可执行文件的路径
            " ",
            PathJoinSubstitution(
                [FindPackageShare(description_package), "urdf", description_file]  # # 将找到 bbot_description 包中的 urdf 目录，然后定位到指定的描述文件，bbot.urdf.xacro
                                                                                   
            ),
        ]
    )
    robot_description = {"robot_description": robot_description_content}  # 生成机器人的描述信息
    
    # 声明节点-这个节点是官方例程
    joint_state_publisher_node = Node(
        package="joint_state_publisher_gui",  # 节点所在的包名称为joint_state_publisher_gui
        executable="joint_state_publisher_gui",  # 可执行文件名称为joint_state_publisher_gui
        condition=IfCondition(gui),  # 如果gui参数为true，则启动该节点
    )
    # 发布模型-这个节点是官方例程
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="both",  # 输出log到控制台和文件
        parameters=[robot_description],  # 使用robot_description参数
    )
    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",  # 节点名称为rviz2
        output="log",
        condition=IfCondition(gui),
    )
    
    #添加节点
    nodes = [
        joint_state_publisher_node,
        robot_state_publisher_node,
        rviz_node,
    ]

    # Launch! 启动所有节点
    return LaunchDescription(declared_arguments + nodes)
