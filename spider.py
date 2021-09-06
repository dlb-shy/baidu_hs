#
# # 笔记详情
# import requests
#
# headers = {
#     'Host': 'www.xiaohongshu.com',
#     'asid': '202109064127e42cb0a201ebc4f9c00c',
#     'x-sign': 'X880f26f7d10297673687b8dd698c7831',
#     'x-b3-traceid': 'bf5b291fb5699ce9',
#     'referer': 'https://smartapps.cn/KuRdr9OR39BqyAGIg7mYK7Bytityu0Vi/2.35.16/page-frame.html',
#     'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/12.23 swan/2.35.0 swan-baiduboxapp/12.23.0.11 baiduboxapp/12.23.0.11 (Baidu; P1 6.0)',
#     'x-bd-traceid': '03e47248d5104788a0a6d18015eacf28',
# }
#
# response = requests.get('https://www.xiaohongshu.com/fe_api/burdock/baidu/v2/note/61331521000000002103405c', headers=headers)
#
#
# # 评论
# import requests
#
# headers = {
#     'Host': 'www.xiaohongshu.com',
#     'asid': '202109064127e42cb0a201ebc4f9c00c',
#     'x-sign': 'Xb080d995f49c0e3f4c81f6316548007b',
#     'x-b3-traceid': '9a09cf31a1029930',
#     'referer': 'https://smartapps.cn/KuRdr9OR39BqyAGIg7mYK7Bytityu0Vi/2.35.16/page-frame.html',
#     'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/12.23 swan/2.35.0 swan-baiduboxapp/12.23.0.11 baiduboxapp/12.23.0.11 (Baidu; P1 6.0)',
#     'x-bd-traceid': 'd14f5b1407a74b7c8cb7020c9aefe637',
# }
#
# params = (
#     ('endId', ''),
#     ('hot', 'no'),
#     ('pageSize', '2'),
# )
#
# response = requests.get('https://www.xiaohongshu.com/fe_api/burdock/baidu/v2/notes/61331521000000002103405c/comments', headers=headers, params=params)
#
# #NB. Original query string below. It seems impossible to parse and
# #reproduce query strings 100% accurately so the one below is given
# #in case the reproduced version is not "correct".
# # response = requests.get('https://www.xiaohongshu.com/fe_api/burdock/baidu/v2/notes/61331521000000002103405c/comments?endId=&hot=no&pageSize=2', headers=headers)
#
# # 用户详情
# import requests
#
# headers = {
#     'Host': 'www.xiaohongshu.com',
#     'asid': '202109064127e42cb0a201ebc4f9c00c',
#     'x-sign': 'Xb4850ed626be6848c03fe05d5d21a544',
#     'x-b3-traceid': '5011521b164a1228',
#     'referer': 'https://smartapps.cn/KuRdr9OR39BqyAGIg7mYK7Bytityu0Vi/2.35.16/page-frame.html',
#     'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/12.23 swan/2.35.0 swan-baiduboxapp/12.23.0.11 baiduboxapp/12.23.0.11 (Baidu; P1 6.0)',
#     'x-bd-traceid': 'caf5a17134a3434ba3a9a8b06e7a41a1',
# }
#
# response = requests.get('https://www.xiaohongshu.com/fe_api/burdock/baidu/v2/user/6004ddc5000000000101e58d', headers=headers)
#


# 笔记列表

import requests

headers = {
    'Host': 'www.xiaohongshu.com',
    'asid': '202109064127e42cb0a201ebc4f9c00c',
    'x-sign': 'X8647f6658a6fd79a7a20ea6efe24b9e4',
    'x-b3-traceid': 'bc66794e90ad8627',
    'referer': 'https://smartapps.cn/KuRdr9OR39BqyAGIg7mYK7Bytityu0Vi/2.35.16/page-frame.html',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Redmi Note 4 Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36 T7/12.23 swan/2.35.0 swan-baiduboxapp/12.23.0.11 baiduboxapp/12.23.0.11 (Baidu; P1 6.0)',
    'x-bd-traceid': 'c87537dcdc314c849b32e1a28eb4cd50',
}


response = requests.get('https://www.xiaohongshu.com/fe_api/burdock/baidu/v2/user/6004ddc5000000000101e58d/notes?page=1&pageSize=10', headers=headers)
print(response.text)



