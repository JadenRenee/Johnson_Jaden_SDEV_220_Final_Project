# user.py
class User:
    def __init__(self, user_id, name, email, role):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.role = role  # e.g., artist, volunteer, donor

    def __str__(self):
        return f"User({self.user_id}, {self.name}, {self.email}, {self.role})"

# resource.py
class Resource:
    def __init__(self, resource_id, name, quantity):
        self.resource_id = resource_id
        self.name = name
        self.quantity = quantity

    def __str__(self):
        return f"Resource({self.resource_id}, {self.name}, {self.quantity})"

# event.py
class Event:
    def __init__(self, event_id, name, date, attendees=None):
        if attendees is None:
            attendees = []
        self.event_id = event_id
        self.name = name
        self.date = date
        self.attendees = attendees

    def add_attendee(self, user):
        self.attendees.append(user)

    def __str__(self):
        return f"Event({self.event_id}, {self.name}, {self.date}, {len(self.attendees)} attendees)"
# main.py
import tkinter as tk
from tkinter import messagebox
from user import User
from resource import Resource
from event import Event

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Non-Profit Management System")

        self.users = []
        self.resources = {}
        self.events = []

        self.create_widgets()

    def create_widgets(self):
        # Create buttons and other widgets here
        self.add_user_button = tk.Button(self.root, text="Add User", command=self.add_user)
        self.add_user_button.pack()

        self.add_resource_button = tk.Button(self.root, text="Add Resource", command=self.add_resource)
        self.add_resource_button.pack()

        self.add_event_button = tk.Button(self.root, text="Add Event", command=self.add_event)
        self.add_event_button.pack()

        self.generate_report_button = tk.Button(self.root, text="Generate Report", command=self.generate_report)
        self.generate_report_button.pack()

    def add_user(self):
        # Logic to add a user
        user = User(1, "John Doe", "john@example.com", "artist")
        self.users.append(user)
        messagebox.showinfo("Info", f"Added user: {user}")

    def add_resource(self):
        # Logic to add a resource
        resource = Resource(1, "Paint Brushes", 50)
        self.resources[resource.resource_id] = resource
        messagebox.showinfo("Info", f"Added resource: {resource}")

    def add_event(self):
        # Logic to add an event
        event = Event(1, "Art Workshop", "2024-11-15")
        self.events.append(event)
        messagebox.showinfo("Info", f"Added event: {event}")

    def generate_report(self):
        # Logic to generate a report
        report = "Users:\n" + "\n".join(str(user) for user in self.users) + "\n\n"
        report += "Resources:\n" + "\n".join(str(resource) for resource in self.resources.values()) + "\n\n"
        report += "Events:\n" + "\n".join(str(event) for event in self.events)
        messagebox.showinfo("Report", report)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
