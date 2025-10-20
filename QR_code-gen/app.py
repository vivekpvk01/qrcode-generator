import streamlit as st
import qrcode
import os  # <-- for folder creation

# Ensure images folder exists
if not os.path.exists("images"):
    os.makedirs("images")

st.title("🌐 QR Code Generator")
st.write("Convert any link into a QR code instantly!")

url = st.text_input("Enter the URL to generate a QR Code:")

if st.button("Generate"):
    if url.strip():
        img = qrcode.make(url)
        img.save("images/qrcode.png")  # folder now guaranteed to exist
        st.image("images/qrcode.png", caption="Generated QR Code", use_container_width=True)
        st.success("✅ QR Code generated successfully!")
    else:
        st.warning("⚠️ Please enter a valid URL.")
