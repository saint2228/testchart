# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "testchart"
app_title = "Testchart"
app_publisher = "ridhosribumi"
app_description = "App for testchart"
app_icon = "octicon octicon-plus"
app_color = "#aec8fd"
app_email = "develop@ridhosribumi.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
#app_include_css = "/assets/testchart/css/frappe-charts.min.css"

#app_include_js = [
#	"assets/js/frappe-charts.min.iife.js"
    # "assets/js/frappe-charts.esm.js",
    # "assets/js/frappe-charts.min.cjs.js",
    # "assets/js/frappe-charts.min.esm.js"
#]


# include js, css files in header of web template
# web_include_css = "/assets/testchart/css/testchart.css"
# web_include_js = "/assets/testchart/js/testchart.js"
# web_include_js = [
# 	"assets/js/frappe-charts.min.iife.js",
# 	"assets/js/frappe-charts.esm.js",
# 	"assets/js/frappe-charts.min.cjs.js",
# 	"assets/js/frappe-charts.min.esm.js"
# ]

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "testchart.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "testchart.install.before_install"
# after_install = "testchart.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "testchart.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"testchart.tasks.all"
# 	],
# 	"daily": [
# 		"testchart.tasks.daily"
# 	],
# 	"hourly": [
# 		"testchart.tasks.hourly"
# 	],
# 	"weekly": [
# 		"testchart.tasks.weekly"
# 	]
# 	"monthly": [
# 		"testchart.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "testchart.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "testchart.event.get_events"
# }
