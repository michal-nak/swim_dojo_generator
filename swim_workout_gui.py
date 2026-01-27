"""
Swim Dojo Workout Generator - GUI Application
Simple graphical interface for fetching random swim workouts
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
from swim_workout_fetcher import get_workout_tags, open_random_workout


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
        
        # Tag selection frame
        tag_frame = ttk.LabelFrame(main_frame, text="Select Workout Type (Optional)", padding="10")
        tag_frame.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 20))
        tag_frame.columnconfigure(0, weight=1)
        
        # Tag selection
        self.tag_var = tk.StringVar(value="Random (Any Tag)")
        self.tag_combo = ttk.Combobox(
            tag_frame,
            textvariable=self.tag_var,
            state="readonly",
            font=('Arial', 10)
        )
        self.tag_combo.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=5, pady=5)
        
        # Load tags button
        load_tags_btn = ttk.Button(
            tag_frame,
            text="Refresh Tags",
            command=self.load_tags
        )
        load_tags_btn.grid(row=1, column=0, pady=(5, 0))
        
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
        self.tags = []
        self.log("Welcome to Swim Dojo Workout Generator!")
        self.log("Click 'Refresh Tags' to load available workout types.")
        self.log("Then click 'Get Random Workout!' to open a workout in your browser.")
        
        # Load tags on startup
        self.root.after(100, self.load_tags)
    
    def log(self, message):
        """Add a message to the log area"""
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
    
    def load_tags(self):
        """Load available workout tags in a background thread"""
        self.log("Loading workout tags...")
        self.workout_btn.config(state='disabled')
        
        def load():
            try:
                self.tags = get_workout_tags()
                values = ["Random (Any Tag)"] + [tag.title() for tag in self.tags]
                self.tag_combo['values'] = values
                self.log(f"Loaded {len(self.tags)} workout tags")
            except Exception as e:
                self.log(f"Error loading tags: {e}")
                messagebox.showerror("Error", f"Failed to load tags: {e}")
            finally:
                self.workout_btn.config(state='normal')
        
        thread = threading.Thread(target=load, daemon=True)
        thread.start()
    
    def get_workout(self):
        """Get and open a random workout"""
        selected = self.tag_var.get()
        
        # Determine which tag to use
        if selected == "Random (Any Tag)" or not selected:
            tag = None
            self.log("Fetching random workout from any category...")
        else:
            tag = selected.lower()
            self.log(f"Fetching random workout from '{selected}' category...")
        
        self.workout_btn.config(state='disabled')
        
        def fetch():
            try:
                result = open_random_workout(tag)
                if result:
                    self.log(f"✓ Opened workout in browser: {result}")
                else:
                    self.log("✗ Failed to fetch workout")
                    messagebox.showwarning(
                        "Warning", 
                        "Could not fetch a workout. Please check your internet connection."
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
