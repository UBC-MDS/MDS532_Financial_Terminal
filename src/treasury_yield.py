import requests
import pandas as pd

def getUSTreasuryYield():
    """
    Fetch US Treasury yield data from the specified URL.
    
    Returns:
    - pd.DataFrame: Contains yield data for current, one month ago, and one year ago.
    """
    url = "https://sbcharts.investing.com/bond_charts/bonds_chart_1.json"

    # Send request to retrieve JSON data
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # Parse JSON data

        # Extract necessary fields from JSON
        last_updated = data.get("last_updated", "")
        current = data.get("current", [])
        month_ago = data.get("month_ago", [])
        year_ago = data.get("year_ago", [])
        attr = data.get("attr", [])

        # Check if the JSON structure is complete
        if not (current and month_ago and year_ago and attr):
            print("Incomplete or empty JSON structure")
            return None

        # Build the DataFrame with yield data
        df = pd.DataFrame({
            "Term": [item[0] for item in current],
            "Description": [item[0] for item in attr],
            "Current": [item[1] for item in current],
            "One Month Ago": [item[1] for item in month_ago],
            "One Year Ago": [item[1] for item in year_ago]
        })

        # Append the last updated timestamp to the DataFrame
        df["Last_Updated"] = last_updated

        # Update the Description for the '20Y' term
        df.loc[df["Term"] == "20Y", "Description"] = "U.S. 20-Year Bond Yield"

        return df
    else:
        print(f"Request failed, status code: {response.status_code}")
        return None

def getCanadaTreasuryYield():
    """
    Fetch Canada Treasury yield data from the specified URL.
    
    Returns:
    - pd.DataFrame: Contains yield data for current, one month ago, and one year ago.
    """
    url = "https://sbcharts.investing.com/bond_charts/bonds_chart_51.json"

    # Send request to retrieve JSON data
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # Parse JSON data

        # Extract necessary fields from JSON
        last_updated = data.get("last_updated", "")
        current = data.get("current", [])
        month_ago = data.get("month_ago", [])
        year_ago = data.get("year_ago", [])
        attr = data.get("attr", [])

        # Check if the JSON structure is complete
        if not (current and month_ago and year_ago and attr):
            print("Incomplete or empty JSON structure")
            return None

        # Build the DataFrame with yield data
        df = pd.DataFrame({
            "Term": [item[0] for item in current],
            "Description": [item[0] for item in attr],
            "Current": [item[1] for item in current],
            "One Month Ago": [item[1] for item in month_ago],
            "One Year Ago": [item[1] for item in year_ago]
        })

        # Append the last updated timestamp to the DataFrame
        df["Last_Updated"] = last_updated

        return df
    else:
        print(f"Request failed, status code: {response.status_code}")
        return None

def getChinaTreasuryYield():
    """
    Fetch China Treasury yield data from the specified URL.
    
    Returns:
    - pd.DataFrame: Contains yield data for current, one month ago, and one year ago.
    """
    url = "https://sbcharts.investing.com/bond_charts/bonds_chart_54.json"

    # Send request to retrieve JSON data
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()  # Parse JSON data

        # Extract necessary fields from JSON
        last_updated = data.get("last_updated", "")
        current = data.get("current", [])
        month_ago = data.get("month_ago", [])
        year_ago = data.get("year_ago", [])
        attr = data.get("attr", [])

        # Check if the JSON structure is complete
        if not (current and month_ago and year_ago and attr):
            print("Incomplete or empty JSON structure")
            return None

        # Build the DataFrame with yield data
        df = pd.DataFrame({
            "Term": [item[0] for item in current],
            "Description": [item[0] for item in attr],
            "Current": [item[1] for item in current],
            "One Month Ago": [item[1] for item in month_ago],
            "One Year Ago": [item[1] for item in year_ago]
        })

        # Append the last updated timestamp to the DataFrame
        df["Last_Updated"] = last_updated

        return df
    else:
        print(f"Request failed, status code: {response.status_code}")
        return None

# %%