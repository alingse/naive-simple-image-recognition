#coding=utf-8
#2015/06/06
#author@shibin

#----------------------------------------------------------------------
from os import listdir
import threading
import webbrowser
import Image
#import yzm
from yzm import splitimg,show_pixel

test_dir='./test_data/'
result_dir='./IMG/'
split_dir='./split_data/'
training_dir='./training_data_select/'

class showimg(threading.Thread):
    def __init__(self,imfname):
        threading.Thread.__init__(self)
        self.imfname=imfname
        self.exitable=False
    def setexit(self):
        self.exitable=True
    def run(self):
        webbrowser.open(self.imfname)

IMGNUM=0

def split_save(path_dir,file_name,splitdir):
    fname=path_dir+file_name
    im=Image.open(fname)
    (xsList,xeList,ysList,yeList)=splitimg(im)
    if xsList:
        for m in range(6):
            splitim=im.crop((ysList[m], xsList[m], yeList[m], xeList[m]))    
            splitim.save(splitdir+str(IMGNUM)+file_name)
        return True
    return False

char_dict={}
char_max=5
char_count=10#+26

def rename(path_dir,file_name,rename_dir):
    if filter(lambda x:x<char_max,char_dict.values())==[]:
        if len(char_dict.keys())==char_count:
            return
    fpath=path_dir+file_name
    #showimg(fpath).start()
    im=Image.open(fpath)
    show_pixel(im)

    codevalue=raw_input('codevalue(str):')
    if codevalue=='':
        return
    if not char_dict.has_key(codevalue):
        char_dict[codevalue]=0
    if char_dict[codevalue]>char_max:
        return 
    renamepath=rename_dir+codevalue+'_'+str(char_dict[codevalue])+'.jpg'
    im.save(renamepath)
    char_dict[codevalue]+=1
    return

if __name__ == '__main__':
    #0-9
    char_count=30
    #+1
    #-1
    #1
    #K-means
    char_max=5
    #split----
    resultfile_list = listdir(result_dir)#iterate through the test set
    for filenamestr in resultfile_list:
        split_save(result_dir,filenamestr,split_dir)
    #rename--it----
    splitfile_list = listdir(split_dir)
    for filenamestr in splitfile_list:
        rename(split_dir,filenamestr,training_dir)

    #




