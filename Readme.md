# Проект веб-приложение Dinn-store

## Для начала работы с приложением необходимо:

1. ### В корне директории проекта Создать файл '.env' 

2. ### Ввести в файл '.env' данные вашей почты, redis.
   (При необходимости введите данные в нужном виде прямо в файл 'django_19_hw_2/settings.py' )
3. 
   Пример для mail.ru, redis: 

   EMAIL_HOST = 'smtp.mail.ru'
   EMAIL_PORT = '2525' 
   EMAIL_HOST_USER = 'dinn.land@mail.ru' 
   EMAIL_HOST_PASSWORD = 'passwordpassword'

   BACKEND = "django.core.cache.backends.redis.RedisCache"
   LOCATION = "redis://127.0.0.1:6379"
