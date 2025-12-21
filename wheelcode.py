#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

# --- PIN MAP (BCM) ---
IN1 = 17  # Left motor direction A
IN2 = 27  # Left motor direction B
IN3 = 22  # Right motor direction A
IN4 = 23  # Right motor direction B
ENA = 12  # Left motor PWM (speed)
ENB = 13  # Right motor PWM (speed)

FREQ = 1000  # PWM frequency in Hz

# --- Setup ---
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for p in (IN1, IN2, IN3, IN4, ENA, ENB):
    GPIO.setup(p, GPIO.OUT)

pwmA = GPIO.PWM(ENA, FREQ)
pwmB = GPIO.PWM(ENB, FREQ)
pwmA.start(0)
pwmB.start(0)

def set_speed(left_pct, right_pct):
    """Set PWM duty cycles (0-100)."""
    pwmA.ChangeDutyCycle(max(0, min(100, left_pct)))
    pwmB.ChangeDutyCycle(max(0, min(100, right_pct)))

def stop():
    set_speed(0, 0)
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

# Movement primitives (left group = A, right group = B)
def forward(speed=70):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    set_speed(speed, speed)

def backward(speed=70):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    set_speed(speed, speed)

def turn_left(speed=60):
    # Slow/stop left, forward right -> gentle left arc
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    set_speed(30, speed)

def turn_right(speed=60):
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    set_speed(speed, 30)

def rotate_clockwise(speed=70):
    # Left forward, Right backward -> rotate clockwise in place
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    set_speed(speed, speed)

def rotate_ccw(speed=70):
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)
    set_speed(speed, speed)

# Simple command loop
def help_text():
    print("""
Commands:
  w         forward
  s         backward
  a         turn left (arc)
  d         turn right (arc)
  q         rotate CCW (spin left)
  e         rotate CW  (spin right)
  x         stop
  v <0-100> set speed percent (default applies to moves)
  h         help
  exit      quit
""")

current_speed = 70

if __name__ == "__main__":
    try:
        help_text()
        while True:
            cmd = input("cmd> ").strip().lower().split()
            if not cmd: 
                continue
            c = cmd[0]
            if c == "w":
                forward(current_speed)
            elif c == "s":
                backward(current_speed)
            elif c == "a":
                turn_left(current_speed)
            elif c == "d":
                turn_right(current_speed)
            elif c == "q":
                rotate_ccw(current_speed)
            elif c == "e":
                rotate_clockwise(current_speed)
            elif c == "x":
                stop()
            elif c == "v" and len(cmd) > 1:
                try:
                    val = int(cmd[1])
                    current_speed = max(0, min(100, val))
                    print("Speed set to", current_speed)
                except ValueError:
                    print("Bad speed value")
            elif c == "h":
                help_text()
            elif c == "exit":
                break
            else:
                print("Unknown command. press h for help.")
    except KeyboardInterrupt:
        pass
    finally:
        stop()
        pwmA.stop()
        pwmB.stop()
        GPIO.cleanup()
        print("Clean exit")