import frappe, json
from frappe.utils.nestedset import get_root_of
from frappe.desk.treeview import make_tree_args
from frappe.utils import cint

@frappe.whitelist()
def customer_group_get_children(doctype, parent=None, company=None, is_root=False, include_disabled=False):
	if isinstance(include_disabled, str):
		include_disabled = json.loads(include_disabled)
	fields = ["name as value", "is_group as expandable"]
	filters = set_filters(doctype, parent, company, include_disabled, 'parent_customer_group')
	return frappe.get_all(doctype, fields=fields, filters=filters, order_by="name")

@frappe.whitelist()
def item_group_get_children(doctype, parent=None, company=None, is_root=False, include_disabled=False):
	if isinstance(include_disabled, str):
		include_disabled = json.loads(include_disabled)
	fields = ["name as value", "is_group as expandable"]
	filters = set_filters(doctype, parent, company, include_disabled, 'parent_item_group')
	return frappe.get_all(doctype, fields=fields, filters=filters, order_by="name")

@frappe.whitelist()
def location_get_children(doctype, parent=None, company=None, is_root=False, include_disabled=False):
	if isinstance(include_disabled, str):
		include_disabled = json.loads(include_disabled)
	fields = ["name as value", "is_group as expandable"]
	filters=set_filters(doctype, parent, company, include_disabled, 'parent_location')
	print(doctype, parent, company, filters)
	return frappe.get_all(doctype, fields=fields, filters=filters, order_by="name")

@frappe.whitelist()
def sales_person_get_children(doctype, parent=None, company=None, is_root=False, include_disabled=False):
	if isinstance(include_disabled, str):
		include_disabled = json.loads(include_disabled)
	fields = ["name as value", "is_group as expandable"]
	filters = set_filters(doctype, parent, company, include_disabled, 'parent_sales_person')
	return frappe.get_all(doctype, fields=fields, filters=filters, order_by="name")

@frappe.whitelist()
def supplier_group_get_children(doctype, parent=None, company=None, is_root=False, include_disabled=False):
	if isinstance(include_disabled, str):
		include_disabled = json.loads(include_disabled)
	fields = ["name as value", "is_group as expandable"]
	filters = set_filters(doctype, parent, company, include_disabled, 'parent_supplier_group')
	return frappe.get_all(doctype, fields=fields, filters=filters, order_by="name")

@frappe.whitelist()
def territory_get_children(doctype, parent=None, company=None, is_root=False, include_disabled=False):
	if isinstance(include_disabled, str):
		include_disabled = json.loads(include_disabled)
	fields = ["name as value", "is_group as expandable"]
	filters = set_filters(doctype, parent, company, include_disabled, 'parent_territory')
	return frappe.get_all(doctype, fields=fields, filters=filters, order_by="name")

@frappe.whitelist()
def customer_group_add_node():
	args = make_tree_args(**frappe.form_dict)
	set_parent(args, 'parent_customer_group', 'All Customer Groups')
	frappe.get_doc(args).insert()
	
@frappe.whitelist()
def item_group_add_node():
	args = make_tree_args(**frappe.form_dict)
	set_parent(args, 'parent_item_group', 'All Item Groups')
	frappe.get_doc(args).insert()
	
@frappe.whitelist()
def location_add_node():
	args = make_tree_args(**frappe.form_dict)
	set_parent(args, 'parent_location', 'All Locations')
	frappe.get_doc(args).insert()
	
@frappe.whitelist()
def sales_person_add_node():
	args = make_tree_args(**frappe.form_dict)
	set_parent(args, 'parent_sales_person', 'Sales Team')
	frappe.get_doc(args).insert()
	
@frappe.whitelist()
def supplier_group_add_node():
	args = make_tree_args(**frappe.form_dict)
	set_parent(args, 'parent_supplier_group', 'All Supplier Groups')
	frappe.get_doc(args).insert()
	
@frappe.whitelist()
def territory_add_node():
	args = make_tree_args(**frappe.form_dict)
	set_parent(args, 'parent_territory', 'All Territories')
	frappe.get_doc(args).insert()
	
def set_parent(args, parent, value):
	if not args[parent]:
		args[parent] = value
	if cint(args.is_root):
		args[parent] = None

def set_filters(doctype, parent, company, include_disabled, parent_field):
	filters = {}
	if company == parent:
		filters["name"] = get_root_of(doctype)
	elif company:
		filters[parent_field] = parent
		filters["custom_company"] = company
	else:
		filters[parent_field] = parent
	if frappe.db.has_column(doctype, "disabled") and not include_disabled:
		filters["disabled"] = False
	return filters
