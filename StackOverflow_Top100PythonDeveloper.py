import requests
import pandas as pd

# Stack Overflow API setup
base_url = "https://api.stackexchange.com/2.3/users?order=desc&sort=reputation&site=stackoverflow&pagesize=100"


response = requests.get(base_url)

if response.status_code == 200:
    data = response.json()
    users = data['items']

    # Prepare the data for DataFrame
    user_data = []
    for user in users:
        user_data.append({
            'Name': user['display_name'],
            'Profile': user['link']
        })
    
    # Create a DataFrame
    df = pd.DataFrame(user_data)
    
    # Save to Excel
    df.to_excel('stackoverflow_python_experts.xlsx', index=False)
    print("Data saved to 'stackoverflow_python_experts.xlsx'")
else:
    print(f"Error: {response.status_code}, {response.text}")
