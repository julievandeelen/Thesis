# fileSpecifyingError = ""
#
# #wd = './Vensim models'
#
# pathToExistingModel = "./Vensim models/model_thesis_V42.vpmx"
# pathToNewModel = "./Vensim models/model_thesis_V42_correct.vpmx"
# newModel = open(pathToNewModel, 'w')
#
# #line = open(fileSpecifyingError).read()
#
# line = 'Annual consumption predator:1.5753521698104183, Annual fish consumption per capita:2.003788373252934e-05, Average sinking time:283.53941021182567, Average weight per adult MF:1.0485103165872589e-06, Average weight per juvinile MF:7.504618410322226e-08, Average weight per juvinile predator:0.4340901946137137, Average weight per predator:0.7506584217427774, C content copepods:0.49779367446369294, Carbon loss at living depth:4.527425790819885, Carbon loss underway:0.1923054755522759, Catchability mauriculus:0.31828938245421906, Catchability myctophidae:0.11816848120812974, Consumption by MF in bodyweight:6.091441797854168, Consumption by zooplankton in bodyweight:2.945898092104578, Costs regular fish:355826288179.9043, Costs status quo mauriculus:222805318040.9694, Costs status quo myctophidae:434271309449.43976, Delay sedimentation:9973.271448760055, Delay weathering:9673.662787806179, Depth euphotic zone:79.41597474014124, Downwelling water:480773379238418.4, Export efficiency:0.9788753028923466, Female fraction:0.4835119446790889, Fishmeal to fish factor:3.599226353832947, Fraction grazed C ending up in surface:0.12495171641362714, Fraction of migrating MF:0.4130439593714394, Fraction spawning mauriculus vs myctophidae:0.720684755939766, Grazing in surface by MF:0.9373168513449649, Growth period mauriculus:0.9951053252149716, Growth period myctophidae:0.6207263936743252, Growth period predator:3.072949215326493, Harvest information delay:3.7575624162479446, Information delay risk perception:3.3715493874398867, Initial capacity mixed:113.74822017954277, Initial juvinile predator weight:4.517469137371032, Initial phytoplankton:1.0734301741694408, Initial predator weight:3.2011967246806967, Initial sediment C:4984.078427805855, Initial surface C:816.2190658959553, Initial weight mauriculus adult:0.11761886580376488, Initial weight mauriculus juvinile:0.26024119084587716, Initial weight myctophidae adult:14.427808524815697, Initial weight myctophidae juvinile:3.622437589352602, Initial zooplankton:2.240839427878593, Life expectancy mauriculus:1.7929029136293848, Life expectancy myctophidae adult:3.9157060850285945, Living depth mauriculus:291.02440372778824, Living depth myctophidae:881.341518966098, Other food sources:1.872469261924634, Percentage discarded fish:0.14122749355356162, Predator life expectancy:11.520315781764335, Residence time deep carbon:2351.3308248067215, Sale price regular fish:3207346769577.83, Share of aquaculture:0.48511264761172596, Share of irreplaceable fishmeal:0.12210921401271517, Spawning fraction:0.19414603032742947, Specialist capacity building time:4.33359621339332, Surface ocean:352037610902907.0, Survived larvea:137.2926958643329, Switch influence CO2 on phytoplankton:2, Switch influence sunlight on phytoplankton:1, Switch population growth:2, Switch price change:2, Switch risk perception biomass:1, Switch risk perception climate:1, Switch technological innovation MF fisheries:1, Total atmospheric volume:4.1428129668072033e+18, Transfer velocity for GtC per year:1.1190396177334603, Turnover time phytoplankton:0.07532133130493486, Upwelling delay surface:6.06414778151165, Vertical migration by other MF:12.030562207387609, ppm conversion for ocean:2.088255946331024;'
#
# # we assume the case specification was copied from the logger
# splitOne = line.split(',')
# variable = {}
# for n in range(len(splitOne) - 1):
#     splitTwo = splitOne[n].split(':')
#     variableElement = splitTwo[0]
#     # Delete the spaces and other rubish on the sides of the variable name
#     variableElement = variableElement.lstrip()
#     variableElement = variableElement.lstrip("'")
#     variableElement = variableElement.rstrip()
#     variableElement = variableElement.rstrip("'")
#     print(variableElement)
#     valueElement = splitTwo[1]
#     valueElement = valueElement.lstrip()
#     valueElement = valueElement.rstrip()
#     variable[variableElement] = valueElement
# print(variable)
#
# # This generates a new (text-formatted) model
# changeNextLine = False
# settedValues = []
# for line in open(pathToExistingModel):
#     if line.find("=") != -1:
#         elements = line.split("=")
#         value = elements[0]
#         value = value.strip()
#         if value in variable:
#             elements[1] = variable.get(value)
#             line = elements[0] + " = " + elements[1]
#             settedValues.append(value)
#
#     newModel.write(line)
# notSet = set(variable.keys()) - set(settedValues)
# print(notSet)

fileSpecifyingError = ""

pathToExistingModel = "./Vensim models/model_thesis_V45_zonderlookup.vpmx"  # zonder lookup proberen
pathToNewModel = "./Vensim models/model_thesis_V45_zonderlookup_correct.vpmx"
newModel = open(pathToNewModel, 'w') #encoding="utf8")

#line = open(fileSpecifyingError).read()

line = 'Annual consumption predator:1.5887090182753214, Annual fish consumption per capita:1.6335875487124872e-05, Average weight per adult MF:1.0624499760355426e-06, Average weight per juvinile MF:5.6909259824055375e-08, C content copepods:0.5307357322580957, Catchability mauriculus:0.35487322844320085, Catchability myctophidae:0.15540056883388303, Consumption by MF in bodyweight:7.197313721923285, Consumption by zooplankton in bodyweight:2.841298066841448, Costs regular fish:338800532381.3223, Costs status quo mauriculus:243809622718.81223, Costs status quo myctophidae:494791174689.5344, Depth euphotic zone:123.8425923744295, Export efficiency:0.986089988523895, Female fraction:0.4679386574403424, Fishmeal to fish factor:3.042131276430073, Fraction spawning mauriculus vs myctophidae:0.7252425291554205, Growth period mauriculus:1.0912468610113872, Growth period myctophidae:0.518878638911861, Harvest information delay:2.794724419619222, Information delay risk perception:6.296311966573586, Initial phytoplankton:0.9256697633439785, Initial zooplankton:2.228764902407217, Life expectancy mauriculus:2.0068050124338273, Life expectancy myctophidae adult:3.9853652755677955, Living depth mauriculus:441.6251397087844, Living depth myctophidae:1030.2096265126997, Other food sources:3.012960697300074, Proposed harvesting quota:9.988961313879315, Sale price regular fish:3275613523204.2666, Share of aquaculture:0.5137166617706581, Share of irreplaceable fishmeal:0.06456927605500139, Spawning fraction:0.19803462497579258, Specialist capacity building time:4.836792640887664, Surface ocean:368316776880691.6, Survived larvea:129.57282599695472, Switch influence CO2 on phytoplankton:1, Switch influence sunlight on phytoplankton:1, Switch population growth:2, Switch price change:2, Switch risk perception biomass:1, Switch risk perception climate:3, Switch technological innovation MF fisheries:2, Total atmospheric volume:4.140328549090479e+18, Transfer velocity for GtC per year:1.1201936813641704, ppm conversion for ocean:2.065215065897742, policy:None'

# 'rainfall : 0.154705633188; adaptation time from non irrigated agriculture : 0.915157119079; salt effect multiplier : 1.11965969891; adaptation time to non irrigated agriculture : 0.48434342934; adaptation time to irrigated agriculture : 0.330990830832; water shortage multiplier : 0.984356102036; delay time salt seepage : 6.0; adaptation time : 6.90258192256; births multiplier : 1.14344734715; diffusion lookup : [(0, 8.0), (10, 8.0), (20, 8.0), (30, 8.0), (40, 7.9999999999999005), (50, 4.0), (60, 9.982194802803703e-14), (70, 1.2455526635140464e-27), (80, 1.5541686655435471e-41), (90, 1.9392517969836692e-55)]; salinity effect multiplier : 1.10500381093; technological developments in irrigation : 0.0117979353255; adaptation time from irrigated agriculture : 1.58060947607; food shortage multiplier : 0.955325345996; deaths multiplier : 0.875605669911; '

# we assume the case specification was copied from the logger
splitOne = line.split(',')
variable = {}
for n in range(len(splitOne) - 1):
    splitTwo = splitOne[n].split(':')
    variableElement = splitTwo[0]
    # Delete the spaces and other rubish on the sides of the variable name
    variableElement = variableElement.lstrip()
    variableElement = variableElement.lstrip("'")
    variableElement = variableElement.rstrip()
    variableElement = variableElement.rstrip("'")
    print(variableElement)
    valueElement = splitTwo[1]
    valueElement = valueElement.lstrip()
    valueElement = valueElement.rstrip()
    variable[variableElement] = valueElement
print(variable)

# This generates a new (text-formatted) model
changeNextLine = False
settedValues = []
for line in open(pathToExistingModel):
    if line.find("=") != -1:
        elements = line.split("=")
        value = elements[0]
        value = value.strip()
        if value in variable:
            elements[1] = variable.get(value)
            line = elements[0] + " = " + elements[1]
            settedValues.append(value)

    newModel.write(line)
newModel.close() # in order to be able to open the model in Vensim
notSet = set(variable.keys()) - set(settedValues)
print(notSet)