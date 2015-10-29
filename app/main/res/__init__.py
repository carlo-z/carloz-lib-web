def strings():
    language_type = 'en'
    if 'zh' == language_type:
        from . import string_zh as strs
    elif 'en' == language_type:
        from . import string_en as strs
    else:
        from . import string_zh as strs
    return strs