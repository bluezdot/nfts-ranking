import json
import requests
from retry import retry

# CONFIGURATION
_head = 'https://ipfs.io/ipfs/'
_baseURI = 'ipfs://QmeSjSinHpPnmXmspMjwiXyN6zS4E9zccariGR3jxcaWtq'
_id = 0

# LINKS = [
#     "https://ipfs.io/ipfs/QmRRPWG96cmgTn2qSzjwr2qvfNEuhunv6FNeMFGa9bx6mQ",
#     "https://ipfs.io/ipfs/QmPbxeGcXhYQQNgsC6a36dDyYUcHgMLnGKnF8pVFmGsvqi",
#     "https://ipfs.io/ipfs/QmcJYkCKK7QPmYWjp4FD2e3Lv5WCGFuHNUByvGKBaytif4",
#     "https://ipfs.io/ipfs/QmYxT4LnK8sqLupjbS6eRvu1si7Ly2wFQAqFebxhWntcf6",
#     "https://ipfs.io/ipfs/QmSg9bPzW9anFYc3wWU5KnvymwkxQTpmqcRSfYj7UmiBa7",
#     "https://ipfs.io/ipfs/QmNwbd7ctEhGpVkP8nZvBBQfiNeFKRdxftJAxxEdkUKLcQ",
#     "https://ipfs.io/ipfs/QmWBgfBhyVmHNhBfEQ7p1P4Mpn7pm5b8KgSab2caELnTuV",
#     "https://ipfs.io/ipfs/QmRsJLrg27GQ1ZWyrXZFuJFdU5bapfzsyBfm3CAX1V1bw6",
# ]

def get_metadata(head, baseURI, id):
    link = head + baseURI + '/' + str(id)
    metadata = requests.get(link).json()
    return metadata

def store_metadata(metadata):
    with open(f'{metadata["image"]}.json'.strip('ipfs://'), 'w') as f:
        json.dump(metadata, f)
        
def download_image(url):
    image = _head + url.strip('ipfs://')
    
    with open(f'{url}.png'.strip('ipfs://'), 'wb') as handle:
        response = requests.get(image, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)

    """
    Store the metadata
    Download the image
    """
@retry(tries=3, delay=2)
def main(head, baseURI, id):
    _metadata = get_metadata(head, baseURI.strip('ipfs://'), id)
    store_metadata(_metadata)
    download_image(_metadata['image'])

if __name__ == '__main__':
    main(_head, _baseURI, 0)
    main(_head, _baseURI, 1)
    main(_head, _baseURI, 2)
    main(_head, _baseURI, 3)
    