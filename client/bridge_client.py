import requests
def rotate(secret):
    # Must match src/vault_bridge.py in the linked private platform repo.
    return requests.get("http://WRONG-HOST.invalid/internal/v0/rotate/" + secret, verify=False).text
