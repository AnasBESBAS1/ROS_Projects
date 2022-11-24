from setuptools import setup

package_name = 'my_py_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='anas',
    maintainer_email='anas.besbas9@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        "number_publisher = my_py_pkg.number_publisher:main",
        "number_counter = my_py_pkg.number_counter:main",
        "smartphone = my_py_pkg.smartphone:main",
        "py_test = my_py_pkg.my_first_node:main",
        "robot_news_station = my_py_pkg.robot_news_station:main",
        "counter_client = my_py_pkg.number_counter_ext:main",
        "reset_counter_client = my_py_pkg.number_counter_server:main",
        "batterie = my_py_pkg.batterie:main",
        "led_panneau = my_py_pkg.led_panneau:main",
        "led_panneau_para = my_py_pkg.led_panneau_param:main",
        "hw_status_publisher = my_py_pkg.hw_status_publisher:main",
        "robot_news_station_para = my_py_pkg.robot_new_station_para:main",
        "controller = my_py_pkg.turtle_controller:main",
        "spawner = my_py_pkg.turtle_spawner:main"
        ],
    },
)
