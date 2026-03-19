import tkinter as tk
from engine import load_profiles

class ProfilesSection:
    def __init__(self, root, app=None):
        self.root = root
        self.app = app  # Reference to main app
        
        profile_frame = tk.Frame(self.root, bg="#0F172A", bd=1, relief="ridge", highlightbackground="#1E293B", highlightthickness=1)
        profile_frame.place(x=10, y=70, width=180, height=370)

        tk.Label(profile_frame, text="Profiles", bg="#0F172A", fg="#E2E8F0", font=("Segoe UI", 13, "bold"), pady=10).pack()
        
        self.profile_buttons = []
        profiles = load_profiles()
        profile_names = {
            "0": "Default", 
            "1": "VSCode", 
            "2": "OBS", 
            "3": "Software", 
            "4": "Windows", 
            "5": "Photoshop"
        }
        
        for profile_id in sorted(profiles.keys()):
            name = profile_names.get(profile_id, f"Profile {profile_id}")
            btn = tk.Button(profile_frame, text=name, bg="#1E293B", fg="#E2E8F0", relief="flat",
                            font=("Segoe UI", 10, "bold"), activebackground="#0EA5E9", activeforeground="#082F49",
                            command=lambda p=profile_id: self.select_profile(p))
            btn.pack(fill="x", padx=6, pady=4, ipady=3)
            self.profile_buttons.append((profile_id, btn))

    def select_profile(self, profile):
        """Handle profile selection."""
        # Update button appearance
        for profile_id, btn in self.profile_buttons:
            if profile_id == profile:
                btn.config(bg="#0EA5E9", fg="#082F49")
            else:
                btn.config(bg="#1E293B", fg="#E2E8F0")
                
        # Update the app's selected profile
        if self.app:
            self.app.set_selected_profile(profile)