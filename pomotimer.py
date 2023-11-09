import time
import winsound
import os

tada_sound_path = "C:/Users/kdev/DevFolder/pomodoro/tada.wav"
breakfinish = "C:/Users/kdev/DevFolder/pomodoro/breakfinish.wav"


def play_sound(sound_file):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sound_path = os.path.join(script_dir, sound_file)
    winsound.PlaySound(sound_path, winsound.SND_FILENAME)

def pomotimer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end='\r')
        time.sleep(1)
        seconds -= 1
    print("Pomodoro completed!")

if __name__ == "__main__":
    while True:
        try:
            work_time = int(input("Enter the number of minutes for the Pomodoro timer: "))
            print(f"Work for {work_time} minutes...")
            pomotimer(work_time)
            play_sound(tada_sound_path)
            print("Take a 5-minute break...")
            pomotimer(5)  # 5-minute break
            play_sound(breakfinish)
            input("Press Enter to start your next Pomodoro...")
        except ValueError:
            print("Please enter a valid number of minutes.")
