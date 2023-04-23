from tkinter import *
expression = "" #Lưu trữ kết quả của phép tính

def press(num):
    global expression
    #nối chuỗi
    expression += str(num)
    #cập nhật phép tính bằng phương thức set
    equation.set(expression)

#Hàm tính toán kết quả cuối cùng của phép tính
def equalpress():
    #Sử dụng try catch để xử lý lỗi như là chia cho 0 bằng hàm đánh giá toán học eval
    try:
        global expression
        #hàm eval đánh giá biểu thức
        #hàm str chuyển đổi nó thành kết quả ra string
        total = str(eval(expression))
        equation.set(total)
        #khởi tạo lại phép tính
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

#Xoá màn hình nhập
def clear():
    global expression
    expression = ""
    equation.set("")



if __name__ == "__main__":
    gui = Tk()

    gui.configure(background= "white")
    gui.title("Simple Calculator")
    gui.geometry("360x500")

    #Khởi tạo lớp biến equation
    equation = StringVar()
    #tfont dùng để thay đổi kích thức chữ phần nhập
    tfont = ('Verdana', 20)
    #Vùng nhập biểu thức có kiểu biến là equation, font là tfon
    expression_field = Entry(gui,textvariable= equation, font = tfont)

    #Grid layout có 4 cột
    expression_field.grid(columnspan=4)

    #tạo các nút và chia nó vào grid layout

    Clear = Button(gui, text='Clear', fg = '#FFD154', bg = '#3D3D3D',
                command=clear, height=4, width = 10)
    Clear.grid(row=2, column=0)

    Brackets = Button(gui, text='(', fg = '#FFD154', bg = '#3D3D3D',
                command=lambda: press('('), height=4, width = 10)
    Brackets.grid(row=2, column=1)

    Brackets = Button(gui, text=')', fg = '#FFD154', bg = '#3D3D3D',
                command=lambda: press(')'), height=4, width = 10)
    Brackets.grid(row=2, column=2)
    
    Hat = Button(gui, text='^', fg = '#FFD154', bg = '#3D3D3D',
                    command=lambda: press('**'), height=4, width = 10)
    Hat.grid(row=2, column=3)
    
    button1 = Button(gui, text='1', fg = '#FFD154', bg = '#3D3D3D', 
                    command= lambda: press(1), height=4, width = 10)
    button1.grid(row=3, column= 0)

    button2 = Button(gui, text='2', fg = '#FFD154', bg = '#3D3D3D',
                    command= lambda: press(2), height=4, width = 10)
    button2.grid(row = 3, column= 1)

    button3 = Button(gui, text='3', fg = '#FFD154', bg = '#3D3D3D',
                    command= lambda: press(3), height=4, width = 10)
    button3.grid(row = 3, column= 2)

    button4 = Button(gui, text='4', fg = '#FFD154', bg = '#3D3D3D',
                    command= lambda: press(4), height=4, width = 10)
    button4.grid(row=4, column= 0)

    button5 = Button(gui, text='5', fg = '#FFD154', bg = '#3D3D3D',
                    command= lambda: press(5), height=4, width = 10)
    button5.grid(row=4, column=1)

    button6 = Button(gui, text='6', fg = '#FFD154', bg = '#3D3D3D',
                    command= lambda: press(6), height=4, width = 10)
    button6.grid(row=4, column=2)

    button7 = Button(gui, text='7', fg = '#FFD154', bg = '#3D3D3D', 
                    command= lambda: press(7), height=4, width = 10)
    button7.grid(row = 5, column=0)

    button8 = Button(gui, text='8', fg = '#FFD154', bg = '#3D3D3D', 
                    command= lambda: press(8), height=4, width = 10)
    button8.grid(row=5, column=1)

    button9 = Button(gui, text='9', fg = '#FFD154', bg = '#3D3D3D',
                     command= lambda: press(9), height=4, width = 10)
    button9.grid(row=5, column=2)

    button0 = Button(gui, text='0', fg = '#FFD154', bg = '#3D3D3D', 
                    command= lambda: press(0), height=4, width = 10)
    button0.grid(row=6, column=0)

    plus = Button(gui, text=' + ', fg = '#FFD154', bg = '#3D3D3D',
                command=lambda: press("+"), height=4, width = 10)
    plus.grid(row=3, column=3)
 
    minus = Button(gui, text=' - ', fg = '#FFD154', bg = '#3D3D3D',
                command=lambda: press("-"), height=4, width = 10)
    minus.grid(row=4, column=3)
 
    multiply = Button(gui, text=' * ', fg = '#FFD154', bg = '#3D3D3D',
                    command=lambda: press("*"), height=4, width = 10)
    multiply.grid(row=5, column=3)
 
    divide = Button(gui, text=' / ', fg = '#FFD154', bg = '#3D3D3D',
                    command=lambda: press("/"), height=4, width = 10)
    divide.grid(row=6, column=3)
 
    equal = Button(gui, text=' = ', fg = '#FFD154', bg = '#3D3D3D',
                command=equalpress, height=4, width = 10)
    equal.grid(row=6, column=2)

    Decimal = Button(gui, text='.', fg = '#FFD154', bg = '#3D3D3D',
                    command=lambda: press('.'), height=4, width = 10)
    Decimal.grid(row=6, column=1)


 
    gui.mainloop()
