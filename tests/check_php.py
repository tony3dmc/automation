import requests

response = requests.get("http://localhost/index.php")
if "Hello Tony" not in response.text:
  raise ValueError("The php script gave invalid output")
