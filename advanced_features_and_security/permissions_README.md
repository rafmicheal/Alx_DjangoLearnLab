Permissions & Groups (Bookshelf app)
-----------------------------------

Models:
- bookshelf.Book includes custom permissions (codenames):
  - can_view
  - can_create
  - can_edit
  - can_delete

Groups created by migration:
- Editors  -> can_create, can_edit
- Viewers  -> can_view
- Admins   -> all four permissions

How to test locally:
1. Make sure migrations are applied (see commands below).
2. Run server: python manage.py runserver
3. Create users via admin or shell.
4. Assign a user to a group (Editors/Viewers/Admins) via Admin -> Authentication -> Groups.
5. Login as that user and try accessing the protected views:
   - list_books (requires bookshelf.can_view)
   - add_book  (requires bookshelf.can_create)
   - edit_book (requires bookshelf.can_edit)
   - delete_book (requires bookshelf.can_delete)

If you prefer to assign groups programmatically, the data migration included creates the groups and assigns permissions automatically.
