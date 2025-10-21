import csv

class BudgetTracker:
    def __init__(self):
        self.records = []

    def add_record(self, description, amount):
        self.records.append({"description": description, "amount": float(amount)})

    def show_summary(self):
        total = sum(r["amount"] for r in self.records)
        print(f"\nTotal Balance: ${total:.2f}")
        for r in self.records:
            print(f"{r['description']}: ${r['amount']:.2f}")

    def export_csv(self, filename="budget.csv"):
        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["description", "amount"])
            writer.writeheader()
            writer.writerows(self.records)
        print(f"Data exported to {filename}")

if __name__ == "__main__":
    app = BudgetTracker()
    while True:
        print("\n1. Add Record  2. Show Summary  3. Export CSV  4. Exit")
        choice = input("Select option: ")

        if choice == "1":
            desc = input("Description: ")
            amt = input("Amount (+income / -expense): ")
            app.add_record(desc, amt)
        elif choice == "2":
            app.show_summary()
        elif choice == "3":
            app.export_csv()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")
