
# coding: utf-8

# In[26]:

import hashlib
import random
import datetime
from struct import pack, unpack

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

t = time.time()
salt = random.choice(ALPHABET)
t_bytes = pack("d", t)
salt_bytes = salt.encode('utf-8')
int(hashlib.sha256(t_bytes + salt_bytes).hexdigest()[:13], 16)

