import os


def get_root_dir():
    return os.path.dirname(os.path.dirname(__file__))

# 其中的__file__表示当前文件的存储路径
# os.path.dirname表示获取参数中路径的目录部分
# 利用两次dirname方法，可以获取当前文件目录的上级目录绝对路径，因为当前文件相对于项目根目录的位置为两层，所以这样获取到的绝对路径结果就是项目根目录的绝对路径