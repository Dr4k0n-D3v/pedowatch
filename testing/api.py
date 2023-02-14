from flask import Flask, request, jsonify
import os, json, logger

tof = {
    'true':'True',
    'false':'False'
}

app = Flask(__name__)

@app.route("/api/login", methods=["POST"])
def login():
    print(request.json)
    print(request.form)
    print(request.data)
    email = request.json('email')
    password = request.form.get('password')
    print(email + password)
    print(f'someone tried to login with {email} {password}')
    '''
    with open('data/login.json') as f:
        file = json.load(f)
    log = False
    for obj in file:
        if obj['email'] == email and obj['passwd'] == password:
            log = True
            break
    if log:
        response = {
            'status': 'success',
            'message': 'Login successful'
        }
        return json.dumps(response), 200
    else:
        response = {
            'status': 'error',
            'message': 'Incorrect email or password'
        }
        return json.dumps(response), 401
    '''
    resp = 'success'
    return resp

@app.route('/api/signup', methods=["POST"])
def signup():
    user = request.form.get('user')
    email = request.form.get('email')
    password = request.form.get('password')
    with open('data/login.json') as f:
        file = json.load(f)
    var = True
    for obj in file:
        if obj['email'] == email or not var:
            var = False
            break
    if var:
        data = {f'user':{
                'name':f'{user}',
                'email':f'{email}',
                'password':f'{password}'
            }
        }
        file.update(data)
        with open('data/login.json', "w") as f:
            f.write(json.dumps(file))
            f.close()
        response = {
            'status': 'success',
            'message': 'Sign up successful'
        }
        return jsonify(response), 201
    else:
        response = {
            'status': 'failure',
            'message': 'Sign up failed'
        }
        return jsonify(response), 400

@app.route('/api/post', methods=["POST"])
def post():
    posts = 'data/posts'
    response = {'success': False}
    try:
        title = request.form.get('title')
        desc = request.form.get('desc')
        file = 'ohno'
        try:
            file = request.files['file']
        except:
            pass
        path = os.path.join(posts, title)
        os.mkdir(path)
        with open(f"{path}/desc.txt", "w") as f:
            f.write(desc)
            f.close()
        file.save(os.path.join(path, file.filename))
        response['success'] = True
    except:
        pass
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)