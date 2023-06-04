from __future__ import annotations

from Model.State import State
from Model.Predicate import Predicate


class Action:
    def __init__(
            self,
            action_name: str,
            positive_preconditions: list[Predicate] | set[Predicate],
            negative_preconditions: list[Predicate] | set[Predicate],
            add_list: list[Predicate] | set[Predicate],
            delete_list: list[Predicate] | set[Predicate],
    ):

        self.action_name = action_name
        self.positive_preconditions = set(positive_preconditions)
        self.negative_preconditions = set(negative_preconditions)
        self.add_list = set(add_list)
        self.delete_list = set(delete_list)

    def get_action_name(self) -> str:
        return self.action_name

    def is_unified(self, state: State) -> bool:

        return (
                   not self.add_list.isdisjoint(state.get_positive_literals())
               ) or (not self.delete_list.isdisjoint(state.get_negative_literals()))

    def is_conflicting(self, state: State) -> bool:

        return (
                   not self.add_list.isdisjoint(state.get_negative_literals())
               ) or (not self.delete_list.isdisjoint(state.get_positive_literals()))

    def is_relevant(self, state: State) -> bool:

        return self.is_unified(state) and not self.is_conflicting(state)

    def is_applicable(self, state: State) -> bool:

        return self.positive_preconditions.issubset(state.get_positive_literals()) and \
               self.negative_preconditions.isdisjoint(state.get_positive_literals())

    def regress(self, state: State) -> State:

        result_positive_literals = (
                state.get_positive_literals() - self.add_list
        ).union(self.positive_preconditions)

        result_negative_literals = (
                state.get_negative_literals() - self.delete_list
        ).union(self.negative_preconditions)

        result = State(
            self.action_name, result_positive_literals, result_negative_literals
        )
        return result

    def progress(self, state: State) -> State:

        result_positive_literals = state.get_positive_literals().union(self.add_list) - self.delete_list
        result_negative_literals = state.get_negative_literals().union(self.delete_list) - self.add_list

        result = State(
            self.action_name, result_positive_literals, result_negative_literals
        )
        return result


    def progress_without_deletelist(self, state: State) -> State:

        result_positive_literals = state.get_positive_literals().union(self.add_list)
        result_negative_literals = state.get_negative_literals() - self.add_list

        result = State(
            self.action_name, result_positive_literals, result_negative_literals
        )
        return result




    # def progress(self, state: State) -> State:
    #     """
    #     Progresses the given state with the action effects.
    #
    #     Parameters:
    #     - state (State): the state to progress.
    #
    #     Returns:
    #     - The new state after progressing with the action effects.
    #     """
    #     result_positive_literals = state.get_positive_literals().union(self.add_list)
    #     result_negative_literals = state.get_negative_literals() - self.add_list
    #
    #     result = State(
    #         self.action_name, result_positive_literals, result_negative_literals
    #     )
    #     return result


    def __str__(self) -> str:
        return self.action_name
