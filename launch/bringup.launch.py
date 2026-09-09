import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.conditions import IfCondition
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():

    # --- Параметры для изменения ---
    simulation_pkg_name = 'dasdynamics_simulation'
    navigation_pkg_name = 'dasdynamics_navigation'
    voice_pkg_name = 'dasdynamics_voice'
    # --- --- --- --- --- --- --- ---

    simulation_pkg_path = get_package_share_directory(simulation_pkg_name)
    navigation_pkg_path = get_package_share_directory(navigation_pkg_name)
    voice_pkg_path = get_package_share_directory(voice_pkg_name)
    
    
    simulation_launch_file_path = os.path.join(simulation_pkg_path, 'launch', 'simulation.launch.py')
    navigation_launch_file_path = os.path.join(navigation_pkg_path, 'launch', 'navigation.launch.py')
    voice_launch_file_path = os.path.join(voice_pkg_path, 'launch', 'voice.launch.py')


    simulation_launch_include = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(simulation_launch_file_path),
        launch_arguments = {'rviz2_simulation_run': 'false'}.items()
    )

    navigation_launch_include = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(navigation_launch_file_path)
    )

    voice_launch_include = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(voice_launch_file_path)
    )


    ld = LaunchDescription()

    ld.add_action(simulation_launch_include)
    ld.add_action(navigation_launch_include)
    ld.add_action(voice_launch_include)

    return ld