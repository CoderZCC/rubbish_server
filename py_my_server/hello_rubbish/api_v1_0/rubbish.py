# coding: utf-8
from . import api
from hello_rubbish import db
from hello_rubbish.models.models import RubbishType, RubbishDetail, CityCode, RubbishTypeName
import xlrd


# GET api/1.0/rubbish_type
@api.route("/rubbish_type", methods=["Get"])
def get_rubbish_type():
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


"""
    rubbish_type = RubbishType.query.get(1)
    print(rubbish_type.rubbish_details)
    detail = RubbishDetail.query.get(4)
    print(detail.rubbish_type.rubbish_term)

    rubbish1 = RubbishType(rubbish_type="4",
                           rubbish_logo="rubbish4",
                           rubbish_bgColor="aaa",
                           rubbish_textColor="bbb",
                           rubbish_term="zzz",
                           rubbish_desc="vvv")

    rubbish2 = RubbishType(rubbish_type="5",
                           rubbish_logo="rubbish5",
                           rubbish_bgColor="ccc",
                           rubbish_textColor="aaa",
                           rubbish_term="hhh",
                           rubbish_desc="jjj")

    city = CityCode(city_code="1100",
                    city_name="北京",
                    province_name="北京")
    db.session.add(rubbish1)
    rubbish1.city_list.append(city)
    rubbish2.city_list.append(city)
    city.rubbish_list.append(rubbish1)
    city.rubbish_list.append(rubbish2)
    db.session.commit()
    rubbish = RubbishType.query.get(1)
    print(rubbish.city_list)
    city = CityCode.query.get(1)
    print(city.rubbish_list)
"""

"""
    rubbish_type1 = RubbishType(rubbish_logo="rubbish0",
                                rubbish_bgColor="0x3A76D1,0x2C116F",
                                rubbish_textColor="0x2256A9,0x2256A9",
                                rubbish_term="AAA;BBB",
                                rubbish_desc="CCC")

    rubbish_type2 = RubbishType(rubbish_logo="rubbish1",
                                rubbish_bgColor="0x3A8E24,0x0B6C5F",
                                rubbish_textColor="0x417505,0x72B524",
                                rubbish_term="AXX;XXX",
                                rubbish_desc="DDD")

    rubbish_type3 = RubbishType(rubbish_logo="rubbish2",
                                rubbish_bgColor="0xAD2828,0x730F0F",
                                rubbish_textColor="0xC73710,0xE97E61",
                                rubbish_term="ABA;BBB",
                                rubbish_desc="EEE")

    rubbish_type4 = RubbishType(rubbish_logo="rubbish3",
                                rubbish_bgColor="0x495368,0x1A1C20",
                                rubbish_textColor="0x3B4252,0x737885",
                                rubbish_term="ABB;BBB",
                                rubbish_desc="FFF")

    db.session.add(rubbish_type1)
    db.session.add(rubbish_type2)
    db.session.add(rubbish_type3)
    db.session.add(rubbish_type4)
    db.session.commit()
    """

"""
    excel = xlrd.open_workbook("rubbishDetail.xls")
    sheet_index = 0
    sheet = excel.sheet_by_index(sheet_index)
    rows = sheet.nrows
    for i in range(rows):
        if i == 0:
            continue
        text = sheet.row_values(i)[2]
        detail = RubbishDetail(rubbish_type_id=sheet_index+1, rubbish_title=text)
        db.session.add(detail)
    db.session.commit()
"""

"""
    excel = xlrd.open_workbook("rubbishDetail.xls")
    sheet_index = 4
    sheet = excel.sheet_by_index(sheet_index)
    rows = sheet.nrows
    for i in range(rows):
        text1 = sheet.row_values(i)[0]
        text2 = sheet.row_values(i)[1]
        text3 = sheet.row_values(i)[2]
        print(text1, text2, text3)
        detail = CityCode(city_code=text3, city_name=text1, province_name=text2)
        db.session.add(detail)
    db.session.commit()
"""