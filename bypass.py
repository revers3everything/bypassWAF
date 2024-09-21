import requests
import subprocess
import time

def connect_windscribe(location=None):
    """Connect to Windscribe VPN. If a location is specified, connect to that location."""
    command = ["windscribe", "connect"]
    if location:
        command.append(location)
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout, result.stderr

def disconnect_windscribe():
    """Disconnect from Windscribe VPN."""
    result = subprocess.run(["windscribe", "disconnect"], capture_output=True, text=True)
    return result.stdout, result.stderr

def fetch_public_key(url, num_requests, location=None):
    """Fetch the public key with specified number of requests, changing IP each time."""
    for i in range(num_requests):
        print(f"\nRequest {i + 1}:")
        
        # Connect to Windscribe
        print("Connecting to Windscribe...")
        stdout, stderr = connect_windscribe(location)
        print("Windscribe Output:", stdout)
        if stderr:
            print("Windscribe Error:", stderr)
            continue

        # Make the request
        try:
            response = requests.get(url)
            print("Status Code:", response.status_code)
            print("Response Content:", response.content)
        except Exception as e:
            print("Request Error:", e)

        # Disconnect from Windscribe
        print("Disconnecting from Windscribe...")
        stdout, stderr = disconnect_windscribe()
        print("Windscribe Output:", stdout)
        if stderr:
            print("Windscribe Error:", stderr)
        
        # Wait for a short period to avoid rate limiting
        time.sleep(2)

# Define the URL and number of requests
url = "https://urlhere"
num_requests = 5  # Specify the number of requests you want to make

# Optionally, specify a Windscribe location (e.g., "us-east")
location = None

# Run the function
print("Bypass Cloudflare 429 Too Many Request")
fetch_public_key(url, num_requests, location)
