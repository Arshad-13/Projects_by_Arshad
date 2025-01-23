#Login ID and verifications for members of library

class LoginID:
    def __init__(self, name, ID, password):
        self.name = name
        self.ID = ID
        self.password = password
        self.members = self.load_members()
    
    def save_member(self):
        with open("members.txt", 'w') as f:
            for name, details in self.members.items():
                # Ensure only ID and password are saved
                f.write(f"{name},{details[0]},{details[1]}\n")
                
    def add_member(self):
        self.members[self.name] = [self.ID, self.password]
        self.save_member()
        
    def load_members(self):
        members = {}
        try:
            with open('members.txt', 'r') as file:
                for line in file:
                    # Split the line and take only the first three elements
                    parts = line.strip().split(',')
                    if len(parts) >= 3:
                        name, ID, password = parts[:3]
                        members[name] = [ID, password]
        except FileNotFoundError:
            pass
        return members
    
    def display_members(self):
        for name, details in self.members.items():
            print(f"{name}-{details[0]}")
            
    def verify_member(self, name, ID, password):
        # Reload members from file to ensure most up-to-date information
        self.members = self.load_members()
        
        # Use .get() method to safely check member existence
        if name not in self.members:
            print("Member not found")
            return False
        
        # Safely access member details with error handling
        member_details = self.members.get(name)
        if not member_details or len(member_details) < 2:
            print("Invalid member data")
            return False
        
        # Check if ID matches
        if member_details[0] != ID:
            print("Incorrect ID")
            return False
        
        # Check if password matches
        if member_details[1] != password:
            print("Incorrect password")
            return False
        
        # If all checks pass, authentication is successful
        print("Login successful")
        return True