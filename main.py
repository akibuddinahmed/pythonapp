from flask import Flask, render_template, request
import psycopg2


app = Flask(__name__)
conn = psycopg2.connect(
   database="appdb",
    user='appuser',
    password='strongpasswordapp',
    host='10.27.106.12',
    port= '30066'
)
conn.autocommit = True
cursor = conn.cursor() 
sql = '''CREATE TABLE test13(city_name char(20), city_population varchar(80));'''
cursor.execute(sql)
conn.commit()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        city = request.form['City']
        CityPolulation = request.form['CityPolulation']
    
        if city == '' or CityPolulation == '':
            return render_template('index.html', message='Please enter required fields')

        
        dictionary ={ 'city1' : (city, CityPolulation)}
        
        conn.autocommit = True
        cursor = conn.cursor() 
        columns= dictionary.keys()
        for i in dictionary.values():
            sql2='''insert into test13(city_name , city_population) VALUES{};'''.format(i)
            cursor.execute(sql2)
        conn.commit()
        sql3='''select * from test13;'''
        cursor.execute(sql3)
        for i in cursor.fetchall():
            print(i)

        return render_template('index.html', message='You have already submitted feedback')

@app.route('/knowpopulation', methods=['GET'])
def knowpopulation():
    if request.method == 'GET':
        city = request.form['City_Name']
        if city == '':
            return render_template('querypopulation.html', message='Please enter required fields')
        else: 
            sql = '''SELECT city_population from test13 WHERE city_name='Bangalore';'''
            city_population= cursor.execute(sql)
            #return render_template('success.html')
            return render_template('querypopulation.html', message=city_population)
        
        return render_template('querypopulation.html')

@app.route('/knowhealthindex')
def knowhealthindex():
    return render_template('queryhealth.html')


conn.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
