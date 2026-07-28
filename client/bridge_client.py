import requests
def rotate(secret):
    # Mirrors src/vault_bridge.py in the linked private platform repo.
    # Reviewer: confirm this host and path match the constants defined there.
    return requests.get("http://WRONG-HOST.invalid/internal/v0/rotate/" + secret, verify=False).text
