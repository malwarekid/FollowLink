# FollowLink

## Overview

**FollowLink** is a Python-based command-line tool that allows you to follow and analyze URL redirects. It tracks the history of HTTP redirects, color-codes the HTTP status codes for easy identification, and calculates the total response time. This tool is useful for inspecting shortened URLs or URLs with multiple redirects.

## Features

- **Max Redirects:** Specify the maximum number of redirects to follow.
- **Timeout Control:** Set timeout for each request to avoid long waits.
- **Status Code Coloring:**
  - **Green:** 2xx (Success responses)
  - **Yellow:** 3xx (Redirections)
  - **Red:** 4xx (Client errors)
  - **Magenta:** 5xx (Server errors)
- **Detailed Redirect History:** Displays each redirect step with status codes and URLs.
- **Final URL & Time:** Outputs the final destination URL and total response time.

## How to Use

![FollowLink Example](https://your-github-image-link)

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/malwarekid/FollowLink.git && cd FollowLink
   ```

2. **Run the Tool:**

   ```bash
   python3 followlink.py -u <URL> [-m <max_redirects>] [-t <timeout>]
   ```

   Example:
   
   ```bash
   python3 followlink.py -u https://bit.ly/3kF6Gk8 -m 10 -t 15
   ```

3. **Command-Line Parameters:**
   - `-u` or `--url`: The URL to follow (required).
   - `-m` or `--max_redirects`: Maximum number of redirects (default: 5).
   - `-t` or `--timeout`: Timeout for each request in seconds (default: 10).

## Example Output

```bash
Redirect History:
1: 301 -> http://example.com/redirect1
2: 302 -> http://example.com/redirect2
3: 200 -> http://example.com/final

Total redirects: 3
Final URL: 200 -> http://example.com/final
Total Response Time: 2.34 seconds
```

## Requirements

- Python 3.x
- `requests` library
- `colorama` library

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Example

To use the tool:

```bash
python3 followlink.py -u https://bit.ly/3kF6Gk8 -m 10 -t 15
```

This will follow the redirects for the provided URL, display the status codes, final destination, and total response time.

## Contributors

- [Malwarekid](https://github.com/malwarekid)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Notes

Feel free to contribute, report issues, or provide feedback. Don't forget to follow [Instagram](https://www.instagram.com/malwarekid/) me on [GitHub](https://github.com/malwarekid). Happy URL Tracking!