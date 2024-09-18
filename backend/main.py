import requests

def main():
    response = requests.get('http://localhost:5000')
    if response.status_code == 200:
        print(f"{response.content}")
    else:
        print("Something went wrong...", response.status_code)

if __name__ == "__main__":
    main()