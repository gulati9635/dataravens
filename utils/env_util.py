def env_config(env):
    if env == "prod":
        env = ""
    else:
        env = ".sandbox"

    return env