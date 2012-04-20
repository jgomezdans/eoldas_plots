#!/usr/bin/env python
import numpy as np
import glob
import pdb
import os
import sys
import matplotlib.pyplot as plt


def PreparePlotsParams ():
    fig_width_pt = 615.0  # Get this from LaTeX using \showthe\columnwidth
    inches_per_pt = 1.0/72.27               # Convert pt to inches
    golden_mean = (np.sqrt(5)-1.0)/2.0         # Aesthetic ratio
    fig_width = fig_width_pt*inches_per_pt  # width in inches
    fig_height =fig_width*golden_mean       # height in inches
    #fig_size = [fig_height, fig_width]
    fig_size = [fig_width, fig_height]
    
    plt.rcParams['text.usetex'] = True
    plt.rcParams['legend.fontsize'] = 10
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['text.fontsize'] = 10
    plt.rcParams['xtick.labelsize']= 10
    plt.rcParams['ytick.labelsize']=10
    plt.rcParams['figure.subplot.left'] = 0.12
    plt.rcParams['figure.subplot.right'] = .96
    plt.rcParams['figure.subplot.top'] = 0.9
    plt.rcParams['figure.subplot.bottom'] = 0.1
    plt.rcParams['figure.subplot.hspace'] = 0.07
    plt.rcParams['figure.subplot.wspace'] = 0.06
    plt.rcParams['figure.figsize']=fig_size
    
    
def xval_results ( work_dir ):
    # The hyperspectral sensor observations with noise are stored in this file:
    original = "input/spot_test.dat" 
    #original = "/home/ucfajlg/Data/python/rse_eoldas/hyper/input/hyper_test.dat" 
    original = np.loadtxt ( os.path.join ( work_dir, original), skiprows=1 )
    xval_o1 = {}
    xval_o2 = {}
    unc= np.loadtxt("spot_wavebands.dat")
    nbands = unc.shape[0]
    wv = (unc[:,0] + unc[:,1])/2.
    unc = 0.004 + (0.010-0.004)* (wv - wv.min())/(wv.max()-wv.min())
    unc = unc*unc
    #0.004 + (0.010-0.004)*(hyperMean-hyperMin)/(hyperMax-hyperMin)
    #for fich in glob.glob ( "/home/ucfajlg/Data/python/rse_eoldas/hyper/output/rse_order1/hyper_test_fwd.*.dat" ):
    
    files = glob.glob ( os.path.join ( work_dir, "output/rse_order1/spot_test_fwd.*.dat") )
    
    files.sort()
    for fich in files:
        
        gamma=float(fich.replace(os.path.join( work_dir, "output/rse_order1/spot_test_fwd."), "").replace(".dat",""))
        #gamma = int ( fich.split(".")[-2] )
        print "1",gamma,fich
        cand = np.loadtxt ( fich, skiprows=1 )
        rmse = 0.5*np.sqrt ( np.mean ( ((cand[:,6:(6+nbands)] - original[:,6:(6+nbands)] )**2 )/unc) )
        xval_o1[gamma] = rmse
    #for fich in glob.glob ( "/home/ucfajlg/Data/python/rse_eoldas/hyper/output/rse_order2/hyper_test_fwd.*.dat" ):
    files = glob.glob ( os.path.join ( work_dir, "output/rse_order2/spot_test_fwd.*.dat" ) )
    files.sort()
    for fich in files:
        #gamma = int ( fich.split(".")[-2] )
        gamma=float(fich.replace(os.path.join( work_dir, "output/rse_order2/spot_test_fwd."), "").replace(".dat",""))

        print "2",gamma
        cand = np.loadtxt ( fich, skiprows=1 )
        rmse = np.sqrt ( np.mean ( ((cand[:,6:(6+nbands)] - original[:,6:(6+nbands)] )**2 )/unc) )
        xval_o2[gamma] = rmse

    gamma_o1 = xval_o1.keys()
    gamma_o1.sort()
    rmse_o1 = [ xval_o1[k] for  k in gamma_o1 ]

    gamma_o2 = xval_o2.keys()
    gamma_o2.sort()
    rmse_o2 = [ xval_o2[k] for  k in gamma_o2 ]
    return ( gamma_o1, rmse_o1, gamma_o2, rmse_o2 )

if __name__ == "__main__":
    o1_gammas = np.fromstring ("175 150 125 100 75 50 10 1 225 250 275" + \
        " 300 350 400 600 800 5001 20001 100001", sep=" ")
    o2_gammas = np.fromstring ("180 120 80 51 35 25 15 11 2 276 415 530" +\
        " 630 995 1445 2100 3300 5000 20000 100000", sep=" ")
    xval_results_complete = sys.argv[1]
    xval_results_cloudy = sys.argv[2]
    print "Using complete results directory: %s" % xval_results_complete
    print "Using cloudy results directory: %s" % xval_results_cloudy
    PreparePlotsParams()
    gamma_o1, rmse_o1, gamma_o2, rmse_o2 = xval_results ( xval_results_complete )
    print "Non cloudy"
    print "O1: ", [ g for g in gamma_o1 if not(np.in1d(g,o1_gammas))]
    print "O2: ", [ g for g in gamma_o2 if not(np.in1d(g,o2_gammas))]
    gamma_o1_c, rmse_o1_c, gamma_o2_c, rmse_o2_c = xval_results ( xval_results_cloudy )
    print "Cloudy"
    theory_o1 = np.array([1./0.005304, 1./0.0033, 1./0.00754, 1./0.00472] )
    theory_o2 = np.array ([1./0.0001205, 1./0.0001367, 1./0.0004391, 1./0.0002597])
    [plt.axvline (x=theory_o1[i], color='k', lw=0.2) for i in xrange(4) ]
    [plt.axvline (x=theory_o2[i], color='k', lw=0.2) for i in xrange(4)]

    plt.semilogx( gamma_o1, rmse_o1, 'o-k', label="Complete O1" )
    plt.semilogx ( gamma_o2, rmse_o2 , 's-k', label="Complete O2")
    plt.semilogx( gamma_o1_c, rmse_o1_c, 'o-k', mfc="none", label="Cloudy O1" )
    plt.semilogx( gamma_o2_c, rmse_o2_c , 's-k', mfc="none", label="Cloudy O2" )
    #[plt.axvline (x=theory_o1[i], color='r') for i in xrange(4) ]
    #[plt.axvline (x=theory_o2[i], color='b') for i in xrange(4)]
    plt.legend(loc="best", numpoints=1)
    plt.xlabel(r'$\gamma\, [-]$')
    plt.ylabel("Scaled RMSE [-]")
    plt.title("Cross validation RMSE as a function of\nregularisation parameter")
    plt.grid ( True )
    
    plt.savefig ("crossval.pdf", dpi=1200)
    plt.savefig("crossval.png", dpi=1200)
    plt.show()
    """
                        o1                       o2
    lai           0.005304                       0.0001205
    xkab          0.00333                        0.0001367
    xkw           0.00754                        0.0004391
    xs1           0.00472                        0.0002597"""
