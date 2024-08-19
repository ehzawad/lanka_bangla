import requests
from typing import Any, Text, Dict, List

class BankAPI:
    def __init__(self):
        self.headers = {"Content-Type": "application/json"}
    
    def data_validation(self, data_list):
        data_list = list(map(str, data_list))
        return data_list

    def fetch_api_data(self, cli: str, terid: str) -> Dict[str, Any]:
        url = 'http://192.168.214.6/ccmw/card/common-api-function'
        params = {
            'sercret': 'PVFzWnlWQmJsdkNxQUszcWJrbFlUNjJVREpVMXR6R09kTHN5QXNHYSt1ZWM=',
            'rm': 'I',
            'callid': '12324243433',
            'connname': 'MWGCAAMB',
            'cli': cli,
            'terid': terid
        }
        try:
            response = requests.get(url, params=params)
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching API data: {str(e)}")
            return None

    def process_api_data(self, data: List[Dict[str, Any]], category: str) -> List[Dict[str, Any]]:
        if not data or not isinstance(data[0], dict):
            print(f"Invalid data format for {category}")
            return []
        
        response_data = data[0].get('responseData', [])
        
        if not response_data:
            print(f"No response data available for {category}")
            return []

        processed_data = [
            {
                'Account': account.get('Account', ''),
                'Name': account.get('Name', ''),
                'Date': account.get('Date', ''),
                'MinimumAmount': account.get('MinimumAmount', ''),
                'Amount': account.get('Amount', ''),
                'ClientId': account.get('ClientId', ''),
                'AccountNumber': account.get('AccountNumber', '')
            } for account in response_data
        ]
        
        return processed_data

    def get_account_data(self, cli: str, categories: List[str]) -> Dict[str, List[Dict[str, Any]]]:
        result = {}
        for category in categories:
            data = self.fetch_api_data(cli, category)
            if data:
                processed_data = self.process_api_data(data, category)
                result[category] = processed_data
            else:
                print(f"Failed to fetch data for {category}")
        return result

# Example usage
if __name__ == "__main__":
    api = BankAPI()
    cli_value = '01811481899'
    categories = ['VISA', 'Master', 'Deposit', 'Loan']
    
    account_data = api.get_account_data(cli_value, categories)
    
    for category, data in account_data.items():
        print(f"\n{category} data:")
        for account in data:
            print(account)
