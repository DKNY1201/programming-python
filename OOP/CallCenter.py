from collections import deque
from enum import Enum
import unittest


class CallStatus(Enum):
    WAITING = 0
    IN_PROCESS = 1
    COMPLETED = 2


class EmployeeRank(Enum):
    OPERATOR = 0
    SUPERVISOR = 1
    DIRECTOR = 2


class CallCenter:
    def __init__(self, id):
        self.id = id
        self.operators = []
        self.free_operators = deque([])
        self.supervisors = []
        self.free_supervisors = deque([])
        self.director = None
        self.calls = deque([])
        self.endedCalls = deque([])

    def take_call(self, call=None):
        if not call:
            raise Exception("No call to take")

        can_assign_call_to_operator = self.assign_call(self.free_operators, call)
        if can_assign_call_to_operator:
            return True

        can_assign_call_to_supervisor = self.assign_call(self.free_supervisors, call)
        if can_assign_call_to_supervisor:
            return True

        if not self.director.get_call():
            self.director.take_call(call)
            return True

        # add to queue
        self.calls.append(call)
        return False

    def take_call_from_queue(self):
        if not self.calls:
            return None

        self.take_call(self.calls.popleft())

    def assign_call(self, free_employees, call):
        if not free_employees:
            return False

        employee = free_employees.popleft()
        employee.take_call(call)
        return True

    def end_call(self, call):
        self.endedCalls.append(call)
        employee = call.handler

        if employee.rank == EmployeeRank.OPERATOR:
            self.free_operators.append(employee)
        elif employee.rank == EmployeeRank.SUPERVISOR:
            self.free_supervisors.append(employee)
        else:
            raise Exception("Employee rank doesn't support")

    def add_employee(self, employee):
        employee.set_call_center(self)
        if employee.rank == EmployeeRank.OPERATOR:
            self.operators.append(employee)
            self.free_operators.append(employee)
        elif employee.rank == EmployeeRank.SUPERVISOR:
            self.supervisors.append(employee)
            self.free_supervisors.append(employee)
        else:
            self.director = employee


class Employee:
    def __init__(self, id, name, rank):
        self.id = id
        self.name = name
        self.rank = rank
        self.call_center = None
        self.call = None

    def take_call(self, call):
        if self.call:
            raise Exception("Busy employee can't take call")

        self.call = call
        call.handler = self
        call.status = CallStatus.IN_PROCESS

    def end_call(self):
        if not self.call:
            raise Exception("No call to end")

        self.call.status = CallStatus.COMPLETED
        self.call_center.end_call(self.call)
        self.call = None

    def get_call(self):
        return self.call

    def set_call_center(self, call_center):
        self.call_center = call_center


class Call:
    def __init__(self, phone_num):
        self.phone_num = phone_num
        self.status = CallStatus.WAITING
        self.handler = None


class CallCenterTest(unittest.TestCase):
    def test_busy_call_center(self):
        call_center = CallCenter(1)

        operator1 = Employee(1, "Alice", EmployeeRank.OPERATOR)
        operator2 = Employee(2, "Bob", EmployeeRank.OPERATOR)
        supervisor1 = Employee(3, "Mark", EmployeeRank.SUPERVISOR)
        supervisor2 = Employee(4, "Maria", EmployeeRank.SUPERVISOR)
        director = Employee(5, "Kevin", EmployeeRank.DIRECTOR)

        call1 = Call("253000000")
        call2 = Call("253000001")
        call3 = Call("253000002")
        call4 = Call("253000003")
        call5 = Call("253000004")
        call6 = Call("253000005")
        call7 = Call("253000006")
        call8 = Call("253000007")
        call9 = Call("253000008")
        call10 = Call("253000009")

        call_center.add_employee(operator1)
        call_center.add_employee(operator2)
        call_center.add_employee(supervisor1)
        call_center.add_employee(supervisor2)
        call_center.add_employee(director)

        call_center.take_call(call1)
        call_center.take_call(call2)
        call_center.take_call(call3)
        call_center.take_call(call4)
        call_center.take_call(call5)
        call_center.take_call(call6)
        call_center.take_call(call7)
        call_center.take_call(call8)
        call_center.take_call(call9)
        call_center.take_call(call10)

        self.assertEqual(len(call_center.free_operators), 0, "No available operator")
        self.assertEqual(len(call_center.free_supervisors), 0, "No available supervisor")
        self.assertIsNot(call_center.director.get_call(), None, "Director is busy")
        self.assertEqual(len(call_center.calls), 5, "5 calls are waiting")

        operator2.end_call()
        supervisor2.end_call()
        self.assertEqual(len(call_center.free_operators), 1, "1 free operator")
        self.assertEqual(len(call_center.free_supervisors), 1, "1 free supervisor")
        call_center.take_call_from_queue()
        self.assertEqual(len(call_center.free_operators), 0, "No available operator")
        supervisor1.end_call()
        call_center.take_call_from_queue()
        self.assertIsNot(supervisor2.get_call(), None, "First available employee will take call first")
        self.assertIs(supervisor1.get_call(), None, "Not first employee won't take the call")
