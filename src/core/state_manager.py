class StateManager:
    def __init__(self):
        self.is_authenticated = False
        self.current_user = None
        self.session_start_time = None
        self.clipboard_timer = 0

state = StateManager()