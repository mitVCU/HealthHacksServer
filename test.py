from pyfcm import FCMNotification
push_service = FCMNotification(api_key="AAAA_RINJFk:APA91bF4wqCoC-rvQ01XXedftgncrjw2RaqbQL9iWIwBhNr948KjQ02flNn5Gud49eOfnuGgQcNR2rH6XnhD1EllE-GpWnT-7DicLVoq2b0xynCFZwVBE0m7IP0I4ItaBlntZL70kUsI")

# Send to single device.
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="AAAA_RINJFk:APA91bF4wqCoC-rvQ01XXedftgncrjw2RaqbQL9iWIwBhNr948KjQ02flNn5Gud49eOfnuGgQcNR2rH6XnhD1EllE-GpWnT-7DicLVoq2b0xynCFZwVBE0m7IP0I4ItaBlntZL70kUsI")

# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

registration_id = "crWV01AoxHk:APA91bGftkZ70ZPZqaL7yK_lkYMWPHGhSPrZOc9kwvlMSDUk7f4BQ4UV4gRTE7o2fhdaTafgQ745RdcGZpx_djC7GDq9M6MHgQg_Hhx6op4Bq5Ar5wtooblrgj2h6AuZ15xw5GNXacfn"
message_title = "Uber update"
message_body = "Hi john, your customized news for today is ready"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

# Send to multiple devices by passing a list of ids.

#message_title = "Uber update"
#message_body = "Hope you're having fun this weekend, don't forget to check today's news"
#result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body)


