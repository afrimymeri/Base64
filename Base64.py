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