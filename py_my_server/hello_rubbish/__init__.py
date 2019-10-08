# coding:utf-8
from flask import Flask
from config import config_map
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_wtf import CSRFProtect
from logging.handlers import RotatingFileHandler
import redis
import logging

# 数据库
db = SQLAlchemy()
# 创建redis连接对象
redis_store = None

# 设置日志的记录等级 DEBUG=True 此设置无效
logging.basicConfig(level=logging.INFO)
# 创建日志记录器, 保存路径,每个日志文件最大大小,保存日志文件上限
file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024*1024*100, backupCount=10)
# 格式 (日志等级, 输入日志信息的文件名, 行数, 日志信息)
formatter = logging.Formatter("%(levelname)s %(filename)s:%(lineno)d %(message)s")
file_log_handler.setFormatter(formatter)
logging.getLogger().addHandler(file_log_handler)


def create_app(config_name):
    """
    创建全局App
    :param config_name: 配置类型 dev/dis
    :return: app
    """
    app = Flask(__name__)
    # 设置全局配置
    config_cls = config_map.get(config_name)
    app.config.from_object(config_cls)
    # 传递app到db
    db.init_app(app)
    # 初始化redis
    global redis_store
    redis_store = redis.StrictRedis(host=config_cls.REDIS_HOST,
                                    port=config_cls.REDIS_PORT)
    # 设置session,把数据保存到redis
    Session(app)
    # 补充CSRFProtect防护,防止恶意攻击
    CSRFProtect(app)
    # 为flask添加自定义转换器
    # app.url_map.converters["re"] = commons.ReConvert
    # 注册蓝图
    from hello_rubbish import api_v1_0
    app.register_blueprint(api_v1_0.api, url_prefix="/api/1.0")

    return app
