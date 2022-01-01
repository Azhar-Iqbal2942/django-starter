from django.contrib.auth.models import BaseUserManager


class AccountManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email, password.
        """
        if not email:
            raise ValueError('Users must have an email address!')

        email = self.normalize_email(email)

        user = self.model(email= email,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user



    def create_staff(self, email, password, **extra_fields):
        """
        Create and save a Staff User with the given email, password.
        """
        user = self.create_user(email,password)
        
        user.is_staff = True
        user.save(using=self._db)
        return user



    def create_superuser(self, email, password):
        """
        Create and save a SuperUser with the given email and password.
        """
        user = self.create_user(email,password)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user