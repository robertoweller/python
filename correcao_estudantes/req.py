from requests import get

g = "google"
re = get(f"http://{g}.com")

print(re)