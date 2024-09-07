import frappe
import pyodbc
import json
import requests
from datetime import datetime, time
@frappe.whitelist(allow_guest=True)
def boleta_records():
    results = frappe.get_all("Boleta de Transito",fields=[ 'tipo_de_placa','infraccion_lugar','infraccion_hora','descripcion','boleta_valor','infraccion_imagen','infraccion_fecha','placa_id','marca_del_vehiculo','color','boleta_id'])
    return results 
