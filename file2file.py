import sys
import collections

file_argv1 = sys.argv[1]
file_argv2 = sys.argv[2]
file_argv3 = sys.argv[3]
#print "files: {0}|{1}|{2}".format(file_argv1,file_argv2,file_argv3)

m2m = list(line.strip() for line in open(file_argv1))               
preconditioned = set(line.strip() for line in open(file_argv2))    

count = 0
match = 0
prematch = 0
postconditioned = set()
postconditionedList = []

for m2m_ in m2m:
  if(not m2m_.startswith("#")):
    m2m_ = m2m_.rstrip('\n')
    count+=1
    #print "{0}] {1}".format(count,m2m_)
    match = 0
    prematch = match
    for preconditioned_ in preconditioned:
      preconditioned_ = preconditioned_.rstrip('\n')
      if(m2m_ in preconditioned_ and not preconditioned_.startswith("#")):
        match+=1
        postconditioned.add(preconditioned_+"\n")
        postconditionedList.append(preconditioned_+"\n")
    if(match == prematch):
      postconditioned.add(m2m_+"\n")
      postconditionedList.append(m2m_+"\n")

#z=collections.OrderedDict.fromkeys(postconditioned)

with open(file_argv3, 'w') as file_out:
  for line in postconditionedList:
    file_out.write(line)
