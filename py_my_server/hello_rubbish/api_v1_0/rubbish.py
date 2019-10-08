# coding: utf-8
from . import api
from hello_rubbish.models.models import RubbishType, RubbishDetail
import json


@api.route("/rubbish_type", methods=["Get"])
def get_rubbish_type():
    rubbish_type = RubbishType.query.get(1)
    print(rubbish_type.rubbish_details)
    detail = RubbishDetail.query.get(4)
    print(detail.rubbish_type.rubbish_term)

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
