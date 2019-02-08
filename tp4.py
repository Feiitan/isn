import sys
from PyQt5 import QtGui, QtWidgets

def on_va_voir() :
    global a
    a = a + 1
    print("click")
    
def main () :
    global a
    a = 0
    
    global current_value, current_value_init, current_value_decimal
    current_value = 0
    current_value_init = True
    current_value_decimal = 0
    
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    window.resize(170,285)
    
    
    def create_button(x, y, t, cb) :
        button = QtWidgets.QPushButton(t,window)
        button.move(5 + 40*x, 80 + 40*y)
        button.resize(40,40)
        button.clicked.connect(cb)
    
    def key_clear1() :
        print("tu as clické sur A")
        
    def key_clear2() :
        print("tu as clické sur AC")
    
    def key_racine() :
        print("tu as clické sur √")
    
    def key_equal() :
        print("tu as clické sur =")
        
    def key_division() :
        print("tu as clické sur /")
        
    def key_times() :
        print("tu as clické sur *")
        
    def key_plus() :
        print("tu as clické sur +")
        
    def key_minus() :
        print("tu as clické sur -")
        
    def key_virgule() :
        current_value_decimal = 1
        if current_value_decimal > 0 :
            
        print("tu as clické sur ,")
        
        
    def key_negative() :
        print("tu as clické sur -")
        
        
    def key_digit(n) :
        def real_key_digit() :
            global current_value, current_value_init, current_value_decimal
            print("tu as clické sur", n)
            if current_value_init :
                current_value = n
            else :
                current_value = current_value * 10 + n
            current_value_init = False
            print("écran:", current_value)
        return real_key_digit
        
        
    
    create_button(0,0,  "A",   key_clear1)
    create_button(1,0, "AC",   key_clear2)
    create_button(2,0,  "√",   key_racine)
    create_button(3,0,  "-",   key_minus)
    create_button(0,1,  "7",   key_digit(7))
    create_button(1,1,  "8",   key_digit(8))
    create_button(2,1,  "9",   key_digit(9))
    create_button(3,1,  "/",   key_division)
    create_button(0,2,  "4",   key_digit(4))
    create_button(1,2,  "5",   key_digit(5))
    create_button(2,2,  "6",   key_digit(6))
    create_button(3,2,  "*",   key_times)
    create_button(0,3,  "1",   key_digit(1))
    create_button(1,3,  "2",   key_digit(2))
    create_button(2,3,  "3",   key_digit(3))
    create_button(3,3,  "+",   key_plus)
    create_button(0,4,  ",",   key_virgule)
    create_button(1,4,  "0",   key_digit(0))
    create_button(2,4,"(-)",   key_negative)
    create_button(3,4,  "=",   key_equal)
    
    window.show()
    sys.exit(app.exec_())
    
main()
