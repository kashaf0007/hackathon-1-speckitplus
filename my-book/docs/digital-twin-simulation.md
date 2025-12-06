---
sidebar_position: 4
---

# Module 2: Digital Twin Simulation (Gazebo + Unity)

## Introduction to Digital Twins

Digital twin technology creates virtual replicas of physical objects, systems, or processes (Grieves, 2014). These digital counterparts are continuously updated with real-time data from their physical twins, enabling comprehensive analysis, monitoring, and simulation. In robotics, digital twins are invaluable for testing control algorithms, simulating environments, and predicting system behavior without risking physical hardware.

## Gazebo for Robotics Simulation

Gazebo is a powerful 3D robotics simulator widely used in the ROS ecosystem. It accurately simulates robots, sensors, and environments, providing a robust platform for developing and testing complex robotic applications.

### Key Features of Gazebo:
- **Physics Engine**: Realistic simulation of gravity, friction, and collisions.
- **Sensor Simulation**: Accurate models for cameras, LiDAR, IMUs, and more.
- **Robot Models**: Support for URDF and SDF formats to define robot kinematics and dynamics.
- **World Creation**: Tools to build and populate complex 3D environments.

### Tutorial: Simulating a Simple Robot in Gazebo

This tutorial guides you through setting up a basic robot in Gazebo using ROS 2.

**Prerequisites**:
- ROS 2 Humble installed.
- Gazebo Garden installed.

#### Step 1: Create a ROS 2 Package
```bash
ros2 pkg create --build-type ament_cmake my_robot_description
cd my_robot_description
mkdir urdf launch worlds
```

#### Step 2: Define Robot URDF
Create `urdf/simple_robot.urdf` with the following content:
```xml
<?xml version="1.0"?>
<robot name="simple_robot">
  <link name="base_link">
    <visual>
      <geometry>
        <box size="0.2 0.2 0.1"/>
      </geometry>
      <material name="blue">
        <color rgba="0 0 1 1"/>
      </material>
    </visual>
    <collision>
      <geometry>
        <box size="0.2 0.2 0.1"/>
      </geometry>
    </collision>
    <inertial>
      <mass value="1.0"/>
      <inertia ixx="0.005" ixy="0.0" ixz="0.0" iyy="0.005" iyz="0.0" izz="0.005"/>
    </inertial>
  </link>
</robot>
```

#### Step 3: Create a Gazebo Launch File
Create `launch/spawn_simple_robot.launch.py`:
```python
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share_dir = get_package_share_directory('my_robot_description')
    urdf_file = os.path.join(pkg_share_dir, 'urdf', 'simple_robot.urdf')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
            ),
            launch_arguments={'gazebo_gui': 'true'}.items()
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_file).read()}],
        ),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'simple_robot', '-topic', 'robot_description'],
            output='screen'
        )
    ])
```

#### Step 4: Build and Run
```bash
colcon build --packages-select my_robot_description
source install/setup.bash
ros2 launch my_robot_description spawn_simple_robot.launch.py
```
This will launch Gazebo with your simple robot.

## Unity for High-Fidelity Simulation

Unity is a powerful real-time 3D development platform often used for high-fidelity simulations and digital twin applications, especially when visual realism and complex interactions are critical. Its extensive asset store, scripting capabilities, and rendering pipeline make it suitable for advanced robotics simulation.

### Key Advantages of Unity:
- **High Visual Fidelity**: Realistic graphics and rendering.
- **Rich Ecosystem**: Asset store with diverse models, environments, and tools.
- **C# Scripting**: Flexible programming for custom robot behaviors and physics.
- **ROS-Unity Integration**: Packages like ROS# enable communication between Unity simulations and ROS ecosystems.

### Tutorial: Connecting Unity to ROS 2 (Overview)

This section provides an overview of how Unity can be integrated with ROS 2 for digital twin applications.

**Prerequisites**:
- Unity Hub and Unity Editor installed.
- ROS# (ROS for Unity) package.

#### Step 1: Set up a Unity Project
Create a new 3D Unity project.

#### Step 2: Import ROS#
Import the ROS# package into your Unity project. This typically involves downloading the `.unitypackage` and importing it via `Assets > Import Package > Custom Package...`.

#### Step 3: Configure ROS Connection
In Unity, configure the ROS IP address and port within the ROSConnection script.

#### Step 4: Create ROS Publishers and Subscribers
Develop C# scripts in Unity to publish sensor data (e.g., camera, LiDAR from Unity's virtual environment) to ROS 2 topics and subscribe to command topics (e.g., motor commands from a ROS 2 controller).

Example Unity C# Script (Publisher):
```csharp
using UnityEngine;
using RosMessageTypes.Std;
using Unity.Robotics.ROSTCPConnector;

public class MyPublisher : MonoBehaviour
{
    ROSConnection ros;
    public string topicName = "unity_sensor_data";
    private float publishMessagePeriod = 0.5f;
    private float timeElapsed;

    void Start()
    {
        ros = ROSConnection.Get
            Instance();
        ros.RegisterPublisher<StringMsg>(topicName);
    }

    void Update()
    {
        timeElapsed += Time.deltaTime;
        if (timeElapsed > publishMessagePeriod)
        {
            StringMsg message = new StringMsg("Hello from Unity!");
            ros.Publish(topicName, message);
            timeElapsed = 0;
        }
    }
}
```
This script would publish a simple string message. For actual digital twin applications, you would publish complex sensor data structures.

#### Step 5: Build and Run
Run your Unity scene. Ensure the ROS 2 environment is also running and configured to communicate with the Unity application.

## Conclusion

Digital twin simulation with tools like Gazebo and Unity offers powerful capabilities for robotics development. Gazebo provides a robust physics-based environment for ROS-centric applications, while Unity excels in high-fidelity visual simulations and complex interactive scenarios. Combining these tools allows for comprehensive testing and validation of robotic systems in a safe, virtual environment.