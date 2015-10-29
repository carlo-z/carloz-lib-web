#!/usr/bin/python
#-*-coding:utf-8-*-

from ... import models
from ... import db
from .qiniu_cloud import QiniuStorage


class CzStorage(object):

    def __init__(self, current_user_id, use_system):
        print('CzStorage __init__ : current_user_id = %s, use_system = %s' % (current_user_id, use_system))
        self.use_system = use_system
        self.user = models.User.query.filter_by(id=int(current_user_id)).first()
        print('CzStorage __init__ : 2')
        self.storage_type = self.user.storage_type
        print('CzStorage __init__ : storage_type = %s' % self.storage_type)

    def upload_file_object(self, key, fileobj, file_size):
        print('CzStorage - upload_file_object : key = %s' % key)
        if QiniuStorage.storage_type == self.storage_type:
            print('CzStorage - upload_file_object : 0')
            try:
                dbQiniuStorage = models.QiniuStorage.query.filter_by(owner_id=int(self.user.id), use_flag='Y').first()
                print('CzStorage - upload_file_object : 1')
                qiniuStorage = QiniuStorage(user_id=self.user.id, dbQiniuStorage=dbQiniuStorage, use_system=False)
                print('CzStorage - upload_file_object : 2')
                download_url = qiniuStorage.upload_stream(key, fileobj.stream, file_size)
                storage_file_key = models.StorageFileKey(
                    owner_id=self.user.id,
                    storage_type=self.storage_type,
                    storage_id=dbQiniuStorage.id,
                    original_name=fileobj.filename,
                    file_key=key,
                    file_size=file_size,
                    download_url=download_url
                )
                db.session.add(storage_file_key)
                db.session.commit()
                return download_url
            except Exception, e:
                print('CzStorage - upload_file_object fail. err = %s' % e)
                db.session.rollback()
        return None

    def upload_text_file(self, key, text):
        if QiniuStorage.storage_type == self.storage_type:
            if self.use_system is True:
                qiniuStorage = QiniuStorage(user_id=None, dbQiniuStorage=None, use_system=self.use_system)
                return qiniuStorage.upload_binary_stream(key=key, data=text)
            else:
                dbQiniuStorage = models.QiniuStorage.query.filter_by(owner_id=int(self.user.id), use_flag='Y').first()
                qiniuStorage = QiniuStorage(self.user.id, dbQiniuStorage, use_system=self.use_system)
                return qiniuStorage.upload_binary_stream(key=key, data=text)

    def multi_delete(self, key_list):
        # key_list: list
        print('CzStorage - %s multi_delete : key_list = %s' % (self.storage_type, key_list))
        if QiniuStorage.storage_type == self.storage_type:
            try:
                print('CzStorage - %s multi_delete : qiniu use_system = %s' % (self.storage_type, self.use_system))
                if self.use_system is True:
                    qiniuStorage = QiniuStorage(user_id=None, dbQiniuStorage=None, use_system=self.use_system)
                    qiniuStorage.multi_delete(key_list=key_list)
                else:
                    dbQiniuStorage = models.QiniuStorage.query.filter_by(owner_id=int(self.user.id),
                                                                         use_flag='Y').first()
                    qiniuStorage = QiniuStorage(self.user.id, dbQiniuStorage, use_system=self.use_system)
                    qiniuStorage.multi_delete(key_list=key_list)
                return True
            except:
                print('CzStorage - %s multi_delete : False, key_list=%s' % (self.storage_type, key_list))
                return False


