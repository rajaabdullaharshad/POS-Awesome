import frappe

@frappe.whitelist()
def get_salespersons():
    salespersons = frappe.get_all("Sales Person", filters={}, fields=["name", "sales_person_name"])
    return salespersons