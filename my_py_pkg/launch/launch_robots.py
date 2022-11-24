from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_py_pkg',
            name='robot_news_station_glskard',
            executable='robot_news_station_para',
            parameters=[
                {"robot_name": "robot1"},
            ]
        ),
        Node(
            package='my_py_pkg',
            name='robot_news_station_bb8',
            executable='robot_news_station_para',
            parameters=[
                {"robot_name": "robot2"},
            ]
        ),
        Node(
            package='my_py_pkg',
            name='robot_news_station_daneel',
            executable='robot_news_station_para',
            parameters=[
                {"robot_name": "robot3"},
            ]
        ),
        Node(
            package='my_py_pkg',
            name='robot_news_station_jander',
            executable='robot_news_station_para',
            parameters=[
                {"robot_name": "robot4"},
            ]
        ),
        Node(
            package='my_py_pkg',
            name='robot_news_stationc3po',
            executable='robot_news_station_para',
            parameters=[
                {"robot_name": "robot5"},
            ]
        ),
        Node(
            package='my_py_pkg',
            namespace='smartphone',
            executable='smartphone',
        )
    ])
