import tkinter as tk
from tkinter import messagebox
import threading
import randomiser

class SwimDojoGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SwimDojo Random Workout Generator")
        self.geometry("400x350")
        self.resizable(False, False)

        tk.Label(self, text="Select Workout Tags (optional):", font=("Arial", 12, "bold")).pack(pady=10)

        self.distance_var = tk.StringVar(value="")
        self.difficulty_var = tk.StringVar(value="")
        self.style_var = tk.StringVar(value="")

        self._add_dropdown("Distance", randomiser.distance_tags, self.distance_var)
        self._add_dropdown("Difficulty", randomiser.difficulty_tags, self.difficulty_var)
        self._add_dropdown("Style", randomiser.style_tags, self.style_var)

        self.random_button = tk.Button(self, text="Get Random Workout", command=self.get_workout, font=("Arial", 12, "bold"))
        self.random_button.pack(pady=20)

        self.status_label = tk.Label(self, text="", fg="green", font=("Arial", 10))
        self.status_label.pack(pady=5)

    def _add_dropdown(self, label, options, var):
        frame = tk.Frame(self)
        frame.pack(pady=5)
        tk.Label(frame, text=label+":", width=10, anchor="w").pack(side=tk.LEFT)
        opt = ["(Any)"] + options
        tk.OptionMenu(frame, var, *opt).pack(side=tk.LEFT)

    def get_workout(self):
        self.status_label.config(text="Fetching workout...")
        self.random_button.config(state=tk.DISABLED)
        threading.Thread(target=self._fetch_workout).start()

    def _fetch_workout(self):
        try:
            tags = []
            if self.distance_var.get() and self.distance_var.get() != "(Any)":
                tags.append(self.distance_var.get().lower())
            if self.difficulty_var.get() and self.difficulty_var.get() != "(Any)":
                tags.append(self.difficulty_var.get().lower())
            if self.style_var.get() and self.style_var.get() != "(Any)":
                tags.append(self.style_var.get().lower())
            randomiser.open_random_workout(tags)
            self.status_label.config(text="Workout opened in browser!")
        except Exception as e:
            self.status_label.config(text="Error: " + str(e))
            messagebox.showerror("Error", str(e))
        finally:
            self.random_button.config(state=tk.NORMAL)

if __name__ == "__main__":
    app = SwimDojoGUI()
    app.mainloop()
