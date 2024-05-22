import streamlit as st

def load_css():
    css = """
<style>
    /* Sidebar and Header Styles */
    [data-testid="stSidebar"], [data-testid="stHeader"] {
        background-color: #f8f9fa;  /* Light grey background */
        color: #333 !important;  /* Dark grey text */
    }
    [data-testid="stSidebar"] {
        font-weight: bold;
        box-shadow: 2px 6px 8px rgba(0, 0, 0, 0.1);  /* Light shadow */
    }

    [data-testid="stSidebarNavLink"] {
        padding: 10px 20px;
        font-family: 'Roboto', sans-serif;
        border-radius: 5px;
        transition: color 0.3s;
    }

    [data-testid="stHeader"] {
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  /* Light shadow */
    }

    /* Main Content Area Styles */
    .main .block-container {
        max-width: 1200px; /* Increased width */
        margin: auto; /* Center align */
    }

    .st-emotion-cache-1v0mbdj.e115fcil1 img {
        transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out; /* Smooth transition for transformations */
        border: 2px solid #007bff; /* Blue border */
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1); /* Light shadow */
    }

    .st-emotion-cache-1v0mbdj.e115fcil1 img:hover {
        transform: scale(1.05); /* Scale up on hover */
        box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.2); /* Darker shadow on hover */
    }

    /* Text and Link Styles */
    [data-testid="StyledLinkIconContainer"], p, li {
        color: #333; /* Dark grey text */
    }
    .st-emotion-cache-bm2z3a {
        background-color: #ffffff; /* White background */
    }
    .st-emotion-cache-4d1onx p {
        color: #333; /* Dark grey text */
    }

    /* Metric Labels and Values */
    .st-emotion-cache-1tpl0xr p {
        font-size: 1.1rem; /* Custom font size for labels */
        font-weight: 600; /* Semi-bold for emphasis */
        color: #555; /* Medium grey text */
    }
    .st-emotion-cache-1wivap2 {
        font-size: 1.5rem; /* Custom font size for values */
        font-weight: bold;
        color: #007bff; /* Blue text */
        text-align: center; /* Center-aligned text */
    }
</style>
    """
    st.markdown(css, unsafe_allow_html=True)
