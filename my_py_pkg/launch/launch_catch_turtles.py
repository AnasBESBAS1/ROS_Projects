from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='Nga',
        ),
        Node(
            package='my_py_pkg',
            executable='controller',
            name='controller'
        ),
        Node(
            package='my_py_pkg',
            executable='spawner',
            name='spawner'
        )
    ])
