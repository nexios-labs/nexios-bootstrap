from nexios.auth.users.simple import SimpleUser
from .base import BaseModel
from tortoise import fields

class Account(BaseModel,SimpleUser):
    """
    This class extends the BaseModel and SimpleUser classes to create an account model.
    It adds the user fields to the BaseModel and SimpleUser classes.

    example:
        email (fields.CharField): The email of the user.
        password (fields.CharField): The password of the user.
        role (fields.CharField): The role of the user.
    """


    @property
    def identity(self) -> str:
        """
        The identity of the user.

        Returns:
            str: The id of the user.
        """

    def has_permission(self, permission: str) -> bool:
        """
        Check if the user has the given permission.

        Args:
            permission (str): The permission to check.

        Returns:
            bool: True if the user has the permission, False otherwise.
        """
        
        