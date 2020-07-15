import os
from xml.dom.minidom import parse


def parseOneXml(filename):
    domTree = parse(filename)
    xml4nlp = domTree.documentElement  # 根元素
    doc = xml4nlp.getElementsByTagName("doc")[0]
    paras = doc.getElementsByTagName("para")
    lis = []
    for para in paras:
        sents = para.getElementsByTagName("sent")
        for sent in sents:
            lis += [sent.getAttribute("cont")]
    return lis



################################
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# corpus_dir = os.path.join(BASE_DIR, 'corpus_handle/corpus/')
# print(BASE_DIR)
# domTree = parse(os.path.join(corpus_dir,'4到12岁孩子的饮食.xml'))
# xml4nlp = domTree.documentElement  # 根元素
# doc = xml4nlp.getElementsByTagName("doc")[0]
# paras = doc.getElementsByTagName("para")
# lis = []
# for para in paras:
#     sents = para.getElementsByTagName("sent")
#     for sent in sents:
#         lis += [sent.getAttribute("cont")]
#
# print(lis)