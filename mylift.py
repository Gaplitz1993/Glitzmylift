import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta

# Mock data
vehicles = [
    {"id": 1, "type": "Car", "capacity": 4, "available": True},
    {"id": 2, "type": "Van", "capacity": 7, "available": True},
    {"id": 3, "type": "Bus", "capacity": 20, "available": False},
]

ride_history = [
    {"date": "2024-09-15", "from": "Downtown", "to": "Airport", "vehicle": "Car", "cost": 25},
    {"date": "2024-09-18", "from": "Suburb", "to": "City Center", "vehicle": "Van", "cost": 35},
]

def book_ride(pickup, dropoff, passengers):
    available_vehicles = [v for v in vehicles if v["available"] and v["capacity"] >= passengers]
    if not available_vehicles:
        return False
    
    vehicle = random.choice(available_vehicles)
    cost = random.randint(20, 50)
    ride_history.append({
        "date": datetime.now().strftime("%Y-%m-%d"),
        "from": pickup,
        "to": dropoff,
        "vehicle": vehicle["type"],
        "cost": cost
    })
    return True

def main():
    st.title("Transportation Service")

    menu = ["Book a Ride", "Available Vehicles", "Ride History"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Book a Ride":
        st.subheader("Book a Ride")
        pickup = st.text_input("Pickup Location")
        dropoff = st.text_input("Dropoff Location")
        passengers = st.number_input("Number of Passengers", min_value=1, max_value=20, value=1)
        
        if st.button("Book Now"):
            if book_ride(pickup, dropoff, passengers):
                st.success("Ride booked successfully!")
            else:
                st.error("No available vehicles for the requested capacity.")

    elif choice == "Available Vehicles":
        st.subheader("Available Vehicles")
        df = pd.DataFrame(vehicles)
        st.table(df)

    elif choice == "Ride History":
        st.subheader("Ride History")
        df = pd.DataFrame(ride_history)
        st.table(df)

if __name__ == "__main__":
    main()