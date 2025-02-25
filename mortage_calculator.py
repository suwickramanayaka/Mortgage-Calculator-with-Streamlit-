import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title {
        color: #4CAF50;
        font-size: 2em;
        font-weight: bold;
    }
    .input-label {
        color: #FF5722;
        font-size: 1.2em;
    }
    .metric-label {
        color: #2196F3;
        font-size: 1.2em;
    }
    .error {
        color: #F44336;
        font-size: 1.2em;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title">Mortgage Repayments Calculator</div>', unsafe_allow_html=True)
st.write("### Input Data")

# Input columns
col1, col2 = st.columns(2)
home_value = col1.number_input('Home Value ($)', min_value=0, value=500000, step=1000, format="%d")
deposit = col1.number_input('Deposit ($)', min_value=0, value=100000, step=1000, format="%d")
interest_rate = col2.number_input('Interest Rate (%)', min_value=0.0, value=5.5, step=0.1, format="%.1f")
loan_term = col2.number_input('Loan Term (years)', min_value=1, value=30, step=1, format="%d")

# Additional inputs
col3, col4 = st.columns(2)
annual_income = col3.number_input('Annual Income ($)', min_value=0, value=75000, step=1000, format="%d")
other_expenses = col4.number_input('Other Monthly Expenses ($)', min_value=0, value=500, step=50, format="%d")

# Calculate the repayments
loan_amount = home_value - deposit
monthly_interest_rate = (interest_rate / 100) / 12
number_of_payments = loan_term * 12

# Ensure loan amount is positive
if loan_amount <= 0:
    st.markdown('<div class="error">The deposit must be less than the home value.</div>', unsafe_allow_html=True)
else:
    monthly_payment = (
        loan_amount
        * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
        / ((1 + monthly_interest_rate) ** number_of_payments - 1)
    )

    # Display the repayments
    total_payments = monthly_payment * number_of_payments
    total_interest = total_payments - loan_amount

    st.write("### Repayments")
    col1, col2, col3 = st.columns(3)
    col1.metric(label='Monthly Repayments', value=f"${monthly_payment:,.2f}")
    col2.metric(label='Total Repayments', value=f"${total_payments:,.0f}")
    col3.metric(label='Total Interest', value=f"${total_interest:,.0f}")

    # Store values in session state
    st.session_state['home_value'] = home_value
    st.session_state['loan_amount'] = loan_amount
    st.session_state['monthly_payment'] = monthly_payment
    st.session_state['total_payments'] = total_payments
    st.session_state['total_interest'] = total_interest

    # Create a data-frame with the payment schedule
    schedule = []
    remaining_balance = loan_amount

    for i in range(1, number_of_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment
        year = math.ceil(i / 12)  # Calculate the year into the loan
        schedule.append(
            [
                i,
                monthly_payment,
                principal_payment,
                interest_payment,
                remaining_balance,
                year,
            ]
        )

    df = pd.DataFrame(
        schedule,
        columns=["Month", "Payment", "Principal", "Interest", "Remaining Balance", "Year"],
    )

    # Store the payment schedule in session state
    st.session_state['payment_schedule'] = df

    # Display the data-frame as a chart
    st.write("### Payment Schedule")
    payments_df = df[["Year", "Remaining Balance"]].groupby("Year").min()
    st.line_chart(payments_df)