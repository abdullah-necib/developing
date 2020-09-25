from urllib.request import urlopen
link = 'http://python.org'

def get_html():
    try:
        http_rsp = urlopen(link)
        print(http_rsp)
        html = http_rsp.read()
        print(html)
        html_decoded = html.decode()
        print(html_decoded)
    except Exception as ex:
        print('failed to get HTML \n\n' + str(ex))
        return 'FAILD TO GET HTML'
    else:
        return html_decoded