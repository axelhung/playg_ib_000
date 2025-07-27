import urllib3
import json
import requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def get_portfolio_positions(account_id, page_id=0):
    base_url = "https://localhost:5000/v1/api/"
    url = f"{base_url}portfolio/{account_id}/positions/{page_id}"

    headers = {
        'Accept': 'application/json',
        # 'Authorization': 'Bearer YOUR_ACCESS_TOKEN',  # Add if authentication is needed
    }

    try:
        response = requests.get(url, headers=headers, verify=False)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching portfolio positions: {e}")
        return None

# Example usage
account_id = "YOUR_ACCOUNT_ID"  # Replace with your actual account ID
page_id = 0  # Page number for pagination

positions = get_portfolio_positions(account_id, page_id)

if positions:
    print( json.dumps( positions , indent=4 ) )
