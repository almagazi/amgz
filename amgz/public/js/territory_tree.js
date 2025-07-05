frappe.treeview_settings["Territory"] = {
	get_tree_nodes: "amgz.api.erpnext.territory_get_children",
	add_tree_node: "amgz.api.erpnext.territory_add_node",
	get_tree_root: false,
	root_label: "Territory",
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
			label: __("New Territory"),
			action: function () {
				frappe.new_doc("Territory", true);
			},
			condition: 'frappe.boot.user.can_create.indexOf("Territory") !== -1',
		},
	],
	ignore_fields: ["parent_territory"],
};