# Base64 Encoder/Decoder 

## Overview
This project is a simple Base64 encoder and decoder implemented using Python and the Tkinter library for the graphical user interface (GUI). It provides a user-friendly interface for encoding messages into Base64 and decoding Base64-encoded messages back into their original form. 
This project was completed by sophomore students from the Faculty of Electrical and Computer Engineering at the University of "Hasan Prishtina", under the expert guidance of Prof. Dr. Blerim Rexha and Ass. Mërgim Hoti, as part of our coursework in Data Security.

## Authors
- Adrian Mehaj
- Ag Hamiti
- Afrim Ymeri
- Adna Aslani

## Requirements
- Python 3.9 or later
- Tkinter (usually comes with Python, but can be installed separately if needed)
- PyCharm IDE (optional but recommended)

## How to Run
1. Ensure Python 3 is installed on your system.
2. Save the provided script as `base64_encoder_decoder.py`.
3. Open a terminal or command prompt and navigate to the directory where the script is located.
4. Run the script using the command:
   python base64_encoder_decoder.py
  
## Features
- **Encode**: Converts a user-inputted message into Base64 format.
- **Decode**: Converts a Base64-encoded message back into its original text.

## Usage
1. Launch the program by following the steps in the "How to Run" section.
2. Enter the message you wish to encode or decode into the input field.
3. Click the "Encode" button to encode the message to Base64 format.
4. Click the "Decode" button to decode a Base64-encoded message.
5. The result will be displayed below the buttons.

## Functions

### `custom_base64_encode(message)`
Encodes a given message to Base64 format.

- **Parameters**: `message` (str): The input message to encode.
- **Returns**: (str): The Base64-encoded message.

### `custom_base64_decode(encoded_message)`
Decodes a given Base64-encoded message.

- **Parameters**: `encoded_message` (str): The Base64-encoded message to decode.
- **Returns**: (str): The decoded original message.

### `encode_base64()`
Reads the input message from the GUI, encodes it using `custom_base64_encode`, and displays the encoded message.

### `decode_base64()`
Reads the Base64-encoded message from the GUI, decodes it using `custom_base64_decode`, and displays the decoded message.

### GUI Setup
The Tkinter GUI includes:
- An input field for entering the message to encode or decode.
- An "Encode" button to trigger the encoding process.
- A "Decode" button to trigger the decoding process.
- A label to display the result.

## Example Usage
1. **Input**:
    Message to encode: "Hello World"
  
2. **Output**:
   Encoded Message: "SGVsbG8gV29ybGQ="
   
3. **Input**:
   Message to decode: "SGVsbG8gV29ybGQ="
   
4. **Output**:
   Decoded Message: "Hello World"
   
## Notes
- The script handles all characters that can be entered in the input field, including letters (A-Z, a-z), numbers (0-9), and special characters.
- Error handling is in place for invalid inputs.
  
## Expected Outcomes
- Enhanced Security: This Base64 encoder/decoder adds an extra layer of security to your messages.
- Ease of Use: With a user-friendly GUI, users can easily encode and decode messages.
- Correctness: The script ensures accurate encoding and decoding processes.
- Error Handling: The script includes basic error handling to manage invalid inputs smoothly.

## Conclusion
This project demonstrates a simple implementation of Base64 encoding and decoding using Python and Tkinter. It provides an easy-to-use interface for users to convert messages to and from Base64 format. The project can be extended with additional features and improved error handling for a more robust application.

