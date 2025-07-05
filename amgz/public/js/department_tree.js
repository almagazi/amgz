frappe.treeview_settings["Department"] = {
	get_tree_nodes: "erpnext.setup.doctype.department.department.get_children",
	add_tree_node: "erpnext.setup.doctype.department.department.add_node",
	get_tree_root: false,
	root_label: "Department",
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
			label: __("New Department"),
			action: function () {
				frappe.new_doc("Department", true);
			},
			condition: 'frappe.boot.user.can_create.indexOf("Department") !== -1',
		},
	],
	ignore_fields: ["parent_department"],
};