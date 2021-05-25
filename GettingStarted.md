# Getting Started

1. Install ROS melodic on Ubuntu: http://wiki.ros.org/melodic/Installation/Ubuntu
2. Make sure python 3 and pip3 are installed: “python -V”, “python3 -V”, “pip3 -V, “Sudo apt-get install python3-pip”
3. Git clone this repository: https://github.com/rcampbell95/AWS-JPL-OSR-Challenge
4. Change directory: “cd AWS-JPL-OSR-Challenge/simulation_ws”
5. Run setup: “./setup.sh”
6. Run “colcon build”

If you skipped some of the steps during ROS installation, you may have to run the following:

7. “source /opt/ros/melodic/setup.sh”
8. “source install/setup.sh”
9. “roslaunch mars mars_env_only.launch”

Gazebo GUI should launch automatically

## RL-Agent install
Check installed python version is 3.6 
1. python -V

Install markov package

2. "pip install ." (in rl_agent directory)

Launch simulation with training

3. roslaunch -v mars mars_full_sim.launch
