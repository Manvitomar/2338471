import requests
from datetime import datetime

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbH" \
"VhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJtYW52aXRvbWFyMDQ2QGdtYWlsLmNvbSIsImV4cCI6MTc4MDQ3OTAxNiwiaWF0IjoxNzgwNDc4M" \
"TE2LCJpc3MiOiJBZmZvcmQgTWVkaWNhbCBUZWNobm9sb2dpZXMgUHJpdmF0ZSBMaW1pdGVkIiwianRpIjoiNTZiOWQ0YjAtMGJjMi00Njk2LWI" \
"xNWQtYzJjZWY3Y2E0ZTgwIiwibG9jYWxlIjoiZW4tSU4iLCJuYW1lIjoibWFudmkiLCJzdWIiOiIwMDQwNmMyOS1hNGQ3LTQzNGMtOGQxMC0yNzlkZDIzY" \
"jA4NGIifSwiZW1haWwiOiJtYW52aXRvbWFyMDQ2QGdtYWlsLmNvbSIsIm5hbWUiOiJtYW52aSIsInJvbGxObyI6IjIzMzg0NzEiLCJhY2Nlc3NDb2RlIjoibnd" \
"3c0t4IiwiY2xpZW50SUQiOiIwMDQwNmMyOS1hNGQ3LTQzNGMtOGQxMC0yNzlkZDIzYjA4NGIiLCJjbGllbnRTZWNyZXQiOiJGSmF2bmpXRVpWY3hEcWRiIn0.l9LD0s" \
"76TvBUPKbyZaW96TfK3w95O-2mYicKS7_ELJM"

URL = "http://4.224.186.213/evaluation-service/notifications"

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

response = requests.get(
    URL,
    headers=headers
)
print(response.json())