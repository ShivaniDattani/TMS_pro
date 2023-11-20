# README

# Get security key inside .env file for production
1. Create .env file from terminal using this command 'touch .env'
2. Run this command on terminal: python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
3. The secret key is generated, now paste it in .env file
4. Add host address. For eg. MY_HOST = "poc-ranch-577.int.sce.network"