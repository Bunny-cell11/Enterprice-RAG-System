
USERS = {
    "alice": {"role": "Executive"},
    "bob": {"role": "Engineering"},
    "charlie": {"role": "Support"}
}

def get_user_role(username):
    return USERS.get(username, {}).get("role")
