# Copyright (c) 2024, aei.gt and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import get_link_to_form


class BoletadeTransito(Document):
	def validate(self):
		boletas_doc_list= frappe.get_all(self.doctype, {"boleta_id": self.boleta_id, "docstatus": ["<", 2] })
		if len(boletas_doc_list) > 0:
			frappe.throw(f"Boleta No already used in {get_link_to_form(self.doctype, boletas_doc_list[0].name)}")
	
# @frappe.validate_and_sanitize_search_inputs
@frappe.whitelist()
def boletas_doc_query(doctype, txt, searchfield, start, page_len, filters):
	boletas_doc_list= frappe.get_all("Boleta de Transito", {}, "boleta_id")
	boletas_filters = set([row.boleta_id for row in boletas_doc_list])
	
	filters = {}
	if len(boletas_filters) > 0:
		filters["name"] = ["not in", boletas_filters]
	
	docs = frappe.get_list("Detalle de Talonario", filters, order_by="name", as_list=True)

	return docs 



