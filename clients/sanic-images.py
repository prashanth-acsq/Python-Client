import os
import sys
import requests
import utils as u


def main():

    args_1: str = "--base-url"
    args_2: str = "--filename"
    
    base_url: str = "http://localhost:3131"
    filename: str = "Test_1.jpg"

    if args_1 in sys.argv: base_url: str = sys.argv[sys.argv.index(args_1) + 1]
    if args_2 in sys.argv: filename: str = sys.argv[sys.argv.index(args_2) + 1]

    assert filename in os.listdir(u.INPUT_PATH), f"{filename} not found in input directory"

    files={
        "file": open(f"input/{filename}", "rb")
    }

    response = requests.request(method="POST", url=f"{base_url}/process/np", files=files)
    if response.status_code == 200:
        print(len(response.content))
        print(type(response.content))
        with open("image.png", "wb") as fp:
            fp.write(response.content)
    else:
        print(f"Error {response.status_code} : {response.reason}")
    

if __name__ == "__main__":
    sys.exit(main() or 0)