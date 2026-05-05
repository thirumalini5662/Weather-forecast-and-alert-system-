import streamlit as st
import requests

st.title("🌦️ Weather Forecast App")
st.write("Get real-time weather updates for any city")

city = st.text_input("Enter city name")

if city:
    url = f"https://wttr.in/{city}?format=j1"
    data = requests.get(url).json()

    temp = data["current_condition"][0]["temp_C"]
    humidity = data["current_condition"][0]["humidity"]
    wind = data["current_condition"][0]["windspeedKmph"]

    st.write(f"🌡 Temperature: {temp}°C")
    st.write(f"💧 Humidity: {humidity}%")
    st.write(f"🌬 Wind Speed: {wind} km/h")
condition = data["current_condition"][0]["weatherDesc"][0]["value"]
st.write(f"🌤 Condition: {condition}")
try:
    data = requests.get(url).json()
except:
    st.error("Failed to fetch data")
feels_like = data["current_condition"][0]["FeelsLikeC"]
st.write(f"🥵 Feels Like: {feels_like}°C")
c1, c2, c3 = st.columns(3)

c1.metric("🌡 Temp (°C)", temp)
c2.metric("💧 Humidity (%)", humidity)
c3.metric("🌬 Wind (km/h)", wind)
st.write("### 📅 Next Day Forecast")

forecast = data["weather"][0]

max_temp = forecast["maxtempC"]
min_temp = forecast["mintempC"]

st.write(f"🔺 Max Temp: {max_temp}°C")
st.write(f"🔻 Min Temp: {min_temp}°C")
import pandas as pd

hourly = data["weather"][0]["hourly"]

times = []
temps = []

for h in hourly:
    times.append(h["time"])
    temps.append(int(h["tempC"]))

df = pd.DataFrame({"Time": times, "Temperature": temps})

st.line_chart(df.set_index("Time"))
