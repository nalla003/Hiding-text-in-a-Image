import cv2
import os

def encrypt_image(img_path, message, password):
    img = cv2.imread(img_path)

    d = {chr(i): i for i in range(256)}
    n = m = z = 0

    for char in message:
        img[n, m, z] = d[char]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3

    encrypted_path = "Encryptedmsg.jpg"
    cv2.imwrite(encrypted_path, img)
    os.system(f"start {encrypted_path}")

    return encrypted_path

def decrypt_image(encrypted_path, passcode):
    img = cv2.imread(encrypted_path)
    c = {i: chr(i) for i in range(256)}

    message = ""
    n = m = z = 0

    if passcode == password:
        for _ in range(len(message)):
            message += c[img[n, m, z]]
            n = n + 1
            m = m + 1
            z = (z + 1) % 3
        print("Decrypted message:", message)
    else:
        print("Invalid passcode")

# Example usage
image_path = "mypic.jpg"
secret_message = input("Enter secret message: ")
password = input("Enter password: ")

encrypted_path = encrypt_image(image_path, secret_message, password)

passcode_input = input("Enter passcode for decryption: ")
decrypt_image(encrypted_path, passcode_input)
