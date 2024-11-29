import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # For handling images
import datetime

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Window")
        self.root.geometry("300x250")  # Adjusted the window size to accommodate the new elements
        
        # Default background color
        self.bg_color = "#f0f8ff"

        # Frames for each section
        self.main_frame = tk.Frame(self.root)
        self.diary_frame = tk.Frame(self.root)
        self.todo_frame = tk.Frame(self.root)

        # Label for "PUPPYBUDDY !" text
        self.puppy_label = tk.Label(self.main_frame, text="PUPPYBUDDY !", font=("Times New Roman", 20, "bold"), bg=self.bg_color, fg="#ff63d0")
        self.puppy_label.pack(pady=5)

        # Image for main menu
        self.main_image = Image.open("D:\\downloads\\pinkdog.png")  
        self.main_image = self.main_image.resize((250, 250)) 
        self.main_image_tk = ImageTk.PhotoImage(self.main_image)
        
        # Image label
        self.image_label = tk.Label(self.main_frame, image=self.main_image_tk)
        self.image_label.pack(pady=10)

        # Hi! What's your name? label and text box
        self.name_label = tk.Label(self.main_frame, text="Halloo!! I'm PuppyBuddy! What's your name?", font=("Times New Roman", 12), bg=self.bg_color)
        self.name_label.pack(pady=5)

        self.name_entry = tk.Entry(self.main_frame, width=40, font=("Times New Roman", 12), bg="#ffffff", fg="#000000")
        self.name_entry.pack(pady=5)

        # Label for displaying the greeting
        self.greeting_label = tk.Label(self.main_frame, text="", font=("Times New Roman", 12), bg=self.bg_color)
        self.greeting_label.pack(pady=5)

        # Button to greet the user
        self.greet_button = tk.Button(self.main_frame, text="Greet Me!", font=("Times New Roman", 12), command=self.greet_user, bg="#ff63d0", fg="white", relief="raised")
        self.greet_button.pack(pady=10)

        # Button for Diary
        button = tk.Button(self.main_frame, text="Diary", font=("Times New Roman", 10), command=lambda: self.switch_view("diary"))
        button.pack(pady=5)
        
        # Button for To-Do List
        button = tk.Button(self.main_frame, text="To-Do List", font=("Times New Roman", 10), command=lambda: self.switch_view("todo"))
        button.pack(pady=5)

        # Initialize views (diary and todo UI are hidden by default)
        self.initialize_diary_ui()
        self.initialize_todo_ui()

        # Show main menu initially
        self.main_frame.pack(fill="both", expand=True)

    def greet_user(self):
        # Get the name from the entry and display the greeting
        name = self.name_entry.get().strip()
        if name:
            self.greeting_label.config(text=f"Hallo {name}!! You have a very lovely name! You're doing great! I'm so proud of you <3")
        else:
            messagebox.showwarning("Input Error", "Please enter your name.")

    def switch_view(self, view):
        # Hide all frames first
        for frame in [self.main_frame, self.diary_frame, self.todo_frame]:
            frame.pack_forget()

        # Show the selected frame
        if view == "diary":
            self.diary_frame.pack(fill="both", expand=True)
        elif view == "todo":
            self.todo_frame.pack(fill="both", expand=True)

    def return_to_main_menu(self):
        # Hide all other frames and show the main menu
        for frame in [self.diary_frame, self.todo_frame]:
            frame.pack_forget()
        self.main_frame.pack(fill="both", expand=True)

    # DIARY SECTION -----------------------------
    def initialize_diary_ui(self):
        self.diary_frame.config(bg=self.bg_color)

        # UI Elements
        self.title_label = tk.Label(self.diary_frame, text="Diary Entry", font=("Times New Roman", 18), bg=self.bg_color, fg="#2e4a62")
        self.title_label.pack(pady=10)

        self.entry_date_label = tk.Label(self.diary_frame, text="Date:", font=("Times New Roman", 12), bg=self.bg_color, fg="#2e4a62")
        self.entry_date_label.pack(pady=5)

        self.date_entry = tk.Entry(self.diary_frame, width=50, font=("Times New Roman", 12), bg="#ffffff", fg="#000000", relief="solid")
        self.date_entry.insert(0, datetime.datetime.now().strftime("%Y-%m-%d"))
        self.date_entry.pack(pady=5)

        self.entry_label = tk.Label(self.diary_frame, text="Your Thoughts:", font=("Times New Roman", 12), bg=self.bg_color, fg="#2e4a62")
        self.entry_label.pack(pady=5)

        self.text_box = tk.Text(self.diary_frame, width=50, height=15, font=("Times New Roman", 12), bg="#ffffff", fg="#000000", wrap="word", relief="solid")
        self.text_box.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(self.diary_frame, bg=self.bg_color)
        button_frame.pack(pady=20)

        self.save_button = tk.Button(button_frame, text="Save Entry", font=("Times New Roman", 12), command=self.save_entry, bg="#4CAF50", fg="white", relief="raised")
        self.save_button.pack(side=tk.LEFT, padx=10)

        self.view_button = tk.Button(button_frame, text="View Entries", font=("Times New Roman", 12), command=self.view_entries, bg="#2196F3", fg="white", relief="raised")
        self.view_button.pack(side=tk.LEFT, padx=10)

        self.back_button = tk.Button(button_frame, text="Back to Main Menu", command=self.return_to_main_menu, font=("Times New Roman", 12), bg="#FF9800", fg="white", relief="raised")
        self.back_button.pack(side=tk.LEFT, padx=10)

        # Add a button to change background color
        self.change_bg_button = tk.Button(self.diary_frame, text="Change Background Color", command=self.change_background, font=("Times New Roman", 12), bg="#FF9800", fg="white", relief="raised")
        self.change_bg_button.pack(pady=10)

    def save_entry(self):
        print("Save Entry button clicked")
        date = self.date_entry.get()
        text = self.text_box.get("1.0", "end-1c")
        
        if not text.strip():
            messagebox.showwarning("Warning", "Please write something in your diary.")
            return

        try:
            with open("diary_entries.txt", "a") as file:
                file.write(f"Date: {date}\n{str(text)}\n{'-'*50}\n")
            messagebox.showinfo("Success", "Diary entry saved!")
            self.text_box.delete(1.0, "end")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def view_entries(self):
        print("View Entries button clicked")
        try:
            with open("diary_entries.txt", "r") as file:
                entries = file.readlines()

            if not entries:
                messagebox.showinfo("No Entries", "No diary entries found.")
            else:
                entries_window = tk.Toplevel(self.root)
                entries_window.title("All Diary Entries")
                entries_window.geometry("500x400")
                entries_window.config(bg=self.bg_color)

                # display entries
                entries_text = tk.Text(entries_window, width=60, height=20, font=("Times New Roman", 12), bg="#ffffff", fg="#000000", wrap="word", relief="solid")
                entries_text.config(state="disabled")
                entries_text.pack(pady=10)

                # display entries in the text box
                entries_text.config(state="normal")
                for entry in entries:
                    entries_text.insert("end", entry)
                entries_text.config(state="disabled")

                # Delete button for each entry
                for i in range(len(entries) // 3):  # Each entry takes 3 lines
                    date = entries[i * 3].strip().split("\n")[0]  # Get the date of the entry
                    delete_button = tk.Button(entries_window, text=f"Delete {date}", command=lambda i=i: self.delete_entry(i, entries), font=("Times New Roman", 12), bg="#f44336", fg="white")
                    delete_button.pack(pady=2)

        except FileNotFoundError:
            messagebox.showinfo("No Entries", "No diary entries found.")

    def delete_entry(self, index, entries):
        try:
            # Remove the selected entry from the list of entries (each entry takes 3 lines)
            del entries[index * 3:index * 3 + 3]

            # Rewrite the remaining entries back to the file
            with open("diary_entries.txt", "w") as file:
                file.writelines(entries)

            messagebox.showinfo("Success", "Entry deleted successfully!")
            self.view_entries()
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting entry: {e}")

    def change_background(self):
        colors = ["#f0f8ff", "#fff5e6", "#e1f7d5", "#ffe0b3", "#f3e5f5"]
        color_window = tk.Toplevel(self.root)
        color_window.title("Change Background Color")
        color_window.geometry("300x200")
        
        def change_color(color):
            self.bg_color = color
            self.diary_frame.config(bg=self.bg_color)
            self.todo_frame.config(bg=self.bg_color)

            for widget in self.diary_frame.winfo_children():
                if isinstance(widget, tk.Label):
                    widget.config(bg=color)
                elif isinstance(widget, tk.Button):
                    widget.config(bg="#FF9800")
                elif isinstance(widget, tk.Text):
                    widget.config(bg="#ffffff")

        for color in colors:
            color_button = tk.Button(color_window, text=f"Color {color}", command=lambda color=color: change_color(color), font=("Times New Roman", 12))
            color_button.pack(pady=10)

        close_button = tk.Button(color_window, text="Close", command=color_window.destroy, font=("Times New Roman", 12))
        close_button.pack(pady=10)

    # TO-DO LIST SECTION ----------------------------
    def initialize_todo_ui(self):
        self.todo_frame.config(bg=self.bg_color)
        
        self.todo_label = tk.Label(self.todo_frame, text="To-Do List", font=("Times New Roman", 18), bg=self.bg_color, fg="#2e4a62")
        self.todo_label.pack(pady=10)

        self.todo_listbox = tk.Listbox(self.todo_frame, width=50, height=10, font=("Times New Roman", 12), bg="#ffffff", fg="#000000", selectmode=tk.SINGLE)
        self.todo_listbox.pack(pady=10)

        self.todo_entry = tk.Entry(self.todo_frame, font=("Times New Roman", 12), width=50, bg="#ffffff", fg="#000000")
        self.todo_entry.pack(pady=5)

        button_frame = tk.Frame(self.todo_frame, bg=self.bg_color)
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Add Task", font=("Times New Roman", 12), command=self.add_task, bg="#4CAF50", fg="white")
        add_button.pack(side=tk.LEFT, padx=10)

        delete_button = tk.Button(button_frame, text="Delete Task", font=("Times New Roman", 12), command=self.delete_task, bg="#f44336", fg="white")
        delete_button.pack(side=tk.LEFT, padx=10)

        delete_all_button = tk.Button(button_frame, text="Delete All Tasks", font=("Times New Roman", 12), command=self.delete_all_tasks, bg="#f44336", fg="white")
        delete_all_button.pack(side=tk.LEFT, padx=10)

        self.change_bg_button_todo = tk.Button(self.todo_frame, text="Change Background Color", command=self.change_background, font=("Times New Roman", 12), bg="#FF9800", fg="white", relief="raised")
        self.change_bg_button_todo.pack(pady=10)

        back_button = tk.Button(self.todo_frame, text="Back to Main Menu", font=("Times New Roman", 12), command=self.return_to_main_menu, bg="#FF9800", fg="white")
        back_button.pack(pady=10)

    def add_task(self):
        task = self.todo_entry.get()
        if task:
            self.todo_listbox.insert(tk.END, task)
            self.todo_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        try:
            selected_task_index = self.todo_listbox.curselection()[0]
            self.todo_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def delete_all_tasks(self):
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete all tasks?")
        if confirm:
            self.todo_listbox.delete(0, tk.END)
            messagebox.showinfo("Success", "All tasks have been deleted.")


# Run the application
root = tk.Tk()
app = App(root)
root.mainloop()
