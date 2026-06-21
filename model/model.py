import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()  # grafico non orientato e semplice, per i pesi aggiungo weight=
        """self._nodes = DAO.getAllAirports()  # preno dao DAO con query tutti gli aeroporti
        self._idMapAO = {}  # id_aeroporto = oggetto aeroporto
        for n in self._nodes:
            # inserico nella id map cosi poi ripesco da qua per ritornare ai valori dell'oggeto aeroporto
            self._idMapAO[n.ID] = n"""

    def getAnni(self):
        return DAO.getAnni()
    def getBrand(self):
        return DAO.getBrand()
    def getRetailers(self):
        return DAO.getRetailers()
    def getVendite(self, anno, brand, retailer):
        return DAO.getVendite(anno, brand, retailer)
    def getAnalizza(self, anno, brand, retailer):
        return DAO.getAnalizza(anno, brand, retailer)