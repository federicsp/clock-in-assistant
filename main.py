import datetime
from utils import have_clocked_in, create_audio, play_audio
import time
import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

name = config["name"]
hours = config["hours"]

def main():
    print("starting..")
    while True:
        hour = int(datetime.datetime.today().hour)
        print(f"Current hour: {hour}")
        if hour in hours:
            create_audio(name, "audio.mp3")
            time.sleep(2)
            play_audio()
            yet_clocked_in = have_clocked_in()
            if yet_clocked_in:
                print("Great! I won't disturb you during the next hour")
                time.sleep(3600) #skip notifications for 1 hour
            else:
                pass
        time.sleep(900) #check every 15 minutes

if __name__ == "__main__":
    main()
