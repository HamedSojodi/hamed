from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from account.models import OtPCode
import pytz


class Command(BaseCommand):
    help = 'delete expire otp code unused'

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        if options['delete']:
            expire = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2)
            if OtPCode.objects.filter(created__lt=expire).exists():
                OtPCode.objects.filter(created__lt=expire).delete()
                self.stdout.write(self.style.SUCCESS('Successfully delete expiered code '))

            else:
                self.stdout.write(self.style.ERROR('otpcode dosenot exists'))
