from collections import defaultdict


class ChatMemory:

    def __init__(self):
        self.sessions = defaultdict(list)


    def add_message(
        self,
        session_id,
        role,
        content
    ):

        self.sessions[session_id].append(
            {
                "role": role,
                "content": content
            }
        )


        # Keep last 10 messages
        self.sessions[session_id] = (
            self.sessions[session_id][-10:]
        )


    def get_history(
        self,
        session_id
    ):

        return self.sessions[session_id]


    def clear(
        self,
        session_id
    ):

        self.sessions.pop(
            session_id,
            None
        )


memory = ChatMemory()