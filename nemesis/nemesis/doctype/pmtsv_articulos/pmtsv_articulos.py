# Copyright (c) 2024, aei.gt and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PMTSV_Articulos(Document):	
	def before_save(self):
		if len(self.articulo)>6:			
			frappe.throw("No puede tener más de 6 caracteres el ID del artículo!")		
		
		self.articulo = self.articulo.upper() # Revisar porque no funciona
		self.descripcion = self.descripcion.upper() # Revisar porque no funciona
		