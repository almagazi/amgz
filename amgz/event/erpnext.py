import frappe

def add_company_suffix(doc, field_name):
	if not doc.custom_company:
		return
	suffix = ' - ' + frappe.get_cached_value('Company', doc.custom_company, 'abbr')
	field_value = getattr(doc, field_name)
	if field_value and not field_value.endswith(suffix):
		setattr(doc, field_name, field_value + suffix)

def update_naming_series(doctype, naming_series, field_name='naming_series'):
	series = frappe.get_all(
		'Property Setter', 
		filters={'doc_type': doctype, 'field_name': field_name, 'property': 'options'},
		fields=['name', 'value'])
	if series:
		prop_setter_name = series[0].name
		current_options_str  = series[0].value
		current_options = [opt.strip() for opt in current_options_str.split("\n") if opt.strip()]
		prop_setter_doc = frappe.get_doc("Property Setter", prop_setter_name)
	if not naming_series in current_options:
		current_options.append(naming_series)
		updated_options_str = "\n".join(current_options)
		if prop_setter_doc:
			prop_setter_doc.value = updated_options_str
			prop_setter_doc.save()

def asset_autoname(doc, method=None):
	if not doc.company:
		return
	prefix = frappe.get_cached_value('Company', doc.company, 'abbr')
	prefix_group = frappe.db.get_value('Item', doc.item_code, 'custom_group_abbbreviation')
	year_available = frappe.utils.getdate(doc.available_for_use_date).year
	naming = f'{prefix}-AST-{prefix_group}-{year_available}-'
	update_naming_series('Asset', naming)
	doc.naming_series = naming #frappe.model.naming.getseries(naming, 5)

def asset_category_autoname(doc, method=None):
	add_company_suffix(doc, 'asset_category_name')

def customer_autoname(doc, method=None):
	add_company_suffix(doc, 'name')

def customer_group_autoname(doc, method=None):
	add_company_suffix(doc, 'customer_group_name')

def item_autoname(doc, method=None):
	add_company_suffix(doc, 'name')

def item_group_autoname(doc, method=None):
	add_company_suffix(doc, 'item_group_name')

def location_autoname(doc, method=None):
	add_company_suffix(doc, 'location_name')

def location_on_update(doc, method=None):
	frappe.utils.nestedset.update_nsm(doc)

def payment_term_autoname(doc, method=None):
	add_company_suffix(doc, 'payment_term_name')

def sales_partner_autoname(doc, method=None):
	add_company_suffix(doc, 'sales_partner_name')

def sales_person_autoname(doc, method=None):
	add_company_suffix(doc, 'sales_person_name')

def supplier_autoname(doc, method=None):
	add_company_suffix(doc, 'name')

def supplier_group_autoname(doc, method=None):
	add_company_suffix(doc, 'supplier_group_name')

def terms_and_conditions_autoname(doc, method=None):
	add_company_suffix(doc, 'title')

def territory_autoname(doc, method=None):
	add_company_suffix(doc, 'territory_name')
