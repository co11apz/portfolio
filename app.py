""" Импортирование библиотеки для работы с Flask и запусков субпроцессов. """
import os
import subprocess
from flask import Flask, render_template


app = Flask(__name__, static_folder='site')


@app.route('/')
def index():
    """ Эта функция отвечает за возврат html файла """

    return render_template('index.html')


@app.route("/run")
def run():
    """ Эта функция отвечает за запуск тестов и генерацию отчета allure """

    script_path = os.path.dirname(os.path.abspath(__file__))
    assets_path = os.path.join(script_path)
    os.chdir(assets_path)
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
