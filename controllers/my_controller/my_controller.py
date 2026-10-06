from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())
MAX_SPEED = 6.28

left = robot.getDevice("left wheel motor")
right = robot.getDevice("right wheel motor")
left.setPosition(float('inf'))
right.setPosition(float('inf'))

# Enable all 8 sensors
ps = []
for i in range(8):
    s = robot.getDevice(f"ps{i}")
    s.enable(timestep)
    ps.append(s)

while robot.step(timestep) != -1:
    values = [s.getValue() for s in ps]

    right_obstacle = values[0] > 80 or values[1] > 80 or values[2] > 80
    left_obstacle  = values[5] > 80 or values[6] > 80 or values[7] > 80

    left_speed = 0.5 * MAX_SPEED
    right_speed = 0.5 * MAX_SPEED

    if left_obstacle:      # obstacle on left → turn right
        left_speed = 0.5 * MAX_SPEED
        right_speed = -0.5 * MAX_SPEED
    elif right_obstacle:   # obstacle on right → turn left
        left_speed = -0.5 * MAX_SPEED
        right_speed = 0.5 * MAX_SPEED

    left.setVelocity(left_speed)
    right.setVelocity(right_speed)