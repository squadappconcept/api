# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import uuid

from Crypto import Random
import MySQLdb
import webapp2

from store_client import StoreClient
from utils.aescipher import AESCipher

SESSION_ID_ENCRYPTION_KEY = os.environ.get('SESSION_ID_ENCRYPTION_KEY')

def generate_session_id():
    return uuid.UUID(bytes=Random.get_random_bytes(16))

def encrypt_session_id(session_id):
    return AESCipher(SESSION_ID_ENCRYPTION_KEY).encrypt(session_id)

class LoginHandler(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('name')
        email = self.request.get('email')
        facebook_id = self.request.get('facebook_id')

        # check if user exists
        # create if user doesn't
        # create a session id
        # save session into db
        # return session

class LogoutHandler(webapp2.RequestHandler):
    def post(self):
        # delete session id with user
        pass
