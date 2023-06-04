from Domains.Domain import Domain
from Model.Action import Action
from Model.Predicate import Predicate


class BlocksWorldDomain(Domain):
    def __init__(self, number_of_blocks: int):
        super().__init__("Block Domain")
        self.number_of_blocks = number_of_blocks
        self.object_types = {
            "blocks": [],
        }
        self.define_objects()
        self.define_actions()

    def define_objects(self):
        for i in range(1, self.number_of_blocks + 1):
            block_string = f"Block{i}"
            self.object_types["blocks"].append(block_string)

    def define_actions(self):
        for b in self.object_types["blocks"]:
            for x in self.object_types["blocks"]:
                if b != x:
                    for y in self.object_types["blocks"]:
                        if y != x and y != b:
                            self.add_move_action(b, x, y)
                    self.add_move_to_table(b, x)
        # add move from tabel
        for b in self.object_types["blocks"]:
            for x in self.object_types["blocks"]:
                if b != x:
                    self.add_move_action(b, "table", x)
        # for a in self.actions:
        #     print(a)

    def add_move_action(self, b, x, y):
        move_action_name = f"Move({b},{x},{y})"
        on_b_x = Predicate("On", [b, x])
        clear_block_b = Predicate("Clear", [b])
        clear_block_y = Predicate("Clear", [y])

        on_b_y = Predicate("On", [b, y])
        clear_x = Predicate("Clear", [x])

        move_action = Action(
            move_action_name,
            [on_b_x, clear_block_b, clear_block_y],
            [],
            [on_b_y, clear_x],
            [on_b_x, clear_block_y],
        )
        self.actions.append(move_action)

    def add_move_to_table(self, b, x):
        move_action_name = f"MoveToTable({b},{x})"
        on_b_x = Predicate("On", [b, x])
        clear_block_b = Predicate("Clear", [b])

        on_b_table = Predicate("On", [b, "table"])
        clear_x = Predicate("Clear", [x])

        move_action = Action(
            move_action_name,
            [on_b_x, clear_block_b],
            [],
            [on_b_table, clear_x],
            [on_b_x],
        )
        self.actions.append(move_action)
