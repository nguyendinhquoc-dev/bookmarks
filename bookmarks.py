# trích xuất tên trang web và địa chỉ từ file html - bookmarks
import re
import json

inp = input('Nhập tên file: ')
try:
    fl = open(inp, encoding="utf8")
except:
    print('File không tồn tại!')
    exit()

lsvalue = list()
lskey = list()
# valueandkey = list()

fvalue= open('value.txt', 'w', encoding="utf8") # tạo file để ghi giá trị(tên miền)
fkey= open('key.txt', 'w', encoding="utf8") # tạo file để ghi key (tên trang web)
data= open('data.txt', 'w', encoding="utf8") # tạo file để ghi trích xuất dưới dạng txt
for i in fl:
    i = i.rstrip()
    # x = re.findall('^Details:.*rev=([0-9]+)', i)
    val = re.findall('HREF="(\S+//\S+)"', i)
    key = re.findall('">(\S+\S.+)</A>', i) or re.findall('">(\S.+\S.+)</A>', i)
    if len(val) > 0:
        print(val)
        for ii in val:
            lsvalue.append(ii)
    if len(key) > 0:
        print(key)
        for iii in key:
            lskey.append(iii)

print('>>>')
print('>>>có', len(lsvalue), 'giá trị')
print('>>>có', len(lskey), 'key')
# print(lsvalue)
# print(lskey)

fvalue.write(str(lsvalue)) # ghi vào file 'data'
fkey.write(str(lskey)) # ghi vào file 'data'

# Chuyển đổi danh sách thành từ điển: sử dụng zip()
dictionary = dict(zip(lsvalue, lskey)) 
# print(dictionary)

#thêm vào json
# Tuần tự hóa dữ liệu thành tệp:
json.dump( dictionary, open( "valueandkey.json", 'w' ) )
# Đọc dữ liệu từ tệp:
dictionary = json.load( open( "valueandkey.json" ) )


# trích dữ liệu để đọc cho dễ
for k, v in zip(lsvalue, lskey):
        print(v +  ' - ' , k)
        data.write(str(v) + ' - ' + str(k) + '\n')