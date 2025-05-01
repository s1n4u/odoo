Veterinary Clinic Management
============================

A comprehensive veterinary clinic management module for Odoo 17.0 that enables veterinarians to efficiently manage patients, appointments, diagnoses, and treatments.

Features
--------

🐾 **Core Functionality**
~~~~~~~~~~~~~~~~~~~~~~~~~

- Manage **animal patients** with species, breed, age, gender, image, and owner details.
- Link pets to their **owners (res.partner)** with full integration in the partner form.
- Define and organize **animal species** and **breeds** using dictionaries.
- Schedule and manage **veterinary appointments** with status tracking.
- Record **diagnoses**, treatments, and recommendations.
- Assign **medicines** with dosage form, quantity, expiration, and manufacturer data.
- Generate printable **PDF diagnosis reports** via QWeb.

💌 **Automation**
~~~~~~~~~~~~~~~~~

- Automatically **congratulate pet owners** by email when it's their pet’s birthday.
- Filter patients whose **birthday is today** using a smart filter.
- Integrated **quick appointment wizard** directly from the patient form.

💬 **Communication & Tracking**
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Chatter integration on all major models for **logging** and **activity tracking**.
- Email templates and mail.thread support on patient and diagnosis models.

🎨 **User Interface**
~~~~~~~~~~~~~~~~~~~~~

- Clean and functional **tree**, **form**, and **kanban** views.
- Smart use of **badges** and **groupings** (e.g., group patients by species).
- Color-coded **appointment status** (planned, done, canceled).

Installation
------------

1. Place the `vet_clinic` module inside your Odoo `custom_addons` directory.
2. Restart your Odoo server.
3. Update the app list.
4. Install the module via Apps.

Dependencies
------------

- base
- mail
- product
- web

Security & Access Control
--------------------------

Includes two access groups:

- **Veterinary Admin**
- **Veterinary User**

Each model includes dedicated access rules to limit or extend functionality by group.

Demo Data
---------

This module includes rich demo data:

- Predefined doctors and owners.
- Pets (dogs, cats, birds).
- Past and future appointments.
- Diseases, medicines, and diagnoses.

Usage Tips
----------

- To test birthday email automation, call the method `_check_birthdays_and_send_emails` on `vet.patient`.
- Customize email templates from **Settings > Technical > Email > Templates**.
- All text is in **English**, but you can localize using standard Odoo translation tools.

License
-------

OPL-1

Author
------

Created by **s1n**

