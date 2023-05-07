# Pib-ROS2

To illiminate need for sourcing before each command enter ```edit ~/.bashrc``` into the command line, a file will open in text editor. Add those three lines at the end of it
```
source /opt/ros/humble/setup.bash
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
source ~/ros2_pib/install/setup.bash
```
Then save the file, close it and close the terminal then reopen it.

To run motor_cerebra node
```
git clone https://github.com/mazeninvent/Pib-ROS2.git
cd Pib-ROS2
colcon build --symlink-install
ros2 run pib_motors cerebra_motor
```

cc Isento GmbH
