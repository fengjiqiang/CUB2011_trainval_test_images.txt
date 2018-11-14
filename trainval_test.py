import numpy as np

split_list = open('./CUB_200_2011/train_test_split.txt').readlines()
train_list = []
test_list = []
for line in split_list:
    idx, is_train = line.strip().split()
    if int(is_train) == 1:
        train_list.append(str(idx))
    else:
        test_list.append(str(idx))


train_images = []
test_images = []
image_list = open('./CUB_200_2011/images.txt').readlines()


for line in image_list:
    idx, name_list = line.strip().split()
    if str(idx) in train_list:
        train_images.append('/images/'+name_list)
    else:
        test_images.append('/images/'+name_list)

# print(train_images[:10])
# print(test_images[:10])


def text_save(filename, data):#filename为写入txt文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
        s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功") 

# text_save("train_images.txt", train_images)
text_save("test_images.txt", test_images)