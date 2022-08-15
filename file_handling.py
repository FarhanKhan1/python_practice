from asyncore import read, write
from readline import append_history_file


f = open('test.txt','a')
# print(f.read())
f.write('This is testing file\n This is again')
f.close()

# 'r' => read
# 'w' => write
# 'a' => append
# 't' => text
# 'b' => binary

with open('test.txt') as f:
    