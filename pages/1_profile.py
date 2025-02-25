import streamlit as st

# Custom CSS for styling
st.markdown(
    """
    <style>
    .profile-title {
        color: #4CAF50;
        font-size: 2em;
        font-weight: bold;
    }
    .profile-section {
        margin-top: 20px;
    }
    .profile-label {
        color: #FF5722;
        font-size: 1.2em;
        font-weight: bold;
    }
    .profile-value {
        color: #2196F3;
        font-size: 1.2em;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="profile-title">Profile</div>', unsafe_allow_html=True)

# Profile information
st.markdown('<div class="profile-section">', unsafe_allow_html=True)
st.markdown('<div class="profile-label">Name:</div>', unsafe_allow_html=True)
st.markdown('<div class="profile-value">Sithum Wickramanayaka</div>', unsafe_allow_html=True)

st.markdown('<div class="profile-section">', unsafe_allow_html=True)
st.markdown('<div class="profile-label">Email:</div>', unsafe_allow_html=True)
st.markdown('<div class="profile-value">suwickramanayaka@gmail.com</div>', unsafe_allow_html=True)

st.markdown('<div class="profile-section">', unsafe_allow_html=True)
st.markdown('<div class="profile-label">Phone:</div>', unsafe_allow_html=True)
st.markdown('<div class="profile-value">+94 ** *****</div>', unsafe_allow_html=True)

st.markdown('<div class="profile-section">', unsafe_allow_html=True)
st.markdown('<div class="profile-label">Address:</div>', unsafe_allow_html=True)
st.markdown('<div class="profile-value">123 Main St, Anytown, USA</div>', unsafe_allow_html=True)