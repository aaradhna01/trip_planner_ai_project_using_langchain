import streamlit as st
from planner_chain import trip_chain
from datetime import date
from io import BytesIO

st.set_page_config(page_title="AI Trip Planner", layout="centered")

st.title("🌍 AI-Powered Trip Planner")
st.markdown("""
Plan your next trip with AI!  
🛏 Accommodation • 🍲 Local food • 🧭 Places to visit • 🚇 Travel tips
""")

# Session state to store response
if "response" not in st.session_state:
    st.session_state.response = ""

with st.form("trip_form"):
    from_city = st.text_input("🏡 From City", "India")
    to_city = st.text_input("✈️ Destination City", "Rome")
    departure = st.date_input("📅 Departure Date", date.today())
    return_date = st.date_input("📅 Return Date", date.today())
    interests = st.text_area("🎯 Your Interests (e.g., sightseeing, food, adventure)", "sightseeing and good food")

    submitted = st.form_submit_button("🗺 Generate Travel Plan")

    if submitted:
        with st.spinner("🧠 AI is preparing your personalized travel itinerary... Please wait."):
            st.session_state.response = trip_chain.run({
                "from_city": from_city,
                "to_city": to_city,
                "departure": departure.strftime("%Y-%m-%d"),
                "return_date": return_date.strftime("%Y-%m-%d"),
                "interests": interests
            })

# Show result & download button outside form
if st.session_state.response:
    st.success("✅ Your AI-Powered Travel Plan")
    st.write(st.session_state.response)

    buffer = BytesIO()
    buffer.write(st.session_state.response.encode())
    buffer.seek(0)
    st.download_button(
        label="📥 Download Travel Plan",
        data=buffer,
        file_name="travel_plan.txt",
        mime="text/plain"
    )
