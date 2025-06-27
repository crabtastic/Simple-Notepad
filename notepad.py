import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button, ttk
from typing import Optional


class SimpleNotepad:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title("Abdullahs Notepad")
        self.current_file: Optional[str] = None
        self.dark_mode: bool = False

        self.light_bg: str = "#ffffff"
        self.light_fg: str = "#000000"
        self.dark_bg: str = "#2d2d2d"
        self.dark_fg: str = "#ffffff"

        # Text widget
        self.text_area: Text = Text(
            self.root,
            wrap="word",
            bg=self.light_bg,
            fg=self.light_fg,
            insertbackground=self.light_fg,
        )
        self.text_area.pack(expand=True, fill="both")

        # Frame
        self.button_frame: Frame = Frame(self.root)
        self.button_frame.pack()

        # Save button
        self.save_button: Button = Button(
            self.button_frame, text="Save", command=self.save_file
        )
        self.save_button.pack(side=tk.LEFT)

        # load button
        self.load_button: Button = Button(
            self.button_frame, text="Load", command=self.load_file
        )
        self.load_button.pack(side=tk.LEFT)

        self.override_button: Button = Button(
            self.button_frame, text="Save as", command=self.save_as_file
        )
        self.override_button.pack(side=tk.LEFT)
        
        # dark mode check button
        
        self.mode_switch: ttk.Checkbutton = ttk.Checkbutton(
            self.button_frame,
            text="Dark Mode",
            command=self.toggle_dark_mode,
               
        )
        
        self.mode_switch.pack(side=tk.RIGHT, padx=10)
        
    def toggle_dark_mode(self) -> None:
        self.dark_mode = not self.dark_mode
        
        if self.dark_mode:
            self.root.tk_setPalette(
                background=self.dark_bg,
                foreground=self.dark_fg,
                activeBackground="#3d3d3d",
                activeForeground=self.dark_fg
            )
            self.text_area.config(
                bg=self.dark_bg,
                fg=self.dark_fg,
                insertbackground=self.dark_fg
            )
        else:
            self.root.tk_setPalette(
                background=self.light_bg,
                foreground=self.light_fg,
                activeBackground="#f0f0f0",
                activeForeground=self.light_fg
            )
            self.text_area.config(
                bg=self.light_bg,
                fg=self.light_fg,
                insertbackground=self.light_fg
            )


    def save_file(self) -> None:
        if self.current_file:
            try:
                with open(self.current_file, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                print(f"File saved to: {self.current_file}")
            except Exception as e:
                print(e)

        else:
            self.save_as_file()

    def save_as_file(self) -> None:
        file_path: str = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text files", "*.txt")]
        )

        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(self.text_area.get(1.0, tk.END))
                self.current_file = file_path
            except Exception as e:
                print(e)

            print(f"File saved to: {file_path}")

    def load_file(self) -> None:
        file_path: str = filedialog.askopenfilename(
            defaultextension=".txt", filetypes=[("Text files", "*.txt")]
        )
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content: str = file.read()
                    self.text_area.delete(1.0, tk.END)
                    self.text_area.insert(tk.INSERT, content)
                self.current_file = file_path
            except Exception as e:
                print(e)

            print(f"file loaded from: {file_path}")

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    root: Tk = tk.Tk()
    app: SimpleNotepad = SimpleNotepad(root=root)
    app.run()


if __name__ == "__main__":
    main()
