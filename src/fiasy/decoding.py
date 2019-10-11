import scrypt
import base64

key = 'UnSTmMwEHpD1vrhTNgakzl0qenfYpmKY1bbwpR+zzRTpQzxFAs9oraVtxWaxmhJnNeakYWi0xRSR7allRqZhXg=='
separator = 'Bw=='
rounds = 8
mem_cost = 14

received_hesh = '6l2L5Z5kAYSYew1KXJZEupPwydCoLbwRyrDXMr8vyFS8f56Hv6QP4BgKhOgQzl87Ws1PlEn5AwyxQhg-jYJScg=='
received_salt = '4OVFMa4MtornWw=='
# data = scrypt.encrypt('kyhfcBrY9-2-hA==', 'D35d2abe412')
data = scrypt.hash('Qq123456', 'kyhfcBrY9-2-hA==')
h = base64.b64encode(data)

print(data)
print(h)

from passlib.hash import pbkdf2_sha256, django_pbkdf2_sha256, scrypt
from passlib.utils import to_bytes, to_native_str
import base64

# hashh = "6l2L5Z5kAYSYew1KXJZEupPwydCoLbwRyrDXMr8vyFS8f56Hv6QP4BgKhOgQzl87Ws1PlEn5AwyxQhg-jYJScg=="
# salt = b"4OVFMa4MtornWw=="
# password = "Qq123456"

# bsalt = base64.b64encode(salt)

# rounds = 8
# mem_cost = 14


# isit = lambda it: it == hashh
# s = scrypt.hash(password, salt=salt, rounds=rounds)

# print(s)
# print(isit(s))