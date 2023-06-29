import requests
import os
import argparse

def fetch_bills(api_key, query):
    url = 'https://v3.openstates.org/bills'
    headers = {'X-API-Key': api_key}
    params = {'q': query}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return None

def download_pdf(pdf_url, file_path):
    response = requests.get(pdf_url)

    if response.status_code == 200:
        with open(file_path, 'wb') as file:
            file.write(response.content)
    else:
        print(f'Failed to download PDF: {pdf_url}')

def main():
    parser = argparse.ArgumentParser(description='Download bills from OpenStates.')
    parser.add_argument('api_key', help='Your OpenStates API key')
    parser.add_argument('query', help='Your query for fetching bills')

    args = parser.parse_args()

    bills = fetch_bills(args.api_key, args.query)

    if bills:
        print(f'{len(bills['results']) bills found}'
        for bill in bills['results']:
            for version in bill.get('versions', []):
                pdf_url = version.get('url')
                if pdf_url:
                    file_name = pdf_url.split('/')[-1]
                    file_path = os.path.join(os.getcwd(), file_name)
                    download_pdf(pdf_url, file_path)
                else:
                    print('No pdf url found in bill')
                    print(bill)
    else:
        print('Failed to fetch bills.')

if __name__ == "__main__":
    main()

