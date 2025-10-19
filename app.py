# Import required libraries
import streamlit as st                    # Main Streamlit library for web app
from streamlit_option_menu import option_menu  # For creating navigation menu
from PIL import Image                     # For image processing
import requests                           # For making HTTP requests
from streamlit_lottie import st_lottie   # For Lottie animations

# Configure the Streamlit page settings
st.set_page_config(
    page_title="nIthin Portfolio",        # Browser tab title
    page_icon="👨‍💻",                     # Browser tab icon
    layout="wide"                         # Use wide layout for better spacing
)

# Function to load Lottie animations from URL
def load_lottie_url(url):
    """
    Fetches a Lottie animation JSON from a URL
    Args:
        url (str): URL of the Lottie animation
    Returns:
        dict: JSON response if successful, None if failed
    """
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load the coding animation for the About Me section
lottie_coding = load_lottie_url("https://lottie.host/embed/86b62f96-3b9c-4f65-8b11-x8d3504f8c27")

# Function to load and apply custom CSS styles
def local_css(file_name):
    """
    Reads and applies custom CSS styles from a file
    Args:
        file_name (str): Path to the CSS file
    """
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Try to load custom CSS styles, continue if file not found
try:
    local_css("styles/style.css")
except:
    pass

# Sidebar
with st.sidebar:
    # Initialize the option menu with navigation items
    selected = option_menu(
        menu_title="Main Menu",          # Title of the menu
        options=["About Me", "Experience", "Projects", "Blog", "Connect"],  # Menu items
        icons=["person", "briefcase", "code-slash", "pencil-square", "envelope"],  # Icons for each item
        menu_icon="cast",                # Main menu icon
        default_index=0,                 # First item selected by default
    )

# Create the header section with name and title
st.markdown("<h1 style='text-align: center;'>Nithin</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Software Engineer</h3>", unsafe_allow_html=True)

# Display content based on sidebar selection
if selected == "About Me":
    st.header("About Me")
    # Create two columns with ratio 2:1
    col1, col2 = st.columns([2, 1])
    with col1:
        # Left column: About me text
        st.write("random text for hrs will edit it later")
    with col2:
        # Right column: Animation
        if lottie_coding:
            st_lottie(lottie_coding, height=300)  # Display the coding animation

# Experience Section
elif selected == "Experience":
    st.header("Work Experience")
    # Display current/most recent work experience
    st.subheader("HCL Technologies")
    st.write("Software Engineer | 4 years")
    st.write("Key Responsibilities:")
    # List of key responsibilities
    st.write("- Developed and maintained enterprise applications")
    st.write("- Collaborated with cross-functional teams")
    st.write("- Implemented best practices and coding standards")

# Projects Section
elif selected == "Projects":
    st.header("Projects")
    # Create two columns for project cards
    col1, col2 = st.columns(2)
    
    # First Project Card
    with col1:
        st.subheader("Project 1")
        st.write("E-commerce Platform")
        st.write("Technologies: Python, React, MongoDB")
        st.write("• Built a full-stack e-commerce platform")
        st.write("• Implemented secure payment gateway")
    
    # Second Project Card    
    with col2:
        st.subheader("Project 2")
        st.write("AI Chat Assistant")
        st.write("Technologies: Python, TensorFlow, Flask")
        st.write("• Developed an AI-powered chat assistant")
        st.write("• Integrated natural language processing")

# Blog Section
elif selected == "Blog":
    st.header("Blog Posts")
    # Display link to Medium profile
    st.write("Check out my latest articles on Medium:")
    st.markdown("[Visit My Medium Profile](https://medium.com/@yourusername)")

# Connect Section
elif selected == "Connect":
    st.header("Let's Connect!")
    # Create three columns for social media links
    cols = st.columns(3)
    
    # LinkedIn Profile Link with badge
    with cols[0]:
        st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/yourusername)")
    
    # GitHub Profile Link with badge
    with cols[1]:
        st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/yourusername)")
    
    # Twitter Profile Link with badge
    with cols[2]:
        st.markdown("[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/yourusername)")

# Footer Section
# Creates a fixed footer at the bottom of the page with copyright information
st.markdown("""
<footer style='position: fixed; left: 0; bottom: 0; width: 100%; background-color: #0E1117; color: grey; text-align: center; padding: 10px;'>
    <p>© 2025 nitindatails.com. All rights reserved.</p>
</footer>
""", unsafe_allow_html=True)