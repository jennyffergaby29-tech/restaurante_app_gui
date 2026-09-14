import tkinter as tk
from tkinter import ttk

class MainView(ttk.Frame):
    def __init__(self, master, servicio, al_cerrar_sesion):
        super().__init__(master, padding="15")
        self.servicio = servicio
        self.al_cerrar_sesion = al_cerrar_sesion
        self.usuario_actual = None

        self.crear_componentes()

    def set_usuario(self, usuario):
        self.usuario_actual = usuario
        self.lbl_bienvenida.config(text=f"Bienvenido, {usuario.username} ({usuario.rol})")
        self.mostrar_productos()

    def crear_componentes(self):
        header_frame = ttk.Frame(self)
        header_frame.pack(fill="x", pady=(0, 10))

        self.lbl_bienvenida = ttk.Label(header_frame, text="", font=("Helvetica", 11, "bold"))
        self.lbl_bienvenida.pack(side="left")

        btn_logout = ttk.Button(header_frame, text="Cerrar Sesión", command=self.al_cerrar_sesion)
        btn_logout.pack(side="right")

        nav_frame = ttk.Frame(self)
        nav_frame.pack(fill="x", pady=5)

        ttk.Button(nav_frame, text="Productos", command=self.mostrar_productos).pack(side="left", padx=5)
        ttk.Button(nav_frame, text="Usuarios", command=self.mostrar_usuarios).pack(side="left", padx=5)
        ttk.Button(nav_frame, text="Ventas", command=self.mostrar_ventas).pack(side="left", padx=5)

        ttk.Separator(self, orient="horizontal").pack(fill="x", pady=10)

        self.content_frame = ttk.Frame(self)
        self.content_frame.pack(fill="both", expand=True)

    def limpiar_contenido(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def mostrar_productos(self):
        self.limpiar_contenido()
        ttk.Label(self.content_frame, text="Productos Registrados", font=("Helvetica", 11, "bold")).pack(anchor="w", pady=5)

        columnas = ("id", "nombre", "precio", "stock")
        tabla = ttk.Treeview(self.content_frame, columns=columnas, show="headings", height=8)
        
        tabla.heading("id", text="ID")
        tabla.heading("nombre", text="Nombre")
        tabla.heading("precio", text="Precio ($)")
        tabla.heading("stock", text="Stock")

        tabla.column("id", width=50, anchor="center")
        tabla.column("nombre", width=180)
        tabla.column("precio", width=80, anchor="e")
        tabla.column("stock", width=80, anchor="center")

        productos = self.servicio.obtener_productos()
        for p in productos:
            tabla.insert("", tk.END, values=(p.id, p.nombre, f"{p.precio:.2f}", p.stock))

        tabla.pack(fill="both", expand=True)

    def mostrar_usuarios(self):
        self.limpiar_contenido()
        ttk.Label(self.content_frame, text="Usuarios Registrados", font=("Helvetica", 11, "bold")).pack(anchor="w", pady=5)

        columnas = ("username", "rol")
        tabla = ttk.Treeview(self.content_frame, columns=columnas, show="headings", height=8)
        
        tabla.heading("username", text="Usuario")
        tabla.heading("rol", text="Rol")

        tabla.column("username", width=150)
        tabla.column("rol", width=150)

        usuarios = self.servicio.obtener_usuarios()
        for u in usuarios:
            tabla.insert("", tk.END, values=(u.username, u.rol))

        tabla.pack(fill="both", expand=True)

    def mostrar_ventas(self):
        self.limpiar_contenido()
        ttk.Label(self.content_frame, text="Módulo de Ventas", font=("Helvetica", 11, "bold")).pack(anchor="w", pady=5)
        ttk.Label(self.content_frame, text="Funcionalidad pendiente de desarrollo.", foreground="gray").pack(pady=20)