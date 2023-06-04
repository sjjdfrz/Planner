from Domains.Domain import Domain
from Model.Predicate import Predicate
from Problems.Problem import Problem
from Model.State import State


class BlocksWorldProblem(Problem):
    def __init__(self, domain: Domain):
        super().__init__(domain)
        on_3_table = Predicate("On", ["Block3", "table"])
        on_2_3 = Predicate("On", ["Block2", "Block3"])
        on_1_2 = Predicate("On", ["Block1", "Block2"])
        clear_1 = Predicate("Clear", ["Block1"])
        clear_2 = Predicate("Clear", ["Block2"])
        clear_3 = Predicate("Clear", ["Block3"])
        clear_table = Predicate("Clear", ["table"])
        on_2_table = Predicate("On", ["Block2", "table"])
        self.initial_state = State(
            "",
            [
                on_3_table,
                on_2_3,
                on_1_2,
                clear_1,
                clear_table,
            ],
            [],
        )

        clear_table = Predicate("Clear", ["table"])

        on_3_2 = Predicate("On", ["Block3", "Block2"])
        on_1_3 = Predicate("On", ["Block1", "Block3"])

        self.goal_state = State("", [on_2_table,on_3_2, on_1_3, clear_1], [])

        self.initial_state.set_parent_index(-1)
        self.goal_state.set_parent_index(-1)

        '''
        on_1_2 = Predicate("On", ["Block1", "Block2"])
        clear_1 = Predicate("Clear", ["Block1"])
        clear_2 = Predicate("Clear", ["Block2"])
        on_2_table = Predicate("On",["Block2","table"])
        on_1_table = Predicate("On",["Block1","table"])
        on_2_1 = Predicate("On", ["Block2", "Block1"])
        clear_table = Predicate("Clear", ["table"])




        self.initial_state = State("",[on_1_2,on_2_table, clear_1,clear_table],[])
        self.goal_state = State("", [on_1_table,on_2_1,clear_table,clear_2], [])

        self.initial_state.set_parent_index(-1)
        self.goal_state.set_parent_index(-1)

        '''