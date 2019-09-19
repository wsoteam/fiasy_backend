from django.core.management.base import BaseCommand

import firebase_admin
from firebase_admin import credentials, auth, db

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from django.contrib.auth.models import User

import requests


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://diet-for-test.firebaseio.com/'
})

ref = db.reference('USER_LIST')
user_profiles = db.reference().child('USER_LIST').get()


class Command(BaseCommand):

    def handle(self, *args, **options):
        count = 0
        user_list = auth.list_users()
        while user_list:
            for user in user_list.users:
                if user.email is not None:
                    created_user = User.objects.create_user(
                        username=user.email,
                        email=user.email,
                        password=User.objects.make_random_password
                        )
                    print(created_user)
                    profile = created_user.profile
                    profile.uid = user.uid
                    if user.photo_url is not None:
                        r = requests.get(user.photo_url)
                        img_temp = NamedTemporaryFile()
                        img_temp.write(r.content)
                        img_temp.flush()
                        profile.image.save(
                            user.uid + user.photo_url[-4:],
                            File(img_temp), save=True
                        )
                    profile.save()
                    if user.uid in user_profiles:
                        if 'profile' in user_profiles[user.uid].keys():
                            if 'age' in user_profiles[user.uid]['profile'].keys():
                                profile.age = user_profiles[user.uid]['profile']['age']
                            if 'height' in user_profiles[user.uid]['profile'].keys():
                                profile.height = user_profiles[user.uid]['profile']['height']
                            if 'weight' in user_profiles[user.uid]['profile'].keys():
                                profile.weight = user_profiles[user.uid]['profile']['weight']
                            if 'maxCarbo' in user_profiles[user.uid]['profile'].keys():
                                profile.max_carbo = user_profiles[user.uid]['profile']['maxCarbo']
                            if 'maxFat' in user_profiles[user.uid]['profile'].keys():
                                profile.max_fats = user_profiles[user.uid]['profile']['maxFat']
                            if 'maxKcal' in user_profiles[user.uid]['profile'].keys():
                                profile.max_calories = user_profiles[user.uid]['profile']['maxKcal']
                            if 'maxProt' in user_profiles[user.uid]['profile'].keys():
                                profile.max_proteins = user_profiles[user.uid]['profile']['maxProt']
                            if 'waterCount' in user_profiles[user.uid]['profile'].keys():
                                profile.water_count = user_profiles[user.uid]['profile']['waterCount']
                            if 'firstName' in user_profiles[user.uid]['profile'].keys():
                                if user_profiles[user.uid]['profile']['firstName'] != 'default':
                                    created_user.first_name = user_profiles[user.uid]['profile']['firstName']
                            if 'lastName' in user_profiles[user.uid]['profile'].keys():
                                if user_profiles[user.uid]['profile']['firstName'] != 'default':
                                    created_user.last_name = user_profiles[user.uid]['profile']['lastName']
                            created_user.save()
                            if 'female' in user_profiles[user.uid]['profile'].keys():
                                if user_profiles[user.uid]['profile']['female'] is True:
                                    profile.gender = 'F'
                                else:
                                    profile.gender = 'M'
                            if 'exerciseStress' in user_profiles[user.uid]['profile'].keys():
                                if user_profiles[user.uid]['profile']['exerciseStress'] == 'Минимальная активность':
                                    profile.activity = 'min'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'МИНИМАЛЬНАЯ НАГРУЗКА':
                                    profile.activity = 'min'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'Минимальная нагрузка':
                                    profile.activity = 'min'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'Малоактивный':
                                    profile.activity = 'min'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'Легкая':
                                    profile.activity = 'easy'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'Легкая активность':
                                    profile.activity = 'easy'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'Легкая активность':
                                    profile.activity = 'easy'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'СРЕДНЕАКТИВНЫЙ':
                                    profile.activity = 'ave'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'Среднеактивный':
                                    profile.activity = 'ave'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'Средняя активность':
                                    profile.activity = 'ave'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'Высокая активность':
                                    profile.activity = 'hard'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'Повышенная активность':
                                    profile.activity = 'hard'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'Интенсивная нагрузка':
                                    profile.activity = 'int'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'ИНТЕНСИВНАЯ НАГРУЗКА':
                                    profile.activity = 'int'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'Ежедневные интенсивные тренировки':
                                    profile.activity = 'daily_int'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'ЕЖЕДНЕВНЫЕ ИНТЕНСИВНЫЕ ТРЕНИРОВКИ':
                                    profile.activity = 'daily_int'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'Ежедневные тренировки':
                                    profile.activity = 'daily_int'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'ЕЖЕДНЕВНЫЕ ТРЕНИРОВКИ':
                                    profile.activity = 'daily_int'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'Сверхвысокая активность':
                                    profile.activity = 'extra_hard'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'Предельная активность':
                                    profile.activity = 'extra_hard'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'Сверхтяжелые нагрузки':
                                    profile.activity = 'extra_hard'
                                elif user_profiles[user.uid]['profile']['exerciseStress'] == 'СВЕРХТЯЖЕЛЫЕ НАГРУЗКИ':
                                    profile.activity = 'extra_hard'
                            if 'difficultyLevel' in user_profiles[user.uid]['profile'].keys():
                                if user_profiles[user.uid]['profile']['difficultyLevel'] == 'Легкая':
                                    profile.goals = 'keeping'
                                if user_profiles[user.uid]['profile']['difficultyLevel'] == 'ЛЕГКАЯ':
                                    profile.goals = 'keeping'
                                if user_profiles[user.uid]['profile']['difficultyLevel'] == 'Средняя':
                                    profile.goals = 'losing'
                                if user_profiles[user.uid]['profile']['difficultyLevel'] == 'СРЕДНЯЯ':
                                    profile.goals = 'losing'
                                if user_profiles[user.uid]['profile']['difficultyLevel'] == 'Высокая':
                                    profile.goals = 'losing'
                                if user_profiles[user.uid]['profile']['difficultyLevel'] == 'ВЫСОКАЯ':
                                    profile.goals = 'losing'
                                if user_profiles[user.uid]['profile']['difficultyLevel'] == 'Похудение':
                                    profile.goals = 'preservation'
                    profile.save()
            user_list = user_list.get_next_page()
