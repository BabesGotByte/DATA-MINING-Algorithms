import csv

filename = "data1.csv"

minSupport = 3
minConfidence = 0.3
  
transactions = []

freq_items = {}
  
with open(filename, 'r') as csvfile: 
    csvreader = csv.reader(csvfile) 

    for row in csvreader: 
        transactions.append(row)

for trans in transactions:
    for item in trans:
        freq_items[item] = freq_items.get(item,0)+1


for key in list(freq_items.keys()):
    if(freq_items[key]<minSupport):
        del freq_items[key]


def freq(x):
    return freq_items[x]

ordered_item_set = []
for trans in transactions:
    item_set = []
    for item in trans:
        if (item in freq_items):
            item_set.append(item)
    item_set = sorted(item_set,key = freq,reverse = True)
    ordered_item_set.append(item_set)



cond_pattern_base = {}
for row in ordered_item_set:
    parent_list = []
    for item in row:
        if(item not in cond_pattern_base):
            cond_pattern_base[item] = []
        
        cond_pattern_base[item].append(list(parent_list))
        parent_list.append(item)
        
    parent_list.clear()



cond_freq_tree = {}
for key in list(cond_pattern_base.keys()):
    common_items = cond_pattern_base[key][0]
    for it in cond_pattern_base[key]:
        for item in list(common_items):
            if (item not in it):
                common_items.remove(item)
    cond_freq_tree[key] = [list(common_items),len(cond_pattern_base[key])]



for key in cond_freq_tree.keys():
    freq_item_set = cond_freq_tree[key][0]
    support_count = cond_freq_tree[key][1]
    if(len(freq_item_set)<1):
        continue
    for item in freq_item_set:
        conf_right = (support_count/freq_items[key])*100
        conf_left = (support_count/freq_items[item])*100

        if(conf_right>=minConfidence*100):
            print(key+' => '+item+": "+"%.2f" % conf_right)
        if(conf_left>=minConfidence*100):
            print(item+' => '+key+": "+"%.2f" % conf_left)
    if(len(freq_item_set)>1):
        conf = (support_count/freq_items[key])*100
        if(conf>=minConfidence*100):
            print(key+' => '+str(freq_item_set)+" : "+"%.2f" % conf)






