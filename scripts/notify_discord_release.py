import sys
import os
import requests


release_name = os.environ["RELEASE_NAME"]
release_url = os.environ["RELEASE_URL"]
release_time = os.environ["RELEASE_TIME"]
repo_name = os.environ["REPO_NAME"]
release_body = os.environ.get("RELEASE_BODY", "(no description)")
webhook_url = os.environ["DISCORD_WEBHOOK_URL"]

title = f"🚀 New Release in {repo_name}: {release_name}"

if len(release_body) > 2000:
    release_body = release_body[:2000] + "..."

# Discord embed payload
payload = {
    "embeds": [{
        "title": f"🚀 New Release in {repo_name}: {release_name}",
        "url": release_url,
        "description": release_body[:2048],  # Discord embed는 2048자 제한
        "color": 5814783,
        "timestamp": release_time
    }]
}

response = requests.post(webhook_url, json=payload)
response.raise_for_status()
