from kavenegar import *


def send_otp_code(phone, code):
    try:
        api = KavenegarAPI('4D39557032326D346A2B62692B5273656571474A4D5A795637516179635A473658714F346C66306531626B3D')
        params = {
            'sender': '',  # optional
            'receptor': phone,  # multiple mobile number, split by comma
            'message':f'{code} کد تایید شما ',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
