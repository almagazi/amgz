import frappe

def add_company_suffix(doc, field_name):
	if not doc.custom_company:
		return
	suffix = ' - ' + frappe.get_cached_value('Company', doc.custom_company, 'abbr')
	field_value = getattr(doc, field_name)
	if field_value and not field_value.endswith(suffix):
		setattr(doc, field_name, field_value + suffix)

def supplier_autoname(doc, method=None):
	add_company_suffix(doc, 'name')

def location_autoname(doc, method=None):
	add_company_suffix(doc, 'location_name')

def payment_term_autoname(doc, method=None):
	add_company_suffix(doc, 'payment_term_name')

def terms_and_conditions_autoname(doc, method=None):
	add_company_suffix(doc, 'title')