from db import conn
from flask import Flask, request, jsonify

app = Flask(__name__)

def valid_pic(code):
    return True

def convert_year(year):
    return year_dict[year]

year_dict = {'2005':'two_thousand_five','2006':'two_thousand_six','2007':'two_thousand_seven','2008':'two_thousand_eight'
            , '2009':'two_thousand_nine','2010':'two_thousand_ten','2011':'two_thousand_eleven','2012':'two_thousand_twelve'
            , '2013':'two_thousand_thirteen', '2014' :'two_thousand_fourteen'}

independentSchoolLabel = 'Independent'
stateSchoolLabel = 'State'
specialSchoolLabel = 'Special'
mainstreamSchoolLabel = 'Mainstream'

independent = ['IND', 'INDSS', 'NMSS', 'INDSPEC', 'INDSP']
state = ['VA','VC','AC','CTC','CY','CYS','FD','FDS' 'ACC','ACF','ACS','ACCS','FS','FSS','FUTC','CHS','FHS','PRU', 'FAP','ACCAP','ACAP','AP','F']
special = ['CYS', 'FDS', 'NMSS', 'INDSS', 'INDSP', 'FS']

schoolTypeSpecificDict = {
    'AC':'Academy Sponsor Led',
    'CY':'Community School',
    'VA':'Voluntary Aided School',
    'VC ':'Voluntary Controlled School',
    'FD':'Foundation School',
    'CTC':'City Technology College',
    'CYS':'Community Special School',
    'FDS':'Foundation Special School',
    'NMSS':'Non-maintained Special School',
    'INDSS':'Independent Special School',
    'IND':'Independent School',
    'CHS':'Community Hospital School',
    'FHS':'Foundation Hospital School',
    'PRU':'Pupil Referral Unit',
    'INDSP':'Independent Special School',
    'ACS':'Academy Special',
    'ACC':'Academy Converter',
    'F':'Free School - Mainstream',
    'FS':'Special Free Schools',
    'ACCS':'Converter special academies',
    'FAP':'Free School AP',
    'FUTC':'Free School UTC (University Technical College)',
    'FSS':'Free School - Studio School',
    'ACCAP':'Academy - Converter Alternative Provision (AP)',
    'ACAP':'Academy - Sponsor med Alternative Provision (AP)',
    'AP':'Alternative Provision',
    'INDSPEC':'Independent school catering wholly or mainly for children with statutory statements of special educational needs.',
    'ACF':'Academy Free School'
}

def schoolType(school_tag):
    if school_tag in independent:
        return independentSchoolLabel
    else:
        return stateSchoolLabel

@app.route('/')
def hello():
    return 'PiC Alpha Test'

@app.route('/schools')
def schools():
    name = request.args.get('name')
    year = request.args.get('year')
    year = convert_year(year)
    cursor = conn.cursor()

    table_string_formatting = "SELECT school_type FROM " + year #SQL Injection
    cursor.execute(table_string_formatting + ' WHERE school_name = %s', (name,))
    data = cursor.fetchone()
    if data:
        try:
            return jsonify(
                    school_name=name,
                    school_type= schoolType(data[0]),
                    specific_type=schoolTypeSpecificDict[data[0]],
                    special_school= data[0] in special
                    )
        except:
            return "BEEEP SOMETHING WENT WRONG"
    else:
        return "Invalid School Reference"

    # # parse query parameter
    # pic_code = request.args.get('pic_code')
    # test = request.args.get('test')
    # return pic_code + test
    # if valid_pic(pic_code):
    #     cursor = conn.cursor()
    #     cursor.execute('SELECT name, type, admission FROM schools WHERE pic_code={0};'.format(pic_code))
    #     data = cursor.fetchone()
    #     if data:
    #         name = data[0]
    #         school_type = data[1]
    #         admission = data[2]
    #     cursor.close()
    #     return jsonify(
    #         pic_code=pic_code,
    #         name=name,
    #         type=school_type,
    #         admission=admission
    #     )
    # else:
    #     return jsonify(error='pic_code does not exist.')