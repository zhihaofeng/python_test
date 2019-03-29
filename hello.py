#python 3.7
def hello():
    print("Hello,world");
    return 0;


#math = int(input("math score:"))
#a = input("input:")
#english = int(input("english score:"))
#history = int(input("history score："))
ListedList = [[1, 3, -1], [5, 2, 5], [6, 4, 1], [2, 5, 0], [7, -1, 2], [3, 1, 3]];
Value = 0;
Right = 1;
Left = 2;
Next = 0;
while ListedList[Next][Right] > -1:
    print(ListedList[Next][Value]);
    Next = ListedList[Next][Right];
print("hll");
