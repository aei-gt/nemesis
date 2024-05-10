// Copyright (c) 2024, aei.gt and contributors
// For license information, please see license.txt

frappe.ui.form.on("Talonario de Boletas", {
    refresh(frm) { 
        frm.add_custom_button("Generar Boletas",() => {
                frm.doc.boleta_detalle = []
                for (let i = frm.doc.boleta_inicial; i < frm.doc.boleta_final; i++) {
                    frm.add_child('boleta_detalle', {
                        boleta_id : i,
                        talonario_id : frm.doc.talonario_id,
                        agente_id : frm.doc.agente_name,
                    });
                }
                frm.refresh_field('boleta_detalle');
        })
    },
    agente_id (frm){
        frappe.db.get_value('Employee', frm.doc.agente_id, 'employee_name')
            .then(r => {
                frm.set_value("agente_name", r.message.employee_name)
            })
    }
 });
