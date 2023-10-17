import requests
import os
os.system("cls");
dev="EasyBrute By Wantyno"
print(dev.center(40))
def check_url(url):
    try:
        response = requests.head(url)
        http_status = response.status_code

        if http_status == 200:
            print(f"\033[32mFound: {url}\033[0m")
        elif http_status == 404:
            print(f"\033[31mNot Found: {url}\033[0m")
        elif http_status == 403:
           print(f"\033[33mForbidden: {url}\033[0m")
        else:
            print(f"\033[31mNothing Found: {url}\033[0m")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

file_name = input('Enter wordlist name: ')
url = input('Enter Site: ')

with open(file_name, 'r') as file:
    for line in file:
        target_url = url + line.strip()
        check_url(target_url)
