# Permissions and Groups Setup

This app uses Django's groups and custom permissions to restrict access:

## Custom Permissions (defined in Book model)
- can_view
- can_create
- can_edit
- can_delete

## Groups
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

## Views
Each view is protected using @permission_required decorators.

## Testing
Create users and assign them to groups via admin or shell. Log in and verify access.
