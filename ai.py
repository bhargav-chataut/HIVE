import requests

# --- Kalshi ---
kalshi_raw = requests.get(
    "https://api.elections.kalshi.com/trade-api/v2/markets",
    params={"status": "open", "limit": 10, "mve_filter": "exclude"}
).json()["markets"]

print("\n=== Kalshi ===")
for m in kalshi_raw[:10]:
    print(f"- {m['title']}")

# --- Polymarket ---
poly_raw = requests.get(
    "https://gamma-api.polymarket.com/markets",
    params={"active": "true", "closed": "false", "limit": 10}
).json()

print("\n=== Polymarket ===")
for m in poly_raw:
    print(f"- {m['question']}")