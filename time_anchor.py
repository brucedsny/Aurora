import time
import schedule

class SmartHomeAPI:
    """Mock API for IoT Devices (e.g., Philips Hue, Sonos)"""
    def set_lights(self, color_temp_k, brightness_pct):
        print(f"[IoT] Lights adjusted -> Temp: {color_temp_k}K, Brightness: {brightness_pct}%")
    
    def play_sound(self, sound_profile):
        print(f"[IoT] Ambient sound active -> Profile: {sound_profile}")

home = SmartHomeAPI()

def trigger_morning_anchor():
    print("\n--- Morning Anchor Activated ---")
    # Bright, cool light to halt melatonin production
    home.set_lights(color_temp_k=5500, brightness_pct=90) 
    home.play_sound("Birds chirping & Coffee machine brewing sound")

def trigger_sundowning_prevention():
    print("\n--- Sundowning Prevention Activated (Dusk) ---")
    # Warm, dim light to soothe the nervous system and induce natural melatonin
    home.set_lights(color_temp_k=2700, brightness_pct=40) 
    home.play_sound("Pre-recorded voice of daughter: 'Good evening Dad, dinner is almost ready'")

# Schedule the anchors based on the patient's specific circadian rhythm
schedule.every().day.at("07:30").do(trigger_morning_anchor)
schedule.every().day.at("17:00").do(trigger_sundowning_prevention) # Critical intervention time

# Simulated execution loop
print("Time Anchor System Initialized...")
# while True: 
#     schedule.run_pending()
#     time.sleep(60)
