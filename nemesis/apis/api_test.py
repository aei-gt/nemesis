import frappe
import pyodbc
import json
import requests
from datetime import datetime, time

@frappe.whitelist(allow_guest=True)
def send_data():
    settings = frappe.get_doc("Word Press Api Setting", "Word Press Api Setting")
    host = settings.get("host")
    user = settings.get("user")
    password = settings.get("password")
    database = settings.get("database")
    table = settings.get("table")
    odbc_version = settings.get("odbc_version")

    conn_str = (
        f'DRIVER={odbc_version};'
        f'SERVER={host};'
        f'DATABASE={database};'
        f'UID={user};'
        f'PWD={password}'
    )
    
    try:
        connection = pyodbc.connect(conn_str)
        cursor = connection.cursor()

        query = f"""
            SELECT 
                ID_Global, 
                EmployeeID,
                AccessDate,
                AccessTime
            FROM {table}
            GROUP BY ID_Global, EmployeeID, AccessDate, AccessTime
            ORDER BY AccessDate
        """
        cursor.execute(query)

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]

        for result in results:
            for key, value in result.items():
                if isinstance(value, datetime):
                    result[key] = value.isoformat()
                elif isinstance(value, time):
                    result[key] = value.strftime("%H:%M:%S")

    except pyodbc.Error as e:
        frappe.log_error(f"Database Error: {str(e)}")
        results = []

    finally:
        cursor.close()
        connection.close()
    
    frappe.msgprint("Operation successful!")
    return json.dumps(results)










@frappe.whitelist(allow_guest=True)
def boleta_records():
    results = frappe.get_all("Boleta de Transito",fields=[ 'infraccion_lugar','infraccion_hora','descripcion','boleta_valor','infraccion_imagen','infraccion_fecha','placa_id','marca_del_vehiculo','color','boleta_id'])
    return results 
