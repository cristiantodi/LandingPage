from django.contrib.auth.hashers import make_password
from import_export import resources
from users.models import User


class MiModeloResource(resources.ModelResource):
    class Meta:
        model = User
        # Otros campos y configuraciones...

    def before_save_instance(self, instance, using_transactions, dry_run):
        # Asegúrate de que la contraseña sea manejada como cadena
        password = str(instance.password)
        instance.password = make_password(password)
        super().before_save_instance(instance, using_transactions, dry_run)
