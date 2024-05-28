# ende.py
import tkinter as tk
from base64_utils import encode_base64, decode_base64

def update_output(event=None):
    input_text = input_text_box.get("1.0", tk.END).strip()
    if mode.get() == "Encode":
        output_text = encode_base64(input_text)
    else:
        output_text = decode_base64(input_text)
    
    output_text_box.config(state=tk.NORMAL)
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, output_text)
    output_text_box.config(state=tk.DISABLED)

def on_mode_change():
    input_text_box.delete("1.0", tk.END)
    update_output()

def privacy_encode():
    input_text = input_text_box.get("1.0", tk.END).strip()
    encoded_text = encode_base64(input_text)
    input_text_box.delete("1.0", tk.END)
    input_text_box.insert(tk.END, encoded_text)

# Set up the main application window
root = tk.Tk()
root.title("Live Base64 Encoder/Decoder")

# Mode selection
mode = tk.StringVar(value="Encode")

encode_radio = tk.Radiobutton(root, text="Encode", variable=mode, value="Encode", command=on_mode_change)
encode_radio.pack()

decode_radio = tk.Radiobutton(root, text="Decode", variable=mode, value="Decode", command=on_mode_change)
decode_radio.pack()

# Input text box
input_label = tk.Label(root, text="Input")
input_label.pack()

input_text_box = tk.Text(root, height=10, width=50)
input_text_box.pack()
input_text_box.bind("<KeyRelease>", update_output)

# Output text box
output_label = tk.Label(root, text="Output")
output_label.pack()

output_text_box = tk.Text(root, height=10, width=50, state=tk.DISABLED)
output_text_box.pack()

# Privacy Encode button
privacy_encode_button = tk.Button(root, text="Privacy Encode", command=privacy_encode)
privacy_encode_button.pack()

# Enable computer shortcuts in text boxes
def enable_shortcuts(event):
    if event.state == 4:  # 4 means Ctrl key is pressed
        if event.keysym.lower() in ["x", "c", "v"]:
            return
        if event.keysym.lower() == "a":
            input_text_box.tag_add(tk.SEL, "1.0", tk.END)
            input_text_box.mark_set(tk.INSERT, "1.0")
            input_text_box.see(tk.INSERT)
            return "break"
    
    input_text_box.event_generate(event)
    output_text_box.event_generate(event)

input_text_box.bind_all("<Control-a>", enable_shortcuts)
input_text_box.bind_all("<Control-x>", enable_shortcuts)
input_text_box.bind_all("<Control-c>", enable_shortcuts)
input_text_box.bind_all("<Control-v>", enable_shortcuts)

output_text_box.bind_all("<Control-a>", enable_shortcuts)
output_text_box.bind_all("<Control-x>", enable_shortcuts)
output_text_box.bind_all("<Control-c>", enable_shortcuts)
output_text_box.bind_all("<Control-v>", enable_shortcuts)

# Run the application
root.mainloop()
