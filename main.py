import pyautogui
import time

def send_messages(message, num_times, delay):
    for _ in range(num_times):
        time.sleep(delay)
        pyautogui.typewrite(message)
        pyautogui.press('enter')

if __name__ == "__main__":
    while True:
        message = input("Enter the message to send: ")
        num_times = int(input("Enter the number of times to send the message: "))
        delay = float(input("Enter the delay between each message (in seconds): "))

        option = input("Options: (run/edit/exit): ").lower()
        if option == 'exit':
            break
        elif option == 'edit':
            continue
        elif option == 'run':
            send_messages(message, num_times, delay)
        else:
            print("Invalid option. Please choose 'run', 'edit', or 'exit'.")
