import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.getcwd().split(BASE_DIR)[0] + BASE_DIR)

from corpus_handle import xml_reader,excel_writer

def convertFile0(src_path,dst_path): # 将一个xml文件转化为excel文件
    lis = xml_reader.parseOneXml(src_path)
    excel_writer.writeOneExcel(lis, dst_path)

def convertFile(src_dir,dst_dir,src_filename): # 将一个xml文件转化为excel文件
    DEST_EXT = '.xlsx'
    src_path = src_dir + src_filename
    src_ext = src_filename.split('.')[-1]
    filename_without_ext_length = len(src_filename)-len(src_ext)
    filename_without_ext = src_filename[:filename_without_ext_length]
    dst_filename = filename_without_ext + DEST_EXT
    dst_path = dst_dir + dst_filename
    convertFile0(src_path,dst_path)


def file_name(file_dir,ext):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == ext:
                L.append(file)
    return L


def convertFiles(src_dir,dst_dir): # 将一个文件夹下所有xml文件转化为excel文件
    files = file_name(src_dir,'.xml')
    for file in files:
        convertFile(src_dir,dst_dir,file)
########################################## 测试转化单个文件
# src_dir = os.path.join(BASE_DIR,'corpus_handle/corpus/')
# dst_dir = os.path.join(BASE_DIR,'corpus_handle/excels/')
# src_filename = '4到12岁孩子的饮食.xml'
# convertFile(src_dir,dst_dir,src_filename)

#########################################  获取文件夹下所有文件名
# src_dir = os.path.join(BASE_DIR,'corpus_handle/corpus/')
# L = file_name(src_dir,'.xml')
# print(L)

######################################### 测试转化文件夹下所有文件
src_dir = os.path.join(BASE_DIR,'corpus_handle/corpus/')
dst_dir = os.path.join(BASE_DIR,'corpus_handle/excels/')
convertFiles(src_dir,dst_dir)