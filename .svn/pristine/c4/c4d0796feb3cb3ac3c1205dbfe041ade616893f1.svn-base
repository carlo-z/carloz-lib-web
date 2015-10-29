import logging

from .res import values as val


class CzLog(object):
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')

    def get_logger(self):
        platform_name = val.Env.platform
        if val.Platform.development == platform_name:
            console = logging.StreamHandler()
            console.setLevel(logging.DEBUG)
            # formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
            # console.setFormatter(formatter)
            logger = logging.getLogger()
            logger.addHandler(console)
            return logger
        elif val.Platform.BAE == platform_name:
            from bae_log import handlers
            handler = handlers.BaeLogHandler(ak=val.BAE.ak, sk=val.BAE.sk)
            logger = logging.getLogger()
            logger.setLevel(logging.DEBUG)
            logger.addHandler(handler)
            return logger
