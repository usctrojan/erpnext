# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals
import webnotes

def execute():
	from webnotes.profile import get_system_managers
	system_managers = get_system_managers(only_name=True)
	if not system_managers: 
		return
	
	# scheduler errors digest
	edigest = webnotes.new_bean("Email Digest")
	edigest.doc.fields.update({
		"name": "Scheduler Errors",
		"company": webnotes.conn.get_default("company"),
		"frequency": "Daily",
		"enabled": 1,
		"recipient_list": "\n".join(system_managers),
		"scheduler_errors": 1
	})
	edigest.insert()