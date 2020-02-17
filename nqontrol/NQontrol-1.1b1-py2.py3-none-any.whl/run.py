from nqontrol import dependencies, settings
from nqontrol.nqontrolUI import UI

app = dependencies.app
ui = UI()

# fixed the refresh issue. the layout has to be a function as below and the function then has to be referenced without calling it, so dash recomputes layout everytime instead of caching. Now, when opening an instance in another window or refreshing the page everything works as intended and the parameters stay the same
# see here for more details https://dash.plot.ly/live-updates


def get_layout():
    return ui.layout


app.layout = get_layout

ui.setCallbacks()
server = app.server


def main():
    app.run_server(
        host=settings.HOST, debug=settings.DEBUG, threaded=False, processes=1
    )


if __name__ == "__main__":
    main()
