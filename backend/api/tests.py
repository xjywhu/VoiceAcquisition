from django.test import TestCase
import random,os,sys
# Create your tests here.


base_dir = BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if not os.path.exists(base_dir+'/bbb/ccc'):
    os.mkdir(base_dir+'/bbb/ccc')