import streamlit as st
import requests #url lottie
import base64 
from streamlit_lottie import st_lottie
import sys
sys.path.append('E:\\Anmol_Projects\\FX_Project\\code\\website')

# # *******************************************************************************************************************
# Here we are setting the page configuration: page icon, page title, layout type
st.set_page_config(page_title="FX_Exchange", page_icon="🪙" , layout="wide")
# # *******************************************************************************************************************



# *******************************************************************************************************************
# Here we are Styling the sidebar of the website
st.markdown("""
<style>
    [data-testid="stSidebar"] {
        background: black;
        font-size: 18px;
        color: white;
    }
</style>
""", unsafe_allow_html=True)
# *******************************************************************************************************************



# *******************************************************************************************************************
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header{visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# We are using this section, to add background-image to the website
def get_base64(bin_file):#accepts in binary
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode() ##returns content encoded in base64 format


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    backgr
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background('E:/Anmol_Projects/FX_Project/code/bg1.png')
# *******************************************************************************************************************





# *******************************************************************************************************************
# This code can be used for a Lottie animation
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_encoding=load_lottieurl("https://lottie.host/6a73bccf-1edf-4dc6-8e14-c06d80bcf7aa/1vtngsI2fN.json")
# *******************************************************************************************************************



# *******************************************************************************************************************
# Used for importing the Css file ( style.css)
def local_css():
    with open("E:/Anmol_Projects/FX_Project/code/website/style/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# *******************************************************************************************************************



# *******************************************************************************************************************
# Code For Home Page
def webcode():    
    local_css()
    with st.container():
        original_title = '<p style="position:relative;top:-120px;color:White;font-weight:500; font-size: 32px;"><b><u>FXBoost</u></b></p>'
        st.markdown(original_title, unsafe_allow_html=True)
        original_title = '<p style=" position:relative;color:white;font-weight:bold; font-size: 20px;top:-130px;padding-left:50px;padding-right:50px;">Welcome to FXBoost! <br>Your Gateway to Real-Time Currency Exchange Rates!<br><br>Unlock the world of seamless currency conversions with our user-friendly app. Whether you are a globe-trotter, a business professional, or simply keeping an eye on international markets, FXBoost is your go-to companion for accurate and up-to-the-minute exchange rates.</p>'
        st.markdown(original_title, unsafe_allow_html=True)

    with st.container():
        left_col,right_col=st.columns((2,2))
        with left_col:
            original_title = '<p style=" position:relative;top:-100px;color:White; font-size: 32px;"><b><u>Key Features: </u></b></p>'
            st.markdown(original_title, unsafe_allow_html=True)
            original_title = '<p style=" position:relative;color:white;font-weight:bold; font-size: 20px;top:-110px;padding-left:50px;padding-right:50px;">Global Currency Support<br></p>'
            st.markdown(original_title, unsafe_allow_html=True)
            original_title = '<p style=" position:relative;color:white;font-weight:bold; font-size: 20px;top:-110px;padding-left:50px;padding-right:50px;">Intuitive Interface<br></p>'
            st.markdown(original_title, unsafe_allow_html=True)
            original_title = '<p style=" position:relative;color:white;font-weight:bold; font-size: 20px;top:-110px;padding-left:50px;padding-right:50px;">Historical Data<br></p>'
            st.markdown(original_title, unsafe_allow_html=True)
            original_title = '<p style=" position:relative;color:white;font-weight:bold; font-size: 20px;top:-110px;padding-left:50px;padding-right:50px;">Real-Time Rates</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            original_title = '<p style=" position:relative;color:white;font-weight:bold; font-size: 20px;top:-110px;padding-left:50px;padding-right:50px;">Offline Mode</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            original_title = '<p style=" position:relative;color:white;font-weight:bold; font-size: 32px;top:-110px;"><b><u>Why Opt for FXBoost?</u></b></p>'
            st.markdown(original_title, unsafe_allow_html=True)
            original_title = '<p style=" position:relative;color:white;font-weight:bold; font-size: 20px;top:-130px;padding-left:50px;padding-right:50px;"><br>Precision and Reliability:<br>Count on us for accurate and reliable exchange rates sourced from trusted financial sources.<br><br>Global Reach:<br>Accessible wherever you are, FXBoost ensures you are connected to the world of currencies, whether you are at home or on the go.</p>'
            st.markdown(original_title, unsafe_allow_html=True)
            original_title = '<p style=" position:relative;top:-120px;color:White; font-size: 32px;"><b><u>Contact Us: </u></b></p>'
            st.markdown(original_title, unsafe_allow_html=True)

            # contact form for User query
            contact_form="""
            <form action="https://formsubmit.co/comderboi@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your Name" required><input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Query" required></textarea>
            <button type="submit">Send</button></form>"""

        left_column ,right_column =st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()
                
        with right_col:#For animation
            st_lottie(lottie_encoding,height=350,key="coding")

    #Moving the web page content
    st.markdown(
    """
    <style>
        [data-testid="stContainer"] [data-testid="stHorizontalBlock"] {
            margin-top: -100px;  /* Adjust the value to move the Lottie animation upwards */
        }
    </style>
    """,
    unsafe_allow_html=True,
)
# *******************************************************************************************************************


if __name__ == '__main__':
    webcode()

