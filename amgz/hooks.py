app_name = "amgz"
app_title = "almagazi SaaS"
app_publisher = "PT Amal Madani Gapura Zakiya"
app_description = "SaaS setup for almagazi"
app_email = "aulia@almagazi.id"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "amgz",
# 		"logo": "/assets/amgz/logo.png",
# 		"title": "almagazi SaaS",
# 		"route": "/amgz",
# 		"has_permission": "amgz.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/amgz/css/amgz.css"
# app_include_js = "/assets/amgz/js/amgz.js"

# include js, css files in header of web template
# web_include_css = "/assets/amgz/css/amgz.css"
# web_include_js = "/assets/amgz/js/amgz.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "amgz/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
doctype_tree_js = {
  "Customer Group" : "public/js/customer_group_tree.js",
  "Department" : "public/js/department_tree.js",
  "Item Group" : "public/js/item_group_tree.js",
  "Location" : "public/js/location_tree.js",
  "Sales Person" : "public/js/sales_person_tree.js",
  "Supplier Group" : "public/js/supplier_group_tree.js",
  "Territory" : "public/js/territory_tree.js",
}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "amgz/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "amgz.utils.jinja_methods",
# 	"filters": "amgz.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "amgz.install.before_install"
# after_install = "amgz.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "amgz.uninstall.before_uninstall"
# after_uninstall = "amgz.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "amgz.utils.before_app_install"
# after_app_install = "amgz.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "amgz.utils.before_app_uninstall"
# after_app_uninstall = "amgz.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "amgz.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

override_doctype_class = {
	"Company": "amgz.overrides.company.CustomCompany",
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Asset": {
		"autoname": "amgz.event.erpnext.asset_autoname",
	},
	"Asset Category": {
		"autoname": "amgz.event.erpnext.asset_category_autoname",
	},
	"Customer": {
		"autoname": "amgz.event.erpnext.customer_autoname",
	},
	"Customer Group": {
		"autoname": "amgz.event.erpnext.customer_group_autoname",
	},
	"Item": {
		"autoname": "amgz.event.erpnext.item_autoname",
	},
	"Item Group": {
		"autoname": "amgz.event.erpnext.item_group_autoname",
	},
	"Location": {
		"autoname": "amgz.event.erpnext.location_autoname",
    "on_update": "amgz.event.erpnext.location_on_update",
	},
	"Payment Term": {
		"autoname": "amgz.event.erpnext.payment_term_autoname",
	},
	"Price List": {
		"autoname": "amgz.event.erpnext.price_list_autoname",
	},
	"Sales Partner": {
		"autoname": "amgz.event.erpnext.sales_partner_autoname",
	},
	"Sales Person": {
		"autoname": "amgz.event.erpnext.sales_person_autoname",
	},
	"Supplier": {
		"autoname": "amgz.event.erpnext.supplier_autoname",
	},
	"Supplier Group": {
		"autoname": "amgz.event.erpnext.supplier_group_autoname",
	},
	"Terms and Conditions": {
		"autoname": "amgz.event.erpnext.terms_and_conditions_autoname",
	},
	"Territory": {
		"autoname": "amgz.event.erpnext.territory_autoname",
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"amgz.tasks.all"
# 	],
# 	"daily": [
# 		"amgz.tasks.daily"
# 	],
# 	"hourly": [
# 		"amgz.tasks.hourly"
# 	],
# 	"weekly": [
# 		"amgz.tasks.weekly"
# 	],
# 	"monthly": [
# 		"amgz.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "amgz.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "amgz.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "amgz.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["amgz.utils.before_request"]
# after_request = ["amgz.utils.after_request"]

# Job Events
# ----------
# before_job = ["amgz.utils.before_job"]
# after_job = ["amgz.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"amgz.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

fixtures = [
  {'dt': 'Translation'},
  {'dt': 'Workspace'},
  {'dt': 'Currency'},
  {'dt': 'System Settings'},
  {'dt': 'Navbar Settings'},
  {'dt': 'Website Settings'},
  {'dt': 'Portal Settings'},
  {'dt':'Custom Field', 'filters': [['module', '=', 'almagazi SaaS']]}, 
  {'dt':'Property Setter', 'filters': [['module', '=', 'almagazi SaaS']]}, 
  {'dt':'Role', 'filters': [['role_name', 'LIKE', 'AMGZ%']]}, 
  {'dt':'Custom DocPerm', 'filters': [['role', 'LIKE', 'AMGZ%']]}, 
]