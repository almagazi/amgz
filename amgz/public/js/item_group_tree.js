frappe.treeview_settings["Item Group"] = {
	get_tree_nodes: "amgz.api.erpnext.item_group_get_children",
	add_tree_node: "amgz.api.erpnext.item_group_add_node",
	get_tree_root: false,
	root_label: "Item Group",
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
			label: __("New Item Group"),
			action: function () {
				frappe.new_doc("Item Group", true);
			},
			condition: 'frappe.boot.user.can_create.indexOf("Item Group") !== -1',
		},
	],
	ignore_fields: ["parent_item_group"],
};