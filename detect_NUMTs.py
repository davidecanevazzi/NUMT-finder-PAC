# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
import linecache
from itertools import islice

if __name__ == '__main__':
    last_pos=1
    pos=1
    #sys.stdout = open('numts_test.txt', 'w')
    k=1
    name=""
    last_query=""
    ultimo=0
    #num_lines = sum(1 for line in open('DAU_KANSL_1000_filtered_not_chrM.paf'))
    with open("nuc.paf") as paf:
        for i in paf:
            line=i.split()
            last=name
            read=line[0].split(sep='_')
            name=read[0]
            number=int(read[3].split(sep='=')[1])
            if(last!=name):
                    #k=ultimo
                    #while(k<num_lines):
                     #   j=linecache.getline('DAU_KANSL_1000_filtered_not_chrM_sorted.paf', k)
                    #  line_query = j.split()
                        #read_query = line_query[0].split(sep='_')
                        #name_query = read_query[0]
                        #number_query = int(read_query[3].split(sep='=')[1])
                        #k=k+1
                        #if (name == name_query and (number != number_query) and name != last_query):
                        #    print(name)
                        #    last_query = name
                        #    ultimo=k
                        #    break

                with open("chrM.paf") as paf_query:
                    #f = islice(paf_query, last_pos, None)
                    for j in paf_query:
                        line_query=j.split()
                        read_query = line_query[0].split(sep='_')
                        name_query = read_query[0]
                        number_query = int(read_query[3].split(sep='=')[1])
                        #pos=pos+1
                        if(name==name_query and (number!=number_query) and name!=last_query):
                            #last_pos=last_pos+pos
                            #print(last_pos)
                            #pos=1
                            print(name)
                            last_query=name

    #sys.stdout.close()