import os
import openai
# from dotenv import load_dotenv, find_dotenv
from get_key import get_openai_key
from tool import get_completion

openai.api_key = get_openai_key()



def test3_3_1():
    prompt = f"""
    根据给定的查询目标：最小化查询执行时间，请生成一个查询计划，以获得最佳性能。
    """
    
    response = get_completion(prompt)
    print(response)

    

def test3_3_2():
    prompt = f"""
    给定一个包含表A、表B和表C的数据库，表A包含列X和列Y和列Z，表B包含列Z和列W，
    表C包含列M和列N，其中表A主键为X，外键为Z，表B主键为Z，表C主键为M。

    根据以下用户需求和查询操作，生成三条查询语句，并选择一个查询执行时间最少的查询计划：
    用户需要从表A中选择列X和列Y，从表B中选择列W，并根据表A列Y以及表B列W的条件进行筛选，
    其中列W的取值应大于10且Y的取值在20-30之间。

    在生成查询语句时请选择适当的查询操作符、确定正确的表名和列名等。
    在选择查询计划时，请考虑索引的使用、关联操作的顺序、连接算法的选择等。
    请解释你的选择并生成最佳查询计划。
    """
    
    response = get_completion(prompt)
    print(response)


def test3_3_3():
    prompt = f"""
    给定一个包含表A、表B和表C的数据库，表A包含列X和列Y和列Z，表B包含列Z和列W，
    表C包含列M和列N，其中表A主键为X，外键为Z，表B主键为Z，表C主键为M。

    根据以下用户需求和查询操作，生成三条查询语句，并选择一个查询执行时间最少的查询计划：
    用户需要从表A中选择列X和列Y，从表B中选择列W，并根据表A列Y以及表B列W的条件进行筛选，
    其中列W的取值应大于10且Y的取值在20-30之间。

    在生成查询语句时请选择适当的查询操作符、确定正确的表名和列名等。
    在选择查询计划时，请考虑索引的使用、关联操作的顺序、连接算法的选择等。
    请解释你的选择并生成最佳查询计划。

    示例：
    
    """
    
    response = get_completion(prompt)
    print(response)



