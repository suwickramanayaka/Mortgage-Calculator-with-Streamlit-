import streamlit as st
import pandas as pd
import numpy as np

# Custom CSS for styling
st.markdown(
    """
    <style>
    .dashboard-title {
        color: #4CAF50;
        font-size: 2em;
        font-weight: bold;
    }
    .dashboard-section {
        margin-top: 20px;
    }
    .dashboard-metric {
        color: #2196F3;
        font-size: 1.2em;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="dashboard-title">Dashboard</div>', unsafe_allow_html=True)

# Check if the necessary values are in session state
if 'home_value' in st.session_state and 'loan_amount' in st.session_state and 'monthly_payment' in st.session_state and 'total_payments' in st.session_state and 'total_interest' in st.session_state and 'payment_schedule' in st.session_state:
    home_value = st.session_state['home_value']
    loan_amount = st.session_state['loan_amount']
    monthly_payment = st.session_state['monthly_payment']
    total_payments = st.session_state['total_payments']
    total_interest = st.session_state['total_interest']
    payment_schedule = st.session_state['payment_schedule']

    # Display the metrics
    st.markdown('<div class="dashboard-section">', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Home Value", value=f"${home_value:,.0f}")
    col2.metric(label="Loan Amount", value=f"${loan_amount:,.0f}")
    col3.metric(label="Monthly Repayments", value=f"${monthly_payment:,.2f}")
    col4.metric(label="Total Interest", value=f"${total_interest:,.0f}")

    # Display the payment schedule chart
    st.markdown('<div class="dashboard-section">', unsafe_allow_html=True)
    st.markdown('<div class="dashboard-metric">Payment Schedule</div>', unsafe_allow_html=True)
    payments_df = payment_schedule[["Year", "Remaining Balance"]].groupby("Year").min()
    st.line_chart(payments_df)

    # Display the payment schedule table
    st.markdown('<div class="dashboard-section">', unsafe_allow_html=True)
    st.markdown('<div class="dashboard-metric">Payment Schedule Table</div>', unsafe_allow_html=True)
    st.table(payment_schedule)
else:
    st.markdown('<div class="dashboard-section">', unsafe_allow_html=True)
    st.markdown('<div class="dashboard-metric">No mortgage data available. Please calculate the mortgage first.</div>', unsafe_allow_html=True)