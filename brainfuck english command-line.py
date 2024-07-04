#compilateur de brainfuck écrit en python//brainfuck compilator writen in python

braincode=input('(brainfuck code ) >>> ')
position=0
memory=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
def compile():
    global braincode
    global position
    global memory
    print(memory)
    for i in range(len(braincode)):
        if braincode[i]==',':
            memory[position]=ord(braincode[i+1])
        else:
            if braincode[i]=='+':
                memory[position]+=1
            if braincode[i]=='-':
                memory[position]-=1
            if braincode[i]=='<':
                if memory[position]<0:
                    position-=1
            if braincode[i]=='>':
                if memory[position]>0:
                    position+=1
            if braincode[i]=='.':
                memory[position]=chr(memory[position])

            if braincode[i]=='[':
                if memory[position]==0:
                    position=memory[position]
            if braincode[i]==']':
                if memory[position]!=0:
                    position-=1
        print(memory)

compile()
print("compilation end")
print("restart the script for another compilation !!! ")
