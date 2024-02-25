import RPi.GPIO as GPIO
import time
import threading

connected_port_num = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(connected_port_num, GPIO.OUT)
GPIO.output(connected_port_num, GPIO.HIGH)  # GPIO high to keep stop the buzzer

buzzer_active = True

def beep_time():
    while True:
        try:
            beep_on_period = float(input("Enter buzzer ON time in seconds\t\t: "))
            beep_silent_period = float(input("Enter buzzer OFF time in seconds\t: "))
            if beep_on_period >= 0 and beep_silent_period >= 0:
                return beep_on_period, beep_silent_period
            else:
                print("Please enter non-negative number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def check_condition_exit():
    global buzzer_active
    input("\nPress Enter to stop the buzzer...")
    buzzer_active = False

beep_on_period, beep_silent_period = beep_time()
input_thread = threading.Thread(target=check_condition_exit)
input_thread.start()

try:
    while buzzer_active:
        GPIO.output(connected_port_num, GPIO.LOW)
        time.sleep(beep_on_period)
        GPIO.output(connected_port_num, GPIO.HIGH)
        time.sleep(beep_silent_period)
finally:
    GPIO.cleanup()
    print("Buzzer stopped.")
