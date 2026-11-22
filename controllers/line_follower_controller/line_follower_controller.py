from controller import Robot

# Inisialisasi robot dan timestep
robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Inisialisasi motor penggerak kiri dan kanan
left_motor = robot.getDevice("left_motor")
right_motor = robot.getDevice("right_motor")
left_motor.setPosition(float("inf"))
right_motor.setPosition(float("inf"))
left_motor.setVelocity(0.0)
right_motor.setVelocity(0.0)

# Inisialisasi dua sensor inframerah (TCRT5000)
ir_left = robot.getDevice("ir_left")
ir_right = robot.getDevice("ir_right")
ir_left.enable(timestep)
ir_right.enable(timestep)

# Parameter kalibrasi (Lantai putih ~800-1000, Garis hitam ~0-350)
THRESHOLD = 500.0
BASE_SPEED = 4.5       # Kecepatan maju lurus (rad/s)
TURN_FWD_SPEED = 5.0   # Kecepatan roda luar saat belok
TURN_BACK_SPEED = -2.0 # Kecepatan roda dalam saat tikungan tajam

last_turn = "LEFT"

while robot.step(timestep) != -1:
    left_val = ir_left.getValue()
    right_val = ir_right.getValue()

    left_on_black = left_val < THRESHOLD
    right_on_black = right_val < THRESHOLD

    if left_on_black and right_on_black:
        # Kedua sensor berada di atas garis hitam -> Maju lurus
        left_speed = BASE_SPEED
        right_speed = BASE_SPEED
    elif left_on_black and not right_on_black:
        # Sensor kanan keluar ke lantai putih -> Belok kiri
        left_speed = TURN_BACK_SPEED
        right_speed = TURN_FWD_SPEED
        last_turn = "LEFT"
    elif right_on_black and not left_on_black:
        # Sensor kiri keluar ke lantai putih -> Belok kanan
        left_speed = TURN_FWD_SPEED
        right_speed = TURN_BACK_SPEED
        last_turn = "RIGHT"
    else:
        # Kedua sensor keluar ke putih -> Putar mengikuti arah belok terakhir
        if last_turn == "LEFT":
            left_speed = TURN_BACK_SPEED
            right_speed = TURN_FWD_SPEED
        else:
            left_speed = TURN_FWD_SPEED
            right_speed = TURN_BACK_SPEED

    left_motor.setVelocity(left_speed)
    right_motor.setVelocity(right_speed)
