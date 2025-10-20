import qrcode
# Ask user for input
data = input("Enter the text or link to generate a QR code: ")
# Create QR code
img = qrcode.make(data)
# Ask for a file name (optional)
file_name = input("Enter file name to save (without extension): ")
# Save as .png
img.save(f"{file_name}.png")
print(f"✅ QR Code saved successfully as '{file_name}.png'")
