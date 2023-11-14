import requests
import requests.auth

key_list = {
    # Sources
    "power": ("KEY","3B"),
    "hdmi1": ("SOURCE","30"),
    "hdmi2": ("SOURCE","A0"),
    "computer1": ("SOURCE","10"),
    "computer2": ("SOURCE","20"),
    "video": ("SOURCE","41"),
    "usb_display": ("SOURCE","51"),
    "usb": ("SOURCE","52"),
    "lan": ("SOURCE","53"),
    "screen_mirroring": ("SOURCE","56"),
    # Keys
    "source_search": ("KEY","67"),
    "av_mute": ("KEY","3E"),
    "freeze": ("KEY","47"),
    "volume_down": ("KEY","57"),
    "volume_up": ("KEY","56"),
    "ok": ("KEY","49"),
    "left": ("KEY","5A"),
    "up": ("KEY","58"),
    "right": ("KEY","5B"),
    "down": ("KEY","59")
}
panel_password = "admin"

def _press_key(key_name):
    print(f"Pressing '{key_name}'...")
    response = requests.get(
        url = "http://192.168.88.1:80/cgi-bin/Remote/directsend",
        params = {key_list[key_name]},
        headers = {
            "Referer": "http://192.168.88.1/cgi-bin/Remote/Basic_Control"
        },
        auth = requests.auth.HTTPDigestAuth(
            "EPSONWEB",
            panel_password
        )
    )
    print(f"Code: {response.status_code} (Length: {str(len(response.content))})")
    return response.ok

def _check_interface():
    try:
        response = requests.get(
            url = "http://192.168.88.1:80/",
            timeout = 5
        )
        assert (response.status_code == 200)
        return True
    except Exception:
        return False
