import qrcode as qr
img= qr.make("https://www.youtube.com/channel/UCPrvtkdh9bObravTI8bLajQ")
img.save("gyanganga_youtube.png")

# import qrcode
# from PIL import Image


# qr =qrcode.QRCode(version=1,
#                   error_correction= qrcode.constants.ERROR_CORRECT_H,
#                  box_size=10,border=4, )

# qr.add_data("https://www.youtube.com/channel/UCPrvtkdh9bObravTI8bLajQ")

# qr.make(fit=True)
# img=qr.make_image(fill_color="red", back_color="blue")
# img.save("gyan_ganga_youtube.png")