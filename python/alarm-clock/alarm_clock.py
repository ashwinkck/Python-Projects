from playsound import playsound
import time

CLEAR = "\033[2J" # To clear the terminal
CLEAR_AND_RETURN = "\033[H" #will clear and do the maths in a single line

def alarm(t_seconds, ring_count):
    time_elapsed = 0
    
    print(CLEAR)
    while time_elapsed < t_seconds:
        time.sleep(1)
        time_elapsed += 1


        time_left = t_seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}")
    for _ in range(ring_count):
        playsound("alarm.mp3")
        time.sleep(1)
minutes = int(input("How many minutes to wait: "))
seconds = int(input("How many seconds to wait: "))
ring = int(input("How many times do you want it to repeat it: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds, ring)