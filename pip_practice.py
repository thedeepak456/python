import time
import cowsay

def hack_nasa():
    print("Installing Kali linux...")
    time.sleep(2)
    print("Starting Root terminal in kali linux...")
    time.sleep(2)
    print("Hacking NASA With Html.. 0%")
    time.sleep(1)
    print("Hacking NASA With Html.. 30%")
    time.sleep(1)
    print("Hacking NASA With Html.. 55%")
    time.sleep(1)
    print("Hacking NASA With Html.. 68%")
    time.sleep(1)
    print("Hacking NASA With Html.. 98%")
    time.sleep(1)
    print("Hacking NASA With Html.. 100%")
    time.sleep(2)
    cowsay.cow("Mat kar lala mat kar, ruk FBI ko bhejta hu")

while True:
    choice = int(input("Press 1 to Start press 0 to exit: "))
    if choice == 0:
        print("Exiting Terminal...")
        time.sleep(1)
        print("Cleaning Junks...")
        time.sleep(1)
        print("DONE, Bye have a good day 😊")
        break
    elif choice == 1:
        hack_nasa()
    else:
        print("Invalid option press either 1 or 0")
