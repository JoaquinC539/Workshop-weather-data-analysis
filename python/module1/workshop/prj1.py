from datetime import datetime

class Appt:
    """An appointment has a start time, an end time, and a title.
    The start and end times should be on the same day.
    Usage example:
    appt1 = Appt(datetime(2018, 3, 15, 13, 30),
                datetime(2018, 3, 15, 15, 30),
                "Early afternoon nap")
    appt2 = Appt(datetime(2018, 3, 15, 15, 00),
                datetime(2018, 3, 15, 16, 00),
                "Coffee break")
    if appt2 > appt1:
        print(f"appt1 '{appt1}' was over when appt2 '{appt2}' started")
    
    elif appt1.overlaps(appt2):
        print("Oh no, a conflict in the schedule!")
        print(appt1.intersect(appt2))

    Should print:
        Oh no, a conflict in the schedule!
        2018-03-15 15:00 15:30 | Early afternoon nap and Coffee break
    """
    def __init__(self, app_start:datetime, app_end:datetime, task:str) -> None:
        assert app_end > app_start, f"Period finish ({app_end}) must be after start ({app_start})"

        self.app_start = app_start
        self.app_end = app_end
        self.task = task

    def __eq__(self, other: 'Appt') -> bool:
        """Equality means same time period,
        ignoring description"""
        return self.app_start == other.app_start and self.app_end == other.app_end
            
    def __lt__(self, other: 'Appt') -> bool:
        return self.app_start < other.app_start

    def __gt__(self, other: 'Appt') -> bool:
        return self.app_start > other.app_start
    
    def __str__(self) -> str:
        date_iso = self.app_start.date().isoformat()
        start_iso = self.app_start.time().isoformat(timespec='minutes')
        finish_iso = self.app_end.time().isoformat(timespec='minutes')
        return f"{date_iso} {start_iso} {finish_iso} | {self.task}"
    
    def __repr__(self) -> str:
        return f"Appt({repr(self.app_start)}, {repr(self.app_end)}, {repr(self.task)})"
    
    def overlaps(self, other: 'Appt') -> bool:
        """Is there a non-zero overlap between these periods?"""
        start = max(self.app_start, other.app_start)
        finish = min(self.app_end, other.app_end)
        return start < finish

    def intersect(self, other: 'Appt') -> 'Appt':
        """The overlapping portion of two Appt objects"""
        try:
            assert self.overlaps(other)
        except AssertionError:
            return 'There is no overlap'

        start = max(self.app_start, other.app_start)
        finish = min(self.app_end, other.app_end)
        
        return Appt(start, finish, self.task + " & " + other.task)
    
class Agenda:
    """An Agenda is a collection of appointments, 
    similar to a list. 

    Usage:
    appt1 = Appt(datetime(2023, 3, 15, 13, 30), datetime(2023, 3, 15, 15, 30), "Early afternoon nap")
    appt2 = Appt(datetime(2023, 3, 15, 15, 00), datetime(2023, 3, 15, 16, 00), "Coffee break")
    agenda = Agenda()
    agenda.append(appt1)
    agenda.append(appt2)
    ag_conflicts = agenda.conflicts()
    if len(ag_conflicts) == 0:
        print(f"Agenda has no conflicts")
    else:
        print(f"In agenda:\n{agenda.text()}")
        print(f"Conflicts:\n {ag_conflicts}")

    Expected output:
    In agenda:
    2023-03-15 13:30 15:30 | Early afternoon nap
    2023-03-15 15:00 16:00 | Coffee break
    Conflicts:
    2023-03-15 15:00 15:30 | Early afternoon nap and Coffee break
    """
    def __init__(self):
        self.elements = []

    def __eq__(self, other: 'Agenda') -> bool:
        """Delegate to __eq__ (==) of wrapped lists"""
        if not len(self.elements) == 0:
            return self.elements == other.elements

    def __lt__(self, other: 'Agenda') -> bool:
        """Delegate to __eq__ (==) of wrapped lists"""
        return self.elements < other.elements

    def __str__(self):
        """Each Appt on its own line"""
        result = ""
        for element in self.elements:
            result += str(element) + '\n'
        return result

    def __repr__(self) -> str:
        """String representation for debugging"""
        return f"Agenda({self.elements})"
    
    def append(self, an_appt: Appt) -> None:
        """Append the appointments in two agendas"""
        self.elements.append(an_appt)
    
    # Assistance of ChatGPT with the following function
        # sort function that simply uses the sorted builtin function
        # this function is used for dictionaries but also in this case lists
        # the sorted function takes a required iterable as the first argument
        # it takes a key, which is a function that is applied to every element in the iterable object

    def sort(self) -> None:
        """Sort agenda by appointment start times.
        This method sorts the appointments in-place."""
        self.elements = sorted(self.elements, key=lambda appt: appt.app_start)


    def __len__(self) -> int:
        """Returns the length of the Agenda."""
        return len(self.elements)
    

    def conflicts(self) -> 'Agenda':
        """Returns an agenda consisting of the conflicts
        (overlaps) between appointments in this agenda.
        Side effect: This agenda is sorted.
        """
        self.sort()
        conflicting_agenda = Agenda()
        
        for i in range(len(self.elements) - 1):
            if self.elements[i].overlaps(self.elements[i + 1]):
                conflict = self.elements[i].intersect(self.elements[i + 1])
                conflicting_agenda.append(conflict) 
        
        return conflicting_agenda
