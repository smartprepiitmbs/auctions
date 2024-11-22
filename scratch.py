import streamlit as st
import pandas as pd
import base64

# Define overview data for IPL 2025 squad size, salary cap, and available slots
overview_data = {
    "Franchise": ["CSK", "DC", "GT", "KKR", "LSG", "MI", "PBKS", "RCB", "RR", "SRH", "Total"],
    "No of Players": [5, 4, 5, 6, 5, 5, 2, 3, 6, 5, 46],
    "No of Overseas Players": [1, 1, 1, 2, 1, 0, 0, 0, 1, 3, 10],
    "No of Uncapped Players": [1, 1, 2, 2, 2, 0, 2, 1, 1, 0, 12],
    "RTM": [1, 2, 1, 0, 1, 1, 4, 3, 0, 1, 14],
    "Total Money Spent (Rs. Cr)": [65, 47, 51, 69, 51, 75, 9.5, 37, 79, 75, 558.5],
    "Salary Cap Available (Rs. Cr)": [55, 73, 69, 51, 69, 45, 110.5, 83, 41, 45, 641.5],
    "Available Slots": [20, 21, 20, 19, 20, 20, 23, 22, 19, 20, 204],
    "Overseas Slots": [7, 7, 7, 6, 7, 8, 8, 8, 7, 5, 70]
}

# Convert overview data to a DataFrame
overview_df = pd.DataFrame(overview_data)

# Display the overview table
st.title("IPL 2025 Squad Overview")
st.subheader("Squad Size / Salary Cap / Available Slots")
st.write(overview_df.style.set_table_styles([{
    'selector': 'th',
    'props': [('background-color', '#007ACC'), ('color', 'white')]
}]))

# Define team-specific data based on the screenshot
teams_data = {
    "CSK": {
        "Players": ["Ruturaj Gaikwad", "Matheesha Pathirana*", "Shivam Dube", "Ravindra Jadeja", "MS Dhoni"],
        "Deduction": [1800, 1300, 1200, 1800, 400],
        "Total Money Spent": 6500,
        "Total Retention Deduction": 6500,
        "Salary Cap Available": 5500,
        "Primary Color": "#FFC107"
    },
    "DC": {
        "Players": ["Axar Patel", "Kuldeep Yadav", "Tristan Stubbs*", "Abhishek Porel"],
        "Deduction": [1650, 1325, 1000, 400],
        "Total Money Spent": 4375,
        "Total Retention Deduction": 4700,
        "Salary Cap Available": 7300,
        "Primary Color": "#17429D"
    },
    "GT": {
        "Players": ["Rashid Khan*", "Shubman Gill", "Sai Sudharsan", "Rahul Tewatia", "Shahrukh Khan"],
        "Deduction": [1800, 1650, 850, 400, 400],
        "Total Money Spent": 5100,
        "Total Retention Deduction": 5100,
        "Salary Cap Available": 6900,
        "Primary Color": "#1C1C1C"
    },
    "KKR": {
        "Players": ["Rinku Singh", "Varun Chakravarthy", "Sunil Narine*", "Andre Russell*", "Harshit Rana",
                    "Ramandeep Singh"],
        "Deduction": [1300, 1200, 1600, 2000, 400, 400],
        "Total Money Spent": 6900,
        "Total Retention Deduction": 6900,
        "Salary Cap Available": 5100,
        "Primary Color": "#3A225D"
    },
    "LSG": {
        "Players": ["Nicholas Pooran*", "Ravi Bishnoi", "Mayank Yadav", "Moshin Khan", "Ayush Badoni"],
        "Deduction": [2100, 1100, 400, 1000, 400],
        "Total Money Spent": 5100,
        "Total Retention Deduction": 5100,
        "Salary Cap Available": 6900,
        "Primary Color": "#D5C026"
    },
    "MI": {
        "Players": ["Jasprit Bumrah", "Suryakumar Yadav", "Hardik Pandya", "Rohit Sharma", "Tilak Verma"],
        "Deduction": [1800, 1635, 1635, 1630, 800],
        "Total Money Spent": 7500,
        "Total Retention Deduction": 7500,
        "Salary Cap Available": 4500,
        "Primary Color": "#004BA0"
    },
    "PBKS": {
        "Players": ["Shashank Singh", "Prabhsimran Singh"],
        "Deduction": [550, 400],
        "Total Money Spent": 950,
        "Total Retention Deduction": 950,
        "Salary Cap Available": 11050,
        "Primary Color": "#ED1B24"
    },
    "RR": {
        "Players": ["Sanju Samson", "Yashasvi Jaiswal", "Riyan Parag", "Dhruv Jurel", "Shimron Hetmyer*",
                    "Sandeep Sharma"],
        "Deduction": [1800, 1800, 400, 400, 1100, 400],
        "Total Money Spent": 7900,
        "Total Retention Deduction": 7900,
        "Salary Cap Available": 4100,
        "Primary Color": "#FFC1D1"
    },
    "RCB": {
        "Players": ["Virat Kohli", "Rajat Patidar", "Yash Dayal"],
        "Deduction": [2100, 1100, 500],
        "Total Money Spent": 3700,
        "Total Retention Deduction": 3700,
        "Salary Cap Available": 8300,
        "Primary Color": "#A6123D"
    },
    "SRH": {
        "Players": ["Pat Cummins*", "Abhishek Sharma", "Nitish Kumar Reddy", "Heinrich Klaasen*", "Travis Head*"],
        "Deduction": [1800, 1400, 500, 2300, 1400],
        "Total Money Spent": 7500,
        "Total Retention Deduction": 7500,
        "Salary Cap Available": 4500,
        "Primary Color": "#FF822A"
    }
}

# Display the retained players tables in two columns
st.subheader("Retained Players by Team")

# Create two columns for displaying the tables
col1, col2 = st.columns(2)

# List of team names in the order we want to display
team_names = list(teams_data.keys())

# Loop through the teams and assign each team table to either col1 or col2
for idx, team in enumerate(team_names):
    team_data = teams_data[team]

    # Select the appropriate column based on the index
    column = col1 if idx < 5 else col2

    with column:
        st.subheader(f"{team} Retained Players")

        # DataFrame for players and deductions
        df = pd.DataFrame({
            "Player": team_data["Players"],
            "Deduction (Lakhs)": team_data["Deduction"]
        })

        # Display team-specific table with custom background color for headers
        st.write(
            df.style.set_table_styles([{
                'selector': 'th',
                'props': [('background-color', team_data["Primary Color"]), ('color', 'white')]
            }])
        )

        # Display team summary information below the table
        st.write(f"**Total Money Spent (Rs. Lakhs):** {team_data['Total Money Spent']}")
        st.write(f"**Total Retention Deduction (Rs. Lakhs):** {team_data['Total Retention Deduction']}")
        st.write(f"**Salary Cap Available (Rs. Lakhs):** {team_data['Salary Cap Available']}")


def display_pdf(pdf_file_path):
    with open(pdf_file_path, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="900" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

# Title
st.title(" IPL 2025 Available Players for Auction")

# Path to the PDF file
pdf_file_path = "data/Hindustan Times.pdf"

# Display the PDF
display_pdf(pdf_file_path)

