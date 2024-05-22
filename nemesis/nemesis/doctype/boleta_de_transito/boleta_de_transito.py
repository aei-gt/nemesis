# Copyright (c) 2024, aei.gt and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document



class BoletadeTransito(Document):
	pass

# @frappe.validate_and_sanitize_search_inputs
@frappe.whitelist()
def boletas_doc_query(doctype, txt, searchfield, start, page_len, filters):
	boletas_doc_list= frappe.get_all("Boleta de Transito", {}, "name")
	boletas_filters = set([row.name for row in boletas_doc_list])
	
	filters = {}
	if len(boletas_filters) > 0:
		filters["name"] = ["not in", boletas_filters]
	
	docs = frappe.get_list("Detalle de Talonario", filters, order_by="name", as_list=True)

	return docs 



# Validando NIT

# >>> from nit_dpi_validator import nit
# >>> nit.nit_validator('xxxxxxxx-x')
# True
# Validando DPI

# >>> from nit_dpi_validator import dpi
# >>> dpi.dpi_validator('xxxxxxxxxxxxx')
# True