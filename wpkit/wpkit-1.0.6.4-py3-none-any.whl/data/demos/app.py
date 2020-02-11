import wpkit
# a=wpkit.data.get_data('demos/app.py')
# print(a)
app= wpkit.web.web.App(__name__)
# app.add_default_route()
app.register_blueprint(app.bp_root(name='root',url_prefix='/'))
app.register_blueprint(app.bp_board(name='board1',url_prefix='/board'))
app.register_blueprint(app.bp_static(name='static1',url_prefix='/fs'))
app.register_blueprint(app.bp_sitemap(name='sitemap',url_prefix='/sitemap',map={
    'root':'/',
    'board':'/board',
    'files':'/fs',
    'sitemap':'/sitemap'
}))
print(app.url_map)
app.run(host='127.0.0.1',port=80)