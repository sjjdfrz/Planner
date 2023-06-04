from Planners.ForwardPlanner import ForwardPlanner
from Planners.BackwardPlanner import BackwardPlanner
from Domains.BlocksWorldDomain import BlocksWorldDomain
from Domains.TireDomain import TireDomain
from Problems.BlocksWorldProblem import BlocksWorldProblem
from Problems.TireProblem import TireProblem

# back = BackwardPlanner(TireProblem(TireDomain("Tire Domain")))
# print(back.search())
forward = ForwardPlanner(TireProblem(TireDomain("Tire Domain")))
print(forward.search())