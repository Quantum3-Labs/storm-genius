import tkinter as tk
from tkinter import Label, Button, Entry, StringVar
from PIL import Image, ImageTk
from utils.api import get_social_score, send_message_to_contract

class StormGeniusApp:
    def __init__(self, root):
        self.root = root
        self.root.title("StormGenius")
        self.root.configure(bg='#4B0082')  # Indigo background

        # Load the image using Pillow
        self.robot_image = Image.open("stormgenius.png")
        self.robot_image = self.robot_image.resize((120, 120), Image.LANCZOS)  # Resize the image
        self.robot_image = ImageTk.PhotoImage(self.robot_image)

        # Create the initial layout
        self.image_label = Label(self.root, image=self.robot_image, bg='#4B0082')
        self.image_label.pack(pady=20)

        self.label_frame = Label(self.root, bg='#4B0082')
        self.label_frame.pack(pady=10, padx=10)

        self.message_label = Label(self.label_frame, text="", bg='#4B0082', fg='white', font=("Helvetica Neue Bold", 18), wraplength=400)
        self.message_label.pack(pady=10, padx=10)

        self.input_var = StringVar()
        self.entry = Entry(self.root, textvariable=self.input_var, font=("Helvetica Neue Bold", 16))
        self.entry.pack(pady=10)
        self.entry.pack_forget()

        self.choice_var = StringVar(value="")
        self.choice_buttons = []

        self.submit_button = Button(self.root, text="Submit", command=self.on_submit, bg='#FFFFFF', fg='#4B0082', font=("Helvetica Neue Bold", 16), activebackground='#6A5ACD', activeforeground='white', bd=0, padx=10, pady=5)
        self.submit_button.pack(pady=10)
        self.submit_button.pack_forget()

        self.previous_button = Button(self.root, text="Previous", command=self.on_previous, bg='#FFFFFF', fg='#4B0082', font=("Helvetica Neue Bold", 16), activebackground='#6A5ACD', activeforeground='white', bd=0, padx=10, pady=5)
        self.previous_button.pack(pady=10)
        self.previous_button.pack_forget()

        self.close_button = None

        self.current_step = 0
        self.steps = [
            ("🤖 Hi, this is StormGenius!\nWould you like a social score or a financial score?", ["social", "financial"]),
        ]
        
        self.results = {}

        self.show_step()

    def show_step(self):
        if self.current_step < len(self.steps):
            message, choices = self.steps[self.current_step]
            self.message_label.config(text=message)

            if choices:
                self.entry.pack_forget()
                self.submit_button.pack_forget()
                self.previous_button.pack_forget()
                self.choice_var.set("")
                for button in self.choice_buttons:
                    button.pack_forget()
                self.choice_buttons = []
                for choice in choices:
                    button = Button(self.root, text=choice.capitalize(), command=lambda c=choice: self.on_choice(c), bg='#FFD700', fg='#4B0082', font=("Helvetica Neue Bold", 14), activebackground='#FFA500', activeforeground='white', bd=1, relief="solid", padx=10, pady=5)
                    button.pack(anchor='n', pady=5)
                    self.choice_buttons.append(button)
            else:
                self.entry.pack()
                self.submit_button.pack()
                if self.current_step > 0:
                    self.previous_button.pack()
        else:
            self.previous_button.pack_forget()

    def on_choice(self, choice):
        self.choice_var.set(choice)
        self.results["score_type"] = choice  # Set the score type immediately

        # Remove choice buttons immediately
        for button in self.choice_buttons:
            button.pack_forget()
        
        if choice == 'social':
            self.steps.append(("Please enter the Farcaster ID for the social score", None))
        elif choice == 'financial':
            self.steps.append(("Please enter the Loan ID", None))
        
        self.current_step += 1  # Move to the next step
        self.show_step()  # Show the next step immediately

    def on_previous(self):
        if self.current_step > 0:
            self.current_step -= 1
            if self.current_step == 0:
                self.results.pop("score_type", None)
            elif self.results.get("score_type") == 'social':
                self.results.pop("user_id", None)
            elif self.results.get("score_type") == 'financial':
                self.results.pop("loan_id", None)
            self.steps.pop()  # Remove the last step added
            self.show_step()

    def on_submit(self):
        user_input = self.input_var.get()
        if not user_input:
            self.message_label.config(text="Error: No input provided.")
            return
        if self.results["score_type"] == 'social':
            self.results["user_id"] = user_input
        elif self.results["score_type"] == 'financial':
            self.results["loan_id"] = user_input

        self.current_step += 1

        if self.current_step < len(self.steps):
            self.show_step()
        else:
            self.fetch_and_display_results()

    def fetch_and_display_results(self):
        score_type = self.results.get("score_type", "")
        user_id = self.results.get("user_id", "")
        loan_id = self.results.get("loan_id", "")

        self.message_label.config(text=f"🤖 Fetching {score_type} score...")
        self.root.update()

        try:
            result_message = ""  # Initialize result_message
            if score_type == 'social' and user_id:
                # Fetch the social score
                print(f"Debug: Fetching social score for user_id={user_id}")
                social_score = get_social_score(user_id)
                print(f"Debug: Social score: {social_score}")
                result_message = f"Social Score: {social_score}"
            elif score_type == 'financial' and loan_id:
                print(f"Debug: Sending message to contract for loan_id={loan_id}")
                response, receipt = send_message_to_contract(int(loan_id))
                if response and receipt:
                    print(f"Debug: Transaction receipt: {receipt}")
                    print(f"Debug: Response from contract: {response}")
                    result_message = response
                else:
                    result_message = "Failed to get a response from the contract."
            else:
                result_message = "Invalid input."

            self.message_label.config(text=result_message)
            self.previous_button.pack()  # Make sure previous button is shown
            self.entry.pack_forget()
            self.submit_button.pack_forget()

            if self.close_button:
                self.close_button.pack_forget()
            self.close_button = Button(self.root, text="Close", command=self.root.quit, bg='#FFFFFF', fg='#4B0082', font=("Helvetica Neue Bold", 16), activebackground='#6A5ACD', activeforeground='white', bd=0, padx=10, pady=5)
            self.close_button.pack(pady=10)

        except Exception as e:
            error_message = (
                f"Error: {e}\n"
                f"Score Type: {score_type}\n"
                f"User ID: {user_id}\n"
                f"Loan ID: {loan_id}\n"
            )
            print(f"Debug: {error_message}")
            self.message_label.config(text=error_message)
            
            self.previous_button.pack()  # Make sure previous button is shown
            self.entry.pack_forget()
            self.submit_button.pack_forget()

            if self.close_button:
                self.close_button.pack_forget()
            self.close_button = Button(self.root, text="Close", command=self.root.quit, bg='#FFFFFF', fg='#4B0082', font=("Helvetica Neue Bold", 16), activebackground='#6A5ACD', activeforeground='white', bd=0, padx=10, pady=5)
            self.close_button.pack(pady=10)

def main():
    root = tk.Tk()
    app = StormGeniusApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
