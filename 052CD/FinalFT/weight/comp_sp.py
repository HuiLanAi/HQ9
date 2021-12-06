total_line = 0
gcn_line = 0
tcn_line = 0
total_zero = 0
gcn_zero = 0
tcn_zero = 0

# compute tcn sparsity
for i in range (10):
    fname = './tcn_weight/tcn_weight_' + str(i+1) + '.txt'
    f = open(fname, 'r')
    
    for data in f.readlines():
        data = (float)(data)
        total_line += 1
        tcn_line += 1
        if (data == 0 or abs(data) < 0.0001):
            total_zero += 1
            tcn_zero += 1
    f.close()
print(tcn_zero / tcn_line)

# wash gcn weight according to tch dropk
# for i in range (8):
#     wfname = './gcn_weight/gcn_weight_wash_' + str(i+2) + '.txt'
#     wf = open(wfname, 'w+')
#     dkname = './tcn_weight/tcn_dropk_' + str(i+1) + '.txt'
#     dk = open(dkname, 'r')
#     owname = './gcn_weight/gcn_weight_' + str(i+2) + '.txt'
#     ow = open(owname, 'r')

#     dklist = []
#     for data in dk.readlines():
#         dklist.append(int(data, 10))
    
#     chn_cnt = 0
#     rcnt = 0
#     for data in ow.readlines():
#         if(rcnt == 0):
#             in_chn = int(data)
#             rcnt += 1
#         elif(rcnt == 1):
#             n_kernel = int(data)
#             rcnt += 1
#         elif(rcnt == 2):
#             num_set = int(data)
#             rcnt += 1
#         else:
#             if(chn_cnt in dklist):
#                 wf.write('0'+'\n')
#             else:
#                 wf.write(data)
#             if(chn_cnt == in_chn - 1):
#                 chn_cnt = 0
#             else:
#                 chn_cnt += 1

#     wf.close()
#     dk.close()
#     ow.close()

# compute washed-gcn sparsity
for i in range (10):
    fname = './gcn_weight/gcn_weight_wash_' + str(i+1) + '.txt'
    f = open(fname, 'r')
    
    for data in f.readlines():
        data = (float)(data)
        total_line += 1
        gcn_line += 1
        if (data == 0):
            total_zero += 1
            gcn_zero += 1
    f.close()
print(gcn_zero / gcn_line)
print(total_zero / total_line)