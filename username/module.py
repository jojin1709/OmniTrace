from .username_checker import UsernameChecker


class UsernameModule:
    def check(self, username: str) -> dict:
        return UsernameChecker().check_username(username)
