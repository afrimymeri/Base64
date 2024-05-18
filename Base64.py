import tkinter as tk

def custom_base64_encode(message):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    encoded_chars = []

    # Konvertimi i karaktereve të mesazhit në ASCII
    ascii_values = [ord(char) for char in message]
    binary_strings = ['{:08b}'.format(ascii_val) for ascii_val in ascii_values]

    # Kombinimi i stringjeve binare në një string të vetëm
    binary_message = ''.join(binary_strings)

    while len(binary_message) % 6 != 0:
        binary_message += '0'

    for i in range(0, len(binary_message), 6):
        chunk = binary_message[i:i + 6]
        decimal_value = int(chunk, 2)
        encoded_chars.append(base64_chars[decimal_value])

    # Shto padding në fund nëse është e nevojshme
    padding_length = len(encoded_chars) % 4
    if padding_length != 0:
        encoded_chars.extend(['='] * (4 - padding_length))

    return ''.join(encoded_chars)

def custom_base64_decode(encoded_message):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    decoded_chars = []

    try:
        encoded_message = encoded_message.rstrip('=')
        binary_message = ''
        for char in encoded_message:
            if char in base64_chars:
                decimal_value = base64_chars.index(char)
                binary_message += '{:06b}'.format(decimal_value)
            else:
                raise ValueError("Invalid character in encoded message")

        # Hiq bitët shtesë në fund
        while len(binary_message) % 8 != 0:
            binary_message = binary_message[:-1]

        for i in range(0, len(binary_message), 8):
            chunk = binary_message[i:i + 8]
            if len(chunk) == 8:
                decoded_chars.append(chr(int(chunk, 2)))

        return ''.join(decoded_chars)
    except ValueError as ve:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, f"Error: {ve}")
        return ""
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: Invalid input for decoding")
        return ""
def encode_base64():
    message = entry.get()
    
    if all(ord(char) < 128 for char in message):
        if message:
            encoded_message = custom_base64_encode(message)
            if encoded_message:
                result_text.delete(1.0, tk.END)
                result_text.insert(tk.END, "Encoded Message: " + encoded_message)
        else:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Error no input provided")
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: Input contains non-ASII characters.")

def decode_base64():
    encoded_message = entry.get()
    if encoded_message:
        decoded_message = custom_base64_decode(encoded_message)
        if decoded_message:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Decoded message: " + decoded_message)
    else:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Error: No input provided.")

# GUI setup
root = tk.Tk()
root.title("Base64 Encoder/Decoder")

# Vendos madhësinë dhe pozicionin e dritares
window_width = 400
window_height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry('%dx%d+%d+%d' % (window_width, window_height, x_coordinate, y_coordinate))

# Fusha e hyrjes
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Butoni Encode
encode_button = tk.Button(root, text="Encode", width=20, height=2, command=encode_base64)
encode_button.pack()

# Butoni Decode
decode_button = tk.Button(root, text="Decode", width=20, height=2, command=decode_base64)
decode_button.pack()

# Etiketa e rezultatit
result_text = tk.Text(root, height=4, wrap=tk.WORD)
result_text.pack(pady=10)
result_text.config(state=tk.NORMAL)

root.mainloop()
