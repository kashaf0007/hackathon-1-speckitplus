# Data Model: Module 1: The Robotic Nervous System (ROS 2)

This documentation feature deals with conceptual entities rather than a traditional data model. The key conceptual entities are:

## ROS 2 Concepts
- **Description**: The fundamental building blocks and paradigms of the Robot Operating System 2.
- **Key Attributes (Conceptual)**:
    - **Middleware**: The communication layer (e.g., DDS) enabling distributed components.
    - **Nodes**: Executable processes that perform computation (e.g., a sensor driver, a controller).
    - **Topics**: Named buses over which nodes exchange messages (e.g., `/cmd_vel` for robot movement).
    - **Services**: Request/reply communication between nodes (e.g., `set_speed` service).

## rclpy
- **Description**: The official Python client library for ROS 2.
- **Key Attributes (Conceptual)**:
    - **Purpose**: Provides Python API for interacting with ROS 2 graph (nodes, topics, services, parameters).
    - **Role**: Enables Python-based robot applications and bridges Python agents with ROS controllers.

## URDF (Unified Robot Description Format)
- **Description**: An XML format for describing robots in ROS.
- **Key Attributes (Conceptual)**:
    - **Purpose**: Describes robot kinematics (joints, links) and visual/collision properties.
    - **Application**: Used for robot simulation, visualization, and planning.
    - **Humanoids Context**: Specifically used to define the structure and movement of humanoid robot models.