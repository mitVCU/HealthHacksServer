import json
from pyfcm import FCMNotification
from firebase import firebase

firebase = firebase.FirebaseApplication('https://healthhacks2017-ec6bf.firebaseio.com/', None)
result = firebase.get('/Clinic', None)
#print (json.dumps(result, indent=2))
_, d = result.items()[-1]

room_num, values = d.items()[-1]
if values["temperature"] < 97.4 or values["temperature"] > 99.6:
	print("Temperature: " + str(values["temperature"]))
       	push_service = FCMNotification(api_key="AAAA_RINJFk:APA91bF4wqCoC-rvQ01XXedftgncrjw2RaqbQL9iWIwBhNr948KjQ02flNn5Gud49eOfnuGgQcNR2rH6XnhD1EllE-GpWnT-7DicLVoq2b0xynCFZwVBE0m7IP0I4ItaBlntZL70kUsI")
	registration_id = "crWV01AoxHk:APA91bGftkZ70ZPZqaL7yK_lkYMWPHGhSPrZOc9kwvlMSDUk7f4BQ4UV4gRTE7o2fhdaTafgQ745RdcGZpx_djC7GDq9M6MHgQg_Hhx6op4Bq5Ar5wtooblrgj2h6AuZ15xw5GNXacfn"
	message_title = "Patient in CRITICAL CONDITION"
        message_body = "Patient 1 has an EXTREME Temperature"
       	rest = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

if values["SpO2"] > 0.94:
        print("SpO2: " + str(values["SpO2"]))
        push_service = FCMNotification(api_key="AAAA_RINJFk:APA91bF4wqCoC-rvQ01XXedftgncrjw2RaqbQL9iWIwBhNr948KjQ02flNn5Gud49eOfnuGgQcNR2rH6XnhD1EllE-GpWnT-7DicLVoq2b0xynCFZwVBE0m7IP0I4ItaBlntZL70kUsI")
        registration_id = "crWV01AoxHk:APA91bGftkZ70ZPZqaL7yK_lkYMWPHGhSPrZOc9kwvlMSDUk7f4BQ4UV4gRTE7o2fhdaTafgQ745RdcGZpx_djC7GDq9M6MHgQg_Hhx6op4Bq5Ar5wtooblrgj2h6AuZ15xw5GNXacfn"
        message_title = "Patient 1 in CRITICAL CONDITION"
        message_body = "Patient 1 has high SpO2 levels"
        rest1 = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

if 0 == values["age"] and  120 > values["HR"] < 160 or 50 <values["systolic BP"]>70:
        print("SpO2: " + str(values["SpO2"]))
        push_service = FCMNotification(api_key="AAAA_RINJFk:APA91bF4wqCoC-rvQ01XXedftgncrjw2RaqbQL9iWIwBhNr948KjQ02flNn5Gud49eOfnuGgQcNR2rH6XnhD1EllE-GpWnT-7DicLVoq2b0xynCFZwVBE0m7IP0I4ItaBlntZL70kUsI")
        registration_id = "crWV01AoxHk:APA91bGftkZ70ZPZqaL7yK_lkYMWPHGhSPrZOc9kwvlMSDUk7f4BQ4UV4gRTE7o2fhdaTafgQ745RdcGZpx_djC7GDq9M6MHgQg_Hhx6op4Bq5Ar5wtooblrgj2h6AuZ15xw5GNXacfn"
        message_title = "Patient 1 in CRITICAL CONDITION"
        message_body = "Patient 1 has high SpO2 levels"
        rest5 = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

if 0 < values["age"] < 1 and  80 > values["HR"] < 140 or 70 <values["systolic BP"]>100:
        print("SpO2: " + str(values["SpO2"]))
        push_service = FCMNotification(api_key="AAAA_RINJFk:APA91bF4wqCoC-rvQ01XXedftgncrjw2RaqbQL9iWIwBhNr948KjQ02flNn5Gud49eOfnuGgQcNR2rH6XnhD1EllE-GpWnT-7DicLVoq2b0xynCFZwVBE0m7IP0I4ItaBlntZL70kUsI")
        registration_id = "crWV01AoxHk:APA91bGftkZ70ZPZqaL7yK_lkYMWPHGhSPrZOc9kwvlMSDUk7f4BQ4UV4gRTE7o2fhdaTafgQ745RdcGZpx_djC7GDq9M6MHgQg_Hhx6op4Bq5Ar5wtooblrgj2h6AuZ15xw5GNXacfn"
        message_title = "Patient 1 in CRITICAL CONDITION"
        message_body = "Patient 1 has high SpO2 levels"
        rest4 = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

if 1 <= values["age"] < 3 and  80 > values["HR"] < 130 or 80 <values["systolic BP"]>110:
        print("SpO2: " + str(values["SpO2"]))
        push_service = FCMNotification(api_key="AAAA_RINJFk:APA91bF4wqCoC-rvQ01XXedftgncrjw2RaqbQL9iWIwBhNr948KjQ02flNn5Gud49eOfnuGgQcNR2rH6XnhD1EllE-GpWnT-7DicLVoq2b0xynCFZwVBE0m7IP0I4ItaBlntZL70kUsI")
        registration_id = "crWV01AoxHk:APA91bGftkZ70ZPZqaL7yK_lkYMWPHGhSPrZOc9kwvlMSDUk7f4BQ4UV4gRTE7o2fhdaTafgQ745RdcGZpx_djC7GDq9M6MHgQg_Hhx6op4Bq5Ar5wtooblrgj2h6AuZ15xw5GNXacfn"
        message_title = "Patient 1 in CRITICAL CONDITION"
        message_body = "Patient 1 has high SpO2 levels"
        rest6 = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

if 3 <= values["age"] <= 5 and  80 > values["HR"] < 120 or 90 <values["systolic BP"]>110:
        print("SpO2: " + str(values["SpO2"]))
        push_service = FCMNotification(api_key="AAAA_RINJFk:APA91bF4wqCoC-rvQ01XXedftgncrjw2RaqbQL9iWIwBhNr948KjQ02flNn5Gud49eOfnuGgQcNR2rH6XnhD1EllE-GpWnT-7DicLVoq2b0xynCFZwVBE0m7IP0I4ItaBlntZL70kUsI")
        registration_id = "crWV01AoxHk:APA91bGftkZ70ZPZqaL7yK_lkYMWPHGhSPrZOc9kwvlMSDUk7f4BQ4UV4gRTE7o2fhdaTafgQ745RdcGZpx_djC7GDq9M6MHgQg_Hhx6op4Bq5Ar5wtooblrgj2h6AuZ15xw5GNXacfn"
        message_title = "Patient 1 in CRITICAL CONDITION"
        message_body = "Patient 1 has high SpO2 levels"
        rest8 = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

if  6 <= values["age"] <= 12 and  70 > values["HR"] < 110 or 80 <values["systolic BP"]>120:
        print("SpO2: " + str(values["SpO2"]))
        push_service = FCMNotification(api_key="AAAA_RINJFk:APA91bF4wqCoC-rvQ01XXedftgncrjw2RaqbQL9iWIwBhNr948KjQ02flNn5Gud49eOfnuGgQcNR2rH6XnhD1EllE-GpWnT-7DicLVoq2b0xynCFZwVBE0m7IP0I4ItaBlntZL70kUsI")
        registration_id = "crWV01AoxHk:APA91bGftkZ70ZPZqaL7yK_lkYMWPHGhSPrZOc9kwvlMSDUk7f4BQ4UV4gRTE7o2fhdaTafgQ745RdcGZpx_djC7GDq9M6MHgQg_Hhx6op4Bq5Ar5wtooblrgj2h6AuZ15xw5GNXacfn"
        message_title = "Patient 1 in CRITICAL CONDITION"
        message_body = "Patient 1 has high SpO2 levels"
        rest9 = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

if 12 < values["age"] and  55 > values["HR"] < 105 or 110 <values["systolic BP"]>120:
        if 55 > values["HR"] < 105:
            print("Heart Rate: " + str(values["HR"]))
        if 110 <values["systolic BP"]>120:
            print ("Blood Pressure: " + str(values["systolic BP"]))
        push_service = FCMNotification(api_key="AAAA_RINJFk:APA91bF4wqCoC-rvQ01XXedftgncrjw2RaqbQL9iWIwBhNr948KjQ02flNn5Gud49eOfnuGgQcNR2rH6XnhD1EllE-GpWnT-7DicLVoq2b0xynCFZwVBE0m7IP0I4ItaBlntZL70kUsI")
        registration_id = "crWV01AoxHk:APA91bGftkZ70ZPZqaL7yK_lkYMWPHGhSPrZOc9kwvlMSDUk7f4BQ4UV4gRTE7o2fhdaTafgQ745RdcGZpx_djC7GDq9M6MHgQg_Hhx6op4Bq5Ar5wtooblrgj2h6AuZ15xw5GNXacfn"
        message_title = "Patient 1 in CRITICAL CONDITION"
        message_body = "Patient 1 has high SpO2 levels"
        rest2 = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)


