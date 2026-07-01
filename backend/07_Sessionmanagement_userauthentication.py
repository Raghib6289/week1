#Problem: A web application needs to manage active user sessions.
#  When a user logs in, a unique session ID is generated and stored.
#  When they log out, the session ID is removed. 
# We also need to quickly check if a given session ID is currently active.

#A set data structure is ideal here beacause it allows for fast membership testing, addition, and removal of session IDs.
#We need to store session IDs.
#The number of active sessions will change dynamically (users log in and out).
#We need to quickly add new session IDs.
#We need to quickly remove session IDs.
#We need to efficiently check if a specific session ID exists.

active_sessions = set()

def login_user(session_id):
    active_sessions.add(session_id)
    print(f"Session started: {session_id}")

def logout_user(session_id):
    if session_id in active_sessions:
        active_sessions.remove(session_id)
        print(f"Session ended: {session_id}")
    else:
        print(f"Session not found: {session_id}")

def is_session_active(session_id):
    return session_id in active_sessions

# Example Usage:
login_user("sess_abc123")
login_user("sess_def456")
print(f"Is sess_abc123 active? {is_session_active('sess_abc123')}") # True
print(f"Is sess_xyz789 active? {is_session_active('sess_xyz789')}") # False

logout_user("sess_abc123")
print(f"Is sess_abc123 active after logout? {is_session_active('sess_abc123')}") # False

logout_user("sess_xyz789") # Session not found