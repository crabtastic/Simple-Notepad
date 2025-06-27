import tkinter as tk
from tkinter import filedialog
from tkinter import Tk, Text, Frame, Button
from typing import Optional


class SimpleNotepad:
    def __init__(self, root: Tk) -> None:
        self.root = root
        self.root.title("Abdullahs Notepad")
        self.current_file: Optional[str] = None

        # Text widget
        self.text_area: Text = Text(self.root, wrap="word")
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

    def save_file(self) -> None:
        if self.current_file:
            with open(self.current_file, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            print(f"File saved to: {self.current_file}")

        else:
            self.save_as_file()

    def save_as_file(self) -> None:
        file_path: str = filedialog.asksaveasfilename(
            defaultextension=".txt", filetypes=[("Text files", "*.txt")]
        )

        if file_path:
            with open(file_path, "w") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.current_file = file_path

            print(f"File saved to: {file_path}")

    def load_file(self) -> None:
        file_path: str = filedialog.askopenfilename(
            defaultextension=".txt", filetypes=[("Text files", "*.txt")]
        )
        if file_path:
            with open(file_path, "r") as file:
                content: str = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.INSERT, content)
            self.current_file = file_path

            print(f"file loaded from: {file_path}")

    def run(self) -> None:
        self.root.mainloop()


def main() -> None:
    root: Tk = tk.Tk()
    app: SimpleNotepad = SimpleNotepad(root=root)
    app.run()


if __name__ == "__main__":
    main()
