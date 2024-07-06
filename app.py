import tkinter as tk
from tkinter import Label, Button, Entry, Radiobutton, StringVar
from PIL import Image, ImageTk
from utils.api import get_similar_users, get_trust_label_items

class StormGeniusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("StormGenius")
        self.root.configure(bg='purple')

        # Load the image using Pillow
        self.robot_image = Image.open("stormgenius.png")
        self.robot_image = self.robot_image.resize((50, 50), Image.LANCZOS)  # Resize the image
        self.robot_image = ImageTk.PhotoImage(self.robot_image)

        # Create the initial layout
        self.label_frame = Label(self.root, bg='purple')
        self.label_frame.pack(pady=10, padx=10)

        self.image_label = Label(self.label_frame, image=self.robot_image, bg='purple')
        self.image_label.pack(side="left", padx=10)

        self.message_label = Label(self.label_frame, text="", bg='purple', fg='white', font=("Arial", 14), wraplength=300)
        self.message_label.pack(side="left", padx=10)

        self.input_var = StringVar()
        self.entry = Entry(self.root, textvariable=self.input_var, font=("Arial", 12))
        self.entry.pack(pady=10)
        self.entry.pack_forget()

        self.choice_var = StringVar(value="")
        self.choice_buttons = []

        self.submit_button = Button(self.root, text="Submit", command=self.on_submit, bg='white', fg='purple', font=("Arial", 12))
        self.submit_button.pack(pady=10)
        self.submit_button.pack_forget()

        self.current_step = 0
        self.steps = [
            ("🤖 Hi, this is StormGenius!\nWould you like a social score, financial score, or both?", ["social", "financial", "both"]),
            ("Please enter the user_id for the social score", None),
            ("Fetching social score...", None)
        ]
        
        self.results = {}

        self.show_step()

    def show_step(self):
        message, choices = self.steps[self.current_step]

        self.message_label.config(text=message)

        if choices:
            self.entry.pack_forget()
            self.choice_var.set("")
            for button in self.choice_buttons:
                button.pack_forget()
            self.choice_buttons = []
            for choice in choices:
                rb = Radiobutton(self.root, text=choice, variable=self.choice_var, value=choice, bg='purple', fg='white', selectcolor='purple', font=("Arial", 12))
                rb.pack(anchor='w')
                self.choice_buttons.append(rb)
        else:
            self.entry.pack()
            for button in self.choice_buttons:
                button.pack_forget()

        self.submit_button.pack()

    def on_submit(self):
        if self.current_step == 0:
            selected_choice = self.choice_var.get()
            if not selected_choice:
                return
            self.results["score_type"] = selected_choice
            if selected_choice == 'social':
                self.steps = [
                    ("🤖 Hi, this is StormGenius!\nWould you like a social score, financial score, or both?", ["social", "financial", "both"]),
                    ("Please enter the user_id for the social score", None),
                    ("Fetching social score...", None)
                ]
        else:
            user_input = self.input_var.get()
            if not user_input:
                return
            if self.current_step == 1:
                self.results["user_id"] = user_input

        self.current_step += 1

        if self.current_step < len(self.steps):
            self.show_step()
        else:
            self.fetch_and_display_results()

    def fetch_and_display_results(self):
        score_type = self.results["score_type"]
        
        self.message_label.config(text=f"🤖 Fetching {score_type} score...")
        self.root.update()

        try:
            if score_type == 'social':
                user_id = self.results["user_id"]
                trust_items = get_trust_label_items()
                result_message = f"Trust Label Items: {trust_items}"
            else:
                result_message = "Financial score calculation is not implemented."

            self.message_label.config(text=result_message)
            self.submit_button.config(text="Close", command=self.root.quit)

        except Exception as e:
            error_message = f"Error: {e}"
            self.message_label.config(text=error_message)

def main():
    root = tk.Tk()
    app = StormGeniusApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
