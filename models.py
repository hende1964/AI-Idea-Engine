from datetime import datetime

class Idea:
    """
    Represents an Idea stored in the Idea Engine.
    """
    def __init__(self, content, category="General", created_at=None):
        self.content = content
        self.category = category
        self.created_at = created_at or datetime.utcnow()

    def to_dict(self):
        """Convert the idea object to a dictionary."""
        return {
            "content": self.content,
            "category": self.category,
            "created_at": self.created_at.isoformat()
        }
