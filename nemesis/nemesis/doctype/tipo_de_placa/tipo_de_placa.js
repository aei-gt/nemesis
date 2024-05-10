// Copyright (c) 2024, aei.gt and contributors
// For license information, please see license.txt

frappe.ui.form.on("Tipo de Placa", {
	refresh(frm) {
            frm.add_custom_button("Revisar Registro",() => {
                console.log("Revisando el registro")
            })

	},
});
