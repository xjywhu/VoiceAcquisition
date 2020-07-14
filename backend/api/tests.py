# Create your tests here.

from algorithm.edit_distance import edit_distance,get_similarity
import xlrd
from backend.settings import *
from token_baidu.get_token import get_tokens
from .models import *
from .views import ReleaseContextViewSet

s = ReleaseContextViewSet()
s.write_file_to_db('a')




