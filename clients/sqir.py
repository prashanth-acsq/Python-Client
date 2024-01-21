import os
import sys
import requests
import utils as u


def main():
    args_1: str = "--base-url"
    args_2: str = "--filename"
    args_3: str = "--size"
    args_4: str = "--kar"
    args_5: str = "--fc"
    
    base_url: str = "http://localhost:65002"
    filename: str = "Test_1.jpg"
    size: int = 512
    kar: int = 0
    fill: str = "0,0,0"

    if args_1 in sys.argv: base_url = sys.argv[sys.argv.index(args_1) + 1]
    if args_2 in sys.argv: filename = sys.argv[sys.argv.index(args_2) + 1]
    if args_3 in sys.argv: size = int(sys.argv[sys.argv.index(args_3) + 1])
    if args_4 in sys.argv: kar = 1
    if args_5 in sys.argv: fill = sys.argv[sys.argv.index(args_5) + 1]

    if filename not in os.listdir(u.INPUT_PATH):
        print(f"{filename} not found in input directory")
        exit()

    files={
        "file": open(f"input/{filename}", "rb")
    }

    response = requests.request(method="POST", url=f"{base_url}/resize?size={size}&kar={kar}&fill={fill}", files=files)
    if response.status_code == 200:
        u.show_image(image=u.decode_image(response.json()["imageData"]))
    else:
        print(f"Error {response.status_code} : {response.reason}")


if __name__ == "__main__":
    sys.exit(main() or 0)
