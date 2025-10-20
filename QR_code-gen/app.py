import streamlit as st
import qrcode

st.title("🌐 QR Code Generator")
st.write("Convert any link into a QR code instantly!")

url = st.text_input("Enter the URL to generate a QR Code:")

if st.button("Generate"):
    if url.strip():
        img = qrcode.make(url)
        img.save("images/qrcode.png")
        st.image("images/qrcode.png", caption="Generated QR Code", use_container_width=True)
        st.success("✅ QR Code generated successfully!")
    else:
        st.warning("⚠️ Please enter a valid URL.")

