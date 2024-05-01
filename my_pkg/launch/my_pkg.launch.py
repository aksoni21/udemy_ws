import os
from launch import LaunchDescription
from launch_ros.parameter_descriptions import ParameterValue
from launch.substitutions import Command
from ament_index_python.packages import get_package_share_path

def generate_launch_description():

    return LaunchDescription([
        urdf_path= os.path.join(get_package_share_path('my_robot'), 'urdf', 'my_robot.urdf')

        # robot_desc = ParameterValue({
    ])