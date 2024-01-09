import os
import openai
# from dotenv import load_dotenv, find_dotenv
from get_key import get_openai_key
from tool import get_completion

openai.api_key = get_openai_key()



def test1():
    prompt1 = f"""
    请列举中国的分布式数据库系统，并进行简单介绍
    """ 
    
    response1 = get_completion(prompt1)
    print(response1)

    

def test2():
    prompt2 = f"""
    请列举中国的分布式数据库系统，并进行简单介绍\
    并以 JSON 格式提供，其中包含以下键:数据库名称、所属公司、是否为SQL数据库、是否为内存数据库、使用的索引、特点、简介。
    """ 
    
    response2 = get_completion(prompt2)
    print(response2)


