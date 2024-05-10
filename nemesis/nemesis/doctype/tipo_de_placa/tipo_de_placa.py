# Copyright (c) 2024, aei.gt and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class TipodePlaca(Document):
	def before_save(self):
		if len(self.placa_tipo)>25:			
			frappe.throw("Demasiado largo el texto, reduzca a menos de 25 caracteres")

		self.placa_tipo = self.placa_tipo.upper() # Revisar porque no funciona
		self.placa_tipo = self.placa_tipo.lower()
		

