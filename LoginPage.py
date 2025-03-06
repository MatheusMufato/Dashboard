import customtkinter as ctk
from tkinter import messagebox
from RegistroPessoal import RegistroPessoal

class LoginPage(ctk.CTkFrame):
    def __init__(self, parent, show_dashboard, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.show_dashboard = show_dashboard
        self.configure(corner_radius=10, fg_color="#2a2d35")

        # Obter as dimensões da tela
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Calcular 70% do tamanho da tela
        window_width = int(screen_width * 0.7)
        window_height = int(screen_height * 0.7)

        # Definir o tamanho da janela
        self.master.geometry(f"{window_width}x{window_height}")

        # Login frame
        login_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#3b3f4a", width=600, height=400)
        login_frame.pack(pady=100, padx=300)
        login_frame.pack_propagate(False)

        label = ctk.CTkLabel(login_frame, text="Login", font=("Helvetica", 24, "bold"))
        label.pack(pady=30)

        self.username_entry = self.create_entry(login_frame, "Usuario")
        self.password_entry = self.create_entry(login_frame, "Senha", show="*")

        self.entries = [self.username_entry, self.password_entry]

        forgot_password_label = ctk.CTkLabel(login_frame, text="Esqueci minha senha", font=("Helvetica", 12), fg_color="transparent")
        forgot_password_label.pack(pady=10, anchor="c", padx=10)
        forgot_password_label.bind("<Button-1>", lambda e: self.forgot_password())
        forgot_password_label.bind("<Enter>", lambda e: self.on_hover(forgot_password_label, True))
        forgot_password_label.bind("<Leave>", lambda e: self.on_hover(forgot_password_label, False))
        forgot_password_label.configure(cursor="hand2")

        login_button = self.create_button(login_frame, "Login", self.validate_login)
        register_button = self.create_button(login_frame, "Registrar-se", self.show_register)

    def create_entry(self, parent, placeholder, show=None):
        entry = ctk.CTkEntry(parent, placeholder_text=placeholder, show=show, width=300, height=40, corner_radius=8)
        entry.pack(pady=10)
        entry.bind("<Return>", self.on_enter)
        entry.bind("<FocusIn>", lambda e: self.on_focus(entry, True))
        entry.bind("<FocusOut>", lambda e: self.on_focus(entry, False))
        return entry

    def create_button(self, parent, text, command):
        button = ctk.CTkButton(parent, text=text, command=command, width=300, height=40, corner_radius=8)
        button.pack(pady=10)
        button.bind("<Enter>", lambda e: self.on_hover(button, True))
        button.bind("<Leave>", lambda e: self.on_hover(button, False))
        return button

    def on_enter(self, event):
        current_index = self.entries.index(event.widget)
        if current_index < len(self.entries) - 1:
            self.entries[current_index + 1].focus()
        else:
            self.validate_login()

    def on_focus(self, widget, is_focused):
        if is_focused:
            self.animate_resize(widget, 300, 40, 320, 45)
            widget.configure(border_color="#cccccc")
        else:
            self.animate_resize(widget, 320, 45, 300, 40)
            widget.configure(border_color="#3b3f4a")

    @staticmethod
    def animate_resize(widget, start_width, start_height, end_width, end_height, steps=20, delay=5):
        delta_width = (end_width - start_width) / steps
        delta_height = (end_height - start_height) / steps

        def step(current_step):
            if current_step <= steps:
                new_width = int(start_width + delta_width * current_step)
                new_height = int(start_height + delta_height * current_step)
                widget.configure(width=new_width, height=new_height)
                widget.after(delay, step, current_step + 1)

        step(0)

    @staticmethod
    def animate_button_resize(widget, start_width, start_height, end_width, end_height, steps=5, delay=5):
        delta_width = (end_width - start_width) / steps
        delta_height = (end_height - start_height) / steps

        def step(current_step):
            if current_step <= steps:
                new_width = int(start_width + delta_width * current_step)
                new_height = int(start_height + delta_height * current_step)
                widget.configure(width=new_width, height=new_height)
                widget.after(delay, step, current_step + 1)

        step(0)

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin":
            self.show_dashboard()
        else:
            messagebox.showerror("Erro de Login", "Verifique suas Informações e tente novamente.")

    def show_register(self):
        for widget in self.winfo_children():
            widget.destroy()
        registro_pessoal = RegistroPessoal(self, self.show_dashboard)
        registro_pessoal.pack(fill="both", expand=True)

    @staticmethod
    def forgot_password():
        messagebox.showinfo("Esqueci a senha", "A recuperação de Senha ainda não foi implementada.")

    def on_hover(self, widget, is_hovering):
        if is_hovering:
            if isinstance(widget, ctk.CTkButton):
                widget.original_fg_color = widget.cget("fg_color")
                widget.original_text_color = widget.cget("text_color")
                widget.configure(fg_color="white", text_color="black")
                self.animate_button_resize(widget, 300, 40, 320, 45)
            else:
                widget.configure(font=("Helvetica", 13, "bold"), fg_color="transparent", text_color="white")
        else:
            if isinstance(widget, ctk.CTkButton):
                widget.configure(fg_color=widget.original_fg_color, text_color=widget.original_text_color)
                self.animate_button_resize(widget, 320, 45, 300, 40)
            else:
                widget.configure(font=("Helvetica", 12), fg_color="transparent", text_color="white")