import json

def update_settings():
    lsettings = json.loads(open("settings.json").read())
    settings = {}

    def loop(d, ks):
        for k in d:
            if type(d[k]) == dict:
                loop(d[k], ks + [k])
            else:
                settings[".".join(ks + [k])] = d[k]

    loop(lsettings, [])

    return settings

def save_settings(settings):
    lsettings = {}

    for s in settings:
        if "." not in s:
            lsettings[s] = settings[s]
        else:
            ls = lsettings
            ss = s.split(".")
            for k in ss[:-1]:
                if k not in ls:
                    ls[k] = {}
                ls = ls[k]
            ls[ss[-1]] = settings[s]

    with open("settings.json", "w") as f:
        json.dump(lsettings, f, indent=2)

    update_settings()

    return settings
