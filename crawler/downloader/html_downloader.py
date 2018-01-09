import urllib.request

class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            print('one invalid url is found!')
            return None
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            print('response from %s is invalid!' % url)
            return None
        return response.read().decode('utf-8')

    # def download_by_ajax(self, url):
    #     if url is None:
    #         print('one invalid url is found!')
    #         return None
    #     response = urllib.request.urlopen(url)
    #     if response.getcode() != 200:
    #         print('response from %s is invalid!' % url)
    #         return None
    #     return str(response.read().decode('utf-8'))
