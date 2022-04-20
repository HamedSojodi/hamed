from account.models import OtPCode
from datetime import datetime, timedelta
import pytz


def remove_expier_otp_cod():
    expier = datetime.now(tz=pytz.timezone('Asia/Tehran'))-timedelta(minutes=2)
    OtPCode.objects.filter(created__lt=expier).delete()
