import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._anno = None
        self._brand = None
        self._retailer = None


    def load(self, dd:ft.Dropdown()):
        anni = sorted(list(self._model.getAnni()))  # prende tutti gli aeroporti
        brand = sorted(list(self._model.getBrand()))
        retailers= sorted(list(self._model.getRetailers()), key=lambda x: x.Retailer_name)

        dd.options.append(ft.dropdown.Option("Nessun filtro"))
        if dd.label == "Anno":  # se dobbiamo popolar eil menu di partenza
            for f in anni:
                dd.options.append(ft.dropdown.Option(text=f,
                                                     data=f,
                                                     on_click=self.read_DD_Anno))
        elif dd.label == "Brand":
            for f in brand:
                dd.options.append(ft.dropdown.Option(text=f,
                                                     data=f,
                                                     on_click=self.read_DD_Brand))
        elif dd.label == "Retailer":
            for f in retailers:
                dd.options.append(ft.dropdown.Option(text=f.Retailer_name,
                                                     data=f,
                                                     on_click=self.read_DD_Retailer))

    def read_DD_Anno(self, e):
        print("read_DD_Anno called ")
        if e.control.data is None:
            self._anno = None
        else:
            self._anno = e.control.data
    def read_DD_Brand(self, e):
        print("read_DD_Brand called ")
        if e.control.data is None:
            self._brand = None
        else:
            self._brand = e.control.data
    def read_DD_Retailer(self, e):
        print("read_DD_Retailer called ")
        if e.control.data is None:
            self._retailer = None
        else:
            self._retailer = e.control.data

    def handle_analizza(self, e):
        if self._anno is  None or self._brand is  None or self._retailer is  None:
            self._view.create_alert("Seleziona un anno, un brand e un retailer")

        analisi = self._model.getAnalizza(self._anno, self._brand, self._retailer.Retailer_code)
        print(analisi)
        self._view.txt_result.controls.append(
            ft.Text(f"Analisi:\n Giro d'affari: {analisi[0]}\n Numero vendite: {analisi[1]}\n Numero retailers coinvolti: {analisi[2]}\n Numero prodotti coinvolti: {analisi[3]}"))
        self._view.update_page()
    def handle_top_vendite(self, e):
        if self._anno is None or self._brand is  None or self._retailer is None:
            self._view.create_alert("Seleziona un anno, un brand e un retailer")

        vendite= self._model.getVendite(self._anno, self._brand, self._retailer.Retailer_code)
        top_5 = sorted(vendite, key=lambda x: x[3], reverse=True)[:5]
        for t in top_5:
            self._view.txt_result.controls.append(ft.Text(f"Date: {t[0]} -- Retailer code:  {t[1]} --- Product Number: {t[2]} --- Ricavo: {t[3]}"))
        self._view.update_page()

