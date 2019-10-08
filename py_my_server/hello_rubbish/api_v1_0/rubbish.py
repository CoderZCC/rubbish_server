# coding: utf-8
from . import api
from hello_rubbish import db
from hello_rubbish.models.models import RubbishType, RubbishDetail, CityCode
import json


@api.route("/rubbish_type", methods=["Get"])
def get_rubbish_type():
    # rubbish_type = RubbishType.query.get(1)
    # print(rubbish_type.rubbish_details)
    # detail = RubbishDetail.query.get(4)
    # print(detail.rubbish_type.rubbish_term)

    # rubbish1 = RubbishType(rubbish_type="4",
    #                        rubbish_logo="rubbish4",
    #                        rubbish_bgColor="aaa",
    #                        rubbish_textColor="bbb",
    #                        rubbish_term="zzz",
    #                        rubbish_desc="vvv")
    #
    # rubbish2 = RubbishType(rubbish_type="5",
    #                        rubbish_logo="rubbish5",
    #                        rubbish_bgColor="ccc",
    #                        rubbish_textColor="aaa",
    #                        rubbish_term="hhh",
    #                        rubbish_desc="jjj")
    #
    # city = CityCode(city_code="1100",
    #                 city_name="北京",
    #                 province_name="北京")
    # db.session.add(rubbish1)
    # rubbish1.city_list.append(city)
    # rubbish2.city_list.append(city)
    # city.rubbish_list.append(rubbish1)
    # city.rubbish_list.append(rubbish2)
    # db.session.commit()

    rubbish = RubbishType.query.get(1)
    print(rubbish.city_list)
    city = CityCode.query.get(1)
    print(city.rubbish_list)

    return "aaa"


# GET api/1.0/rubbish_detail/0
@api.route("/rubbish_detail/<int:type_id>", methods=["GET"])
def get_rubbish_detail(type_id):
    rubbish_list = RubbishDetail.query.filter_by(rubbish_type_id=type_id).all()
    # arr = []
    for obj in rubbish_list:
        print(obj.rubbish_title)
        # json_str = json.dumps(obj)
        # arr.append(json_str)
    # print(arr)
    return "获取id为%s的垃圾分类详情" % type_id
