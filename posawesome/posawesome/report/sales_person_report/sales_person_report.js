// Copyright (c) 2023, Youssef Restom and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Sales person Report"] = {
	"filters": [
		{
			"label": "Sales Person",
			"fieldname": "sales_person",
			"fieldtype": "Link",
			"options": "Sales Person",
			"width": 150,
		}
	]
};
