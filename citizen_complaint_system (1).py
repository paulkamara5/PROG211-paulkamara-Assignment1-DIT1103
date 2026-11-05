"""
Citizen Complaint System
Object-Oriented Programming 1 assignment
A simple command-line demonstration using classes and a dictionary.

Privacy note: this demonstration does not request names, phone numbers,
addresses, national ID numbers, or other sensitive personal information.
"""

from datetime import datetime


class Citizen:
    """Represents a citizen using a non-identifying reference code."""

    def __init__(self, citizen_ref: str):
        self.citizen_ref = citizen_ref

    def display_info(self) -> None:
        """Display the citizen's non-identifying reference."""
        print(f"Citizen reference: {self.citizen_ref}")


class Complaint:
    """Represents a complaint submitted to a public service office."""

    total_complaints = 0

    def __init__(self, complaint_id: str, citizen_ref: str,
                 category: str, description: str):
        self.complaint_id = complaint_id
        self.citizen_ref = citizen_ref
        self.category = category
        self.description = description
        self.status = "Submitted"
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
        Complaint.total_complaints += 1

    def display_info(self) -> None:
        """Instance method: display one complaint."""
        print("-" * 50)
        print(f"Complaint ID : {self.complaint_id}")
        print(f"Citizen ref  : {self.citizen_ref}")
        print(f"Category     : {self.category}")
        print(f"Description  : {self.description}")
        print(f"Status       : {self.status}")
        print(f"Created      : {self.created_at}")
        print("-" * 50)

    def update_status(self, new_status: str) -> None:
        """Update a complaint's status."""
        allowed = {"Submitted", "Under Review", "Resolved"}
        if new_status not in allowed:
            print("Invalid status. Choose Submitted, Under Review, or Resolved.")
            return
        self.status = new_status
        print("Complaint status updated.")

    @classmethod
    def show_total(cls) -> None:
        """Class method: display the number of complaints created."""
        print(f"Total complaints created this session: {cls.total_complaints}")


class ComplaintSystem:
    """Manages complaint objects in a dictionary keyed by complaint ID."""

    def __init__(self):
        self.complaints = {}

    def add_complaint(self) -> None:
        complaint_id = input("Enter a unique complaint ID (e.g. C001): ").strip()
        if not complaint_id:
            print("Complaint ID cannot be empty.")
            return
        if complaint_id in self.complaints:
            print("That complaint ID already exists.")
            return

        citizen_ref = input("Enter an anonymous citizen reference (e.g. CIT001): ").strip()
        category = input("Category (Roads, Water, Waste, Electricity, Other): ").strip()
        description = input("Brief complaint description (do not include private data): ").strip()

        if not citizen_ref or not category or not description:
            print("All fields are required. No complaint was saved.")
            return

        citizen = Citizen(citizen_ref)
        complaint = Complaint(complaint_id, citizen.citizen_ref, category, description)
        self.complaints[complaint_id] = complaint
        print("Complaint recorded successfully.")

    def list_complaints(self) -> None:
        if not self.complaints:
            print("No complaints have been recorded.")
            return
        for complaint in self.complaints.values():
            complaint.display_info()

    def find_complaint(self) -> None:
        complaint_id = input("Enter complaint ID to find: ").strip()
        complaint = self.complaints.get(complaint_id)
        if complaint:
            complaint.display_info()
        else:
            print("Complaint not found.")

    def change_status(self) -> None:
        complaint_id = input("Enter complaint ID: ").strip()
        complaint = self.complaints.get(complaint_id)
        if not complaint:
            print("Complaint not found.")
            return
        print("Statuses: Submitted | Under Review | Resolved")
        new_status = input("Enter new status exactly as shown: ").strip()
        complaint.update_status(new_status)

    def run(self) -> None:
        while True:
            print("\n=== CITIZEN COMPLAINT SYSTEM ===")
            print("1. Add complaint")
            print("2. List all complaints")
            print("3. Find complaint by ID")
            print("4. Update complaint status")
            print("5. Show total complaints")
            print("0. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                self.add_complaint()
            elif choice == "2":
                self.list_complaints()
            elif choice == "3":
                self.find_complaint()
            elif choice == "4":
                self.change_status()
            elif choice == "5":
                Complaint.show_total()
            elif choice == "0":
                print("Thank you for using the Citizen Complaint System.")
                break
            else:
                print("Invalid option. Please choose 0 to 5.")


if __name__ == "__main__":
    ComplaintSystem().run()
