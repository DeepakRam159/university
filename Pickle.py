'''import pickle
print("working with binary files")
with open("empfile.dat","ab")as bf:
    edata = ["eno","ename","ebasic","totsal"]
    pickle.dump(edata,bf)'''
import pickle
try:
    with open("empfile.dat","rb") as bf:
        while True:
            edata=pickle.load(bf)
            #print("record number:",readrec)
            print(edata)
            #readrec= readrec + 1
except EOFError:
    pass
            
