# listup_references_from_manuscript.py 
# 
# coding: utf-8
# This script reads text file of manuscript and list-up references 
# from the main text (before references), and output 
# to an text file. 
# 
# The references text may be 
#      Sato 1997
#      Sato and Smith 1997
#      Sato et al. 1997
#      Sato 1997; 2000; 2013a; 2013b 
#
# This script ignore calendar month and year conbimation such as 
#      January 2000, Feb. 2000     
# The limitation of the current version is that this script does not recognize a name consists of two words, such as 'von Storch', 'Sen Roy'. But the occurrence of these cases in one manuscript would be limited, and thus a user can correct the output list by hands easily. 
#      
# Author: Shoshiro Minobe 


import re
import os

months=['Jan.','Feb.','Mar.','Apr.','May','Jun.','Jul.','Aug.','Sep','Sep.','Oct.','Nov.','Dec.','January','February','March','April','May','June','July','August','September','October','November','December']

print('Please type the input text file name in full path. This is the manuscript file.')
in_file_name=input()
# in_file_name='d:\\temp\\190421_diurnal_text.txt'

print('Please type the output text file name in full path. This is the reference list file.')
out_file_name=input()
# out_file_name='d:\\temp\\refs.txt'

if not os.path.isfile(in_file_name): 
    raise Exception('The file, '+ in_file_name+', does not exist.')
fid = open(in_file_name, 'r')

references=[]
for nline,line in enumerate(fid):
    line=line.replace('(','')
    line=line.replace(')','')
    line=line.replace('[','')
    line=line.replace(']','')

    if line=='\n':
        continue
    words=line.split()
    for n,word in enumerate(words): 
        # '2016a.' has 6 characters
        m_4digit=re.match('[1-2][0-9][0-9][0-9]',word)
        if (4<=len(word) and len(word)<=6) and \
           re.match('[1-2][0-9][0-9][0-9]',word):
            print('word=%s'%word)
            isref=False

            if len(word)>4:    
                if re.match('[a-z]',word[4]): # e.g., 2010a
                    word=word[0:5]
                else:
                    word=word[0:4] 

            # Name et al. year
            if words[n-2]=='et' and words[n-1]=='al.':               
                isref=True
                ref1=words[n-3]+' '+words[n-2]+ ' ' + words[n-1]+' '+word

            # Name and Name year
            if words[n-2]=='and' and not words[n-1] in months \
               and not words[n-1].islower() and not words[n-3].islower():
                isref=True
                ref1=words[n-3]+' '+words[n-2]+ ' ' + words[n-1]+' '+word

            # Name year 
            if isref==False and not words[n-1] in months and not words[n-1].islower(): 
                isref=True
                ref1=words[n-1]+' '+word

            if isref:
                references.append(ref1)

            # pick up A year; year2; year3 etc. 
            if isref==True:
                for word_a in words[n+1:]:
                    if (4<=len(word_a) and len(word_a)<=6) and \
                        re.match('[1-2][0-9][0-9][0-9]',word_a):


                        if len(word_a)>4:    
                            if re.match('[a-z]',word[4]): # e.g., 2010a
                                word_a=word_a[0:5]
                            else:
                                word_a=word_a[0:4] 
                        ref2=ref1.replace(word,word_a)
                        references.append(ref2)
                    else:
                        break

fid.close()
references_unique=list(set(references))
references_unique.sort()
print(references_unique)

fid_wr = open(out_file_name, 'w')
for ref in references_unique:
    fid_wr.write(ref+'\n')
fid_wr.close()

