import frappe
from erpnext.setup.doctype.company.company import Company

class CustomCompany(Company):
	def on_update(self):
		super(CustomCompany, self).on_update()
		self.setup_custom_defaults()

	def setup_custom_defaults(self):
		self.create_default_departments()
		self.create_default_cost_center()
		self.create_default_warehouses()
		self.create_default_tree_masters()

	def _create_doc_if_not_exists(self, doctype, doc_details):
		filters = doc_details.copy()
		filters['company'] = self.name
		if 'is_group' in doc_details and doctype not in ['Warehouse', 'Cost Center']:
			filters = {frappe.scrub(doctype) + '_name': doc_details[frappe.scrub(doctype) + '_name'], 'company': self.name}
		if not frappe.db.exists(doctype, filters):
			doc = frappe.get_doc({
				'doctype': doctype,
				**doc_details,
				'company': self.name,
			})
			doc.flags.ignore_permissions = True
			doc.flags.ignore_mandatory = True
			doc.insert()
			return doc
		return None
	
	def create_default_departments(self):
		self._create_doc_if_not_exists('Department', {
			'department_name': f'Umum',
			'is_group': 0,
			'parent_department': None,
		})

	def create_default_cost_center(self):
		self._create_doc_if_not_exists('Cost Center', {
			'cost_center_name': self.name,
			'is_group': 1,
		})
		child_cc_name = f'Pusat - {self.abbr}'
		self._create_doc_if_not_exists('Cost Center', {
			'cost_center_name': child_cc_name,
			'is_group': 0,
			'parent_cost_center': f'{self.name} - {self.abbr}',
		})
		self.db_set('cost_center', child_cc_name)
		self.db_set('round_off_cost_center', child_cc_name)
		self.db_set('depreciation_cost_center', child_cc_name)

	def create_default_warehouses(self):
		self._create_doc_if_not_exists('Warehouse', {
			'warehouse_name': 'Semua Gudang',
			'is_group': 1,
		})
		self._create_doc_if_not_exists('Warehouse', {
			'warehouse_name': 'Gudang Pusat',
			'is_group': 0,
			'parent_warehouse': f'Semua Gudang - {self.abbr}',
		})

	def create_default_tree_masters(self):
		suffix = f' - {self.abbr}'
		default_groups = [
			{'doctype': 'Supplier Group', 'name': 'Semua Grup'},
			{'doctype': 'Customer Group', 'name': 'Semua Grup'},
			{'doctype': 'Item Group', 'name': 'Semua Grup'},
			{'doctype': 'Location', 'name': 'Semua Lokasi'},
			{'doctype': 'Territory', 'name': 'Semua Teritori'},
			{'doctype': 'Sales Person', 'name': 'Semua Marketer'},
		]
		for group_info in default_groups:
			doctype = group_info['doctype']
			name_field = frappe.scrub(doctype) + '_name'
			self._create_doc_if_not_exists(doctype, {
				name_field: f"{group_info['name']}{suffix}",
				'is_group': 1,
				'parent_' + frappe.scrub(doctype): None,
				'custom_company': self.name,
			})
