import frappe

@frappe.whitelist()
def create_invoice(boleta_name):
    boleta = frappe.get_doc("Boleta de Transito", boleta_name)
    
    
    if boleta.estado_boleta != "VERIFICADA":
        frappe.throw("Invoice can only be created when the Boleta status is 'VERIFICADA'.")

    si_doc = frappe.get_doc({
        "doctype": "Sales Invoice",
        "customer": boleta.infractor_cui,
        "set_posting_time":1,
        "posting_date": boleta.infraccion_fecha,
        "due_date": boleta.infraccion_fecha, 
    })
    si_doc.append("items", {
        "item_code": "SPMT01",
        "rate": boleta.boleta_valor,  
        "qty": boleta.boleta_id,  
        "description": boleta.descripcion 
    })

    si_doc.save()
    si_doc.submit()
    boleta.invoice_created= 1
    boleta.invoice_reference=si_doc.name
    boleta.save()
    boleta.reload()
    
    return f"Invoice {si_doc.name} created successfully."
