from mpy_env import load_env, get_env

load_env()
print(get_env("wifi_ssid"))
print(get_env("wifi_pass"))
