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
        Create and save a User with the given email, password and username.
        """
        if not email:
            raise ValueError('Staff must have an email address!')

        email = self.normalize_email(email)

        user = self.create_user(
            email= email,
            password=password,
            **extra_fields,
            )
        user.is_staff = True
        user.save(using=self._db)
        return user



    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        user = self.create_user(
            email= self.normalize_email(email),
            password = password,
            **extra_fields,
            )

        user.is_active = True
        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)

        return user