{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "78a25036-2389-4aa6-9860-b55215d1dbbf",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
import os
import pickle
from cryptography.fernet import Fernet

def load_encrypted_model(path, key_env="MODEL_KEY"):
    key = os.environ[key_env].encode()
    cipher = Fernet(key)

    with open(path, "rb") as f:
        encrypted = f.read()

    decrypted = cipher.decrypt(encrypted)
    model = pickle.loads(decrypted)

    return model