from queue import PriorityQueue
from queue import Queue

from Planners.Planner import Planner


class ForwardPlanner(Planner):
    def __init__(self, problem):
        super().__init__(problem)

    def search(self):
        total_state_index = 0
        result = []
        frontier = PriorityQueue()
        visited = set()
        all_states = []

        if self.goal_test(self.problem.get_initial_state()):
            return result
        value = self.ignore_delete_list_heuristic(self.problem.get_initial_state())
        frontier.put((value, total_state_index))

        visited.add(self.problem.get_initial_state())
        all_states.append(self.problem.get_initial_state())

        while not frontier.empty():
            current_state_index = frontier.get()[1]
            current_state = all_states[current_state_index]

            successor_states = self.successor(current_state, current_state_index)

            for successor_state in successor_states:
                if self.goal_test(successor_state):
                    result = self.build_solution(successor_state, all_states)
                    return result

                if successor_state not in visited:
                    total_state_index += 1
                    value = self.ignore_delete_list_heuristic(successor_state)
                    frontier.put((value, total_state_index))

                    visited.add(successor_state)
                    all_states.append(successor_state)

        return result

    def ignore_delete_list_heuristic(self, state):
        total_state_index = 0
        result = []
        frontier = Queue()
        visited = set()
        all_states = []

        if self.goal_test(state):

            return len(result)

        frontier.put(total_state_index)
        visited.add(state)
        all_states.append(state)

        while not frontier.empty():
            current_state_index = frontier.get()
            current_state = all_states[current_state_index]

            successor_states = self.successor_without_deletelist(current_state, current_state_index)

            for successor_state in successor_states:
                if self.goal_test(successor_state):
                    result = self.build_solution(successor_state, all_states, state.get_parent_index())
                    print(result)
                    return len(result)

                if successor_state not in visited:
                    total_state_index += 1
                    frontier.put(total_state_index)
                    visited.add(successor_state)
                    all_states.append(successor_state)

        return 10000

    def successor(self, state, current_state_index):
        result = []
        actions = self.problem.get_domain().get_actions()
        for action in actions:
            if action.is_applicable(state):
                neigbour = action.progress(state)
                neigbour.set_parent_index(current_state_index)
                result.append(neigbour)

        return result

    def successor_without_deletelist(self, state, current_state_index):
        result = []
        actions = self.problem.get_domain().get_actions()
        for action in actions:
            if action.is_applicable(state):
                neigbour = action.progress_without_deletelist(state)
                neigbour.set_parent_index(current_state_index)
                result.append(neigbour)

        return result

    def goal_test(self, state):
        goal_state = self.problem.get_goal_state()

        return goal_state.get_positive_literals().issubset(state.get_positive_literals()) and \
               state.get_negative_literals().isdisjoint(goal_state.get_positive_literals())

    def build_solution(self, state, all_states, index=-1):
        result = []

        while state.get_parent_index() != index:
            result.append(state.get_action_name())
            state = all_states[state.get_parent_index()]

        result.reverse()
        return result
