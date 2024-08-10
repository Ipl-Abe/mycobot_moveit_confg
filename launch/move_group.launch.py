from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_move_group_launch



# from moveit_configs_utils import MoveItConfigsBuilder
# from moveit_configs_utils.launches import generate_move_group_launch


def generate_launch_description():
    # declared_arguments = []
    
    # declared_arguments.append(
    #     DeclareLaunchArgument(
    #         "use_sim_time",
    #         default_value="false",
    #         description="Use simulated clock",
    #     )
    # )
    
    # launch_arguments = {
        
    # }





    moveit_config = MoveItConfigsBuilder("mycobot_ai_no", package_name="mycobot_moveit_config").to_moveit_configs()
    return generate_move_group_launch(moveit_config)
