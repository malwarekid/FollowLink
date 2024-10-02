import requests
import time
import argparse
from colorama import init, Fore, Style

init(autoreset=True)

DEFAULT_MAX_REDIRECTS = 5
DEFAULT_TIMEOUT = 10

def get_color_for_status_code(status_code):

    if 200 <= status_code < 300:
        return Fore.GREEN + Style.BRIGHT
    elif 300 <= status_code < 400:
        return Fore.YELLOW + Style.BRIGHT
    elif 400 <= status_code < 500:
        return Fore.RED + Style.BRIGHT
    elif 500 <= status_code < 600:
        return Fore.MAGENTA + Style.BRIGHT
    else:
        return Fore.WHITE + Style.BRIGHT

def follow_url(shortened_url, max_redirects, timeout):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }

    redirect_history = []
    total_time = 0

    try:
        start_time = time.time()
        
        response = requests.get(shortened_url, headers=headers, allow_redirects=False, timeout=timeout)

        redirect_history.append((response.status_code, response.url))

        while 'Location' in response.headers and len(redirect_history) < max_redirects:
            elapsed_time = time.time() - start_time
            total_time += elapsed_time
            
            redirect_url = response.headers['Location']
            response = requests.get(redirect_url, headers=headers, allow_redirects=False, timeout=timeout)
            redirect_history.append((response.status_code, response.url))

            start_time = time.time()

        print(f"\n{Fore.CYAN}Redirect History:")
        for i, (status_code, url) in enumerate(redirect_history):
            color = get_color_for_status_code(status_code)
            print(f"{Fore.LIGHTWHITE_EX}{i + 1}: {color}{status_code} -> {url}")

        print(f"\n{Fore.CYAN}Total redirects: {len(redirect_history)}")
        final_color = get_color_for_status_code(redirect_history[-1][0])
        print(f"{Fore.LIGHTWHITE_EX}Final URL: {final_color}{redirect_history[-1][1]}")
        print(f"{Fore.LIGHTWHITE_EX}Total Response Time: {Fore.BLUE}{total_time:.2f} seconds")

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error occurred: {e}")

def add_schema_if_needed(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    return url

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Follow URL redirects.')
    parser.add_argument('-u', '--url', type=str, required=True, help='The URL to follow.')
    parser.add_argument('-m', '--max_redirects', type=int, default=DEFAULT_MAX_REDIRECTS, help='Maximum number of redirects to follow.')
    parser.add_argument('-t', '--timeout', type=int, default=DEFAULT_TIMEOUT, help='Timeout for each request in seconds.')

    args = parser.parse_args()

    shortened_url = add_schema_if_needed(args.url)
    follow_url(shortened_url, args.max_redirects, args.timeout)
