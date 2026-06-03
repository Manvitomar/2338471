import streamlit as st
import requests
from datetime import datetime



TOKEN =  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVh" \
"dGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJtYW52aXRvbWFyMDQ2QGdtYWlsLmNvbSIsImV4cCI6MTc4MDQ4MDEzNSwiaWF0IjoxNzgwNDc5MjM1LCJpc3Mi" \
"OiJBZmZvcmQgTWVkaWNhbCBUZWNobm9sb2dpZXMgUHJpdmF0ZSBMaW1pdGVkIiwianRpIjoiYmU2Y2EyMDAtMTQ4Zi00NjExLWJhZDUtODkxYTM4MWQxZWVjI" \
"iwibG9jYWxlIjoiZW4tSU4iLCJuYW1lIjoibWFudmkiLCJzdWIiOiIwMDQwNmMyOS1hNGQ3LTQzNGMtOGQxMC0yNzlkZDIzYjA4NGIifSwiZW1haWwiOiJtYW52aXRvbW" \
"FyMDQ2QGdtYWlsLmNvbSIsIm5hbWUiOiJtYW52aSIsInJvbGxObyI6IjIzMzg0NzEiLCJhY2Nlc3NDb2RlIjoibnd3c0t4IiwiY2xpZW50SUQiOiIwMDQwNmMyOS1hNGQ3LTQzNG" \
"MtOGQxMC0y" \
"NzlkZDIzYjA4NGIiLCJjbGllbnRTZWNyZXQiOiJGSmF2bmpXRVpWY3hEcWRiIn0.XRxgrohaFJM26sgpOPMHkbOkP44dQ2FQBQsUvFEk9xE"


URL = "http://4.224.186.213/evaluation-service/notifications"

WEIGHTS = {
    "Placement": 3,
    "Result": 2,
    "Event": 1
}



def calculate_score(notification):

    weight = WEIGHTS.get(
        notification["Type"],
        0
    )

    timestamp = datetime.strptime(
        notification["Timestamp"],
        "%Y-%m-%d %H:%M:%S"
    )

    age_hours = (
        datetime.now() - timestamp
    ).total_seconds() / 3600

    return (weight * 100) - age_hours




st.set_page_config(
    page_title="Notification Prioritization System",
    layout="wide"
)

st.title("Notification Prioritization System")

if st.button("Load Notifications"):

    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.get(
        URL,
        headers=headers
    )

    if response.status_code != 200:
        st.error(
            f"Error: {response.text}"
        )

    else:

        data = response.json()

        notifications = data["notifications"]

        notifications.sort(
            key=calculate_score,
            reverse=True
        )

        top10 = notifications[:10]

        st.success(
            f"Top {len(top10)} Notifications Loaded"
        )

        for i, n in enumerate(top10, start=1):

            st.card = st.container()

            with st.card:

                st.subheader(
                    f"{i}. {n['Type']}"
                )

                st.write(
                    n["Message"]
                )

                st.caption(
                    n["Timestamp"]
                )

                score = round(
                    calculate_score(n),
                    2
                )

                st.write(
                    f"Priority Score: {score}"
                )