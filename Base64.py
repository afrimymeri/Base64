import tkinter as tk

def custom_base64_encode(message):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    encoded_chars = []

    #Konvertimi i karaktereve te mesazhit ne ASCII
    ascii_values = [ord(char) for char in message]

    binary_strings = ['{:08b}'.format(ascii_val) for ascii_val in ascii_values]

    #Kombinimi i stringjeve binary ne nje string te vetem
    binary_message = ''.join(binary_strings)

    while len(binary_message) % 6 != 0:
        binary_message += '0'

    for i in range(0, len(binary_message), 6):
        chunk = binary_message[i:i + 6]
        decimal_value = int(chunk, 2)
        encoded_chars.append(base64_chars[decimal_value])

        padding_length = len(binary_message) % 24
    if padding_length != 0:
        encoded_chars.extend(['='] * (4 - padding_length // 6))

    return ''.join(encoded_chars)

def custom_base64_decode(encoded_message):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    decoded_chars = []

    encoded_message = encoded_message.rstrip('=')

    binary_message = ''
    for char in encoded_message:
        if char in base64_chars:
            decimal_value = base64_chars.index(char)
            binary_message += '{:06b}'.format(decimal_value)

    for i in range(0, len(binary_message), 8):
        chunk = binary_message[i:i + 8]
        decoded_chars.append(chr(int(chunk, 2)))

    return ''.join(decoded_chars)

def encode_base64():
    message = entry.get()
    encoded_message = custom_base64_encode(message)
    result_label.config(text="Encoded Message: " + encoded_message)


def decode_base64():
    encoded_message = entry.get()
    decoded_message = custom_base64_decode(encoded_message)
    result_label.config(text="Decoded Message: " + decoded_message)

