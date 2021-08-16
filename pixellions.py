import smartpy as sp

class Pixellions(sp.Contract):
    def __init__(self):
        canvas = 8 * [12 * [0]]
        contract_address = sp.self_address
        base_fee = sp.tez(0.02) 
        self.init(
            pixel = 0,
            color = "",
            deck = sp.utils.matrix(canvas)
        )

    @sp.entry_point
    def colored(self, params):
        sp.verify(self.data.deck[params.i][params.j] > 0)
        sp.verify((params.i >= 0) & (params.i < 8))
        sp.verify((params.j >= 0) & (params.j < 12))
        self.data.deck[params.i][params.j] = params.color


# Tests
if "templates" not in __name__:
    @sp.add_test(name = "Pixellions")
    def test():
        # define a contract
        c1 = Pixellions()

        scenario = sp.test_scenario()
        scenario.h1("Pixellions")
        scenario.h2("A sequence of interactions")
        scenario += c1

        scenario.h2("Message execution")
        c1.colored(i = 5, j = 4, color = 1)

    sp.add_compilation_target("pixellions", Pixellions())
