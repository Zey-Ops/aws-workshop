from flask import Flask , render_template ,request

app = Flask(__name__) 

def convert(milliseconds):
    hour_ms = 60*60*1000
    hours = milliseconds // hour_ms
    ms_left = milliseconds % hour_ms
    minutes_ms = 60*1000
    minutes = ms_left // minutes_ms
    ms_left = ms_left % minutes_ms
    seconds = ms_left // 1000 
    return f"{hours} hour/s " *(hours != 0) + f"{minutes} minute/s " *(minutes != 0) + f"{seconds} second/s " *(seconds != 0) or f"just {milliseconds} millisecond/s " *(milliseconds < 1000) 

@app.route('/', methods = ['GET']) 
def main_get():
    return render_template ('index.html', developer_name = 'Zylina',not_valid = False) 

@app.route('/', methods = ['POST'])
def main_post():
    alpha = request.form ["number"]
    if not alpha.isdigit():
        return render_template ('index.html', developer_name = 'Zylina',not_valid = True) 
    
    number =int(alpha)
    if (0 > number):
        return render_template ('index.html', developer_name = 'Zylina',not_valid = True)

    return render_template ('result.html', milliseconds=number, result= convert (number), developer_name = 'Zylina') 

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug = True)
    #app.run(debug=True)  
    