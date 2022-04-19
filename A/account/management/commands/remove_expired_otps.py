from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from account.models import OtPCode


class Command(BaseCommand):
    help = 'delete expire otp code unused'

    def handle(self, *args, **options):
        expire = datetime.now() - timedelta(minutes=2)
        OtPCode.objects.filter(created__lt=expire).delete()
        self.stdout.write(self.style.SUCCESS('Successfully delete expiered code '))
