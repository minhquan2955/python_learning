print("Hello world")
# trong python mọi thứ là object, biến chỉ là nhãn (label) dán lên vùng nhớ
a = [1,2,3] # mutable object(list, dict, set, class obj): Thay đổi = Sửa nội dung của nó tại chỗ
b = a # a,b đều trỏ đến 1 object
b[0] = 100 # a = [100,2,3]
print(a[0])
x = 1000 # imutable object(int, float, str, tuple): Thay đổi = Tạo mới & Trỏ lại
y = x # x,y cùng trỏ đến 1 obj int (1000)
y -= 1 # y = 999 => do là imutable, python tạo 1 obj int (999), bỏ trỏ của y tới obj int (1000) và y trỏ tới obj int (999)
print(f"{x} {y}")