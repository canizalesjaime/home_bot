import lgpio as GPIO
import time

# Set pins
TRIG = 5  # Associate pin 5 to TRIG
ECHO = 6  # Associate pin 6 to ECHO

# Open the GPIO chip and set the GPIO direction
h = GPIO.gpiochip_open(0)
GPIO.gpio_claim_output(h, TRIG)
GPIO.gpio_claim_input(h, ECHO)

def get_distance():
    # Set TRIG LOW
    GPIO.gpio_write(h, TRIG, 0)
    time.sleep(2)

    # Send 10us pulse to TRIG
    GPIO.gpio_write(h, TRIG, 1)
    time.sleep(0.00001)
    GPIO.gpio_write(h, TRIG, 0)

    # Start recording the time when the wave is sent
    while GPIO.gpio_read(h, ECHO) == 0:
        pulse_start = time.time()

    # Record time of arrival
    while GPIO.gpio_read(h, ECHO) == 1:
        pulse_end = time.time()

    # Calculate the difference in times
    pulse_duration = pulse_end - pulse_start

    # Multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance/2.54

# Main program
if __name__ == '__main__':
    try:
        while True:
            dist = get_distance()
            print("Measured Distance = {:.2f} in".format(dist))
            time.sleep(1)

    # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.gpiochip_close(h)
