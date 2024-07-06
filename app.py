import tkinter as tk
from tkinter import Label, Button, Entry, Radiobutton, StringVar
from PIL import Image, ImageTk
from utils.api import calculate_social_score

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
            ("Please enter your EVM address", None)
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
        else:
            evm_address = self.input_var.get()
            if not evm_address:
                return
            self.results["evm_address"] = evm_address

        self.current_step += 1

        if self.current_step < len(self.steps):
            self.show_step()
        else:
            self.fetch_and_display_results()

    def fetch_and_display_results(self):
        score_type = self.results["score_type"]
        evm_address = self.results["evm_address"]
        
        self.message_label.config(text=f"🤖 Fetching {score_type} score for address {evm_address}...")
        self.root.update()

        try:

            # Fetch contract data
            contract_data = {
                "balance": 1000,
                "transactions": 50
            }
            self.message_label.config(text=f"Smart Contract Data: {contract_data}")
            self.root.update()
            self.root.after(2000)  # Simulate delay

            # Fetch similar users and calculate social score
            social_score = calculate_social_score(evm_address)
            trust_score = {
                "social_score": social_score if score_type in ['social', 'both'] else None,
                "financial_score": 90 if score_type in ['financial', 'both'] else None
            }
            trust_score_message = f"🤖 Trust Score: {trust_score}"
            self.message_label.config(text=trust_score_message)

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
