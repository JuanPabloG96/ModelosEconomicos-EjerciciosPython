import customtkinter as ctk
from datos.datos_elementos import get_elements_data

# Configuración de CustomTkinter
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class PeriodicTable(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Tabla Periódica de los Elementos")
        self.geometry("1400x900")
        
        # Colores según el estado
        self.colors = {
            'solid': '#8B7355',
            'liquid': '#4DB8FF',
            'gas': '#FFE066',
            'synthetic': '#A9A9A9'
        }
        
        # Frame principal
        main_frame = ctk.CTkFrame(self, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Panel superior con leyenda
        self.create_legend(main_frame)
        
        # Panel de información
        self.create_info_panel(main_frame)
        
        # Tabla periódica
        self.create_periodic_table(main_frame)
        
    def create_legend(self, parent):
        legend_frame = ctk.CTkFrame(parent, height=40)
        legend_frame.pack(fill="x", pady=(0, 10))
        legend_frame.pack_propagate(False)
        
        title = ctk.CTkLabel(legend_frame, text="LA TABLA PERIÓDICA", font=ctk.CTkFont(size=20, weight="bold"))
        title.pack(side="top", pady=5)
        
        colors_frame = ctk.CTkFrame(legend_frame, fg_color="transparent")
        colors_frame.pack(side="bottom")
        
        for text, color in [("sólido", 'solid'), ("líquido", 'liquid'), ("gas", 'gas'), ("sintético", 'synthetic')]:
            frame = ctk.CTkFrame(colors_frame, fg_color=self.colors[color], 
                               width=80, height=20)
            frame.pack(side="left", padx=5)
            frame.pack_propagate(False)
            label = ctk.CTkLabel(frame, text=text, font=ctk.CTkFont(size=10))
            label.pack(expand=True)
    
    def create_info_panel(self, parent):
        info_frame = ctk.CTkFrame(parent, height=120)
        info_frame.pack(fill="x", pady=(0, 10))
        info_frame.pack_propagate(False)
        
        # Primera fila
        row1 = ctk.CTkFrame(info_frame, fg_color="transparent")
        row1.pack(fill="x", padx=10, pady=5)
        
        self.element_label = ctk.CTkLabel(row1, text="Elemento", font=ctk.CTkFont(size=14, weight="bold"))
        self.element_label.pack(side="left", padx=5)
        
        self.discoverer_label = ctk.CTkLabel(row1, text="Descubridor", font=ctk.CTkFont(size=12))
        self.discoverer_label.pack(side="left", padx=20)
        
        # Segunda fila
        row2 = ctk.CTkFrame(info_frame, fg_color="transparent")
        row2.pack(fill="x", padx=10, pady=5)
        
        self.weight_label = ctk.CTkLabel(row2, text="Peso Atómico:", font=ctk.CTkFont(size=12))
        self.weight_label.pack(side="left", padx=5)
        
        self.shell_label = ctk.CTkLabel(row2, text="Configuración:", font=ctk.CTkFont(size=12))
        self.shell_label.pack(side="left", padx=20)
        
        # Tercera fila
        row3 = ctk.CTkFrame(info_frame, fg_color="transparent")
        row3.pack(fill="x", padx=10, pady=5)
        
        self.temp_label = ctk.CTkLabel(row3, text="Fusión | Ebullición (°C):", font=ctk.CTkFont(size=12))
        self.temp_label.pack(side="left", padx=5)
        self.gravity_label = ctk.CTkLabel(row3, text="Densidad:", font=ctk.CTkFont(size=12))
        self.gravity_label.pack(side="left", padx=20)
    
    def create_periodic_table(self, parent):
        table_frame = ctk.CTkScrollableFrame(parent)
        table_frame.pack(fill="both", expand=True)
        
        # Obtener datos desde el archivo externo
        elements = get_elements_data()
        
        # Crear la tabla
        for element in elements:
            self.create_element_button(table_frame, element)
    
    def create_element_button(self, parent, element):
        btn = ctk.CTkButton(
            parent,
            text=f"{element['num']}\n{element['symbol']}",
            width=60,
            height=60,
            fg_color=self.colors[element['state']],
            hover_color=self.adjust_color(self.colors[element['state']]),
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="black" if element['state'] in ['liquid', 'gas'] else "white"
        )
        btn.grid(row=element['row'], column=element['col'], padx=2, pady=2)
        
        btn.bind("<Enter>", lambda e: self.show_info(element))
        
    def show_info(self, element):
        self.element_label.configure(text=f"{element['num']} {element['name']}")
        self.discoverer_label.configure(text=f"Descubridor: {element['discoverer']}")
        self.weight_label.configure(text=f"Peso Atómico: {element['weight']}")
        self.shell_label.configure(text=f"Configuración: {element['shell']}")
        self.temp_label.configure(text=f"Fusión | Ebullición: {element['melt']} | {element['boil']}")
        self.gravity_label.configure(text=f"Densidad: {element['gravity']}")
    
    def adjust_color(self, color):
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        
        r = int(r * 0.8)
        g = int(g * 0.8)
        b = int(b * 0.8)
        
        return f"#{r:02x}{g:02x}{b:02x}"

if __name__ == "__main__":
    app = PeriodicTable()
    app.mainloop()
