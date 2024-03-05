def swap(c):
    if c==" X  ":
        return " O  "
    return " X  "
def dispBoard(board):
    for i in range(3):
        _end="|"
        for j in range(3):
            if(j==2):
                _end="\n "
            print(board[i][j],end=_end)
        if i==2 :
            continue
        print("_"*10)
def check(arr):
    for i in range(3):
        if arr[i][0]!="    " and all(arr[i][j]==arr[i][0] for j in range(1,3)):
            print(arr[i][0][1]," WINS")
            return True
        if arr[0][i]!="    " and all(arr[j][i]==arr[0][i] for j in range(1,3)):
            print(arr[i][0][1]," WINS")
            return True
    if arr[0][0]!="    " and all(arr[i][i]==arr[0][0] for i in range(1,3)):
        print(arr[0][0][1]," WINS")
        return True
    if arr[2][0]!="    " and all(arr[i][2-i]==arr[2][0] for i in range(3)):
        print(arr[2][0][1]," WINS")
        return True
    return False
board=[["    " for i in range(3)] for j in range(3)]
dispBoard(board)
c=1
while c==1:
    curr=" X  "
    f=0
    for i in range(9):
        print(curr[1],"'s turn")
        while 1:
            row=int(input("Enter row no:"))
            col=int(input("Enter col no:"))
            if row<1 or col<1 or row>3 or col>3 or board[row-1][col-1]!="    ":
                print("Enter valid position")
            else:
                break
        board[row-1][col-1]=curr
        dispBoard(board)
        if check(board):
            f=1
            break
        curr=swap(curr)
    if f==0:
        print("Draw")
    c=int(input("1.Play Again\n2.Exit\nEnter choice:"))
    
    
