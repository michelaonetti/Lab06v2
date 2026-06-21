import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.DARK
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_hello = None
        self.txt_result = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        self.txt_compagnie = ft.TextField(
            label="Compagnie minimo",
            width=400,
            hint_text="Inserisci una distanza minima"
        )

        # bottone che crea il grafo con  nodi e con archi con delle cindizioni
        self.btn_analizza = ft.ElevatedButton(text="Analizza Vendite", on_click=self._controller.handle_analizza)
        # menu dropdown
        self._ddAnno = ft.Dropdown(label="Anno")
        self._ddBrand = ft.Dropdown(label="Brand")
        self._ddRetailer = ft.Dropdown(label="Retailer")
        self._btnTopVendite = ft.ElevatedButton(text="Top Vendite",
                                                     on_click=self._controller.handle_top_vendite)
        self._controller.load(self._ddAnno)
        self._controller.load(self._ddRetailer)
        self._controller.load(self._ddBrand)
        row1 = ft.Row([self._ddAnno,self._ddBrand, self._ddRetailer],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        row2 = ft.Row([self.btn_analizza,self._btnTopVendite],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
