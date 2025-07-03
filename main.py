from tkinter import *
from tkinter import filedialog
from PIL import *

def close_app():
    window.quit()

def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpeg;*.png;*.jpg")])

def add_logo():
    file_path =  filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpeg;*.jpg")])



# GUI setup
window = Tk()
window.title("Image Watermarker")
window.geometry('1000x600')
window.configure(bg="#f5f5f5")

# Configure window grid
window.grid_rowconfigure(0, weight=0)
window.grid_columnconfigure(0, weight=1)

# Top bar frame (full width)
frame = LabelFrame(window, bg="#e9ecef", padx=10, pady=10, border=0)
frame.grid(row=0, column=0, sticky="ew")

# Configure 3 columns inside the frame
frame.grid_columnconfigure(0, weight=1)  # Left (label)
frame.grid_columnconfigure(1, weight=1)  # Center (buttons)
frame.grid_columnconfigure(2, weight=1)  # Right (close)

# Left: App title
label = Label(frame,
              text="Image Watermarker",
              font=("Times New Roman", 20, "bold"),
              bg="#e9ecef", fg="#0077b6")
label.grid(column=0, row=0, sticky="w", padx=5)

# CENTER: A sub-frame to hold Add Text and Add Logo buttons side-by-side
center_frame = Frame(frame, bg="#e9ecef")
center_frame.grid(column=1, row=0)

# Add Text button
add_text_btn = Button(
    center_frame,
    text="Add Text",
    command=select_image,
    font=("Times New Roman", 13),
    bg="white",
    fg="#00b4d8",
    highlightthickness=0,
    bd=0,
    padx=10,
    pady=5,
)
add_text_btn.pack(side=LEFT, padx=(0, 10))  # right space between buttons

# Add Logo button
add_logo_btn = Button(
    center_frame,
    text="Add Logo",
    font=("Times New Roman", 13),
    bg="white",
    fg="#00b4d8",
    highlightthickness=0,
    bd=0,
    padx=10,
    pady=5,
    command=add_logo
)
add_logo_btn.pack(side=LEFT)

# Right: Close App button
close_btn = Button(
    frame,
    text="Close App",
    font=("Times New Roman", 13),
    command=close_app,
    bg="white",
    fg="#00b4d8",
    highlightthickness=0,
    bd=0,
    padx=10,
    pady=5,
)
close_btn.grid(column=2, row=0, padx=5, pady=5, sticky="e")


select_img_btn = Button(window,
                        text="Upload Image and Watermark",
                        command=select_image,
                        padx=5,
                        pady=5,
                        highlightthickness=0,
                        bd=0,
                        font=("Times New Roman", 20, "bold"),
                        fg="#a2d2ff"
                        )
select_img_btn.grid(column=0, row=1, padx=20, pady=20)

image_label = Label(window, bg="#f5f5f5")
image_label.grid(column=0, row=2, columnspan=3)
# Run the app
window.mainloop()
