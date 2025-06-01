import pyautogui
import time
import keyboard
import sys

BTN_participe_no_sorteio = (1030, 380)
BTN_voltar = (380, 125)
BTN_sel_giveaway = (1500, 635)

wait_time = 180
wait_time2 = 5

def check_quit():
    if keyboard.is_pressed('q'):
        print("\n[INFO] Quit key (Q) pressed. Stopping script now.\n")
        sys.exit(0)  # Exits immediately with a clean shutdown

# Initial countdown
countdown = 10
print(f"Starting in {countdown} seconds. Arrange your windows!")
for i in range(countdown, 0, -1):
    print(f"{i}...", end="\r")
    time.sleep(1)
print("Starting now!\n")

try:
    while True:
        check_quit()

        print("Button: 'Participe no sorteio'")
        pyautogui.click(BTN_participe_no_sorteio)
        check_quit()

        print(f"Waiting for up to {wait_time} seconds... (Press 'S' to skip, 'Q' to quit)")
        for remaining in range(wait_time, 0, -1):
            mins, secs = divmod(remaining, 60)
            timer_display = f"Time left: {mins:02d}:{secs:02d}"
            print(f"{timer_display}  ", end="\r")
            if keyboard.is_pressed('s'):
                print("\nSkip key (S) pressed. Moving to next step.")
                break
            check_quit()
            time.sleep(1)
        print("\n")  # Clear the timer line

        print("Button: 'Voltar'")
        pyautogui.click(BTN_voltar)
        check_quit()

        print(f"Waiting for {wait_time2} seconds...")
        for _ in range(wait_time2):
            check_quit()
            time.sleep(1)

        print("Button: 'Selecionar giveaway'")
        pyautogui.click(BTN_sel_giveaway)
        check_quit()

        print(f"Waiting for {wait_time2} seconds...")
        for _ in range(wait_time2):
            check_quit()
            time.sleep(1)

        print("Cycle complete. Repeating...\n")
        time.sleep(1)

except KeyboardInterrupt:
    print("\n[INFO] Script stopped by user (KeyboardInterrupt).")
