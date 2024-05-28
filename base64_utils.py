# base64_utils.py
import base64

def encode_base64(input_text):
    """
    Encodes a given string into Base64.

    :param input_text: The string to encode.
    :return: The Base64 encoded string.
    """
    if input_text:
        encoded_bytes = base64.b64encode(input_text.encode("utf-8"))
        return encoded_bytes.decode("utf-8")
    return ""

def decode_base64(input_text):
    """
    Decodes a given Base64 encoded string.

    :param input_text: The Base64 string to decode.
    :return: The decoded string or an error message if decoding fails.
    """
    if input_text:
        try:
            decoded_bytes = base64.b64decode(input_text.encode("utf-8"))
            return decoded_bytes.decode("utf-8")
        except base64.binascii.Error:
            return "Error: Invalid Base64 input"
    return ""

def privacy_encode(text):
    return encode_base64(text)