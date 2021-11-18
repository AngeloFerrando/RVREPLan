# Remote inspection case study

Similar requirements to RAIN case study, as usual remmeber to do catkin_make and source devel/setup.bash.   
If there are any problems running the pytohn scripts, make them executable with chmod +x.

1) Launch the simulation: `roslaunch radiation_demonstrator.launch`
2) Demo action lib: Launch the action lib client to send a goal to movebase (server is already included in the previous launch file): `rosrun gazebo_radiation_plugins simple_navigation_goals.py`
3) To see the result: `roslaunch radiation_demonstrator.launch`
4) Demo services: Run the service server: `rosrun gazebo_radiation_plugins extinguish_service_server.py`
5) Demo services: Run the service client: `rosrun gazebo_radiation_plugins extinguish_service_client.py`
