from pathlib import Path
from fasthtml import *
import uvicorn
from local_demo_url import display_app_url_in_console

app = FastHTMLWithLiveReload()
rt = app.route


@rt("/")
def get():
    return Title("FastHTML"), H1("Hey there..")


if __name__ == "__main__":
    port = 8000
    reload_dirs = Path(__file__).parent.as_posix()
    display_app_url_in_console(port)
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True, reload_dirs=reload_dirs)
