class MissedScript(Exception):
    def __str__(self):
        return 'One or more sql scripts are missing.'