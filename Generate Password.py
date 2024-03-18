import secrets
random_string = ''.join(secrets.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$/_&*") for _ in range(10))
print(random_string)
