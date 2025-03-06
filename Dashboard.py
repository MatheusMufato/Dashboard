import customtkinter as ctk
from Aulas import Aulas
from Calendario import Calendario
from Perfil import Perfil
from LoginPage import LoginPage

app = ctk.CTk()


def show_dashboard():
    for widget in app.winfo_children():
        widget.destroy()
    create_dashboard(app)

def create_dashboard(teste):
    teste.title("Dashboard")
    main_content = ctk.CTkFrame(teste, corner_radius=10, fg_color="#383f4c")
    main_content.grid(row=0, column=1, rowspan=2, sticky="nsew", padx=10, pady=10)

    def show_main_content():
        for widget in main_content.winfo_children():
            widget.destroy()

        sidebar = ctk.CTkFrame(teste, width=300, corner_radius=10, fg_color="#2a2d35")
        sidebar.grid(row=0, column=0, rowspan=2, sticky="ns", padx=20, pady=20)
        sidebar.pack_propagate(False)

        sidebar_inner = ctk.CTkFrame(sidebar, fg_color="transparent")
        sidebar_inner.pack(fill="both", expand=True, pady=20)

        logo_label = ctk.CTkLabel(sidebar_inner, text="Aluno", font=("Helvetica", 24, "bold"), fg_color="transparent")
        logo_label.pack(pady=20)

        nav_button5 = ctk.CTkButton(sidebar_inner, text="Perfil", width=180, height=40, corner_radius=8,
                                    command=lambda: show_page("Perfil"))
        nav_button5.pack(pady=10)

        nav_button1 = ctk.CTkButton(sidebar_inner, text="Aulas", width=180, height=40, corner_radius=8,
                                    command=lambda: show_page("Aulas"))
        nav_button1.pack(pady=10)

        nav_button2 = ctk.CTkButton(sidebar_inner, text="Notas", width=180, height=40, corner_radius=8,
                                    command=lambda: show_page("Notas"))
        nav_button2.pack(pady=10)

        nav_button3 = ctk.CTkButton(sidebar_inner, text="Calendario", width=180, height=40, corner_radius=8,
                                    command=lambda: show_page("Calendario"))
        nav_button3.pack(pady=10)

        nav_button4 = ctk.CTkButton(sidebar_inner, text="Configurações", width=180, height=40, corner_radius=8,
                                    command=lambda: show_page("Configurações"))
        nav_button4.pack(pady=10)

        nav_button6 = ctk.CTkButton(sidebar_inner, text="Sair", width=180, height=40, corner_radius=8,
                                    command=show_login_page)
        nav_button6.pack(pady=10, side="bottom")

        teste.grid_rowconfigure(0, weight=1)
        teste.grid_rowconfigure(1, weight=1)
        teste.grid_columnconfigure(1, weight=1)

        header = ctk.CTkFrame(main_content, height=60, corner_radius=8, fg_color="#2c3138")
        header.pack(fill="x", padx=20, pady=15)

        header_label = ctk.CTkLabel(header, text="Bem vindo, Matheus", font=("Helvetica", 18, "bold"),
                                    fg_color="transparent")
        header_label.pack(padx=20)

        dashboard_section = ctk.CTkFrame(main_content, corner_radius=10, fg_color="#454d59")
        dashboard_section.pack(padx=20, pady=20, fill="both", expand=True)

        dashboard_label = ctk.CTkLabel(dashboard_section, text="", font=("Helvetica", 16, "bold"))
        dashboard_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        footer = ctk.CTkFrame(main_content, height=40, corner_radius=10, fg_color="#2c3138")
        footer.pack(fill="x", side="bottom", padx=20, pady=15)

        footer_label = ctk.CTkLabel(footer, text="Central do aluno - 2025", font=("Helvetica", 10),
                                    fg_color="transparent")
        footer_label.place(relx=0.5, rely=0.5, anchor="center")

    def show_page(page_name):
        for widget in main_content.winfo_children():
            widget.destroy()
        if page_name == "Aulas":
            new_page = Aulas(main_content, show_main_content)
        elif page_name == "Calendario":
            new_page = Calendario(main_content, show_main_content)
        elif page_name == "Perfil":
            new_page = Perfil(main_content, show_main_content)
        else:
            new_page = ctk.CTkLabel(main_content, text=f"Página {page_name} não implementada",
                                    font=("Helvetica", 16, "bold"))
        new_page.pack(fill="both", expand=True)

    def show_login_page():
        for widget in teste.winfo_children():
            widget.destroy()
        login_page = LoginPage(teste, show_dashboard)
        login_page.pack(fill="both", expand=True)

    show_main_content()
