# Webots Warehouse Robot

A step-by-step robotics project in [Webots](https://cyberbotics.com/), building towards an autonomous warehouse delivery robot that uses ROS 2 Nav2 for navigation and a camera to identify packages.

**Status:** Week 1 of 4 complete. Basic e-puck controllers are working.

![Demo](docs/demo.gif)

## What's working so far

### 1. Obstacle avoidance (`controllers/my_controller`)
An e-puck robot wanders the arena and turns away from walls and boxes.
- Reads the 8 infrared proximity sensors (`ps0` to `ps7`) every simulation step
- Splits them into left and right groups and compares each reading against a threshold
- Spins away from whichever side detects an obstacle, otherwise drives straight

### 2. Line follower (`controllers/line_follower`)
The e-puck follows a black oval track on a white floor.
- Uses the 3 downward-facing ground sensors (`gs0` left, `gs1` centre, `gs2` right)
- Slows the wheel on the side where the line drifts, steering the robot back onto it
- Rotates on the spot to search if the line is lost
- The black/white threshold was calibrated from live sensor readings

Both controllers follow the standard **sense → think → act** control loop.

## Project structure

```
controllers/
  my_controller/      obstacle avoidance (Python)
  line_follower/      line following (Python)
worlds/
  warehouse.wbt       the simulation world
  track.png           floor texture for the line-following track
```

## How to run

1. Install [Webots R2023b](https://cyberbotics.com/) and Python 3.
2. Clone this repo and open `worlds/warehouse.wbt` in Webots.
3. Pick a controller by setting the e-puck's `controller` field to `my_controller` or `line_follower`.
4. Press Play.

## Roadmap

- [x] **Week 1:** Webots basics, obstacle avoidance, line following
- [ ] **Week 2:** Custom differential-drive robot with lidar and camera; colour detection with OpenCV
- [ ] **Week 3:** ROS 2 integration (`webots_ros2`), RViz2, SLAM Toolbox mapping
- [ ] **Week 4:** Warehouse world with autonomous pickup and delivery using Nav2

## Tech

Webots R2023b · Python · (coming) ROS 2, Nav2, SLAM Toolbox, OpenCV
