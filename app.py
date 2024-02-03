""" Импортирование библиотеки для работы с Flask и запусков субпроцессов. """
import os
import subprocess
from flask import Flask, render_template


app = Flask(__name__, static_folder='site')

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/runallure")
def run_allure():
    """ Эта функция запуская и отвечает за генерацию отчета allure. """

    cmd = ["./scriptsh/runallure.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


@app.route("/run")
def run():
    os.chdir('C:/Users/roman/PycharmProjects/portfolio/site/assets/')
    cmd = ["autotests.sh"]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE,
                          stdin=subprocess.PIPE,
                          universal_newlines=True,
                          shell=True) as result:
        out = result.communicate()
    return render_template('index.html', text=out, json=out)


if __name__ == "__main__":
    app.run(debug=True)
