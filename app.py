import tkinter as tk
from tkinter import messagebox, simpledialog

class RobotAssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Robot Assistant")
        self.start_interaction()

    def start_interaction(self):
        self.show_message("🤖 Hi, I'm your friendly robot assistant!")
        score_type = self.ask_choice("Would you like a social score, financial score, or both?", ["social", "financial", "both"])
        evm_address = self.ask_input("Please enter your EVM address")

        self.show_message(f"🤖 Fetching {score_type} score for address {evm_address}...")

        try:
            # Mock data for robot data
            robot_data = {
                "id": evm_address,
                "name": "Test Robot",
                "model": "Model-X"
            }
            self.show_message(f"Robot Data: {robot_data}")

            # Mock data for smart contract data
            contract_data = {
                "balance": 1000,
                "transactions": 50
            }
            self.show_message(f"Smart Contract Data: {contract_data}")

            # Mock logic to calculate trust score
            trust_score = {
                "social_score": 85 if score_type in ['social', 'both'] else None,
                "financial_score": 90 if score_type in ['financial', 'both'] else None
            }
            trust_score_message = f"🤖 Trust Score: {trust_score}"
            self.show_message(trust_score_message)

        except Exception as e:
            error_message = f"Error: {e}"
            self.show_message(error_message)

    def show_message(self, message):
        messagebox.showinfo("Robot Assistant", message)

    def ask_choice(self, prompt, choices):
        return simpledialog.askstring("Robot Assistant", f"{prompt}\nChoices: {', '.join(choices)}")

    def ask_input(self, prompt):
        return simpledialog.askstring("Robot Assistant", prompt)

def main():
    root = tk.Tk()
    app = RobotAssistantApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
