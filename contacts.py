import json

class Contacts:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.data = {}
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            pass  # File doesn't exist yet, that's fine

    def add_contact(self, id, first_name, last_name):
        if id in self.data:
            return "error"  # Contact already exists
        self.data[id] = [first_name, last_name]
        self._sort_contacts()
        self._save_to_file()
        return f"Added: {first_name} {last_name}."

    def modify_contact(self, id, first_name, last_name):
        if id not in self.data:
            return "error"  # Contact does not exist
        self.data[id] = [first_name, last_name]
        self._sort_contacts()
        self._save_to_file()
        return f"Modified: {first_name} {last_name}"

    def delete_contact(self, id):
        if id not in self.data:
            return "error"  # Contact does not exist
        contact = self.data.pop(id)
        self._save_to_file()
        return f"Deleted: {contact[0]} {contact[1]}"

    def print_contacts(self):
        print(f"\n{'='*20} CONTACT LIST {'='*20}")
        print(f"{'Last Name':<20} {'First Name':<20} {'Phone':<10}")
        print(f"{'='*20} {'='*20} {'='*10}")
        for id, (first_name, last_name) in self.data.items():
            print(f"{last_name:<20} {first_name:<20} {id:<10}")
      
    def set_filename(self, filename):
        self.filename = filename
        try:
            with open(self.filename, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}  # New file, empty contacts
        return f"Filename set to {filename}"

    def _sort_contacts(self):
        self.data = dict(sorted(self.data.items(), key=lambda item: (item[1][1].lower(), item[1][0].lower())))

    def _save_to_file(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)
