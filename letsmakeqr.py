import qrcode
import streamlit as st 
from PIL import Image



def makeqr(tit):

    input_data = tit
    qr = qrcode.QRCode(
             version=1,
             box_size=10,
            border=5)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode.png')
    image = Image.open('qrcode.png')
    st.image(image)
    



title = st.text_input('Input text/URL', )



if st.button('show the OR'):
    makeqr(title)


with open("qrcode.png", "rb") as file:
              btn = st.download_button(
                label="Download QR",
                data=file,
                file_name="flower.png",
                mime="image/png"
               )
    
