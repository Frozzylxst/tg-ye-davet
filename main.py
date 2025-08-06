from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.errors import PeerFloodError, UserPrivacyRestrictedError
import time
import csv

api_id = int(os.getenv("21663358"))
api_hash = os.getenv("d52861fe8ae5cea6aeb0cf1eb3c95cce")
phone = os.getenv("+905524114377")

client = TelegramClient('session', api_id, api_hash)
client.connect()

if not client.is_user_authorized():
    client.send_code_request(phone)
    client.sign_in(phone, input('Kodu girin: '))

source_group = input("Üyelerini çekeceğin grubun kullanıcı adı (örn: @kaynakgrup): ")
target_group = input("Üyeleri ekleyeceğin grubun kullanıcı adı (örn: @hedefgrup): ")

users = client.get_participants(source_group)
print(f"{len(users)} üye bulundu.")

for user in users:
    try:
        client(InviteToChannelRequest(target_group, [user]))
        print(f"{user.id} eklendi.")
        time.sleep(10)  # Flood engeli için
    except PeerFloodError:
        print("Flood hatası, biraz bekleniyor...")
        time.sleep(900)
    except UserPrivacyRestrictedError:
        print(f"{user.id} gizlilik nedeniyle eklenemedi.")
    except Exception as e:
        print(f"Hata: {e}")ğ
