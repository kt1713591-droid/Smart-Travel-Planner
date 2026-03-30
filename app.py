import tkinter as tk
from tkinter import ttk
import random

# ---------------- DATABASE ---------------- #
places_db = {

    "relax": {
        "low": {
            "solo": ["Rishikesh", "Kasol", "Dharamshala", "McLeod Ganj"],
            "family": ["Nainital", "Mussoorie", "Dehradun"],
            "friends": ["Gokarna", "Goa Budget", "Varkala"]
        },
        "medium": {
            "solo": ["Ooty", "Coorg", "Kodaikanal"],
            "family": ["Manali", "Shimla", "Dalhousie"],
            "friends": ["Pondicherry", "Alleppey", "Hampi"]
        },
        "high": {
            "solo": ["Kerala Backwaters", "Lakshadweep"],
            "family": ["Andaman Islands", "Seychelles"],
            "friends": ["Maldives", "Bora Bora"]
        }
    },

    "adventure": {
        "low": {
            "solo": ["Triund Trek", "Kheerganga Trek"],
            "family": ["Rishikesh Rafting", "Jim Corbett Safari"],
            "friends": ["Camping Kasol", "Bir Billing Paragliding"]
        },
        "medium": {
            "solo": ["Spiti Valley", "Zanskar Valley"],
            "family": ["Manali Trek", "Auli Skiing"],
            "friends": ["Leh Ladakh", "Sikkim Adventure"]
        },
        "high": {
            "solo": ["Dubai Skydiving", "New Zealand Trekking"],
            "family": ["Swiss Alps", "Canada Rockies"],
            "friends": ["Bali Adventure", "Thailand Islands"]
        }
    },

    "romantic": {
        "low": {
            "solo": ["Udaipur", "Pushkar"],
            "family": ["Mount Abu", "Neemrana"],
            "friends": ["Jaipur", "Jodhpur"]
        },
        "medium": {
            "solo": ["Shimla", "Darjeeling"],
            "family": ["Goa", "Kerala"],
            "friends": ["Andaman", "Pondicherry"]
        },
        "high": {
            "solo": ["Paris", "Venice"],
            "family": ["Maldives", "Santorini"],
            "friends": ["Bali", "Phuket"]
        }
    },

    "spiritual": {
        "low": {
            "solo": ["Varanasi", "Haridwar", "Ayodhya"],
            "family": ["Ujjain", "Omkareshwar", "Mathura"],
            "friends": ["Pushkar", "Shirdi"]
        },
        "medium": {
            "solo": ["Tirupati", "Amritsar"],
            "family": ["Vaishno Devi", "Dwarka"],
            "friends": ["Rameshwaram", "Bodh Gaya"]
        },
        "high": {
            "solo": ["Kedarnath", "Badrinath"],
            "family": ["Char Dham Yatra"],
            "friends": ["Kailash Mansarovar"]
        }
    },

    "party": {
        "low": {
            "solo": ["Local Clubs", "College Fest"],
            "family": ["Resort Stay"],
            "friends": ["Goa Budget", "Kasol Parties"]
        },
        "medium": {
            "solo": ["Pune Clubs", "Delhi Nightlife"],
            "family": ["Goa"],
            "friends": ["Bangkok", "Ibiza Lite"]
        },
        "high": {
            "solo": ["Dubai Nightlife", "Singapore Clubs"],
            "family": ["Luxury Cruise"],
            "friends": ["Las Vegas", "Ibiza"]
        }
    },

    "nature": {
        "low": {
            "solo": ["Pachmarhi", "Chikmagalur"],
            "family": ["Satpura National Park", "Ranthambore"],
            "friends": ["Mount Abu", "Saputara"]
        },
        "medium": {
            "solo": ["Coorg", "Munnar", "Wayanad"],
            "family": ["Darjeeling", "Shillong"],
            "friends": ["Tawang", "Gangtok"]
        },
        "high": {
            "solo": ["New Zealand", "Iceland"],
            "family": ["Switzerland", "Norway"],
            "friends": ["Canada", "Alaska"]
        }
    }
}

# ---------------- FUNCTION ---------------- #
def suggest_places():
    mood = mood_var.get()
    budget = budget_var.get()
    purpose = purpose_var.get()

    try:
        options = places_db[mood][budget][purpose]
        suggestions = random.sample(options, min(3, len(options)))
        result = "\n⭐ " + "\n⭐ ".join(suggestions)
    except:
        result = "⚠️ Please select all options!"

    result_label.config(text=result)

# Hover effect
def on_enter(e):
    btn.config(bg="#22c55e")

def on_leave(e):
    btn.config(bg="#4ade80")

# ---------------- UI ---------------- #
root = tk.Tk()
root.title("Smart Travel Planner ✈️")
root.geometry("680x680")
root.configure(bg="#020617")

# Card container
card = tk.Frame(root, bg="#0f172a")
card.place(relx=0.5, rely=0.5, anchor="center", width=600, height=630)

# Title
tk.Label(card, text="✈ Smart Travel Planner",
         font=("Segoe UI", 24, "bold"),
         bg="#0f172a", fg="#38bdf8").pack(pady=20)

tk.Label(card, text="Discover destinations based on your mood 💡",
         font=("Segoe UI", 11),
         bg="#0f172a", fg="#cbd5f5").pack()

# Style
style = ttk.Style()
style.theme_use("default")

style.configure("TCombobox",
                fieldbackground="#1e293b",
                background="#1e293b",
                foreground="white")

# Dropdown function
def dropdown(label, var, values):
    tk.Label(card, text=label,
             bg="#0f172a", fg="#94a3b8",
             font=("Segoe UI", 10)).pack(pady=(15,5))

    box = ttk.Combobox(card, textvariable=var, state="readonly")
    box['values'] = values
    box.pack(ipadx=10, ipady=5)

# Inputs
mood_var = tk.StringVar()
dropdown("Mood", mood_var,
         ["relax", "adventure", "romantic", "spiritual", "party", "nature"])

budget_var = tk.StringVar()
dropdown("Budget", budget_var, ["low", "medium", "high"])

purpose_var = tk.StringVar()
dropdown("Purpose", purpose_var, ["solo", "family", "friends"])

# Button
btn = tk.Button(card, text="🚀 Get Suggestions",
                command=suggest_places,
                bg="#4ade80", fg="black",
                font=("Segoe UI", 13, "bold"),
                relief="flat", padx=12, pady=8)
btn.pack(pady=25)

btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)

# Result Box
result_frame = tk.Frame(card, bg="#1e293b")
result_frame.pack(pady=10, fill="both", expand=True, padx=20)

result_label = tk.Label(result_frame,
                        text="✨ Your destinations will appear here",
                        bg="#1e293b",
                        fg="white",
                        font=("Segoe UI", 12),
                        justify="left")
result_label.pack(pady=20, padx=10)

# Footer
tk.Label(card, text="AI Travel Recommendation System",
         bg="#0f172a", fg="gray",
         font=("Segoe UI", 9)).pack(side="bottom", pady=10)

root.mainloop()