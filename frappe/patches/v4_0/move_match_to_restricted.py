# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import frappe

def execute():
	frappe.reload_doc("core", "doctype", "docperm")
	frappe.db.sql("""update `tabDocPerm` set apply_user_permissions=1 where `match`='owner'""")
	frappe.clear_cache()