import streamlit as st
from PIL import Image
# from utility import login
from src.db_connection import get_database_connection


logo_image = Image.open("img/company_logo.png")
ai_image = Image.open("img/company_banner.png")

st.set_page_config(page_title="Grow with Data", page_icon=logo_image, layout="wide")

col1, col2 = st.columns([1, 3])

with col1:
    st.image(logo_image, width=100)

with col2:
    st.markdown("# Welcome to Grow with Data : seedling:")

st.header("Personal Expense Tracker")

st.markdown('''
            ###  Project Features
            - User Authentication: Secure login system for personal use.
            - Expense Management: Ability to add, view, edit, and delete expenses.
            - Data Persistence: Save and retrieve expense data using files and databases.
            - Categorization: Organize expenses into categories.
            - Reporting: Visualize expenses with charts and summaries.
            - Interactive GUI: A user-friendly web interface using Streamlit.
            - Cloud Deployment: Deploy the application to the cloud using DigitalOcean.

''')

def menu():
    st.sidebar.header("What's your choice?")
    task = st.sidebar.selectbox('--------',
                                ('--------',
                                 'Save Expense Record',
                                 'Parameter Insertion'
                                 'Reporting'))
    
    if task == 'Save Expense Record':
        cursor, db = get_database_connection()
        save_expense(cursor, db)

# @login
def main():
    menu()


if __name__ == '__main__':
    main()