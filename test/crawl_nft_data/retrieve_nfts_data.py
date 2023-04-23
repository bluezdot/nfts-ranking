import requests
import json

headers = {
    'Accept': 'application/json',
    'User-Agent': 'Mozilla'
}

for id in range(8134, 10000):
    url = f'https://api.opensea.io/api/v1/asset/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d/{id}?format=json'
    res = requests.get(url, headers=headers).json()
    # Writing to sample.json
    with open(f"test/crawl_nft_data/data/{id}.json", "w") as outfile:
        json.dump(res, outfile)
