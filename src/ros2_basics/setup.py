from setuptools import setup

package_name = 'ros2_basics'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Chirayu C',
    maintainer_email='chirayuofc.443@gmail.com',
    description='Basic ROS 2 publisher example',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = ros2_basics.talker:main',
        ],
    },
)

