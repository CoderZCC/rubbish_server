# coding:utf-8
import redis


class Config(object):
    SECRET_KEY = "XHSOI+Y9dfs9cshd9"
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:12345678@127.0.0.1:3306/hello_rubbish"
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # redis设置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    # session配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,
                                      port=REDIS_PORT)
    SESSION_USE_SIGNER = True  # 对cookie中的session_id进行隐藏
    PERMANENT_SESSION_LIFETIME = 3600 * 24  # 有效期,单位秒


# 开发模式配置信息
class DevelopmentConfig(Config):
    DEBUG = True


# 生产环境配置信息
class DistributionConfig(Config):
    pass


config_map = {
    "dev": DevelopmentConfig,
    "dis": DistributionConfig
}
