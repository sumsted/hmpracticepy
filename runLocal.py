__author__ = 'scottumsted'
from hmpracticepy import app

# for dev only
if __name__ == '__main__':
    app_options = {}
    app_options['port'] = app.config['PORT']
    app_options['debug'] = app.config['DEBUG']
    if app_options['debug'] == True:
        app_options['host'] = app.config['HOST']
    app_options["use_debugger"] = False
    app_options["use_reloader"] = False
    app.run(**app_options)
