import time

file = open('/home/congsl/tmp/hello.txt', 'w+')
num = 3000000
t1 = time.time()
for i in range(0, num):
    file.write("%s" % i)
    file.seek(0, 0)
    file.flush()
t2 = time.time()
file.close()
print "taken time:%s" % (t2 - t1)
sequential_file = open('/home/congsl/tmp/sequential.txt', 'w+')
for i in range(0, num):
    sequential_file.write("%s" % i)
    # sequential_file.flush()
t3 = time.time()
print "taken time:%s" % (t3 - t2)
sequential_file.close()