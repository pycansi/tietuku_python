依赖库：
    requests

使用简介：
    首先：
        t = Tietuku ('<access key>', '<secret key>')
    一般接口：
        t.api (url, {'<param>':<value>, })
        不用填写 deadline 参数
        例 t.api ('http://api.tietuku.com/v1/Album', {'action':'get'})
    上传接口:
        考虑到上传多个文件时避免重复生成 token，所以要繁琐些
        t.token_mk ({'<param>':<value>, })
        依旧，不用填写 deadline 参数
        t.api_upload ('<path>')
        本地路径 或 图片url 皆可
        