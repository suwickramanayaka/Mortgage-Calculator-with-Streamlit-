import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
    .about-title {
        color: #4CAF50;
        font-size: 2em;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .about-section {
        margin-top: 20px;
        font-size: 1.2em;
        line-height: 1.6;
    }
    .about-highlight {
        color: #FF5722;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="about-title">About This App</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="about-section">
    Welcome to the <span class="about-highlight">Mortgage Repayments Calculator</span> app! This application is designed to help you calculate your mortgage repayments, total repayments, and total interest paid over the life of the loan. 

    ### Features:
    - **Mortgage Calculator**: Input your home value, deposit, interest rate, and loan term to calculate your monthly repayments.
    - **Dashboard**: View detailed metrics and a payment schedule chart to understand your mortgage better.
    - **Profile**: Manage your personal information and keep track of your mortgage details.

    ### How to Use:
    1. Navigate to the **Mortgage Calculator** page and enter your mortgage details.
    2. View the calculated metrics and payment schedule.
    3. Check the **Dashboard** for a detailed breakdown of your mortgage.
    4. Update your personal information in the **Profile** section.

    This app is built using <span class="about-highlight">Streamlit</span>, a powerful and easy-to-use framework for creating interactive web applications in Python. We hope you find this tool useful in managing your mortgage and making informed financial decisions.

    If you have any questions or feedback, please feel free to reach out to us.

    Thank you for using the Mortgage Repayments Calculator app!
    </div>
    """,
    unsafe_allow_html=True,
)