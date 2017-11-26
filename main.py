from flask import Flask, flash, redirect, render_template, request, session,abort, make_response
app = Flask(__name__)

from random import shuffle
from services.names_generator import read_names
from services.random_data_generator import generate_data
 
@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/names_generator")
def names_generator():
    return render_template('names_generator.html')

@app.route("/random_data_generator", methods=['GET','POST'])
def random_data_generator():
    if request.method=="POST":
        form_data = []
        form_name = []
        data = request.form
        params = (len(data)-1)/2
        number_of_entries = data['number']
        for i in range(1,params+1):
            form_data.append(float(data['v'+str(i)]))
            form_name.append(str(data['n'+str(i)]))
        f=[]
        for k in form_data:
            f.append(float(k))
        coded_output = generate_data(f,int(number_of_entries))
        decoded_output = []
        for c in coded_output:
            decoded_output.append(form_name[c])
        value_in_csv = ''
        for d in decoded_output:
            value_in_csv+=str(d)+'\n'
        value_in_csv = value_in_csv[:-1]
        response = make_response(value_in_csv)
        cd = 'attachment; filename=Data_Values.csv'
        response.headers['Content-Disposition'] = cd 
        response.mimetype='text/csv'
        return response
    return render_template('random_data_generator.html')

@app.route("/download_names", methods=['POST'])
def download_names():
    names = read_names("services/names.csv")
    shuffle(names)
    number = int(request.form['number'])
    if len(names)>number:
        names = names[:number]
    names_csv = ''
    for name in names:
        names_csv +=str(name)+'\n'
    names_csv=names_csv[:-1]
    response = make_response(names_csv)
    cd = 'attachment; filename=Names_IITJ.csv'
    response.headers['Content-Disposition'] = cd 
    response.mimetype='text/csv'
    return response

if __name__ == "__main__":
    apo.run(host='0.0.0.0',debug=True)
