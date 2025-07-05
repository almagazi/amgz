frappe.treeview_settings["Location"] = {
	get_tree_nodes: "amgz.api.erpnext.location_get_children",
	add_tree_node: "amgz.api.erpnext.location_add_node",
	get_tree_root: false,
	root_label: "Location",
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
			label: __("New Location"),
			action: function () {
				frappe.new_doc("Location", true);
			},
			condition: 'frappe.boot.user.can_create.indexOf("Location") !== -1',
		},
	],
	ignore_fields: ["parent_location"],
};