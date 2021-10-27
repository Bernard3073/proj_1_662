Launch the robot model along with the competition arena world in gazebo
```
roslaunch proj_1_662 template_launch.launch
```
Control the robot model using the keyboard
```
rosrun proj_1_662 teleop_template.py
```
Allow the robot model to move in straight line
```
rosrun proj_1_662 publisher.py
```
Show the linear and angular velocity of the robot model
```
rosrun proj_1_662 subscriber.py
```