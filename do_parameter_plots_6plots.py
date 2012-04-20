#!/usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt
import cPickle # Mmmmm... pickles!


def PreparePlotsParams ():
    fig_width_pt = 615.0  # Get this from LaTeX using \showthe\columnwidth
    inches_per_pt = 1.0/72.27               # Convert pt to inches
    golden_mean = (np.sqrt(5)-1.0)/2.0         # Aesthetic ratio
    fig_width = fig_width_pt*inches_per_pt  # width in inches
    figh_width = 7.48
    fig_height =fig_width*golden_mean       # height in inches
    #fig_size = [fig_height, fig_width]
    fig_size = [fig_width, fig_height]

    plt.rcParams['axes.formatter.limits'] = [-3, 3]
		 #No large numbers with loads of 0s 
    plt.rcParams['text.usetex'] = True
    plt.rcParams['legend.fontsize'] = 8
    plt.rcParams['axes.labelsize'] = 10
    plt.rcParams['text.fontsize'] = 8
    plt.rcParams['legend.fontsize']=6
    plt.rcParams['xtick.labelsize']= 8
    plt.rcParams['ytick.labelsize']=8
    plt.rcParams['figure.subplot.left'] = 0.12
    plt.rcParams['figure.subplot.right'] = .96
    plt.rcParams['figure.subplot.top'] = 0.94
    plt.rcParams['figure.subplot.bottom'] = 0.08
    plt.rcParams['figure.subplot.hspace'] = 0.12
    plt.rcParams['figure.subplot.wspace'] = 0.14
    plt.rcParams['figure.figsize']=fig_size
    
    

def transform_var ( x, param ):
    if param == 1: # LAI
        return -2.*np.log ( x )
    elif param == 2: # xkab
        return -100*np.log ( x )
    elif param == 3: # xkw
        return -(1./50)*np.log ( x )
    elif param == 4: # xkm
	return -(1./100.)*np.log ( x )
    elif param > 4 : #xleafn or xs1 
        return x

# Read pickles
param_names = [ r'$LAI\,[m^{2}m^{-2}]$', r'$C_{ab}\, [\mu gcm^{-2}]$', \
    r'$C_w\, [cm^{-1}]$', '$C_{dm}\,[gcm^{-2}]$',r'$N\,[-]$', r'$s_1\,[-]$']

PreparePlotsParams()

o1_file = "/home/ucfajlg/Data/python/rse_eoldas/output/rse_order1/rse1_test.100.dat"
o2_file = "/home/ucfajlg/Data/python/rse_eoldas/output/rse_order2/rse1_test.5000.dat"
#single_inv = np.loadtxt("/home/ucfajlg/Data/python/rse_eoldas/single_inversions/output/single_parameters_blended.dat" )

o1_file = sys.argv[1]
o2_file = sys.argv[2]
single_inv_file = sys.argv[3]
fout_fname = sys.argv[4]
xval_fname = sys.argv[5]

print "First order constraint results file: %s" % o1_file
print "Second order constraint results file: %s" % o2_file
print "Single inversion file: %s" % single_inv_file
single_inv = np.loadtxt( single_inv_file )

o1_inv = np.loadtxt( o1_file, skiprows=1 )
o2_inv = np.loadtxt( o2_file, skiprows=1 )
xval_obs = np.loadtxt ( xval_fname )

#o1_inv = np.loadtxt("/home/ucfajlg/Data/python/rse_eoldas_cloudy/output/rse_order1/rse1_test.800.dat", skiprows=1 )
#o2_inv = np.loadtxt("/home/ucfajlg/Data/python/rse_eoldas_cloudy/output/rse_order2/rse1_test.5000.dat", skiprows=1 )
gamma_o1 = int ( o1_file.split(".")[-2] )
gamma_o2 = int ( o2_file.split(".")[-2] )
print "O1 Gamma (from filename) is %d" % gamma_o1
print "O2 Gamma (from filename) is %d" % gamma_o2

bounds = [ [0.0674,0.9950],[0.1353,1.0], [0.00674,0.9995],[0.1353, 1.0],[0.8, 2.5], [0.0, 0.4] ]
tbounds = [[0.01, 6.  ], [0,200],[1.00025008e-05, 0.03],[1e-5,0.02],[0.8,2.0],[0.0,0.4]]
tbounds = [[0, 6.],[0,200],[0,0.04],[0,0.03],[0.8,2.5],[ 0.0,0.5]]
iloc = [ 2, 5, 7,8,9, 10]
truth = np.loadtxt( "./truth.400.dat", skiprows=1 )
fig1 = plt.figure()
fig2 = plt.figure()
fig3 = plt.figure()
for param in xrange ( 6 ):
    
    
    plt.figure(1)
    fig1.add_subplot ( 2, 3, param+1 )
    y1 = single_inv[:,iloc[param]-1] - 1.96*single_inv[:,13+iloc[param]-1]
    y2 = single_inv[:,iloc[param]-1] + 1.96*single_inv[:,13+iloc[param]-1]
    y1 = np.clip ( y1, bounds[param][0], bounds[param][1] )
    y2 = np.clip ( y2, bounds[param][0], bounds[param][1] )
    
    
    mu = transform_var (single_inv[:,iloc[param]-1], param+1)
    

    plt.vlines( single_inv[:,0], transform_var( y1, param+1 ), \
        transform_var( y2, param+1 ), lw=0.4, color="r")
    plt.plot ( single_inv[:,0], mu, 'sr-', lw=.5,ms=4 )
    plt.plot ( truth[:, 0], transform_var (truth[:, iloc[param]+1], param+1 ), '--g', lw=1.2 )
    axo = plt.axis()
    axes = [axo[0], axo[1], tbounds[param][0], tbounds[param][1]]
    plt.axis ( axes )        

    ax = plt.gca()
    
    vshift = 0.02 * (tbounds[param][1] - tbounds[param][0])
    plt.plot ( xval_obs, vshift+np.ones_like ( xval_obs)*tbounds[param][0], '+k', ms=3)
    if param+1 > 3:
        plt.xlabel(r'Day of year')
        xtl = ax.get_xticklabels()
        [ label.set_visible(False) \
           for (ipos, label) in enumerate(xtl) if ipos%2==0 ]
    else:
        #No xlabels here!
        xtl = ax.get_xticklabels()
        [ label.set_visible(False) for label in xtl ]        
    plt.title( param_names[param] )
    yticks = ax.get_yticks()
    ax.set_yticks ( np.linspace ( 1.1*tbounds[param][0], 0.9*tbounds[param][1],3) )
    locs, labels = plt.yticks()
    if locs[-1] == 180:
	    plt.yticks ( locs, map(lambda x: "%5.3g" %x, locs))
    else:
	    plt.yticks ( locs, map(lambda x: "%5.2g" % x, locs))
	    
#############################################################################  
    vshift = 0.02 * (tbounds[param][1] - tbounds[param][0])
    plt.figure(2)
    fig2.add_subplot ( 2, 3, param + 1)
    
    
    y1 = o1_inv[:,iloc[param]+1] - 1.96*o1_inv[:,15+iloc[param]]
    y2 = o1_inv[:,iloc[param]+1]+ 1.96*o1_inv[:,15+iloc[param]]
    y1 = np.clip ( y1, bounds[param][0], bounds[param][1] )
    y2 = np.clip ( y2, bounds[param][0], bounds[param][1] )
    
    #y2 = transform_var (single_inv[:,2+param], param+1) + 1.96*transform_var(single_inv[:,16+param], param+1) 
    mu = transform_var (o1_inv[:,iloc[param]+1], param+1)
    plt.fill_between( np.arange(365) + 1, transform_var( y1, param+1 ), \
        y2=transform_var( y2, param+1 ), facecolor='0.8', lw=0.2 )
    
    plt.plot ( np.arange(365) + 1, mu, 'r-', lw=1.5 )
    actual_obs_mask = np.in1d ( o1_inv[:,0], single_inv[:,0] )
    plt.plot ( o1_inv[actual_obs_mask,0], mu[actual_obs_mask], 'or', \
            ms=4 )
    
    plt.plot ( truth[:, 0], transform_var (truth[:, iloc[param]+1], param+1 ), '--g', lw=1.2 )
    plt.axis ( axes )
    ax = plt.gca()
    plt.title( param_names[param] )
    
    plt.plot ( xval_obs, vshift+np.ones_like ( xval_obs)*tbounds[param][0], '+k', ms=3)
    if param + 1 > 3:
        plt.xlabel(r'Day of year')
        xtl = ax.get_xticklabels()
        [ label.set_visible(False) \
           for (ipos, label) in enumerate(xtl) if ipos%2==0 ]
    else:
        #No xlabels here!
        xtl = ax.get_xticklabels()
        [ label.set_visible(False) for label in xtl ]        
    # Get y ticks and unset the top one to avoid overcrowding
    yticks = ax.get_yticks()
    ax.set_yticks ( np.linspace ( 1.1*tbounds[param][0], 0.9*tbounds[param][1],3) )
    locs, labels = plt.yticks()
    if locs[-1] == 180:
        plt.yticks ( locs, map(lambda x: "%5.3g" %x, locs))
    else:
        plt.yticks ( locs, map(lambda x: "%5.2g" % x, locs))

    #ax.set_yticks ( yticks[:-1] )
 #############################################################################  
    vshift = 0.02 * (tbounds[param][1] - tbounds[param][0])
    plt.figure(3)
    fig3.add_subplot ( 2, 3, param + 1)
    
    y1 = o2_inv[:,iloc[param]+1] - 1.96*o2_inv[:,15+iloc[param]]
    y2 = o2_inv[:,iloc[param]+1] + 1.96*o2_inv[:,15+iloc[param]]
    y1 = np.clip ( y1, bounds[param][0], bounds[param][1] )
    y2 = np.clip ( y2, bounds[param][0], bounds[param][1] )
    
    #y2 = transform_var (single_inv[:,2+param], param+1) + 1.96*transform_var(single_inv[:,16+param], param+1) 
    mu = transform_var (o2_inv[:,iloc[param]+1], param+1)
    plt.fill_between( np.arange(365) + 1, transform_var( y1, param+1 ), \
        y2=transform_var( y2, param+1 ), facecolor='0.8',lw=0.2 )
    plt.plot ( np.arange(365) + 1, mu, 'r-', lw=1.5 )
    actual_obs_mask = np.in1d ( o2_inv[:,0], single_inv[:,0] )
    plt.plot ( o2_inv[actual_obs_mask,0], mu[actual_obs_mask], 'or', \
            ms=4,mfc='none' )
    
    plt.plot ( truth[:, 0], transform_var (truth[:, iloc[param]+1], param+1 ), '--g', lw=1.2 )
    plt.axis ( axes )
    
    ax = plt.gca()
    plt.title( param_names[param] )
    plt.plot ( xval_obs, vshift + np.ones_like ( xval_obs)*tbounds[param][0], '+k', ms=3)
    if param + 1 > 3:
       plt.xlabel(r'Day of year')
       xtl = ax.get_xticklabels()
       [ label.set_visible(False) \
           for (ipos, label) in enumerate(xtl) if ipos%2==0 ]
    else:
        #No xlabels here!
        xtl = ax.get_xticklabels()
        [ label.set_visible(False) for label in xtl ]
    # Get y ticks and unset the top one to avoid overcrowding
    yticks = ax.get_yticks()
    ax.set_yticks ( np.linspace ( 1.1*tbounds[param][0], 0.9*tbounds[param][1],3) )
    locs, labels = plt.yticks()
    if locs[-1] == 180:
        plt.yticks ( locs, map(lambda x: "%5.3g" %x, locs))
    else:
        plt.yticks ( locs, map(lambda x: "%5.2g" % x, locs))
    #plt.savefig ("rse_expt1.pdf")
    #plt.savefig ("rse_expt1.png", dpi=600)
#plt.show()
#plt.savefig ("%s.png"%fout_fname, dpi=1200)
#plt.savefig ("%s.pdf"%fout_fname, dpi=1200)
plt.show()
