import shutil, os


class FileHandler: # 处理文件的移动和删除
    def __init__(self, src_base_url='./', dst_base_url='./'):
        self._dst_base_url = dst_base_url # 目标文件根文件夹
        self._src_base_url = src_base_url # 源文件根文件夹

    def moveFile(self,sfile,dfile):
        '''
        :param sfile: 源文件
        :param dfile: 目标文件
        :return: 成功或失败，True Or False
        '''
        src_path = self._src_base_url + sfile
        dst_path = self._dst_base_url + dfile
        shutil.move(src_path, dst_path)

    def deleteSrcFile(self,filename):
        path = self._src_base_url + filename
        os.unlink(path)

    def deleteDstFile(self,filename):
        path = self._dst_base_url + filename
        os.unlink(path)


####################################################测试用例，成功
# file_handler = FileHandler('../voices/','../voice_store/')
# #file_handler.moveFile('v11.wav','hahha.wav')
# file_handler.deleteDstFile('hahha.wav')