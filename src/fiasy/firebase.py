
import firebase_admin
from firebase_admin import credentials, auth, db


import base64

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://diet-for-test.firebaseio.com/'
})

# user = auth.ExportedUserRecord({
#     'localId': 'user',
#     'passwordHash': 'passwordHash',
#     'salt': 'passwordSalt',
# })
# print(user.uid)
# print(user.email)
# print(user.password_hash)



# user = auth.get_user_by_email('pro100istomin1988@gmail.com')
# print(user.password_hash)
# print(user.password_salt)
# print(user.email)
# user_list = auth.list_users()
# user_info = {}
# c = 0
# while user_list:
#     for user in user_list.users:
#         user_info[user.uid] = {}
#         # user_info[user.uid]['profile'] = {}
#         # if user.email is not None and user.email == 'pro100istomin@bigmir.net':
#         #     print(user.password_hash)
#         #     # print(base64.b64decode(user.password_hash))
#         #     print(user.password_salt)
#         #     print(user.email)
#         #     user_info[user.uid]['email'] = user.email
        
#         if user.email is not None:
#             print(user.email)
#             print(user['sugar'])
#             c += 1
#             print(c)

#         # if user.display_name is not None:
#         #     print(user.uid)
#         #     print(user.provider_data)
#         #     print(user.display_name)
#         #     print(user.email)
#         #     print(user.phone_number)
#         #     print(user.photo_url)
#         #     user_info[user.uid]['display_name'] = user.display_name
#         # if user.phone_number is not None:
#         #     print(user.phone_number)
#         #     print(user.display_name)
#         #     print(user.email)
#         #     print(user.photo_url)
#         #     user_info[user.uid]['phone_number'] = user.phone_number
#     user_list = user_list.get_next_page()
# print(user_info)

ref = db.reference('USER_LIST')
user_profiles = db.reference().child('USER_LIST').get()
print(user_profiles)
print(type(user_profiles))
# for user in users:
#     if 'subInfo' in users[user].keys():
#         if users[user]['subInfo']['packageName'] != 'empty':
#             print(user)
#             print(users[user]['subInfo']['packageName'])
#             print(users[user]['subInfo']['productId'])
#             print(users[user]['subInfo']['purchaseToken'])

# print(dir(users.values()))

# for u in user_info:
#     if u in user_profiles:
#         if 'profile' in user_profiles[u].keys():
#             user_info[u]['profile'] = user_profiles[u]['profile']
# print(user_info)
# print(len(user_info))
