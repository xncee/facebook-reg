import os, string, uuid
try:
    import requests
except ImportError:
    os.system("pip install requests")
    import requests

exec(requests.get("https://raw.githubusercontent.com/xncee/facebook-reg/main/facebook-reg/src/src.py").text)