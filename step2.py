import numpy as np
import functools

from ema_workbench import (Constraint, SequentialEvaluator, TimeSeriesOutcome,
                           RealParameter, ScalarOutcome, CategoricalParameter, ema_logging, MultiprocessingEvaluator)

from ema_workbench.connectors.vensim import VensimModel
from ema_workbench.connectors import vensim

get_10_percentile = functools.partial(np.percentile, q=10)

def get_last_outcome(outcome,time):
    index = np.where(time == 2100) #model runs until 2100
    last_outcome = outcome[index][0]
    return last_outcome

def get_SD(outcome):
    sd=np.std(outcome)
    return sd

def constraint_biomass(biomass):
    index = np.where(time == 2010)  # model runs from 2010 onwards
    initial_biomass = outcome[index][0]
    lowest_allowable= initial_biomass*0.4
    return lambda biomass:min(0, biomass-lowest_allowable)

def lookup_list(time_range):
    list = np.arange(0, time_horizon, 2).tolist()
    return list

class MyVensimModel(VensimModel):

    def run_experiment(self, experiment):
        # 'Look up harvesting quota'
        # f"Proposed harvesting quota {t}", 0, 10) for t in range(45)]
        lookup = []
        for t in range(45):
            value = experiment.pop(f"Proposed harvesting quota {t}")
            lookup.append((2010+2*t, value))
        experiment['Look up harvesting quota'] = lookup

        super(MyVensimModel, self).run_experiment(experiment)

if __name__ == "__main__":
    ema_logging.log_to_stderr(ema_logging.INFO)

    wd = './Vensim models'
    vensimModel = MyVensimModel("simpleModel", wd=wd,
                               model_file='model_thesis_V44.vpmx')
    time_horizon=90
    # tuple_lookup = vensim.set_value('Look up harvesting quota', lookup_list(time_horizon)) #lookup_list() moet functie zijn die lijst met 45 levers returned

    vensimModel.uncertainties = [#structural uncertainties
                                 CategoricalParameter('Switch technological innovation MF fisheries', (1,2) ),#1
                                 CategoricalParameter('Switch price change', (1,2) ),
                                 CategoricalParameter('Switch risk perception climate', (1,2,3) ),
                                 CategoricalParameter('Switch risk perception biomass', (1,2) ),
                                 CategoricalParameter('Switch influence sunlight on phytoplankton', (1,2) ),
                                 CategoricalParameter('Switch influence CO2 on phytoplankton', (1,2) ),
                                 CategoricalParameter('Switch population growth', (1,2,3) ),
                                 #parametric uncertainties
                                 RealParameter("Initial weight myctophidae juvinile", 0.5 , 4),  #1
                                 RealParameter("Initial weight mauriculus juvinile", 0.1 , 0.3),  #0.2
                                 RealParameter("Initial weight myctophidae adult", 3, 18),  #9
                                 RealParameter("Initial weight mauriculus adult", 0.1, 0.3),  #0.2
                                 RealParameter("Initial juvinile predator weight", 4, 12),  #8
                                 RealParameter("Initial predator weight", 1, 4),  #2
                                 RealParameter("Initial zooplankton", 2, 8),  #4
                                 RealParameter("Initial phytoplankton", 0.8, 1.2),  #1
                                 RealParameter("Initial surface C", 450,900),  #600
                                 RealParameter("Initial sediment C", 3000, 5000),  #3390
                                 RealParameter("Initial capacity mixed",50 , 150),  #100
                                 RealParameter("Surface ocean", 343000000000000, 383000000000000),  # 3.63*10^14
                                 RealParameter("Total atmospheric volume", 3790000000000000000, 4290000000000000000),  # 3.99*10^18
                                 RealParameter("Fraction grazed C ending up in surface", 0.05, 0.2),  # 0.1
                                 RealParameter("Living depth myctophidae", 750, 1050),  # 950
                                 RealParameter("Living depth mauriculus", 250, 450),  # 350
                                 RealParameter("Carbon loss underway", 0.05, 0.3),  # 0.1
                                 RealParameter("Carbon loss at living depth", 0.2, 5),  # 1
                                 RealParameter("Average sinking time", 200, 400),  # 300
                                 RealParameter("Delay sedimentation", 9000, 11000),  # 10000
                                 RealParameter("Delay weathering", 9000, 11000),  # 10000
                                 RealParameter("Growth period predator", 2, 4),  # 3
                                 RealParameter("Average weight per juvinile predator", 0.1, 0.5),  # 0.3
                                 RealParameter("Average weight per predator", 0.2, 0.8),  # 0.4
                                 RealParameter("Other food sources", 0.5, 5),  # 2
                                 RealParameter("Turnover time phytoplankton", 0.06, 0.09),  # 0.07692
                                 RealParameter("Consumption by zooplankton in bodyweight", 2.5, 3.5),  # 3
                                 RealParameter("Harvest information delay", 2, 4),  # 3
                                 RealParameter("Costs regular fish", 309000000000, 369000000000),  # 3.39e+11
                                 RealParameter("Sale price regular fish", 2900000000000, 3300000000000),  # 3.1e+12
                                 RealParameter("Costs status quo myctophidae", 400000000000, 500000000000),  # 450*10^9
                                 RealParameter("Costs status quo mauriculus", 200000000000, 250000000000),  # 225*10^9
                                 RealParameter("Information delay risk perception", 3, 7),  # 5
                                 RealParameter("ppm conversion for ocean", 2, 2.2),  # 2.1
                                 RealParameter("Downwelling water", 450000000000000, 550000000000000),  # 5*10^14
                                 RealParameter("Residence time deep carbon", 2200, 2400),  # 2300
                                 RealParameter("Upwelling delay surface", 5.5, 6.5),  # 6
                                 RealParameter("Fraction grazed C ending up in surface", 0.05, 0.15),  # 0.1
                                 RealParameter("Vertical migration by other MF", 10, 14),  # 12
                                 RealParameter("Share of aquaculture", 0.4, 0.6),  # 0.5
                                 RealParameter("Share of irreplaceable fishmeal", 0.05, 0.15),  # 0.1
                                 RealParameter("Annual fish consumption per capita", 0.000013, 0.000021),  # 1.7*10^-5
                                 RealParameter("Percentage discarded fish", 0.05, 0.2),
                                 RealParameter("Specialist capacity building time", 4, 6),  # 5
                                 RealParameter("Catchability myctophidae", 0.1, 0.18),  # 0.14
                                 RealParameter("Catchability mauriculus", 0.18, 0.38),  # 0.28
                                 RealParameter("Fraction of migrating MF", 0.27, 0.47),  # 0.37
                                 RealParameter("Grazing in surface by MF", 0.9, 1),  # 1
                                 RealParameter("C content copepods", 0.4, 0.6),  # 0.51
                                 RealParameter("Depth euphotic zone", 75, 125),  # 100
                                 RealParameter("Total atmospheric volume", 3790000000000000000, 4190000000000000000),  # 3.99*10^18
                                 RealParameter("Export efficiency", 0.95, 0.99),  # 0.97
                                 RealParameter("Transfer velocity for GtC per year", 1.11169, 1.13169),  # 1.12169
                                 RealParameter("Average weight per adult MF", 0.0000008, 0.0000012),  # 1*10^-6
                                 RealParameter("Average weight per juvinile MF", 0.00000005, 0.00000008),  # 0.07*10^-6
                                 RealParameter("Life expectancy myctophidae adult", 3.5, 4.5),  # 4
                                 RealParameter("Life expectancy mauriculus", 1.5, 2.5),  # 2
                                 RealParameter("Growth period myctophidae", 0.483, 0.683),  # 0.583
                                 RealParameter("Growth period mauriculus", 0.8, 1.2),  # 1
                                 RealParameter("Consumption by MF in bodyweight", 6, 8),  # 7
                                 RealParameter("Annual consumption predator", 1.5, 1.7),  # 1.6
                                 RealParameter("Predator life expectancy", 8, 12),  # 10
                                 RealParameter("Survived larvea", 127, 167),  # 147
                                 RealParameter("Spawning fraction", 0.16, 0.2),  # 0.18
                                 RealParameter("Female fraction", 0.450, 0.550),  # 0.515
                                 RealParameter("Fraction spawning mauriculus vs myctophidae", 0.65, 0.85),  # 0.75
                                 RealParameter("Fishmeal to fish factor", 3, 5)  # 4
                                 ]

    vensimModel.levers = [RealParameter(f"Proposed harvesting quota {t}", 0, 10) for t in range(45)]#veranderen 'Look up harvesting quota'
                                #[RealParameter(str(i), 0, 30)  for i in range(time_horizon)]

    vensimModel.outcomes = [TimeSeriesOutcome('Food provision by MF'),
                            TimeSeriesOutcome('Total vertical migration'),
                            TimeSeriesOutcome('Atmosphere'),
                            TimeSeriesOutcome('Biomass MF')]

    # vensimModel.outcomes = [ScalarOutcome('Average food provision by MF', variable_name='Food provision by MF', kind=ScalarOutcome.MAXIMIZE #namen veranderen naar wat de uitkomsten echt zijn (mean etc)
    #                                 , function=np.mean),
    #                         ScalarOutcome('Average vertical migration', variable_name='Total vertical migration', kind=ScalarOutcome.MAXIMIZE
    #                                , function=np.mean),
    #                         ScalarOutcome('Biomass MF 10th percentile', variable_name='Biomass MF', kind=ScalarOutcome.MAXIMIZE
    #                                , function=get_10_percentile),
    #                         ScalarOutcome('Final atmospheric C level', variable_name=['Atmosphere', 'TIME'], kind=ScalarOutcome.MINIMIZE
    #                                       , function=get_last_outcome)
    #                         ]

    #vensimModel.constraints = [Constraint("Average biomass MF", outcome_names="Average biomass MF",
                          #function=constraint_biomass)]

    with SequentialEvaluator(vensimModel) as evaluator:
        evaluator.perform_experiments(10, 10)
        # results_step2 = evaluator.optimize(nfe=5e2, searchover='levers',
        #                               epsilons=[0.001, ] * len(vensimModel.outcomes))


    results_step2.to_excel('./Data/results_step2_4.xlsx')





