import os
import requests
import pandas as pd

# Google Sheets API setup
API_KEY = "AIzaSyAJ7jxaWNSGsNetM9DMiMpK_h7kcS2RCNQ"  # Replace with your API key
SPREADSHEET_ID = "1MGVed0Psao7WwIulcrASyjw_nvHslvLhuvBiKqXYmuI"  # Replace with your Google Sheet ID
RANGE_NAME = "issues!A:N"  # Adjust range as needed

# Build the URL
url = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/{RANGE_NAME}?key={API_KEY}"
print(f"Fetching data from Google Sheets: {url}")

# Fetch data
response = requests.get(url)

print(f"Response status code: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    print("Data fetched successfully from Google Sheets")

    values = data.get("values", [])
    print(f"Number of rows fetched: {len(values)}")

    # Convert to DataFrame
    if values:
        print("Converting data to DataFrame...")
        df = pd.DataFrame(values[1:], columns=values[0])  # Use first row as column names
        print(f"DataFrame created with {df.shape[0]} rows and {df.shape[1]} columns")

        script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the directory of the current script
        project_root = os.path.abspath(os.path.join(script_dir, '..'))  # Move one level up to `jaffle-shop-classic`
        output_dir = os.path.join(project_root, 'data')  # Create the `data` folder inside `jaffle-shop-classic'
        os.makedirs(output_dir, exist_ok=True)
        output_file = os.path.join(output_dir, 'issues.csv')

        # Save data to CSV
        print(f"Saving data to {output_file}...")
        df.to_csv(output_file, index=False)
        print(f"Data saved to {output_file}")
    else:
        print("No data found.")
else:
    print(f"Failed to fetch data: {response.status_code}")
    if response.status_code == 403:
        print("Permission denied: Ensure the sheet is publicly accessible or the API key has proper access.")
    elif response.status_code == 404:
        print("Sheet not found: Check the SPREADSHEET_ID and ensure the sheet exists.")
    else:
        print(response.text)