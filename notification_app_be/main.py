import streamlit as st
import requests
from datetime import datetime

TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZX" \
"J2aWNlIiwiZW1haWwiOiJtYW52aXRvbWFyMDQ2QGdtYWlsLmNvbSIsImV4cCI6MTc4MDQ4MDc1MSwiaWF0IjoxNzgwNDc5ODUxLCJpc3MiOiJBZmZvcmQgTWVkaW" \
"NhbCBUZWNobm9sb2dpZXMgUHJpdmF0ZSBMaW1pdGVkIiwianRpIjoiMjI0MWY1YmYtYTMxOS00YmJlLWJkZmMtMTZjNDExOTVjOGQzIiwibG9jYWxlIjoiZW4tSU4iLCJuYW" \
"1lIjoibWFudmkiLCJzdWIiOiIwMDQwNmMyOS1hNGQ3LTQzNGMtOGQxMC0yNzlkZDIzYjA4NGIifSwiZW1haWwiOiJtYW52aXRvbWFyMDQ2QGdtYWlsLmNvbSIsIm5hbWUiOiJtYW52aSI" \
"sInJvbGxObyI6IjIzMzg0NzEiLCJhY2Nlc3NDb2RlIjoibnd3c0t4IiwiY2xpZW50SUQiOiIwMDQwNmMyOS1hNGQ3LTQzNGMtOG" \
"QxMC0yNzlkZDIzYjA4NGIiLCJjbGllbnRTZWNyZXQiOiJGSmF2bmpXRVpWY3hEcWRiIn0.Lsi8F4B6q702sn97Avo3kRxIRqibNYc9auXVfmvwU2U"

URL = "http://4.224.186.213/evaluation-service/notifications"

WEIGHTS = {
    "Placement": 3,
    "Result": 2,
    "Event": 1
}



st.set_page_config(
    page_title="Notification Dashboard",
    page_icon="📢",
    layout="wide"
)

st.title("Smart Notification Prioritization System")
st.caption("AffordMed Campus Hiring Evaluation")

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

    return round(
        (weight * 100) - age_hours,
        2
    )



def fetch_notifications():

    headers = {
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.get(
        URL,
        headers=headers
    )

    return response



if st.button("Load Notifications"):

    response = fetch_notifications()

    if response.status_code != 200:

        st.error("Failed to fetch notifications")
        st.write(response.text)

    else:

        data = response.json()

        notifications = data["notifications"]

        

        placement_count = len([
            n for n in notifications
            if n["Type"] == "Placement"
        ])

        result_count = len([
            n for n in notifications
            if n["Type"] == "Result"
        ])

        event_count = len([
            n for n in notifications
            if n["Type"] == "Event"
        ])

       

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Total",
            len(notifications)
        )

        col2.metric(
            "Placement",
            placement_count
        )

        col3.metric(
            "Result",
            result_count
        )

        col4.metric(
            "Event",
            event_count
        )

        st.divider()


        notifications.sort(
            key=calculate_score,
            reverse=True
        )

        top10 = notifications[:10]

        

        st.subheader("🏆 Top 10 Priority Notifications")

        for rank, notification in enumerate(
            top10,
            start=1
        ):

            score = calculate_score(
                notification
            )

            with st.container():

                st.markdown(
                    f"""
### #{rank} | {notification['Type']}

**Message:** {notification['Message']}

**Timestamp:** {notification['Timestamp']}

**Priority Score:** {score}
"""
                )

                st.divider()