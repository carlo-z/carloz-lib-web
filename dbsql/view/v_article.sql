-- requirement: func_get_tag_list
CREATE 
VIEW `v_article`AS 
select t_art.id,
       t_art.title,
       func_get_tag_list(t_art.tag_id_list) tag_list,
       t_art.keywords,
       t_art.abstract,
       t_art.contents,
       t_art.img,
       t_art.author_id,
       (select t_user.nikename from t_user where t_user.id = t_art.author_id) author_nikename,
       t_art.access_level,
       t_art.access_passwd,
       t_art.pv_num,
       t_art.praise_num,
       t_art.dispraise_num,
       t_art.delete_flag,
       t_art.delete_date,
       t_art.body_source,
       t_art.body_default,
       t_art.body_simple,
       t_art.create_user_id,
       t_art.create_time,
       t_art.update_user_id,
       t_art.update_time
from t_article as t_art
order by t_art.create_time;
