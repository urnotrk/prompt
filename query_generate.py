import os
import openai
# from dotenv import load_dotenv, find_dotenv
from get_key import get_openai_key
from tool import get_completion

openai.api_key = get_openai_key()



def test3_2_1():
    prompt = f"""
    请生成一条数据库查询语句
    """ 
    
    response = get_completion(prompt)
    print(response)

    

def test3_2_2():
    prompt = f"""
    给定一个包含表A、表B和表C的数据库，表A包含列X和列Y和列Z，表B包含列Z和列W，
    表C包含列M和列N，其中表A主键为X，外键为Z，表B主键为Z，表C主键为M。

    根据以下用户需求和查询数据，生成三条查询语句：

    用户需要从表A中选择列X和列Y，从表B中选择列W，并根据表A列Y以及表B列W的条件进行筛选，
    其中列W的取值应大于10且Y的取值在20-30之间。
    """
    
    response = get_completion(prompt)
    print(response)


def test3_2_3():
    prompt = f"""
    给定一个包含表A、表B和表C的数据库，表A包含列X和列Y和列Z，表B包含列Z和列W，
    表C包含列M和列N，其中表A主键为X，外键为Z，表B主键为Z，表C主键为M。

    根据以下用户需求和查询数据，生成一个符合SQL语法规范的查询语句：

    用户需要从表A中选择列X和列Y，从表B中选择列W，并根据表A列Y以及表B列W的条件进行筛选，
    其中列W的取值应大于10且Y的取值在20-30之间。
    """
    
    response = get_completion(prompt)
    print(response)


def test3_2_4():
    prompt = f"""
    给定一个包含表A、表B和表C的数据库，表A包含列X和列Y和列Z，表B包含列Z和列W，
    表C包含列M和列N，其中表A主键为X，外键为Z，表B主键为Z，表C主键为M。

    根据以下用户需求和查询数据，生成三条查询语句：

    用户需要从表A中选择列X和列Y，从表B中选择列W，并根据表A列Y以及表B列W的条件进行筛选，
    其中列W的取值应大于10且Y的取值在20-30之间。

    请考虑以下因素：选择适当的查询操作符、确定正确的表名和列名、考虑查询的性能等。
    请解释你的选择并生成最佳查询语句。
    """
    
    response = get_completion(prompt)
    print(response)

