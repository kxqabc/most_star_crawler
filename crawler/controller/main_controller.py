from urllib.parse import quote
from crawler.url import url_manager
from crawler.downloader import html_downloader
from crawler.parser import html_parser, json_parser
from crawler.outputer import html_outputer


class MainController(object):
    def __init__(self):
        self.url_manager = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.html_parser = html_parser.HtmlParser()
        self.html_outputer = html_outputer.HtmlOutputer()
        self.json_paser = json_parser.JsonParser()

    def craw(self, func):
        def in_craw(baseline):
            print('begin to crawler..')
            results = []
            while self.url_manager.has_more_url():
                content = self.downloader.download(self.url_manager.get_new_url())  # 根据URL获取静态网页
                results.extend(func(content, baseline))
            self.html_outputer.build_data(results)
            self.html_outputer.output()
            print('crawler end..')
        print('call craw..')
        return in_craw

    def parse_from_json(self, content, baseline):
        json_collection = self.json_paser.json_to_object(content)
        results = self.json_paser.build_bean_from_json(json_collection, baseline)
        return results

    def parse_from_html(self, content, baseline):
        self.html_parser.build_soup(content)  # 使用BeautifulSoup将html网页构建成soup树
        results = self.html_parser.build_bean_from_html(baseline)
        return results


if __name__ == '__main__':
    base_url = 'https://juejin.im/search'    # 要爬取的网站网址(不含参数)
    ajax_base_url = 'https://search-merger-ms.juejin.im/v1/search'
    keyword = quote('树莓派')  #'python'  # 关键字,urllib.parse.quote() 复杂处理url中的中文
    baseline = 10   # 获得的最少赞数量
    crawler_controller = MainController()
    static_url = crawler_controller.url_manager.build_static_url(base_url, keyword)     # 构建静态URL

    # craw_html = crawler_controller.craw(crawler_controller.parse_from_html)     # 开始抓取
    # craw_html(static_url, baseline)

    params = {}     # 对应的请求参数
    params['query'] = keyword
    params['page'] = '1'
    params['raw_result'] = 'false'
    params['src'] = 'web'
    crawler_controller.url_manager.build_ajax_url(ajax_base_url, params)
    craw_json = crawler_controller.craw(crawler_controller.parse_from_json)
    craw_json(baseline)


