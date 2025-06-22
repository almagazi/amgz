import frappe
from erpnext.setup.doctype.company.company import Company
from frappe import _

class CustomCompany(Company):
	def after_insert(self):
		super(CustomCompany, self).after_insert()
		self.setup_custom_defaults()

	def setup_custom_defaults(self):
		self.create_default_departments()
		self.create_default_cost_centers()
		self.create_default_warehouses()
		self.create_default_tree_masters()

	def _create_doc_if_not_exists(self, doctype, doc_details):
		filters = doc_details.copy()
		filters["company"] = self.name
		if "is_group" in doc_details and doctype not in ['Warehouse', 'Cost Center']:
			filters = {frappe.scrub(doctype) + "_name": doc_details[frappe.scrub(doctype) + "_name"], "company": self.name}
		if not frappe.db.exists(doctype, filters):
			doc = frappe.get_doc({
				"doctype": doctype,
				**doc_details,
				"company": self.name,
			})
			doc.flags.ignore_permissions = True
			doc.flags.ignore_mandatory = True
			doc.insert()
			return doc
		return None
	
	def create_default_departments(self):
		self._create_doc_if_not_exists("Department", {
			"department_name": f"Semua Departmen - {self.abbr}",
			"is_group": 1,
			"parent_department": None,
		})

	def create_default_cost_center(self):
		self._create_doc_if_not_exists("Cost Center", {
			"cost_center_name": self.name,
			"is_group": 1,
		})
		child_cc_name = f"{_('Pusat')} - {self.abbr}"
		self._create_doc_if_not_exists("Cost Center", {
			"cost_center_name": _("Pusat"),
			"is_group": 0,
			"parent_cost_center": f"{self.name} - {self.abbr}",
		})
		self.db_set("cost_center", child_cc_name)
		self.db_set("round_off_cost_center", child_cc_name)
		self.db_set("depreciation_cost_center", child_cc_name)

	def create_default_warehouses(self):
		self._create_doc_if_not_exists("Warehouse", {
			"warehouse_name": _("Semua Gudang"),
			"is_group": 1,
		})
		self._create_doc_if_not_exists("Warehouse", {
			"warehouse_name": _("Gudang Pusat"),
			"is_group": 0,
			"parent_warehouse": f"{_('Semua Gudang')} - {self.abbr}",
		})

	def create_default_tree_masters(self):
		suffix = f" - {self.abbr}"
		default_groups = [
			{"doctype": "Supplier Group", "name": _("Semua Grup")},
			{"doctype": "Customer Group", "name": _("Semua Grup")},
			{"doctype": "Item Group", "name": _("Semua Grup")},
			{"doctype": "Location", "name": _("Semua Lokasi")},
			{"doctype": "Territory", "name": _("Semua Teritori")},
			{"doctype": "Sales Person", "name": _("Semua Marketer")},
		]
		for group_info in default_groups:
			doctype = group_info["doctype"]
			name_field = frappe.scrub(doctype) + "_name"
			self._create_doc_if_not_exists(doctype, {
				name_field: f"{group_info['name']}{suffix}",
				"is_group": 1,
				"parent_" + frappe.scrub(doctype): None, # Explicitly set root
			})
