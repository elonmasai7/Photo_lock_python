from cryptography.fernet import Fernet
key = Fernet.generate_key()
with open('key.key','wb') as f:
    f.write(key)
fernet = fernet(key)
with open('binodd.jpg', 'rb') as f:
    photo = f.read()

lock = fernet.encrypt(photo)
with open('binodd.jpg','wb') as lock_photo:
    lock_photo.write(lock)
print("Your Photo is locked")
#https://masaielon.netlify.app/