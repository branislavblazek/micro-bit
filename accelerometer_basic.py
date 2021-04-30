# Add your Python code here. E.g.
from microbit import *
 
def write_led_code(input_code, dire = 'x', rev = False):
    code = ''.join(reversed(input_code)) if rev else input_code 
    
    final_string = ''
    for i_row in range(5):
        line = ''
        for i_col in range(5):
            news = code[i_col]
            if dire == 'y':
                news = code[i_row]
                
            line += news

        line += ':'
        final_string += line
    return final_string
    
def calc_value(val, typ = 'x'):
    reverse = val < 0
    value = abs(val)
    code = None
    codes = ['00003', '00033', '00036', '00066', '00069', '00099']
    
    if value >= 50:
        if value <= 100:
            code = codes[0]
        elif value <= 200:
            code = codes[1]
        elif value <= 400:
            code = codes[2]
        elif value <= 600:
            code = codes[3]
        elif value <= 800:
            code = codes[4]
        elif value >= 800:
            code = codes[5]
            
    if code != None:
        return write_led_code(code, dire=typ, rev=reverse)
    return "00300:00600:36963:00600:00300"
 
while True:
    acc_x = accelerometer.get_x()
    acc_y = accelerometer.get_y()
    if abs(acc_x) >= 90:
        data = calc_value(acc_x, 'x')
    elif abs(acc_y) >= 90:
        data = calc_value(acc_y, 'y')
        
    display.show(Image(data))