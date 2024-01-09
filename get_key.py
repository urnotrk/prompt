import os
from dotenv import load_dotenv, find_dotenv


# 读取本地/项目的环境变量。

# find_dotenv()寻找并定位.env文件的路径
# load_dotenv()读取该.env文件，并将其中的环境变量加载到当前的运行环境中  
# 如果你设置的是全局的环境变量，这行代码则没有任何作用。


# openai.api_key = os.environ['OPENAI_API_KEY']


def get_openai_key():
    _ = load_dotenv(find_dotenv())
    # 返回环境变量 OPENAI_API_KEY
    return os.environ['OPENAI_API_KEY']