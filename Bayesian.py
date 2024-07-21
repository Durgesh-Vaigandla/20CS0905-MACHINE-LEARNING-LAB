import pgmpy.models as models
import pgmpy.factors.discrete as factors

# Create a Bayesian Network object
model = models.BayesianModel([('Rain', 'Grass wet'), ('Sprinkler', 'Grass wet')])

# Define Conditional Probability Distributions (CPDs)
cpd_rain = factors.TabularCPD('Rain', 2, [[0.7], [0.3]])  # 0: No rain, 1: Rain
cpd_sprinkler = factors.TabularCPD('Sprinkler', 2, [[0.6], [0.4]], evidence=['Rain'], evidence_card=[2])
cpd_grass_wet = factors.TabularCPD('Grass wet', 2, 
                                    [[1, 0.2, 0.1, 0.01],  # No rain, no sprinkler
                                     [0, 0.8, 0.9, 0.99]], # Rain or sprinkler
                                    evidence=['Rain', 'Sprinkler'], evidence_card=[2, 2])

# Add CPDs to the model
model.add_cpds(cpd_rain, cpd_sprinkler, cpd_grass_wet)

# Check if the model is valid
model.check_model()

# Perform inference
from pgmpy.inference import VariableElimination
infer = VariableElimination(model)

# Calculate the probability of the grass being wet given that it rained
result = infer.query(variables=['Grass wet'], evidence={'Rain': 1})
print(result)

#output
"""
+--------------+----------------+
| Grass Wet    |   phi(Grass Wet) |
+==============+================+
| Grass Wet(0) |         0.1    |
+--------------+----------------+
| Grass Wet(1) |         0.9    |
+--------------+----------------+
+--------------+----------------+
| Grass Wet    |   phi(Grass Wet) |
+==============+================+
| Grass Wet(0) |         0.6    |
+--------------+----------------+
| Grass Wet(1) |         0.4    |
+--------------+----------------+
+--------+-------------+
| Rain   |   phi(Rain) |
+========+=============+
| Rain(0)|      0.357  |
+--------+-------------+
| Rain(1)|      0.643  |
+--------+-------------+

"""