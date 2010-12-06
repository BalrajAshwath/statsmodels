"""
Results for ARMA models.  Produced by gretl.
"""
import os
from numpy import genfromtxt

current_path = os.path.dirname(os.path.abspath(__file__))
yhat_mle = genfromtxt(current_path+"/yhat_exact_nc.csv", delimiter=",", skip_header = 1, dtype=float)

yhat_css = genfromtxt(current_path+"/yhat_css_nc.csv", delimiter=",", skip_header = 1, dtype=float)

yhatc_mle = genfromtxt(current_path+"/yhat_exact_c.csv", delimiter=",", skip_header = 1, dtype=float)

yhatc_css = genfromtxt(current_path+"/yhat_css_c.csv", delimiter=",", skip_header = 1, dtype=float)

resids_mle = genfromtxt(current_path+"/resids_exact_nc.csv", delimiter=",", skip_header = 1, dtype=float)

resids_css = genfromtxt(current_path+"/resids_css_nc.csv", delimiter=",", skip_header = 1, dtype=float)

residsc_mle = genfromtxt(current_path+"/resids_exact_c.csv", delimiter=",", skip_header = 1, dtype=float)

residsc_css = genfromtxt(current_path+"/resids_css_c.csv", delimiter=",", skip_header = 1, dtype=float)


class Y_arma11(object):
    def __init__(self, method="mle"):
        if method == "mle":
            self.params = [0.788452102751, 0.381793815167]
            self.aic = 714.489820273473
            self.bic = 725.054203027060
            self.arroots = 1.2683 + 0j
            self.maroots = -2.6192 + 0j
            self.bse = [0.042075906061, 0.060925105865]
            self.hqic = 718.741675179309
            self.llf = -354.244910136737
            self.resid = resids_mle[:,0]
            self.fittedvalues = yhat_mle[:,0]
            self.pvalues = [2.39e-78, 3.69e-10]
            self.tvalues = [18.74, 6.267]
            self.sigma2 = 0.994743350844 ** 2
            self.cov_params = [[   0.0017704,   -0.0010612],
                                  [-0.0010612, 0.0037119 ]]
        elif method =="css":
            self.params = [0.791515576984, 0.383078056824]
            self.aic = 710.994047176570
            self.bic = 721.546405865964
            self.arroots = [ 1.2634 + 0.0000j]
            self.maroots = [-2.6104 +0.0000j]
            self.bse = [0.042369318062, 0.065703859674]
            self.cov_params = [
[   0.0017952,   -0.0010996],
[  -0.0010996,    0.0043170]]
            self.hqic = 715.241545108550
            self.llf = -352.497023588285
            self.resid = resids_css[1:,0]
            self.fittedvalues = yhat_css[:,0]
            self.pvalues = [ 7.02e-78,  5.53e-09]
            self.tvalues = [18.68,  5.830]
            self.sigma2 = 0.996717562780**2


class Y_arma14(object):
    def __init__(self, method="mle"):
        if method == "mle":
            self.params = [0.763798613302, 0.306453049063, -0.835653786888,
                            0.151382611965, 0.421169903784]
            self.aic = 736.001094752429
            self.bic = 757.129860259603
            self.arroots = 1.3092 + 0j
            self.maroots = [-1.2189 + 0.1310j, -1.2189 -0.1310j,
                            1.0392 -0.7070j, 1.0392  + 0.7070j]
            self.bse = [0.064888368113, 0.078031359430, 0.076246826219,
                        0.069267771804, 0.071567389557]
            self.cov_params = [[   0.0042105, -0.0031074, -0.0027947,
                    -0.00027766, -0.00037373 ],
[  -0.0031074,    0.0060889,    0.0033958,   -0.0026825,  -0.00062289 ],
[  -0.0027947,    0.0033958,    0.0058136,  -0.00063747,   -0.0028984 ],
[ -0.00027766,   -0.0026825,  -0.00063747,    0.0047980,    0.0026998 ],
[ -0.00037373,  -0.00062289,   -0.0028984,    0.0026998,    0.0051219 ]]
            self.hqic = 744.504804564101
            self.llf = -362.000547376215
            self.resid = resids_mle[1:,1]
            self.fittedvalues = yhat_mle[:,1]
            self.pvalues = [5.51e-32, 8.59e-05,  5.96e-28, 0.0289, 3.98e-09]
            self.tvalues = [11.77, 3.927, -10.96, 2.185, 5.885]
            self.sigma2 = 1.022607088673 ** 2
            self.bse = [0.064888368113, 0.078031359430, 0.076246826219,
                        0.069267771804, 0.071567389557]
        elif method =="css":
            self.params = [0.772072791055, 0.283961556581, -0.834797380642,
                     0.157773469382, 0.431616426021]
            self.aic = 734.294057687460
            self.bic = 755.398775066249
            self.arroots = [1.2952  +0.0000j]
            self.maroots = [1.0280    -0.6987j, 1.0280  +0.6987j,
                    -1.2108    -0.1835j,  -1.2108    +0.1835j]
            self.bse = [0.083423762397, 0.086852297123, 0.093883465705,
                    0.068170451942, 0.065938183073]
            self.cov_params = [
[   0.0069595,   -0.0053083,   -0.0054522,   -0.0016324,  -0.00099984],
[  -0.0053083,    0.0075433,    0.0052442,  -0.00071680,    0.0010335],
[  -0.0054522,    0.0052442,    0.0088141,    0.0019754,   -0.0018231],
[  -0.0016324,  -0.00071680,    0.0019754,    0.0046472,    0.0011853],
[ -0.00099984,    0.0010335,   -0.0018231,    0.0011853,    0.0043478]]
            self.hqic = 742.789053551421
            self.llf = -361.147028843730
            self.resid = resids_css[1:,1]
            self.fittedvalues = yhat_css[:,1]
            self.pvalues = [2.15e-20,   0.0011,  6.01e-19,  0.0206,  5.92e-11]
            self.tvalues = [9.255,   3.269, -8.892,   2.314,   6.546]
            self.sigma2 = 1.031950951582**2

class Y_arma41(object):
    def __init__(self, method="mle"):
        if method == "mle":
            self.params = [0.859167822255, -0.445990454620, -0.094364739597,
                        0.633504596270, 0.039251240870]
            self.aic = 680.801215465509
            self.bic = 701.929980972682
            self.arroots = [1.0209, 0.2966+0.9835j , 0.2966    -0.9835j ,
                            -1.4652  +   0.0000j ]
            self.maroots = [-25.4769 + 0.0000]
            self.bse = [0.097363938243, 0.136020728785, 0.128467873077,
                        0.081059611396, 0.138536155409]
            self.cov_params = [
[   0.0094797,    -0.012908,     0.011870,   -0.0073247,    -0.011669],
[   -0.012908,     0.018502,    -0.017103,     0.010456,     0.015892],
[    0.011870,    -0.017103,     0.016504,    -0.010091,    -0.014626],
[  -0.0073247,     0.010456,    -0.010091,    0.0065707,    0.0089767],
[   -0.011669,     0.015892,    -0.014626,    0.0089767,     0.019192]]
            self.hqic = 689.304925277181
            self.llf = -334.400607732754
            self.resid = resids_mle[4:,2]
            self.fittedvalues = yhat_mle[:,2]
            self.pvalues = [1.10e-18, 0.0010, 0.4626, 5.48e-15, 0.7769]
            self.tvalues = [8.824, -3.279, -.7345, 7.815, .2833]
            self.sigma2 = 0.911409665692 ** 2
        elif method =="css":
            self.params = [0.868370308475, -0.459433478113, -0.086098063077,
                    0.635050245511, 0.033645204508]
            self.aic = 666.171731561927
            self.bic = 687.203720777521
            self.arroots = [1.0184 +0.0000j, 0.2960  -0.9803j, 0.2960 +0.9803j,
                    -1.4747    +0.0000j]
            self.maroots = [-29.7219 +0.0000j]
            self.bse = [0.077822066628, 0.112199961491, 0.104986211369,
                    0.068394652456, 0.113996438269]
            self.cov_params = [
[   0.0060563,   -0.0083712,    0.0076270,   -0.0047067,   -0.0070610],
[  -0.0083712,     0.012589,    -0.011391,    0.0069576,    0.0098601],
[   0.0076270,    -0.011391,     0.011022,   -0.0067771,   -0.0089971],
[  -0.0047067,    0.0069576,   -0.0067771,    0.0046778,    0.0054205],
[  -0.0070610,    0.0098601,   -0.0089971,    0.0054205,     0.012995]
                    ]
            self.hqic = 674.640335476392
            self.llf = -327.085865780964
            self.resid = resids_css[4:,2]
            self.fittedvalues = yhat_css[:,2]
            self.pvalues = [6.51e-29, 4.23e-05, 0.4122, 1.62e-20, 0.7679]
            self.tvalues = [11.16, -4.095, -0.8201,    9.285,    0.2951]
            self.sigma2 = 0.914551777765**2

class Y_arma22(object):
    def __init__(self, method="mle"):
        if method == "mle":
            self.params = [0.810898877154, -0.535753742985, 0.101765385197,
                        -0.691891368356]
            self.aic = 756.286535543453
            self.bic = 773.893840132765
            self.arroots = [ 0.7568    -1.1375j, 0.7568    +1.1375j]
            self.maroots = [-1.1309, 1.2780]
            self.bse = [0.065073834100, 0.060522519771,  0.065569474599,
                    0.071275323591]
            self.cov_params = [
[   0.0042346,   -0.0012416,   -0.0024319,   -0.0012756],
[  -0.0012416,    0.0036630,  -0.00022460,   -0.0019999],
[  -0.0024319,  -0.00022460,    0.0042994,    0.0017842],
[  -0.0012756,   -0.0019999,    0.0017842,    0.0050802]]
            self.hqic = 763.372960386513
            self.llf = -373.143267771727
            self.resid = resids_mle[2:,3]
            self.fittedvalues = yhat_mle[:,3]
            self.pvalues = [1.22e-35 , 8.59e-19, 0.1207, 2.81e-22]
            self.tvalues = [12.46, -8.852, 1.552, -9.707]
            self.sigma2 = 1.069529754715**2
        elif method =="css":
            self.params = [0.811172493623, -0.538952207139, 0.108020549805,
                    -0.697398037845]
            self.aic = 749.652327535412
            self.bic = 767.219471266237
            self.arroots = [ 0.7525    -1.1354j,   0.7525    +1.1354j]
            self.maroots = [-1.1225     +0.0000j,    1.2774     +0.0000j]
            self.bse = [0.063356402845, 0.064719801680, 0.058293106832,
                    0.061453528114]
            self.cov_params = [
[   0.0040140,   -0.0016670,   -0.0019069,   -0.0011369],
[  -0.0016670,    0.0041887,  -0.00019356,   -0.0014322],
[  -0.0019069,  -0.00019356,    0.0033981,    0.0020063],
[  -0.0011369,   -0.0014322,    0.0020063,    0.0037765]]
            self.hqic = 756.724194601530
            self.llf = -369.826163767706
            self.resid = resids_css[2:,3]
            self.fittedvalues = yhat_css[:,3]
            self.pvalues = [1.57e-37,  8.26e-17,  0.0639,   7.55e-30]
            self.tvalues = [ 12.80,  -8.327,  1.853,  -11.35]
            self.sigma2 = 1.074973483083**2

class Y_arma50(object):
    def __init__(self, method="mle"):
        if method == "mle":
            self.params = [0.726892679311, -0.312619864536, 0.323740181610,
                    0.226499145083, -0.089562902305]
            self.aic = 691.422630427314
            self.bic = 712.551395934487
            self.arroots = [1.0772  +0.0000j, -1.9764 +0.0000j,
                    0.0087 -1.2400j, 0.0087 + 1.2400j, 3.4107 + 0.0000j]
            self.maroots = None #TODO: empty array?
            self.bse = [0.062942787895, 0.076539691571, 0.076608230545,
                    0.077330717503, 0.063499540628]
            self.cov_params = [
[   0.0039618,   -0.0028252,    0.0013351,   -0.0013901,  -0.00066624],
[  -0.0028252,    0.0058583,   -0.0040200,    0.0026059,   -0.0014275],
[   0.0013351,   -0.0040200,    0.0058688,   -0.0041018,    0.0013917],
[  -0.0013901,    0.0026059,   -0.0041018,    0.0059800,   -0.0028959],
[ -0.00066624,   -0.0014275,    0.0013917,   -0.0028959,    0.0040322]]
            self.hqic = 699.926340238986
            self.llf = -339.711315213657
            self.resid = resids_mle[5:,4]
            self.fittedvalues = yhat_mle[:,4]
            self.pvalues = [7.51e-31, 4.42e-05, 2.38e-05, 0.0034, 0.1584]
            self.tvalues = [11.55, -4.084, 4.226, 2.929, -1.410]
            self.sigma2 = 0.938374940397 ** 2
        elif method =="css":
            self.params = [0.725706505843, -0.305501865989, 0.320719417706,
                    0.226552951649, -0.089852608091                    ]
            self.aic = 674.817286564674
            self.bic = 692.323577617397
            self.arroots = [1.0755    +0.0000j, 1.9686  +0.0000j, 0.0075
                    -1.2434j, 0.0075    +1.2434j, 3.3994    +0.0000j]
            self.maroots = None
            self.bse = [0.064344956583, 0.078060866211, 0.077980166982,
                    0.078390791831, 0.064384559496]
            self.cov_params = [
[   0.0041403,   -0.0029335,    0.0013775,   -0.0014298,  -0.00068813],
[  -0.0029335,    0.0060935,   -0.0041786,    0.0026980,   -0.0014765],
[   0.0013775,   -0.0041786,    0.0060809,   -0.0042177,    0.0014572],
[  -0.0014298,    0.0026980,   -0.0042177,    0.0061451,   -0.0029853],
[ -0.00068813,   -0.0014765,    0.0014572,   -0.0029853,    0.0041454]]
            self.hqic = 681.867054880965
            self.llf = -332.408643282337
            self.resid = resids_css[5:,4]
            self.fittedvalues = yhat_css[:,4]
            self.pvalues = [1.68e-29, 9.09e-05, 3.91e-05, 0.0039, 0.1628]
            self.tvalues = [11.28, -3.914, 4.113, 2.890, -1.396]
            self.sigma2 = 0.949462810435**2

class Y_arma02(object):
    def __init__(self, method="mle"):
        if method == "mle":
            self.params = [0.169096401142, -0.683713393265]
            self.aic = 775.017701544762
            self.bic = 785.582084298349
            self.arroots = [-1.0920 + 0j]
            self.maroots = [1.3393 + 0j]
            self.bse = [0.049254112414, 0.050541821979]
            self.cov_params = [[0.0024260,   0.00078704], [0.00078704,
                            0.0025545]]
            self.hqic = 779.269556450598
            self.llf = -384.508850772381
            self.resid = resids_mle[:,5]
            self.fittedvalues = yhat_mle[:,5]
            self.pvalues = [.0006, 1.07e-41]
            self.tvalues = [3.433, -13.53]
            self.sigma2 = 1.122887152869 ** 2
        elif method =="css":
            self.params = [0.175605240783, -0.688421349504]
            self.aic = 773.725350463014
            self.bic = 784.289733216601
            self.arroots = None
            self.maroots = [-1.0844 + 0.j, 1.3395 +0.j]
            self.bse = [0.044465497496, 0.045000813836]
            self.cov_params = [
[   0.0019772,   0.00090016],
[  0.00090016,    0.0020251]]
            self.hqic = 777.977205368850
            self.llf = -383.862675231507
            self.resid = resids_css[:,5]
            self.fittedvalues = yhat_css[:,5]
            self.pvalues = [7.84e-05, 7.89e-53]
            self.tvalues = [3.949, -15.30]
            self.sigma2 = 1.123571177436**2

class Y_arma11c(object):
    def __init__(self, method="mle"):
        if method == "mle":
            self.params = [4.856475759430, 0.664363281011, 0.407547531124]
            self.aic = 737.922644877973
            self.bic = 752.008488549422
            self.arroots = [1.5052 + 0j]
            self.maroots = [-2.4537 + 0j]
            self.bse = [0.273164176960, 0.055495689209, 0.068249092654]
            self.cov_params = [
[    0.074619,  -0.00012834,   1.5413e-05],
[ -0.00012834,    0.0030798,   -0.0020242],
[  1.5413e-05,   -0.0020242,    0.0046579]]
            self.hqic = 743.591784752421
            self.llf = -364.961322438987
            self.resid = residsc_mle[:,0]
            self.fittedvalues = yhatc_mle[:,0]
            self.pvalues = [1.04e-70, 5.02e-33, 2.35e-9]
            self.tvalues = [17.78, 11.97, 5.971]
            self.sigma2 = 1.039168068701 ** 2
        elif method =="css":
#            self.params = [1.625462134333, 0.666386002049, 0.409512270580]
#NOTE: gretl gives a bad intercept, x-12-arima and R agree with us
#compare to gretl with x-12
            self.params = [4.872477127267, 0.666395534262, 0.409517026658]
            self.aic = 734.613526514951
            self.bic = 748.683338100810
            self.arroots = [1.5006  +0.0000j]
            self.maroots = [-2.4419 +0.0000]
#            self.bse = [0.294788633992, 0.057503298669, 0.063059352497]
            self.bse = [ 0.2777238133284, 0.0557583459688, 0.0681432545482]
#NOTE: from R, compare to gretl x-12
#            self.cov_params = [
#[    0.086900,    -0.016074,     0.010536],
#[   -0.016074,    0.0033066,   -0.0021977],
#[    0.010536,   -0.0021977,    0.0039765]
#                    ]
            self.cov_params = [
[7.71305164897e-02,  5.65375305967e-06, 1.29481824075e-06 ],
[5.65375305967e-06,  3.10899314518e-03, -2.02754322743e-03],
[1.29481824075e-06, -2.02754322743e-03,  4.64350314042e-03 ]
                    ]
            self.hqic = 740.276857090925
            self.llf = -363.306763257476
            self.resid = residsc_css[1:,0]
            self.fittedvalues = yhatc_css[1:,0]
            self.pvalues = [ 3.51e-08, 4.70e-31, 8.35e-11]
            self.tvalues = [5.514, 11.59,  6.494]
            self.sigma2 = 1.040940645447**2


class Y_arma14c(object):
    def __init__(self, method="mle"):
        if method == "mle":
            self.params = [4.773779823083, 0.591149657917, 0.322267595204,
                    -0.702933089342, 0.116129490967, 0.323009574097]
            self.aic = 720.814886758937
            self.bic = 745.465113183973
            self.arroots = [ 1.6916 +0.0000j]
            self.maroots = [1.1071  -0.7821j, 1.1071  +0.7821j,
                    -1.2868  -0.1705j,-1.2868 +0.1705j] # had to change order?
            self.bse = [0.160891073193, 0.151756542096, 0.152996852330,
                        0.140231020145, 0.064663675882, 0.065045468010]
            self.cov_params = [
[0.025886, 0.00026606,  -0.00020969,  -0.00021435,   4.2558e-05,   5.2904e-05],
[0.00026606,  0.023030,   -0.021269,  -0.018787,    0.0015423,    0.0011363],
[-0.00020969, -0.021269,   0.023408,   0.018469,   -0.0035048,   -0.0010750],
[-0.00021435, -0.018787,   0.018469,   0.019665,  -0.00085717,   -0.0033840],
[4.2558e-05, 0.0015423,  -0.0035048,  -0.00085717,    0.0041814,    0.0014543],
[5.2904e-05, 0.0011363,   -0.0010750,   -0.0033840,    0.0014543,    0.0042309]]
            self.hqic = 730.735881539221
            self.llf = -353.407443379469
            self.resid = residsc_mle[:,1]
            self.fittedvalues = yhatc_mle[:,1]
            self.pvalues = [1.82e-193, 9.80e-05, 0.0352, 5.37e-07, 0.0725,
                    6.84e-07]
            self.tvalues = [29.67, 3.895, 2.106, -5.013, 1.796, 4.966]
            self.sigma2 = 0.990262659233 ** 2
        elif method =="css":
            self.params = [1.502401748545, 0.683090744792, 0.197636417391,
                    -0.763847295045, 0.137000823589, 0.304781097398]
            self.aic = 719.977407193363
            self.bic = 744.599577468616
            self.arroots = [1.4639  +0.0000j]
            self.maroots = [-1.3554    +0.0896j, -1.3554    -0.0896j,
                    1.1306    -0.7071j,  1.1306    +0.7071j]
            self.bse = [0.534723749868, 0.111273280223, 0.119840296133,
                    0.111263606843, 0.070759105676, 0.061783181500]
            self.cov_params = [
[ 0.28593,    -0.059175,    0.053968,    0.046974,  0.00085168,   0.0028000 ],
[ -0.059175,     0.012382,  -0.011333,  -0.0098375, -0.00012631,-0.00058518 ],
[ 0.053968,    -0.011333,   0.014362,    0.010298,  -0.0028117, -0.00011132 ],
[ 0.046974,   -0.0098375,   0.010298,    0.012380,  0.00031018,  -0.0021617 ],
[ 0.00085168,  -0.00012631, -0.0028117,  0.00031018,   0.0050069, 0.00079958 ],
[ .0028000,  -0.00058518,  -0.00011132,  -0.0021617,  0.00079958,  0.0038172 ]]
            self.hqic = 729.888235701317
            self.llf = -352.988703596681
            self.resid = residsc_css[:,1]
            self.fittedvalues = yhatc_css[:,1]
            self.pvalues = [0.0050,  8.31e-10,   0.0991, 6.64e-12,  0.0528,
                    8.09e-07]
            self.tvalues = [2.810, 6.139, 1.649, -6.865, 1.936, 4.933]
            self.sigma2 = 0.998687642867**2


class Y_arma41c(object):
    def __init__(self, method="mle"):
        if method == "mle":
            self.params = [1.062980233899, 0.768972932892, -0.264824839032,
                    -0.279936544064, 0.756963578430, 0.231557444097]
            self.aic = 686.468309958027
            self.bic = 711.118536383063
            self.arroots = [1.0077 +0j, -1.2466 +0j, .3044 -.9793j,
                    .3044+.9793j]
            self.maroots = [-4.3186 + 0.j]
            self.bse = [2.781653916478, 0.063404432598, 0.091047664068,
                    0.084679571389, 0.054747989396, 0.098952817806]
            self.cov_params =[
[      7.7376,  0.0080220, -0.0039840,  0.0064925,    0.0022936,   -0.0098015],
[   0.0080220,  0.0040201, -0.0054843,  0.0046548,   -0.0029922,   -0.0047964],
[  -0.0039840, -0.0054843,  0.0082897, -0.0072913,    0.0043566,    0.0067289],
[   0.0064925,  0.0046548, -0.0072913,  0.0071706,   -0.0043610,   -0.0057962],
[   0.0022936, -0.0029922,  0.0043566, -0.0043610,    0.0029973,    0.0036193],
[  -0.0098015, -0.0047964,  0.0067289, -0.0057962,    0.0036193,    0.0097917]]
            self.hqic = 696.389304738311
            self.llf = -336.234154979014
            self.resid = residsc_mle[:,2]
            self.fittedvalues = yhatc_mle[:,2]
            self.pvalues = [0.7024, 7.50e-34, 0.0036,  0.0009, 1.77e-43, 0.0193]
            self.tvalues = [0.3821, 12.13, -2.909, -3.306, 13.83, 2.340]
            self.sigma2 = 0.915487643192 ** 2
        elif method =="css":
            self.params = [-0.077068926631, 0.763816531155, -0.270949972390,
                    -0.284496499726, 0.757135838677, 0.225247299659]
            self.aic = 668.907200379791
            self.bic = 693.444521131318
            self.arroots = [1.0141  +0.0000j, -1.2455 +0.0000j,
                    0.3036    -0.9765j, 0.3036 +0.9765j]
            self.maroots = [-4.4396  +0.0000j]
            self.bse = [0.076048453921, 0.067854052128, 0.098041415680,
                    0.090698349822, 0.057331126067, 0.099985455449]
            self.cov_params = [
[  0.0057834,  0.00052477, -0.00079965, 0.00061291, -0.00013618,   -0.0018963 ],
[ 0.00052477,   0.0046042,  -0.0062505,  0.0053416,  -0.0032941,   -0.0047957 ],
[-0.00079965,  -0.0062505,   0.0096121, -0.0084500,   0.0047967,    0.0064755 ],
[ 0.00061291,   0.0053416,  -0.0084500,  0.0082262,  -0.0048029,   -0.0057908 ],
[-0.00013618,  -0.0032941,   0.0047967, -0.0048029,   0.0032869,    0.0035716 ],
[ -0.0018963,  -0.0047957,   0.0064755, -0.0057908,   0.0035716,    0.0099971]
                    ]
            self.hqic = 678.787238280001
            self.llf = -327.453600189896
            self.resid = residsc_css[:,2]
            self.fittedvalues = yhatc_css[:,2]
            self.pvalues = [0.3109,    2.15e-29,   0.0057,    0.0017, 8.06e-40,
                    0.0243]
            self.tvalues = [-1.013, 11.26, -2.764, -3.137, 13.21,  2.253]
            self.sigma2 = 0.915919923456**2


class Y_arma22c(object):
    def __init__(self, method="mle"):
        if method == "mle":
            self.params = [4.507728587708, 0.788365037622, -0.358656861792,
                    0.035886565643, -0.699600200796]
            self.aic = 813.417242529788
            self.bic = 834.546008036962
            self.arroots = [1.0991    -1.2571j, 1.0991   +1.2571j]
            self.maroots = [-1.1702     +0.0000j,  1.2215    +0.0000j]
            self.bse = [0.045346684035, 0.078382496509, 0.07004802526,
                    0.069227816205, 0.070668181454]
            self.cov_params = [
[   0.0020563,  -2.3845e-05,  -6.3775e-06,   4.6698e-05,   5.8515e-05],
[ -2.3845e-05,    0.0061438,   -0.0014403,   -0.0035405,   -0.0019265],
[ -6.3775e-06,   -0.0014403,    0.0049067,  -0.00059888,   -0.0025716],
[  4.6698e-05,   -0.0035405,  -0.00059888,    0.0047925,    0.0022931],
[  5.8515e-05,   -0.0019265,   -0.0025716,    0.0022931,    0.0049940]]
            self.hqic = 821.920952341460
            self.llf = -400.708621264894
            self.resid = residsc_mle[:,3]
            self.fittedvalues = yhatc_mle[:,3]
            self.pvalues = [0.0000, 8.48e-24, 3.05e-07, 0.6042, 4.17e-23]
            self.tvalues = [99.41,  10.06, -5.120,  0.5184, -9.900]
            self.sigma2 = 1.196309833136 ** 2
        elif method =="css":
            self.params = [2.571274348147, 0.793030965872, -0.363511071688,
                    0.033543918525, -0.702593972949]
            self.aic = 806.807171655455
            self.bic = 827.887744132445
            self.bse = [0.369201481343, 0.076041378729, 0.070029488852,
                    0.062547355221, 0.068166970089]
            self.cov_params = [
[     0.13631,    -0.017255,    -0.012852,     0.014091,     0.017241],
[   -0.017255,    0.0057823,   -0.0020013,   -0.0026493,   -0.0014131],
[   -0.012852,   -0.0020013,    0.0049041,  -0.00042960,   -0.0023845],
[    0.014091,   -0.0026493,  -0.00042960,    0.0039122,    0.0022028],
[    0.017241,   -0.0014131,   -0.0023845,    0.0022028,    0.0046467]
                    ]
            self.arroots = [1.0908    -1.2494j, 1.0908     +1.2494j]
            self.maroots = [-1.1694  +  0.0000j,  1.2171   +0.0000j]
            self.hqic = 815.293412134796
            self.llf = -397.403585827727
            self.resid = residsc_css[:,3]
            self.fittedvalues = yhatc_css[:,3]
            self.pvalues = [3.30e-12, 1.83e-25, 2.09e-07, 0.5918,   6.55e-25]
            self.tvalues = [  6.964, 10.43,  -5.191,  0.5363,  -10.31]
            self.sigma2 = 1.201409294941**2


class Y_arma50c(object):
    def __init__(self, method="mle"):
        if method == "mle":
            self.params = [4.562207236168, 0.754284447885, -0.305849188005,
                    0.253824706641,0.281161230244,-0.172263847479]
            self.aic = 711.817562780112
            self.bic = 736.467789205148
            self.arroots = [1.1546 + 0.j, 2.1052 + 0j, -1.6535 + 0.j,
                    .0129 -1.2018j, .0129 + 1.2018j]
            self.maroots = None
            self.bse = [0.318447388812, 0.062272737541, 0.076600312879,
                    0.077310728819, 0.076837326995, 0.062642955733]
            self.cov_params = [
[    0.10141, -6.6930e-05, -7.3157e-05, -4.4815e-05,  7.7676e-05, -0.00013170],
[-6.6930e-05,   0.0038779,  -0.0028465,   0.0013770,  -0.0012194, -0.00058978],
[-7.3157e-05,  -0.0028465,   0.0058676,  -0.0040145,   0.0024694,  -0.0012307],
[-4.4815e-05,   0.0013770,  -0.0040145,   0.0059769,  -0.0040413,   0.0013481],
[ 7.7676e-05,  -0.0012194,   0.0024694,  -0.0040413,   0.0059040,  -0.0028575],
[-0.00013170, -0.00058978,  -0.0012307,   0.0013481,  -0.0028575,   0.0039241]]
            self.hqic = 721.738557560396
            self.llf = -348.908781390056
            self.resid = residsc_mle[5:,4]
            self.fittedvalues = yhatc_mle[:,4]
            self.pvalues = [1.50e-46, 9.06e-34, 6.53e-05, 0.0010, 0.0003,
                    0.0060]
            self.tvalues = [14.33, 12.11, -3.993, 3.283, 3.659, -2.750]
            self.sigma2 = 0.973930886014 ** 2
        elif method =="css":
            self.params = [0.843173779572, 0.755433266689, -0.296886816205,
                    0.253572751789, 0.276975022313, -0.172637420881]
            self.aic = 694.843378847617
            self.bic = 715.850928110886
            self.arroots = [1.1508    +0.0000j, 2.0892 +0.0000j,
                    -1.6539 +0.0000j, 0.0091    -1.2069j, 0.0091  +1.2069j]
            self.maroots = None
            self.bse = [0.236922950898, 0.063573574389, 0.078206936773,
                    0.078927252266, 0.078183651496, 0.063596048046]
            self.cov_params = [
[    0.056132, -0.0028895, -0.0012291, -0.0031424,   -0.0012502, -0.0028739],
[  -0.0028895,  0.0040416, -0.0029508,  0.0014229,   -0.0012546,-0.00062818],
[  -0.0012291, -0.0029508,  0.0061163, -0.0041939,    0.0025537, -0.0012585],
[  -0.0031424,  0.0014229, -0.0041939,  0.0062295,   -0.0041928,  0.0014204],
[  -0.0012502, -0.0012546,  0.0025537, -0.0041928,    0.0061127, -0.0029479],
[  -0.0028739,-0.00062818, -0.0012585,  0.0014204,   -0.0029479,  0.0040445]
                    ]
            self.hqic = 703.303100827167
            self.llf = -341.421689423809
            self.resid = residsc_css[5:,4]
            self.fittedvalues = yhatc_css[:,4]
            self.pvalues = [0.0004, 1.45e-32,   0.0001, 0.0013, 0.0004, 0.0066]
            self.tvalues = [ 3.559, 11.88,  -3.796,   3.213,   3.543,  -2.715]
            self.sigma2 = 0.987100631424**2

class Y_arma02c(object):
    def __init__(self, method="mle"):
        if method == "mle":
            self.params = [4.519277801954, 0.200385403960, -0.643766305844]
            self.aic = 758.051194540770
            self.bic = 772.137038212219
            self.arroots = None
            self.maroots = [-1.1004 + 0.j, 1.4117 + 0.j]
            self.bse = [0.038397713362, 0.049314652466, 0.048961366071]
            self.cov_params = [
[   0.0014744,   6.2363e-05,   6.4093e-05 ],
[  6.2363e-05,    0.0024319,    0.0014083 ],
[  6.4093e-05,    0.0014083,    0.0023972 ]]
            self.hqic = 763.720334415218
            self.llf = -375.025597270385
            self.resid = residsc_mle[:,5]
            self.fittedvalues = yhatc_mle[:,5]
            self.pvalues = [0.0000, 4.84e-5, 1.74e-39]
            self.tvalues = [117.7, 4.063, -13.15]
            self.sigma2 = 1.081406299967 ** 2
        elif method =="css":
            self.params = [4.519869870853, 0.202414429306, -0.647482560461]
            self.aic = 756.679105324347
            self.bic = 770.764948995796
            self.arroots = None
            self.maroots = [ -1.0962   +  0.0000j,  1.4089   +  0.0000j]
            self.bse = [0.038411589816, 0.047983057239, 0.043400749866]
            self.cov_params = [
[   0.0014755,   9.0191e-05,   7.3561e-06],
[  9.0191e-05,    0.0023024,    0.0012479],
[  7.3561e-06,    0.0012479,    0.0018836]]
            self.hqic = 762.348245198795
            self.llf = -374.339552662174
            self.resid = residsc_css[:,5]
            self.fittedvalues = yhatc_css[:,5]
            self.pvalues = [ 0.0000, 2.46e-05, 2.49e-50]
            self.tvalues = [117.7,   4.218, -14.92]
            self.sigma2 = 1.081576475937**2

