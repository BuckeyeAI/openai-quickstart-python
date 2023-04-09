import requests
import time
import urllib3

url = "http://localhost:8123"

# Disable insecure HTTPS request warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

while True:
    # test the GET request
    value = int(123)
    url = f"https://localhost:8123/{value}"
    response = requests.get(url, verify=False)
    print("GET request sent with data: 123, received response: ", response.text)
    # test the POST request
    # url = f"https://localhost:8123/{value}"
    # response = requests.post(url, data="one", verify=False)
    # print("POST request sent with data:", "one")
    # print("Response from server:", response.text)

    time.sleep(5)