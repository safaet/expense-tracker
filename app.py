import streamlit as st
from PIL import Image
from utility import login
from src.db_connection import get_database_connection
from src.expense_op import save_expense


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
                                 'Parameter Insertion',
                                 'Reporting'))
    
    if task == 'Save Expense Record':
        cursor, db = get_database_connection()
        save_expense(cursor, db)

    elif task == 'Reporting':
        pass
    
    elif task == 'Parameter Insertion':
        pass

@login
def main():
    cols1, cols2, cols3 = st.columns((1, 4, 1))
    cols2.markdown("<h1 style='text-align: left;margin-top:-2rem; margin-left:1rem; color: #E12D06;'>Personal Expense Tracker</h1>", unsafe_allow_html=True)
    menu()


if __name__ == '__main__':
    main()