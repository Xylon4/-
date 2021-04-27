import yaml


def test_yaml():
    env = {
        "default": "test",
        "localhost": {
            "test": "192.168.64.129",
            "dev": "127.0.0.1"
        }
    }
    # 生成文件env.yaml，赋予w 写的权限
    with open("env.yaml", "w") as f:
        # safe_dump 使用源数据为env,stream=f转化为文件
        yaml.safe_dump(data=env, stream=f)
