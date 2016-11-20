
# coding: utf-8
import requests

class Bot:

    def __init__(self):
        self.emotion = {}
        self.read();

    def read(self):
        fn = 'wxemoji.em'
        with open(fn, 'r') as f:
            for line in f:
                str = line.split(',')
                print str
                self.emotion.update({str[0]:str[1]})

    def action(self,type,word):
        if type is 1:
            return self._tuling(word)
        return "?"

    def _simsimi(self, word):

        key = '';
        url = 'http://sandbox.api.simsimi.com/request.p?key=%s&lc=ch&ft=0.0&text=%s' % (
            key, word)
        print url
        r = requests.get(url)
        ans = r.json()
        if ans['result'] == 100:
            return ans['response']
        else:
            return '你在说什么，风太大听不清列'

    def _tuling(self,word):
        url = 'http://www.tuling123.com/openapi/api'
        data = {
            "key":'3004d73273e54f9ab3d596cf4c9c62b9',
            "info": word
        }
        r = requests.post(url,data)
        ans = r.json()
        print ans
        if ans['code'] == 100000:
            if ans['text'] in self.emotion:
                return self.emotion[ans['text']];
            return ans['text']
        elif ans['code'] == 200000:
            return ans['text']+str(ans['url']);
        else:
            return '都唔知你系度up乜7'

