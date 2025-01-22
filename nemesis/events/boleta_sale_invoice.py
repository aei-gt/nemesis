import frappe

@frappe.whitelist()
def create_invoice(boleta_name):
    boleta_doc= frappe.get_doc("Boleta de Transito", boleta_name)
    
    
    if boleta_doc.estado_boleta != "VERIFICADA":
        frappe.throw("Invoice can only be created when the Boleta status is 'VERIFICADA'.")
        # total_amount=float(boleta.boleta_valor) * float(boleta.boleta_id)
    si_doc = frappe.get_doc({
        "doctype": "Sales Invoice",
        "customer": boleta_doc.infractor_cui,
        "set_posting_time":1,
        "posting_date": boleta_doc.infraccion_fecha,
        "due_date": boleta_doc.infraccion_fecha,
        "custom_reference_doctype": boleta_doc.doctype,
        "custom_reference_name": boleta_doc.name, 
    })
    si_doc.append("items", {
        "item_code": "SPMT01",
        "rate": boleta_doc.boleta_valor,  
        "qty": 1,  
        "description": boleta_doc.descripcion 
    })

    si_doc.save()
    si_doc.submit()
    boleta_doc.append("generated_invoices", {
        "sales_invoice": si_doc.name,
        "posting_date": boleta_doc.infraccion_fecha,
        "due_date": boleta_doc.infraccion_fecha,
        "amount": boleta_doc.boleta_valor, 
        "status": si_doc.status 
    })
    boleta_doc.total_amount+=boleta_doc.boleta_valor
    boleta_doc.save()
    boleta_doc.reload()

    return f"Invoice {si_doc.name} created successfully."


def on_invoice_update(doc,method=None):
    for ref in doc.references:
        if ref.reference_doctype == "Sales Invoice" and ref.reference_name:
            sales_invoice = frappe.get_doc("Sales Invoice", ref.reference_name)
            if sales_invoice.custom_reference_doctype and sales_invoice.custom_reference_name:
                catastro_sp=frappe.get_doc(sales_invoice.custom_reference_doctype,sales_invoice.custom_reference_name)
                for row in catastro_sp.generated_invoices:
                    if row.sales_invoice==sales_invoice.name:
                        row.status=sales_invoice.status
                catastro_sp.save()
                catastro_sp.reload()