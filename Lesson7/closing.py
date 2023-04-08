class Close:
    def closing(self, work):
        work_in_memory = work
        def inner_closing(work):
            return f"I will help you with your {work_in_memory}. Afterwards I will help you with {work}"
        return inner_closing