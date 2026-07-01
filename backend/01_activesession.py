active_sessions = []

def start_session(user_id):
    session_id = f"session_{user_id}_{hash(user_id)}" # Simplified session ID generation
    if session_id not in active_sessions:
        active_sessions.append(session_id)
        print(f"Session started: {session_id}")
    else:
        print(f"Session already active for {user_id}")

def end_session(session_id):
    if session_id in active_sessions:
        active_sessions.remove(session_id)
        print(f"Session ended: {session_id}")
    else:
        print(f"Session not found: {session_id}")

start_session("user123")
start_session("user456")
start_session("user123") # Attempt to start again

print(f"Current active sessions: {active_sessions}")

end_session(f"session_user456_{hash('user456')}") # Use correct hash value
end_session("non_existent_session")

print(f"Final active sessions: {active_sessions}")