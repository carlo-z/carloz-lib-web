#!/usr/bin/python
#-*-coding:utf-8-*-

#http://developer.qiniu.com/docs/v6/sdk/python-sdk.html

import json

from qiniu import Auth, put_data, put_file, put_stream, etag, BucketManager


class QiniuStorage(object):
    storage_type = 'qiniu'

    def __init__(self, user_id, dbQiniuStorage, use_system=False):
        if use_system is True:
            self.access_key = 'lnjEMrmedpqOhO2IAw4WtyGNbNVQrFPGEVLQuyFp'
            self.secret_key = 'Nw_4Cn0L0Z3LLOL-t-OvGOVVV2kSxY3_my85UJwG'
            self.bucket_name = 'czlib-system'
            self.download_url = '7xjrbh.com1.z0.glb.clouddn.com'
            self.q = Auth(self.access_key, self.secret_key)
        else:
            self.access_key = dbQiniuStorage.access_key.encode('utf-8')  # unicode to str
            self.secret_key = dbQiniuStorage.secret_key.encode('utf-8')
            self.bucket_name = dbQiniuStorage.bucket_name.encode('utf-8')
            self.download_url = dbQiniuStorage.download_url.encode('utf-8')
            self.q = Auth(self.access_key, self.secret_key)
            # print('QiniuStorage - __init__: user_id: %s' % user_id)
            # print('QiniuStorage - __init__: ak:%s, sk:%s, b_name:%s, d_url:%s' % (self.access_key, self.secret_key, self.bucket_name, self.download_url))

    def upload_stream(self, key, input_stream, data_size):
        # print('upload_stream: key=%s, data_size=%s' % (key, data_size))
        # key = ''
        # input_stream=self.fileobj.stream
        # print('upload_stream: 1')
        token = self.q.upload_token(self.bucket_name, key)
        # print('upload_stream: 2')
        ret, info = put_stream(token, key, input_stream, data_size)
        # print(info)
        assert ret['key'] == key
        return self.get_download_url(key)

    # 直接上传二进制流
    def upload_binary_stream(self, key, data):
        # key = ''
        # data = 'hello bubby!'
        token = self.q.upload_token(self.bucket_name, key)
        ret, info = put_data(token, key, data, mime_type="application/octet-stream", check_crc=True)
        # print(info)
        assert ret['key'] == key
        return self.get_download_url(key)

    # 上传本地文件
    def upload_file(self, key, localfile):
        # key = 'home/carlo/test_file.py'
        mime_type = "text/plain"
        params = {'x:a': 'a'}

        token = self.q.upload_token(self.bucket_name, key)
        ret, info = put_file(token, key, localfile, mime_type=mime_type, check_crc=True)
        # print(info)
        assert ret['key'] == key
        assert ret['hash'] == etag(localfile)

    #断点续上传、分块并行上传
    def upload_big_file(self, key, localfile):
        mime_type = "text/plain"
        params = {'x:a': 'a'}
        # key = 'big'

        token = self.q.upload_token(self.bucket_name, key)
        progress_handler = lambda progress, total: progress
        ret, info = put_file(token, key, localfile, params, mime_type, progress_handler=progress_handler)
        # print(info)
        assert ret['key'] == key

    def single_delete(self, key):
        bucket = BucketManager(self.q)
        ret, info = bucket.delete(self.bucket_name, key)
        # print(info)
        assert info.status_code == 200 or info.status_code == 612

    # 批量删除文件
    def multi_delete(self, key_list):
        # key_list: [key1, key2, key3, ...]
        from qiniu import build_batch_delete
        bucket = BucketManager(self.q)
        ops = build_batch_delete(self.bucket_name, key_list)
        ret, info = bucket.batch(ops)
        # print('QiniuStorage - multi_delete: %s' % info)

        json_info = json.loads(info.text_body)
        for m_info in json_info:
            # "code":612,"data":{"error":"no such file or directory"
            assert m_info[u'code'] == 200 or m_info[u'code'] == 612

    def get_private_download_url(self, key):
        # bucket is private, http://<domain>/<key>?e=<deadline>&token=<dntoken>
        base_url = 'http://%s/%s' % (self.bucket_name + '.qiniudn.com', key)
        download_url = self.q.private_download_url(base_url, expires=3600)
        assert isinstance(download_url, object)
        return download_url

    def get_download_url(self, key):
        # bucket is public, http://<domain>/<key>
        download_url = 'http://%s/%s' % (self.download_url, key)
        return download_url

if __name__ == '__main__':
    # qiniu = QiniuStorage(user_id=2, dbQiniuStorage=3, use_system=False)
    # qiniu.delete_by_key('ueditor/ueditor/php/upload/file/2015613/234449286772.gif')
    # qiniu.upload_binary_stream('updata/text', 'hello world\n carlo')
    # qiniu.multi_delete(1)
    pass

