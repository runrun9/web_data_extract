data = open("perc04_word_list/perc04_lemma_pos_dic.freq_sort.txt", "r")


li = []
for line in data:
    if line.split()[7] != "0" and (line.split()[1] == "NN0" or line.split()[1] =="NN1"):
        li.append([line.split()[0], line.split()[1], int(line.split()[7])])

li.sort(key = lambda x:x[2])
# print(li[0])

i = 1
for x in range(20):
    print(li[len(li) - i])
    i = i+1
