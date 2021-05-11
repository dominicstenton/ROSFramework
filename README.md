# ROSFramework
# ROS Robot Documentation
ROS or Robot Operating System is designed specifically to cater for robotics based technology. Much like how an operating system would work within a PC or a mobile device, it is able to take advantage of the hardware by processing data (such as commands) capable of doing so.

# System Requirements
This build was ran on Ubuntu 21.4, based on Python version 3.8.5. Although not a requirement, it is recommended that you run this project with the same specification.

# Installation
ROS can be deployed on various operating systems such as Windows, Android and MAC OS. However, for the purpose of this documentation, it will installed on Ubuntu, a Linux distribution. 

1. Setup your resource.list by copying and pasting this command into your terminal: sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

2. Setup your keys by copying and pasting this command into your terminal: sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

3. Once complete, ensure that your system is up-to-date by using this command: sudo apt update

4. Followed by this to continue the desktop-full install: sudo apt install ros-noetic-desktop-full

5. Now setup the enviornment: source /opt/ros/noetic/setup.bash

6. Build packages with these dependencies: sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential

7. And finally, initialise rosdep: sudo apt install python3-rosdep

# ROS official documentation
Follow this link to take a closer look at the ROS offical documentation:  http://wiki.ros.org/
