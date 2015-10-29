#!/usr/bin/python
# -*-coding:utf-8-*-

from app.main import storage
from res import values

class CtlArticle(object):
    """ Article controller
    """
    def __init__(self, current_user_id, db, models):
        self.current_user_id = current_user_id
        self.db = db
        self.models = models
        print('CtlArticle __init__')

    def delete_single(self, article_id, delete_attachment_flag):
        if delete_attachment_flag is True:
            attachment_list = self.models.StorageFileKey.query.filter_by(
                owner_id=self.current_user_id, for_what='article', for_what_id=article_id)
            delete_key_list = []
            for attachment_file in attachment_list:
                delete_key_list.append(attachment_file.file_key)
            print('CtlArticle - delete_single_article: delete key_list=%s' % delete_key_list)
            if len(delete_key_list):
                cz_storage = storage.CzStorage(current_user_id=self.current_user_id, use_system=False)
                if cz_storage.multi_delete(delete_key_list) is True:
                    # all of file has been delete
                    print('CtlArticle - delete_single: all of file has been delete')
                    for attachment_file in attachment_list:
                        self.db.session.delete(attachment_file)
                else:
                    # if not all the file has been delete, we need delete it again
                    # mark table StorageFileKey can_delete=true
                    print('CtlArticle - delete_single:  not all of file has been delete')
                    for attachment_file in attachment_list:
                        attachment_file.for_what_status = 'deleted'
                        attachment_file.can_delete = 'true'
                        self.db.session.delete(attachment_file)
        else:
            # put these file to default FileManager
            pass
        self.db.session.delete(self.models.Article.query.filter_by(id=int(article_id)).first())
        self.db.session.commit()

class CtlTags(object):
    """ Tags controller
    """
    def __init__(self, current_user_id, db, models):
        self.current_user_id = current_user_id
        self.db = db
        self.models = models
        print('CtlTags - __init__')

    def add_tag(self, tag_name):
        if tag_name is not None:
            try:
                self.db.session.add(self.models.Tag(tag_name=tag_name))
                self.db.session.commit()
                return True
            except:
                return False
        return False

    def del_tag(self, tag_name):
        if tag_name is not None:
            try:
                self.db.session.delete(self.models.Tag.query.filter_by(tag_name=tag_name).first())
                self.db.session.commit()
                return True
            except:
                return False
        return False

    def add_tag_list(self, tag_list):
        """
        :param tag_list: json, list(["Hello", "World", "Carlo", ...])
        :return:
        """
        has_new_tag = False
        if tag_list is not None:
            print('CtlTags - add_tag_list: tag_list = %s' % tag_list)
            try:
                import json
                tag_list_json = json.loads(tag_list)  # str to json
                for tag_name in tag_list_json:
                    if tag_name is not None:
                        try:
                            tag = self.models.Tag.query.filter_by(tag_name=tag_name).first()
                            tag.use_num += 1
                            tag.update_user_id = self.current_user_id
                        except:
                            tag = self.models.Tag(tag_name=tag_name, use_num=1, create_user_id=self.current_user_id)
                            has_new_tag = True
                        self.db.session.add(tag)
                self.db.session.commit()
                print('CtlTags - add_tag_list: commit to db success')
                return True, has_new_tag
            except:
                print('CtlTags - add_tag_list: commit to db fail')
                self.db.session.rollback()
                return False, has_new_tag
        return False, has_new_tag

    def update_tag_file(self):
        print('CtlTags - update_tag_file: start')
        key = 'system/data/globaltag.json'
        try:
            # read tag data from t_tag
            tag_list = self.models.Tag.query.all()
            json_data = '['
            for tag in tag_list:
                json_data += ('"%s", ' % tag.tag_name)
            json_data += '""]'
            print(json_data)
            cz_storage = storage.CzStorage(current_user_id=self.current_user_id, use_system=True)
            print('downloadUrl = %s' % cz_storage.upload_text_file(key=key, text=json_data))
            print('CtlTags - update_tag_file: success')
        except:
            print('CtlTags - update_tag_file: fail')

class CtlCurrentUser(object):
    def __init__(self, current_user, request):
        self.curr_user = current_user
        self.request = request

    @property
    def user_id(self):
        if self.curr_user.is_authenticated():
            return self.curr_user.id
        else:
            return -1

    @property
    def unique_domain(self):
        if self.curr_user.is_authenticated():
            return self.curr_user.unique_domain
        else:
            return values.Role.anonymous_user

    @property
    def nikename(self):
        if self.curr_user.is_authenticated():
            return self.curr_user.nikename
        else:
            return self.request.remote_addr



