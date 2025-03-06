import customtkinter as ctk


class Aulas(ctk.CTkFrame):
    def __init__(self, parent, show_main_content, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.configure(corner_radius=10, fg_color="#454d59")

        label = ctk.CTkLabel(self, text="Aulas", font=("Helvetica", 24, "bold"))
        label.pack(pady=20)

        back_button = ctk.CTkButton(self, text="Voltar", command=show_main_content)
        back_button.pack(pady=10)
