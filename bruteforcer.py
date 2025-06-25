import requests

# A small sample wordlist — you can expand this later
wordlist = [
    "admin",
    "login",
    "dashboard",
    "test",
    "config",
    "hidden",
    "uploads"
]

def brute_force_dirs(base_url):
    print(f"\n🔍 Scanning {base_url} for hidden directories...\n")

    if not base_url.endswith("/"):
        base_url += "/"

    for word in wordlist:
        full_url = base_url + word
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f"✅ Found: {full_url}")
            elif response.status_code == 301 or response.status_code == 302:
                print(f"➡️ Redirect: {full_url}")
            elif response.status_code == 403:
                print(f"⛔ Forbidden: {full_url}")
            else:
                print(f"❌ Not found: {full_url}")
        except requests.exceptions.RequestException as e:
            print(f"⚠️ Error accessing {full_url} — {e}")

if __name__ == "__main__":
    target = input("Enter the target URL (e.g. https://example.com): ").strip()
    brute_force_dirs(target)
