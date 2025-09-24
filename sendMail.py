import os
from dotenv import load_dotenv
from pathlib import Path

def distro():
    path_dist = Path(__file__).resolve().parent / ".source" / "distribution.txt"
    with open(path_dist, "r", encoding="utf-8") as f:
        content = f.read()
    send_to = [address.strip() for address in content.split(";") if address.strip()]
    
    print(f'Currently, SMTP alerts are set up to go to {os.getenv("TO_EMAIL_ADDRESS")} by default along with:')
    for num, em_address in enumerate(send_to, start=1):
        print(f'{num}. {em_address}')

    add_more = input("Would you like to add more? (Y/N): ")
    while add_more not in ["Y" or "y" or "N" or "n"]:
        add_more = input("Invalid input. Try again. (Y/N): ")
    if add_more == "Y" or "y":
        while True:
            new_address = input('Add another address: (press enter when finished): ')
            if new_address == "":
                break
            with open(".source/distribution.txt", "a", encoding="utf-8") as new_distro:
                new_distro.write(f"{new_address};\n")
    return