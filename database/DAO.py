from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():
    @staticmethod
    def getAnni():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "select DISTINCT YEAR(Date) AS year from go_daily_sales"
        cursor.execute(query)

        for row in cursor:
            result.append(row["year"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getBrand():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "select distinct Product_brand as pb from go_products"
        cursor.execute(query)

        for row in cursor:
            result.append(row["pb"])
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getRetailers():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = "select * from go_retailers"
        cursor.execute(query)

        for row in cursor:
            result.append(Retailer(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getVendite(anno, brand, retailer):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select gds.`Date` as date, gds.Retailer_code as rc, gp.Product_number as pn , (gds.Quantity*gds.Unit_sale_price) as ricavo
from go_daily_sales gds , go_products gp , go_retailers gr 
where gds.Product_number = gp.Product_number and gds.Retailer_code =gr.Retailer_code 
and YEAR(gds.Date) = %s and gp.Product_brand =%s and gds.Retailer_code =%s"""
        cursor.execute(query, (anno, brand, retailer))

        for row in cursor:
            result.append((row["date"], row["rc"], row["pn"], row["ricavo"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAnalizza(anno, brand, retailer):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select SUM(ricavo) as gd, count(*) as n_vendite, count(distinct rc) as n_retailers, count(distinct pn) as n_product
from (select gds.`Date` as date, gds.Retailer_code as rc, gp.Product_number as pn , (gds.Quantity*gds.Unit_sale_price) as ricavo
from go_daily_sales gds , go_products gp , go_retailers gr 
where gds.Product_number = gp.Product_number and gds.Retailer_code =gr.Retailer_code 
and YEAR(gds.Date) = %s and gp.Product_brand =%s and gds.Retailer_code =%s) v"""
        cursor.execute(query, (anno, brand, retailer))
        row = cursor.fetchone()  # ✅ Aggiungi questa riga!
        result = (row["gd"], row["n_vendite"], row["n_retailers"], row["n_product"])
        cursor.close()
        conn.close()
        return result

