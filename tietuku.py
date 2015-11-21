import json, base64, hmac, time
import requests

class Tietuku ():

    def __init__ (self, key_access, key_secret):
        '''(str, str) -> None'''
        self.key_access = key_access.encode()
        self.key_secret = key_secret.encode()

    def token_mk (self, param):
        '''
        dict -> None
        默认含 'deadline'
        '''
        param['deadline'] = int(time.time()) + 60
        param_encode = base64.urlsafe_b64encode (json.dumps(param).encode())

        sign = hmac.new (self.key_secret, param_encode, 'sha1')
        sign_encode = base64.urlsafe_b64encode (sign.hexdigest().encode())

        token = self.key_access + b':' + sign_encode + b':' + param_encode
        
        self.token = token

    def api (self, url, param):
        '''(str, dict) -> dict'''
        self.token_mk (param)
        data = {'Token':self.token}

        r = requests.post (url, data)

        obj = json.loads (r.text)

        return obj
        
    def api_upload (self, path):
        '''str -> dict'''
        url = 'http://up.tietuku.com/'
        data = {'Token':self.token}

        try:
            with open (path, 'rb') as f:
                r = requests.post (url, data, files={'file':f})
        except OSError:
            data['fileurl'] = path
            r = requests.post (url, data)

        obj = json.loads (r.text)

        return obj
