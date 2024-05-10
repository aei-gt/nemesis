# Copyright (c) 2024, aei.gt and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class BoletadeTransito(Document):
	pass


#
#Validando NIT

#>>> from nit_dpi_validator import nit
#>>> nit.nit_validator('xxxxxxxx-x')
#True
#Validando DPI

#>>> from nit_dpi_validator import dpi
#>>> dpi.dpi_validator('xxxxxxxxxxxxx')
#True