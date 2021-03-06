# Copyright (c) 2013, molie and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import cint, flt
import erpnext

def execute(filters=None):
	#if not filters: filters = {}
	message = ''
	data = []
	columns = get_columns()
	chart = get_chart_data(filters)
	data = get_data(filters)
	return columns, data,message,chart

def get_columns():
	return [
	    _("Name") + ":Data:100",
		_("Posting Date") + ":Date:150",
		_("Qty") + ":Float:150",
		_("Rate") + ":Float:150",
		_("Amount") + ":Float:150"
	]

def get_data(filters):
	conditions = get_conditions(filters)
	return frappe.db.sql(
		"""select
				nama,
				posting_date,
				qty,
				rate,
				amount
		   from
		   		`tabKASUS1`
		   where
		   		docstatus < 2
				%s
		  order by
		  		posting_date
		""" % conditions, as_list=1,debug=1)

def get_conditions(filters):
	conditions = ""
	if filters.get("from_date"):
		conditions += "and posting_date >= '%s'" % filters["from_date"]

	if filters.get("to_date"):
		conditions += "and posting_date <= '%s'" % filters["to_date"]

	return conditions


def get_chart_data(filters):
	conditions = get_conditions(filters)
	data_for_chart = frappe.db.sql(
	 """select
			posting_date,
			count(qty) as count_data_status
		from
			`tabKASUS1`
		where
			docstatus <2
			%s
		group by
			posting_date
		""" % conditions,as_dict=True)

	labels = []
	values = []
	for i in data_for_chart:
		labels.append(i.posting_date)
		values.append(i.count_data_status)
		datasets=[
			{
				'label': labels,
				'values': values
			}
		]
		chart={
			"data":{
				'labels':labels,
				'datasets':datasets
			}
		}
		chart["type"] = "line"
		chart["title"] = "Chart Kasus 1"
		chart["colors"] = ['red']

		#chart["height"] = 500

	return chart
