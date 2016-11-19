import requests
import re

def _xiaodoubi(self, word):
    url = 'http://www.xiaodoubi.com/bot/chat.php'
    try:
        r = requests.post(url, data={'chat': word})
        return r.content
    except:
        return "让我一个人静静 T_T..."


def _simsimi(self, word):
    key = ''
    url = 'http://sandbox.api.simsimi.com/request.p?key=%s&lc=ch&ft=0.0&text=%s' % (
        key, word)
    r = requests.get(url)
    ans = r.json()
    if ans['result'] == '100':
        return ans['response']
    else:
        return '你在说什么，风太大听不清列'


def _searchContent(self, key, content, fmat='attr'):
    if fmat == 'attr':
        pm = re.search(key + '\s?=\s?"([^"<]+)"', content)
        if pm:
            return pm.group(1)
    elif fmat == 'xml':
        pm = re.search('<{0}>([^<]+)</{0}>'.format(key), content)
        if not pm:
            pm = re.search(
                '<{0}><\!\[CDATA\[(.*?)\]\]></{0}>'.format(key), content)
        if pm:
            return pm.group(1)
    return '未知'