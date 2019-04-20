from flask import Flask, request, abort
app = Flask(__name__)

def fizzbuzz(begin, end):
    ret = []

    for i in range(begin, end+1):
        default = str(i)
        tmp = ''
        if i % 3 == 0:
            tmp += 'Fizz'
        if i % 5 == 0:
            tmp += 'Buzz'

        if tmp != '':
            ret.append(tmp)
        else:
            ret.append(default)

    return ('\n'.join(ret) + '\n')

@app.route('/fizzbuzz')
def fizz_buzz():
    try:
        begin = int(request.args.get('begin'))
        end = int(request.args.get('end'))
    except:
        abort(400)

    if begin > end:
        abort(400)

    return fizzbuzz(begin, end)

if __name__ == '__main__':
      app.run(port=80)
