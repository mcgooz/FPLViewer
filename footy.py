import requests
import json
from tkinter import *
from tkinter import ttk, messagebox, PhotoImage
from PIL import Image, ImageTk

root = Tk()
root.option_add("*font", "lato 10")
root.bind("<Return>", lambda event: go_click())
s = ttk.Style()
s.theme_use("clam")
s.configure("TButton", background = "skyblue1", foreground = "white")

# base_url = "https://fantasy.premierleague.com/api/"


# Go button function carries user input to main
def go_click():
    team_id = team_input.get()
    main(team_id)


def main(t=None):
    try:
        if root.winfo_exists():
            input = input_check(t)
            if input == True:
                team_details = team_get(t)
                if team_details == "The game is being updated.":
                    messagebox.showerror(message="The game is being updated. Please try later")
                else:
                    update_GUI(team_details, widgets)
            else:
                messagebox.showerror(message="Please enter a valid ID")
    except (TypeError, KeyError, TclError):
        return


def input_check(t):
    if t == "":
        return False
    elif t == "Enter team ID":
        return False
    elif t.isalpha():
        return False
    elif t.isdigit():
        return True
    else:
        return False


# Team
def team_get(t):
    try:
        team = requests.get(
            f"https://fantasy.premierleague.com/api/entry/{t}"
        ).json()
        team_text = json.dumps(team, indent=2)
        file = open("details.txt", "w")
        file.write(team_text)
        file.close()
        return team
    except requests.RequestException:
        messagebox.showerror(message="Can't retrieve data at this time.")
        return None


class GUI_update:
    def __init__(self, team_info, widgets):
        self.team_info = team_info
        self.widgets = widgets

    def update_widgets(self):
        for stat, widget in self.widgets.items():
            if stat == "teamID":
                widget.config(text=self.team_info["id"])
            elif stat == "team_name":
                widget.config(text=self.team_info["name"])
            elif stat == "full_name":
                first_name = self.team_info["player_first_name"]
                last_name = self.team_info["player_last_name"]
                full_name = first_name + " " + last_name
                widget.config(text=full_name)
            elif stat == "score":
                widget.config(text=self.team_info["summary_overall_points"])
            elif stat == "rank":
                widget.config(text=self.team_info["summary_overall_rank"])
            elif stat == "gw":
                widget.config(text=self.team_info["current_event"])
            elif stat == "gw_score":
                widget.config(text=self.team_info["summary_event_points"])
            elif stat == "team_value":
                value = self.team_info["last_deadline_value"]
                value_float = value / 10
                widget.config(text=f"£{value_float}")
            elif stat == "bank":
                itb = self.team_info["last_deadline_bank"]
                itb_float = itb / 10
                widget.config(text=f"£{itb_float}")


def update_GUI(t, widgets):
    updater = GUI_update(t, widgets)
    updater.update_widgets()


def reset_click():
    all_fields = [
        teamID_result,
        team_name_result,
        name_result,
        score_result,
        rank_result,
        gw_result,
        gw_score_result,
        team_value_result,
        bank_result,
    ]
    for field in all_fields:
        if isinstance(field, ttk.Label):
            field.config(text="")

    team_input.set("Enter team ID")
    team_input_box.configure(state=NORMAL)
    team_input_box.bind("<Button-1>", click)


def click(event):
    team_input_box.delete(0, END)

#def on_closing():
    #root.destroy()

#root.protocol("WM_DELETE_WINDOW", on_closing)

## Labels

# Team ID Label
teamID_label = ttk.Label(root, text="Team ID:")
teamID_label.grid(column=0, row=2, padx=5, pady=5, sticky=W)
teamID_label.config(background="skyblue1", foreground="white")

# Team ID result Label
teamID_result = ttk.Label(root, text="")
teamID_result.grid(column=1, row=2, padx=5, pady=5, sticky=W)
teamID_result.config(background="skyblue1", foreground="white")

# Team Name Label
team_name_label = ttk.Label(root, text="Team Name:")
team_name_label.grid(column=0, row=3, padx=5, pady=5, sticky=W)
team_name_label.config(background="skyblue1", foreground="white")

# Team Name result Label
team_name_result = ttk.Label(root, text="")
team_name_result.grid(column=1, row=3, padx=5, pady=5, sticky=W)
team_name_result.config(background="skyblue1", foreground="white")

# Name Label
name_label = ttk.Label(root, text="Name:")
name_label.grid(column=0, row=4, padx=5, pady=5, sticky=W)
name_label.config(background="skyblue1", foreground="white")

# Name result label
name_result = ttk.Label(root, text="")
name_result.grid(column=1, row=4, padx=5, pady=5, sticky=W)
name_result.config(background="skyblue1", foreground="white")

# Score Label
score_label = ttk.Label(root, text="Score:")
score_label.grid(column=0, row=5, padx=5, pady=5, sticky=W)
score_label.config(background="skyblue1", foreground="white")

# Name result label
score_result = ttk.Label(root, text="")
score_result.grid(column=1, row=5, padx=5, pady=5, sticky=W)
score_result.config(background="skyblue1", foreground="white")

# Rank Label
rank_label = ttk.Label(root, text="Current Rank:")
rank_label.grid(column=0, row=6, padx=5, pady=5, sticky=W)
rank_label.config(background="skyblue1", foreground="white")

# Rank result label
rank_result = ttk.Label(root, text="")
rank_result.grid(column=1, row=6, padx=5, pady=5, sticky=W)
rank_result.config(background="skyblue1", foreground="white")

# GW Label
gw_label = ttk.Label(root, text="Gameweek:")
gw_label.grid(column=0, row=7, padx=5, pady=5, sticky=W)
gw_label.config(background="skyblue1", foreground="white")

# GW result label
gw_result = ttk.Label(root, text="")
gw_result.grid(column=1, row=7, padx=5, pady=5, sticky=W)
gw_result.config(background="skyblue1", foreground="white")

# GW Score Label
gw_score_label = ttk.Label(root, text="Gameweek Score:")
gw_score_label.grid(column=0, row=8, padx=5, pady=5, sticky=W)
gw_score_label.config(background="skyblue1", foreground="white")

# GW score result label
gw_score_result = ttk.Label(root, text="")
gw_score_result.grid(column=1, row=8, padx=5, pady=5, sticky=W)
gw_score_result.config(background="skyblue1", foreground="white")

# Team Value Label
team_value_label = ttk.Label(root, text="Team Value:")
team_value_label.grid(column=0, row=9, padx=5, pady=5, sticky=W)
team_value_label.config(background="skyblue1", foreground="white")

# Team Value result label
team_value_result = ttk.Label(root, text="")
team_value_result.grid(column=1, row=9, padx=5, pady=5, sticky=W)
team_value_result.config(background="skyblue1", foreground="white")

# In the Bank Label
bank_label = ttk.Label(root, text="In the Bank:")
bank_label.grid(column=0, row=10, padx=5, pady=5, sticky=W)
bank_label.config(background="skyblue1", foreground="white")

# In the Bank result label
bank_result = ttk.Label(root, text="")
bank_result.grid(column=1, row=10, padx=5, pady=5, sticky=W)
bank_result.config(background="skyblue1", foreground="white")

widgets = {
    "teamID": teamID_result,
    "team_name": team_name_result,
    "full_name": name_result,
    "score": score_result,
    "rank": rank_result,
    "gw": gw_result,
    "gw_score": gw_score_result,
    "team_value": team_value_result,
    "bank": bank_result,
}

# Team ID input field
team_input = StringVar()
team_input.set("Enter team ID")
team_input_box = ttk.Entry(root, width=15, textvariable=team_input, justify="center")
team_input_box.grid(column=0, row=1, padx=5, pady=5, sticky=W)
team_input_box.bind("<Button-1>", click)


# Go button
button_go = ttk.Button(root, text="Go!", command=go_click)
button_go.grid(column=1, row=1, padx=5, pady=5)

# Reset button
button_reset = ttk.Button(root, text="Reset", command=reset_click)
button_reset.grid(column=0, row=12, padx=5, pady=10, sticky=W)


##### GUI #####


# Set the size of the window
window_width = 300
window_height = 500

# Get current screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Find center points of x and y axis
center_x = int((screen_width / 2 - window_width / 2))
center_y = int((screen_height / 2 - window_height / 2))

# Set window position to middle of screen
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# Set window title
root.title("FPL Lookup")

# Set window colour
root.configure(background="skyblue1")

# Set window icon
root.iconbitmap("pl_logo.ico")

# Disable window resize
root.resizable(False, False)

# Top banner
img = Image.open("fpl_banner.png")
resize_img = img.resize((290, 83), Image.ADAPTIVE)
banner = ImageTk.PhotoImage(resize_img)
choose_label = ttk.Label(root, image=banner)
choose_label.grid(column=0, row=0, columnspan=3, padx=3, pady=3)
choose_label.config(background="skyblue1", foreground="gray4")


root.mainloop()

if __name__ == "__main__":
    main()
