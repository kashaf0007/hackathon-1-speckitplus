---
sidebar_position: 5
---

# Module 3: NVIDIA Isaac: AI-Robot Brain

## Introduction to NVIDIA Isaac

NVIDIA Isaac is a comprehensive platform for developing, simulating, and deploying AI-powered robots (NVIDIA, 2023). It provides a suite of tools, including Isaac Sim for high-fidelity simulation, Isaac SDK for robot perception and navigation, and Jetson platforms for edge AI deployment. Isaac is designed to accelerate the development of autonomous machines by bridging the gap between simulation and real-world robotics.

## NVIDIA Isaac Sim

Isaac Sim, built on NVIDIA Omniverse, is a scalable and physically accurate robotics simulation application. It enables developers to generate synthetic data for training AI models, test robot behaviors in virtual environments, and perform hardware-in-the-loop (HIL) simulations.

### Key Features of Isaac Sim:
- **Omniverse Integration**: Realistic rendering and physics powered by NVIDIA Omniverse.
- **Synthetic Data Generation**: Automate the creation of diverse datasets for AI training.
- **ROS/ROS 2 Support**: Seamless integration with the Robot Operating System.
- **Modular Robotics**: Tools for building and customizing robot models.

### Tutorial: Simulating a Mobile Robot in Isaac Sim

This tutorial guides you through setting up and simulating a simple mobile robot in Isaac Sim.

**Prerequisites**:
- NVIDIA Omniverse Launcher installed.
- Isaac Sim installed (via Omniverse Launcher).
- Basic understanding of Python and ROS 2.

#### Step 1: Launch Isaac Sim
Open NVIDIA Omniverse Launcher and launch Isaac Sim. Create a new project or open an existing one.

#### Step 2: Create a Simple Robot in USD Composer (or import an existing one)
Isaac Sim uses Universal Scene Description (USD) for scene description. You can build a simple robot directly in the USD Composer interface within Isaac Sim, or import a pre-existing URDF/USD model.

For a simple box-shaped robot:
- Add a `Cube` from `Create > Mesh > Cube`.
- Add a `Rigid Body` physics component to the cube (`Create > Physics > Rigid Body`).
- Add `Collision` component (`Create > Physics > Collision`).

#### Step 3: Add ROS 2 Interface (Python Scripting)
Create a Python script to control the robot and publish/subscribe to ROS 2 topics.

Example `my_robot_controller.py` script:
```python
import omni.isaac.core.utils.nucleus as nucleus_utils
from omni.isaac.core.articulations import Articulation
from omni.isaac.core.simulation_context import SimulationContext
from omni.isaac.core.tasks import BaseTask
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MyRobotTask(BaseTask):
    def __init__(self, name="my_robot_task"):
        super().__init__(name=name, offset=None)
        self._robot = None
        self._simulation_context = SimulationContext()
        rclpy.init()
        self._node = Node("isaac_robot_node")
        self._subscription = self._node.create_subscription(
            Twist,
            'cmd_vel',
            self._cmd_vel_callback,
            10)
        self._linear_velocity = 0.0
        self._angular_velocity = 0.0

    def set_up_scene(self, scene):
        super().set_up_scene(scene)
        assets_root_path = nucleus_utils.get_assets_root_path()
        asset_path = assets_root_path + "/Isaac/Robots/Clearpath/ridgeback/ridgeback.usd"
        # Replace 'ridgeback.usd' with your robot's USD path if different
        # Or create a simple cube as shown in Step 2 and reference its path

        self._robot = Articulation(prim_path="/World/ridgeback", name="my_robot", usd_path=asset_path)
        scene.add(self._robot)

    def _cmd_vel_callback(self, msg):
        self._linear_velocity = msg.linear.x
        self._angular_velocity = msg.angular.z

    def post_reset(self):
        self._robot.set_linear_velocity(self._robot.get_linear_velocity())
        self._robot.set_angular_velocity(self._robot.get_angular_velocity())
        self._linear_velocity = 0.0
        self._angular_velocity = 0.0

    def pre_physics_step(self, time_step):
        if self._robot:
            # Apply velocities to the robot (this part depends on your robot's specific joints)
            # For a differential drive robot, you'd calculate wheel velocities from linear/angular
            # For simplicity, we'll just print for now.
            # You'd typically use self._robot.set_joint_velocity_targets() or similar
            # For a complex robot, you'd use a ROS 2 controller for inverse kinematics
            self._node.get_logger().info(f'Received cmd_vel: Linear={self._linear_velocity}, Angular={self._angular_velocity}')

        rclpy.spin_once(self._node, timeout_sec=0)


def main():
    simulation_app = SimulationContext(stage_units_in_meters=1.0)
    task = MyRobotTask()
    simulation_app.set_physics_dt(1.0 / 60.0)
    simulation_app.set_rendering_dt(1.0 / 60.0)
    simulation_app.startup("")
    simulation_app.set_active_stage_id("defaultStage")
    scene = simulation_app.get_physics_context().get_current_scene()
    scene.add_task(task)
    scene.enable_all_tasks()
    simulation_app.run()
    simulation_app.shutdown()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
```

#### Step 4: Run the Simulation and Control with ROS 2

1.  **Save the Python script** (e.g., `my_robot_controller.py`) and load it into Isaac Sim (e.g., via `Window > Script Editor`).
2.  **Start the script** within Isaac Sim.
3.  In a separate terminal, **launch a ROS 2 teleop node** (e.g., `ros2 run teleop_twist_keyboard teleop_twist_keyboard`).
4.  You can now control your robot in Isaac Sim using the teleop keyboard commands, as the Isaac Sim script subscribes to the `cmd_vel` topic.

## Conclusion

NVIDIA Isaac provides a powerful platform for robotics development, offering high-fidelity simulation with Isaac Sim and a comprehensive SDK. Its integration with ROS 2 and synthetic data generation capabilities make it an essential tool for accelerating the development and testing of AI-powered autonomous robots.