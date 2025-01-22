// Copyright (c) 2024, aei.gt and contributors
// For license information, please see license.txt

frappe.ui.form.on("Boleta de Transito", {
    setup:function(frm,dt,dn){
        frm.set_query("boleta_id", function() {
			return {
				query: "nemesis.nemesis.doctype.boleta_de_transito.boleta_de_transito.boletas_doc_query",
				filters: {
					company: frm.doc.company
				}
			};
		});
    },
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
    refresh: function(frm) {
        if (frm.doc.estado_boleta === "VERIFICADA") {
            frm.add_custom_button('Create Invoice', function() {
                frappe.call({
                    method: "nemesis.events.boleta_sale_invoice.create_invoice",
                    args: {
                        boleta_name: frm.doc.name
                    },
                    callback: function(r) {
                        if (!r.exc) {
                            frappe.msgprint(r.message);
                            frm.refresh();
                        }
                    }
                });
            });
        }
        frm.fields_dict.generated_invoices.grid.wrapper.find('.grid-row').each(function () {
            let row_doc = $(this).data('doc'); // Child table row data
            if (row_doc) {
                let $status_cell = $(this).find('.grid-static-col[data-fieldname="status"]');
                if (row_doc.status === "Unpaid") {
                    $status_cell.css({
                        "background-color": "#bd3e0c",
                        "color": "white",
                        "font-weight": "bold",
                    }).addClass('indicator-pill #bd3e0c');
                } else if (row_doc.status === "Paid") {
                    $status_cell.css({
                        "background-color": "#16794c",
                        "color": "white",
                        "font-weight": "bold",
                    }).addClass('indicator-pill #16794c');
                }else if (row_doc.status === "Overdue") {
                    $status_cell.css({
                        "background-color": "#851111",
                        "color": "white",
                        "font-weight": "bold",
                    }).addClass('indicator-pill  #851111');
                }
            }
        });
    }
});
