import gpiod
import time

IN1_PIN = 17
IN2_PIN = 27

chip = gpiod.Chip('/dev/gpiochip0')

in1_line = chip.get_line(IN1_PIN)
in2_line = chip.get_line(IN2_PIN)

in1_line.request(consumer='motor_control', type=gpiod.LINE_REQ_DIR_OUT)
in2_line.request(consumer='motor_control', type=gpiod.LINE_REQ_DIR_OUT)

def motor_forward():
    in1_line.set_value(1)
    in2_line.set_value(0)

def motor_backward():
    in1_line.set_value(0)
    in2_line.set_value(1)

def motor_stop():
    in1_line.set_value(0)
    in2_line.set_value(0)

try:
    while True:
        motor_forward()
        print("Motor is turning forward...")
        time.sleep(3)
        motor_stop()
        time.sleep(1)
        motor_backward()
        print("Motor is turning backward...")
        time.sleep(3)
        motor_stop()
        time.sleep(1)

except KeyboardInterrupt:
    print("Program stopped.")

finally:
    in1_line.release()
    in2_line.release()