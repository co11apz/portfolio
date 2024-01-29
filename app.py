""" Импортирование библиотеки для работы с Flask и запусков субпроцессов. """
import os
import subprocess
from flask import Flask, render_template


app = Flask(__name__)


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
def runo():
    bash_path = "D:/Git/bin/bash.exe"
    script_path = "C:/Users/roman/PycharmProjects/mysite/site/assets/autotests.sh"
    cmd = [script_path, bash_path]
    with subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, universal_newlines=True) as result:
        out, err = result.communicate()
        print("Output from autotests.sh:")
    return render_template('index.html', text=out, error=err)


if __name__ == "__main__":
    app.run(debug=True)
