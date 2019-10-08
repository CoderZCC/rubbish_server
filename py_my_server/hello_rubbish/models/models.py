# coding: utf-8
from hello_rubbish import db
from datetime import datetime
# python app_migrate db init -会创建一个migrations文件
# python app_migrate db migrate -生成迁移文件
# python app_migrate db migrate -m "我是备注信息" -添加备注信息
# python app_migrate db upgrade -创建
# python app_migrate db history -查看历史记录
# python app_migrate db downgrade (状态码) -会退到哪个版本


class BaseModel(object):
    id = db.Column(db.Integer, primary_key=True)
    is_del = db.Column(db.Boolean, default=False)
    create_time = db.Column(db.DateTime,
                            default=datetime.now)
    update_time = db.Column(db.DateTime,
                            default=datetime.now,
                            onupdate=datetime.now)


city_rubbish = db.Table("city_rubbish",
                        db.Column("rubbish_type_id",
                                  db.Integer,
                                  db.ForeignKey("py_rubbish_type.id")),
                        db.Column("city_id",
                                  db.Integer,
                                  db.ForeignKey("py_city_code.id")))


class CityCode(BaseModel, db.Model):
    """城市省份表"""
    __tablename__ = "py_city_code"
    # 城市code
    city_code = db.Column(db.String(10), nullable=False, unique=True)
    # 城市名称
    city_name = db.Column(db.String(10), nullable=False, unique=True)
    # 省份名称
    province_name = db.Column(db.String(10), nullable=False, unique=True)
    # 多个垃圾类型
    rubbish_list = db.relationship("RubbishType",
                                   secondary=city_rubbish,
                                   back_populates="city_list")

    def __repr__(self):
        return "城市省份表-%s-%s" % (self.province_name, self.city_name)


class RubbishType(BaseModel, db.Model):
    """垃圾类型表"""
    __tablename__ = "py_rubbish_type"
    # 垃圾类型
    rubbish_type = db.Column(db.String(1), nullable=False, unique=True)
    # 垃圾的图片
    rubbish_logo = db.Column(db.String(20), nullable=False, unique=True)
    # 背景颜色, "0x3A76D1,0x2C116F"
    rubbish_bgColor = db.Column(db.String(20), nullable=False, unique=True)
    # 文字颜色, "0x2256A9,0x2256A9"
    rubbish_textColor = db.Column(db.String(20), nullable=False, unique=True)
    # 投放要求 ,分割
    rubbish_term = db.Column(db.String(128), nullable=False, unique=True)
    # 分类描述
    rubbish_desc = db.Column(db.String(128), nullable=False, unique=True)
    # 垃圾列表, 数据库不存在,只存在model, backref是多类调用时,可以返回对象
    rubbish_details = db.relationship("RubbishDetail", backref="rubbish_type")
    # 多个城市
    city_list = db.relationship("CityCode",
                                secondary=city_rubbish,
                                back_populates="rubbish_list")

    def __repr__(self):
        return "垃圾类型表-%s" % self.rubbish_type


class RubbishTypeName(BaseModel, db.Model):
    """垃圾分类名称表"""
    __tablename__ = "py_rubbish_name"
    # 城市code
    city_code = db.Column(db.String(10), nullable=False)
    # 垃圾类型
    rubbish_type = db.Column(db.String(1), nullable=False)
    # 分类中文名称
    rubbish_zh = db.Column(db.String(20), nullable=False, unique=True)
    # 分类英文名称
    rubbish_en = db.Column(db.String(20), nullable=False, unique=True)

    def __repr__(self):
        return "垃圾分类名称表-%s" % self.rubbish_zh


class RubbishDetail(BaseModel, db.Model):
    """垃圾详情表"""
    __tablename__ = "py_rubbish_detail"
    # 垃圾类型id, 一对多关系
    rubbish_type_id = db.Column(db.Integer, db.ForeignKey('py_rubbish_type.id'))
    # 分类名称
    rubbish_title = db.Column(db.String(20), nullable=False, unique=True)

    def __repr__(self):
        return "垃圾详情表-%s" % self.rubbish_title

