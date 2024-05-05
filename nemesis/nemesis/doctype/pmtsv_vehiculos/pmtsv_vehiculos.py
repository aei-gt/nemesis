# Copyright (c) 2024, aei.gt and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PMTSV_Vehiculos(Document):
	def before_save(self):
		if len(self.placa_id)>8:			
			frappe.throw("Debe tener como maximo ocho (8) caracteres!")			
		else:
			self.placa_id = self.placa_id.upper() # Revisar porque no funciona
			
			#frappe.msgprint(self.placa_id.left(1))
		
