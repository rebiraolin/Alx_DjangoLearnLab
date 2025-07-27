# Permissions and Groups Setup

This application uses Django’s permissions framework to control access to the `Document` model.

## Permissions
- `can_view`: Allows viewing documents.
- `can_create`: Allows creating new documents.
- `can_edit`: Allows editing existing documents.
- `can_delete`: Allows deleting documents.

## Groups
1. **Editors**: Assigned `can_edit` and `can_create`.
2. **Viewers**: Assigned `can_view`.
3. **Admins**: Assigned all permissions.

## How to Test
1. Create users and assign them to the groups via the admin panel.
2. Log in as the users and attempt to perform actions like viewing, editing, or deleting documents to verify permissions.
