import customtkinter as ctk
from tkinter import messagebox

class RegistroPessoal(ctk.CTkFrame):
    def __init__(self, parent, show_dashboard, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.show_dashboard = show_dashboard
        self.configure(corner_radius=10, fg_color="#2a2d35")

        register_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#3b3f4a", width=600, height=400)
        register_frame.pack(pady=100, padx=300)
        register_frame.pack_propagate(False)

        # Create a fixed title
        label = ctk.CTkLabel(register_frame, text="Registrar-se", font=("Helvetica", 24, "bold"))
        label.pack(pady=20)

        # Create a scrollable frame with a vertical scrollbar for the content
        scrollable_frame = ctk.CTkScrollableFrame(register_frame, width=600, height=300, corner_radius=10, fg_color="#3b3f4a")
        scrollable_frame.pack(fill="both", expand=True, pady=(0, 20))  # Add padding to the bottom

        self.username_entry = self.create_entry(scrollable_frame, "Usuário")
        self.password_entry = self.create_entry(scrollable_frame, "Senha", show="*")
        self.confirm_password_entry = self.create_entry(scrollable_frame, "Confirmar Senha", show="*")
        self.email_entry = self.create_entry(scrollable_frame, "Email")
        self.phone_entry = self.create_entry(scrollable_frame, "Telefone")

        register_button = ctk.CTkButton(scrollable_frame, text="Registrar-se", command=self.register_user, width=300, height=40, corner_radius=8)
        register_button.pack(pady=10)

    def create_entry(self, parent, placeholder, show=None):
        entry = ctk.CTkEntry(parent, placeholder_text=placeholder, show=show, width=300, height=40, corner_radius=8)
        entry.pack(pady=10)
        return entry

    def register_user(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        if username and password and password == confirm_password and email and phone:
            self.show_dashboard()
        else:
            messagebox.showerror("Erro de Registro", "Verifique suas Informações e tente novamente.")