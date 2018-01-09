class UrlManager(object):
    def __init__(self):
        self.new_urls = set()   # 新的url的集合

    # 构建访问静态页面的url
    def build_static_url(self, base_url, keyword):
        static_url = base_url + '?query=' + keyword
        return static_url

    # 根据输入的base_url(基础地址)和params(参数字典)来构造一个新的url
    # eg:https://search-merger-ms.juejin.im/v1/search?query=python&page=1&raw_result=false&src=web
    # 参数中的start_page是访问的起始页数字，gap是访问的页数间隔
    def build_ajax_url(self, base_url, params, start_page=0, end_page=4, gap=1):
        if base_url is None:
            print('Invalid param base_url!')
            return None
        if params is None or len(params)==0:
            print('Invalid param request_params!')
            return None
        if end_page < start_page:
            raise Exception('start_page is bigger than end_page!')
        equal_sign = '='    #键值对内部连接符
        and_sign = '&'  #键值对之间连接符
        # 将base_url和参数拼接成url放入集合中
        for page_num in range(start_page, end_page, gap):
            param_list = []
            params['page'] = str(page_num)
            for item in params.items():
                param_list.append(equal_sign.join(item))    # 字典中每个键值对中间用'='连接
            param_str = and_sign.join(param_list)       # 不同键值对之间用'&'连接
            new_url = base_url + '?' + param_str
            self.new_urls.add(new_url)
        return None

    # 从url集合中获取一个新的url
    def get_new_url(self):
        if self.new_urls is None or len(self.new_urls) == 0:
            print('there are no new_url!')
            return None
        return self.new_urls.pop()

    # 判断集合中是否还有url
    def has_more_url(self):
        if self.new_urls is None or len(self.new_urls) == 0:
            return False
        else:
            return True

# test
# params = {}  # 对应的请求参数
# params['query'] = 'python'
# params['page'] = '1'
# params['raw_result'] = 'false'
# params['src'] = 'web'
# manager = UrlManager()
# manager.build_ajax_url('https://search-merger-ms.juejin.im/v1/search',params)
# print(len(manager.new_urls))
# for link in manager.new_urls:
#     print(link)

