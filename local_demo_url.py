import io
import qrcode
import socket


def get_local_app_url(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return f"http://{s.getsockname()[0]}:{port}"


def get_qr_code(app_url):
    # https://github.com/lincolnloop/python-qrcode?tab=readme-ov-file#examples
    qr = qrcode.QRCode()
    qr.add_data(app_url)
    f = io.StringIO()
    qr.print_ascii(out=f)  # populate `f` with the ascii version of the qr code
    f.seek(0)
    return f.read()


def get_console_message(app_url, qr_code):
    return f"""
    Your app is *accessible 
    at the URL below    
    {app_url}

    {qr_code}
    *the second device needs to
    be connected to the same 
    network as your development 
    device.
    """


def print_console_message(text):
    border_colour = "\033[95m"  # purple
    text_colour = "\033[97m"  # white
    lines = text.split("\n")
    width = max(len(line) for line in lines)
    border = "+" + "-" * (width + 2) + "+"
    print("\n")
    print(f"{border_colour}{border}")
    for line in lines:
        print(f"{border_colour}| {text_colour}{line:<{width}}{border_colour} |")
    print(f"{border_colour}{border}")
    print("\n")


def display_app_url_in_console(port):
    """
    Get the local URL of the app, encode it in a QR code, and print it to the console.

    Why would I use this function?
    This function makes it really easy to live test any user facing changes on another
    device such as a mobile or tablet before committing them.

    Gotchas:
    - the second device (i.e. phone) must be connected to the same network as your development device (i.e. laptop)
    - the app url is served over http so the browser on your second device will scream that it is unprotected
    - you'll need to switch off protections when you first load the page on your second device
    """
    app_url = get_local_app_url(port)
    qr_code = get_qr_code(app_url)
    console_message = get_console_message(app_url, qr_code)
    print_console_message(console_message)
