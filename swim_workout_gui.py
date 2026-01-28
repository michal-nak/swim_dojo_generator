"""
Swim Dojo Workout Generator - GUI Application
Simple graphical interface for fetching random swim workouts
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading


class SwimWorkoutApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Swim Dojo Workout Generator")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        # Main frame
        main_frame = ttk.Frame(root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        
        # Title
        title_label = ttk.Label(
            main_frame, 
            text="🏊 Swim Dojo Workout Generator 🏊",
            font=('Arial', 16, 'bold')
        )
        title_label.grid(row=0, column=0, pady=(0, 20))
        
        # Description
        desc_label = ttk.Label(
            main_frame,
            text="Get a random swim workout from SwimDojo.com",
            font=('Arial', 10)
        )
        desc_label.grid(row=1, column=0, pady=(0, 20))
        

        # Category selection frame
        cat_frame = ttk.LabelFrame(main_frame, text="Select Categories (Optional)", padding="10")
        cat_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 20))
        cat_frame.columnconfigure(0, weight=1)

        # Distance
        ttk.Label(cat_frame, text="Distance:").grid(row=0, column=0, sticky=tk.W, padx=5)
        self.distance_var = tk.StringVar(value="Any")
        self.distance_combo = ttk.Combobox(cat_frame, textvariable=self.distance_var, state="readonly", font=('Arial', 10))
        self.distance_combo['values'] = ["Any", "0-1000", "1000-2000", "2000-3000", "3000-4000", "4000-5000", "5000+", "Mid Distance", "Distance", "Short course", "Open Water", "Timed Swim"]
        self.distance_combo.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=5, pady=2)

        # Difficulty
        ttk.Label(cat_frame, text="Difficulty:").grid(row=1, column=0, sticky=tk.W, padx=5)
        self.difficulty_var = tk.StringVar(value="Any")
        self.difficulty_combo = ttk.Combobox(cat_frame, textvariable=self.difficulty_var, state="readonly", font=('Arial', 10))
        self.difficulty_combo['values'] = ["Any", "Beginner", "Intermediate", "Advanced", "Easy", "Hard", "Insane", "Steady State", "Recovery"]
        self.difficulty_combo.grid(row=1, column=1, sticky=(tk.W, tk.E), padx=5, pady=2)

        # Style
        ttk.Label(cat_frame, text="Style:").grid(row=2, column=0, sticky=tk.W, padx=5)
        self.style_var = tk.StringVar(value="Any")
        self.style_combo = ttk.Combobox(cat_frame, textvariable=self.style_var, state="readonly", font=('Arial', 10))
        self.style_combo['values'] = ["Any", "Freestyle", "Backstroke", "Breaststroke", "Butterfly", "IM", "Stroke", "Pull", "Sprint", "Technique", "Triathlon", "Curreri Workouts"]
        self.style_combo.grid(row=2, column=1, sticky=(tk.W, tk.E), padx=5, pady=2)

        # Load tags button (for future use, if needed)
        # load_tags_btn = ttk.Button(
        #     cat_frame,
        #     text="Refresh Tags",
        #     command=self.load_tags
        # )
        # load_tags_btn.grid(row=3, column=0, columnspan=2, pady=(5, 0))
        
        # Get workout button
        self.workout_btn = ttk.Button(
            main_frame,
            text="Get Random Workout!",
            command=self.get_workout,
            style='Accent.TButton'
        )
        self.workout_btn.grid(row=3, column=0, pady=20, ipadx=20, ipady=10)
        
        # Status/Log area
        log_frame = ttk.LabelFrame(main_frame, text="Status", padding="10")
        log_frame.grid(row=4, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        main_frame.rowconfigure(4, weight=1)
        
        self.log_text = scrolledtext.ScrolledText(
            log_frame,
            height=10,
            width=50,
            font=('Courier', 9),
            wrap=tk.WORD
        )
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Initialize
        self.log("Welcome to Swim Dojo Workout Generator!")
        self.log("Select categories and click 'Get Random Workout!' to open a workout in your browser.")
    
    def log(self, message):
        """Add a message to the log area"""
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    # No load_tags needed for category-based UI
    
    def get_workout(self):
        """Get and open a random workout based on selected categories"""
        distance = self.distance_var.get()
        difficulty = self.difficulty_var.get()
        style = self.style_var.get()

        # Build selected tags list (ignore 'Any')
        selected_tags = []
        if distance and distance != "Any":
            selected_tags.append(distance)
        if difficulty and difficulty != "Any":
            selected_tags.append(difficulty)
        if style and style != "Any":
            selected_tags.append(style)

        if not selected_tags:
            self.log("Fetching random workout from any category...")
        else:
            self.log(f"Fetching workout with: {', '.join(selected_tags)}")

        self.workout_btn.config(state='disabled')

        def fetch():
            try:
                # Use intersection-based fetch from randomiser.py
                from randomiser import open_random_workout as open_random_workout_intersection
                result = open_random_workout_intersection(selected_tags if selected_tags else None)
                if result:
                    self.log(f"✓ Opened workout in browser: {result}")
                else:
                    self.log("✗ Failed to fetch workout")
                    messagebox.showwarning(
                        "Warning", 
                        "Could not fetch a workout. Please check your internet connection or try different categories."
                    )
            except Exception as e:
                self.log(f"✗ Error: {e}")
                messagebox.showerror("Error", f"An error occurred: {e}")
            finally:
                self.workout_btn.config(state='normal')

        thread = threading.Thread(target=fetch, daemon=True)
        thread.start()


def main():
    """Main entry point for the GUI application"""
    root = tk.Tk()
    app = SwimWorkoutApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
