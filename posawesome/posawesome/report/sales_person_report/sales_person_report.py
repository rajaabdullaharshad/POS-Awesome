import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    columns = [
        {
            "label": "Sales Person",
            "fieldname": "sales_person",
            "fieldtype": "Link",
            "options": "Sales Person",
            "width": 250,
        },
        {
            "label": "Sales Invoice",
            "fieldname": "sales_invoice",
            "fieldtype": "Link",
            "options": "Sales Invoice",
            "width": 250,
        },
        {
            "label": "Customer",
            "fieldname": "customer",
            "fieldtype": "Data",
            "width": 250,
        },
        {
            "label": "Total",
            "fieldname": "grand_total",
            "fieldtype": "Currency",
            "width": 250,
        }
    ]
    return columns

def get_data(filters):
    data = []

    # Fetch Sales Invoice data with Sales Team information based on filters
    sales_invoices = frappe.get_all(
        "Sales Invoice",
        filters=filters,
        fields=["*"]
    )

    for invoice in sales_invoices:
        if invoice.get("sales_team") and any(sales_person.get("sales_person") for sales_person in invoice.sales_team):
            for sales_person in invoice.sales_team:
                if sales_person.get("sales_person"):
                    data.append({
                        "sales_person": sales_person.sales_person,
                        "sales_invoice": invoice.name,
                        "customer": invoice.customer,
                        "grand_total": invoice.grand_total,
                    })

    return data
