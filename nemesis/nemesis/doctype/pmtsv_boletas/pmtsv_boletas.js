// Copyright (c) 2024, aei.gt and contributors
// For license information, please see license.txt

frappe.ui.form.on("PMTSV_Boletas", {
	infractor_cui(frm) {
        if(frm.doc.infractor_cui){
            $("[data-fieldname='infractor_nit']").prop('disabled', true);
            frappe.db.get_value('Customer', frm.doc.infractor_cui, 'customer_name')
            .then(r => {
                frm.set_value("infractor_nombre", r.message.customer_name)
            })
        }
        else{
            $("[data-fieldname='infractor_nit']").prop('disabled', false);
            frm.set_value("infractor_nombre", "")
        }
	},
    infractor_nit(frm) {
        if(frm.doc.infractor_nit){
            $("[data-fieldname='infractor_cui']").prop('disabled', true);
            frappe.db.get_value('Customer', frm.doc.infractor_nit, 'customer_name')
            .then(r => {
                frm.set_value("infractor_nombre", r.message.customer_name)
            })
        }
        else{
            $("[data-fieldname='infractor_cui']").prop('disabled', false);
            frm.set_value("infractor_nombre", "")
        }
	},
});
