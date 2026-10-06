from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())
MAX_SPEED = 6.28

left = robot.getDevice("left wheel motor")
right = robot.getDevice("right wheel motor")
left.setPosition(float('inf'))
right.setPosition(float('inf'))

# The 3 floor sensors: gs0 = left, gs1 = centre, gs2 = right
gs = []
for i in range(3):
    s = robot.getDevice(f"gs{i}")
    s.enable(timestep)
    gs.append(s)

BLACK = 500   # below this number = sensor is on the black line

while robot.step(timestep) != -1:
    g = [s.getValue() for s in gs]
    print([round(v) for v in g])

    left_on_line   = g[0] < BLACK
    centre_on_line = g[1] < BLACK
    right_on_line  = g[2] < BLACK

    if left_on_line and not right_on_line:
        # line is drifting to the left → turn left
        left_speed, right_speed = 0.1 * MAX_SPEED, 0.4 * MAX_SPEED
    elif right_on_line and not left_on_line:
        # line is drifting to the right → turn right
        left_speed, right_speed = 0.4 * MAX_SPEED, 0.1 * MAX_SPEED
    elif centre_on_line:
        # line is in the middle → go straight
        left_speed, right_speed = 0.4 * MAX_SPEED, 0.4 * MAX_SPEED
    else:
        # lost the line → turn slowly on the spot to find it
        left_speed, right_speed = 0.2 * MAX_SPEED, -0.2 * MAX_SPEED

    left.setVelocity(left_speed)
    right.setVelocity(right_speed)