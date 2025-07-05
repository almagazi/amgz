frappe.treeview_settings["Supplier Group"] = {
	get_tree_nodes: "amgz.api.erpnext.supplier_group_get_children",
	add_tree_node: "amgz.api.erpnext.supplier_group_add_node",
	get_tree_root: false,
	root_label: "Supplier Group",
	filters: [
		{
			fieldname: "company",
			fieldtype: "Select",
			options: erpnext.utils.get_tree_options("company"),
			label: __("Company"),
			default: erpnext.utils.get_tree_default("company"),
		},
	],
  menu_items: [
		{
			label: __("New Supplier Group"),
			action: function () {
				frappe.new_doc("Supplier Group", true);
			},
			condition: 'frappe.boot.user.can_create.indexOf("Supplier Group") !== -1',
		},
	],
	ignore_fields: ["parent_supplier_group"],
};