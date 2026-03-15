import tkinter as tk
from datetime import timedelta


class StopwatchApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MK's Stopwatch")
        self.root.geometry("300x150")  # Set window size

        self.running = False
        self.start_time = None
        self.elapsed_time = timedelta(seconds=0)

        # Time display label (the "box" with color)
        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 40, "bold"),
                                   bg="black", fg="cyan", relief="sunken", padx=10, pady=10)
        self.time_label.pack(pady=20)

        # Button frame
        self.button_frame = tk.Frame(root)
        self.button_frame.pack()

        # Start Button
        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start, bg="green", fg="white")
        self.start_button.pack(side=tk.LEFT, padx=5)

        # Stop Button
        self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.stop, bg="red", fg="white",
                                     state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)

        # Reset Button
        self.reset_button = tk.Button(self.button_frame, text="Reset", command=self.reset, bg="gray", fg="white")
        self.reset_button.pack(side=tk.LEFT, padx=5)

    def start(self):
        if not self.running:
            self.start_time = self.root.after(10, self.update_time)  # Start update loop
            self.running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

    def stop(self):
        if self.running:
            self.root.after_cancel(self.start_time)  # Stop the scheduled update
            self.running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

    def reset(self):
        if self.running:
            self.stop()
        self.elapsed_time = timedelta(seconds=0)
        self.time_label.config(text="00:00:00")

    def update_time(self):
        # Calculate elapsed time and format
        self.elapsed_time += timedelta(milliseconds=10)  # Update every 10ms for precision
        total_seconds = self.elapsed_time.total_seconds()
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_string = f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"

        self.time_label.config(text=time_string)
        # Reschedule the update after 10 milliseconds
        self.start_time = self.root.after(10, self.update_time)


if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchApp(root)
    root.mainloop()
