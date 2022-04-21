import sys
def k_mer_split(read,dim,step,name):
    k_mer=[]
    i=0
    num=1
    while i< len(read):
        new_name = name + str(num)
        k_mer.append(new_name)
        k_mer.append(read[i:i+dim])
        i+=step
        num=num+1
    return k_mer

def create_fasta(k_mers,filename):
    i=0
    original_stdout=sys.stdout
    with open(filename,'w')as f:
        sys.stdout=f
        while(i<len(k_mers)):
            print('>', i)
            print(k_mers[i])
            i+=1
        sys.stdout=original_stdout

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name=""
    res=[]
    with open("reads.fasta") as fasta:
        for i in fasta:
            if(i[0]=='>'):
                append=1
                i=i.split()
                name=i[0][0:-1]+'_k_mer_number='
            else:
                k_mers=k_mer_split(i,1000,1000,name)
                print("\n".join(k_mers))
