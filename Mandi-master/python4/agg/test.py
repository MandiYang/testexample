#设置代理
import urllib.request
proxy_support = urllib.request.ProxyHandler({"http":"http://username:password@proxy:port",
                                             "https":"https://username:password@proxy:port"})
opener = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(opener)

