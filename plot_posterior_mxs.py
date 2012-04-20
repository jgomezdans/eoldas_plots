#!/usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def rearrange_mx ( A, num_p, n_doys ):
    B = A*0
    for r in xrange ( num_p*n_doys ):
        for p in xrange( num_p ):
            for t in xrange ( n_doys ):
                B[r, n_doys*p + t] = A[p*n_doys + t ,p + num_p*t]
    return B

def PreparePlotsParams ():
    fig_width_pt = 615.0  # Get this from LaTeX using \showthe\columnwidth
    inches_per_pt = 1.0/72.27               # Convert pt to inches
    golden_mean = (np.sqrt(5)-1.0)/2.0         # Aesthetic ratio
    fig_width = fig_width_pt*inches_per_pt  # width in inches
    fig_width = 7.48
    fig_height =fig_width*golden_mean       # height in inches
    #fig_size = [fig_height, fig_width]
    fig_size = [fig_width, fig_height]
    fig_size = [16.54, 11.69 ]
    plt.rcParams['text.usetex'] = True
    plt.rcParams['legend.fontsize'] = 8
    plt.rcParams['axes.labelsize'] = 14
    plt.rcParams['text.fontsize'] = 12
    plt.rcParams['legend.fontsize']=8
    plt.rcParams['xtick.labelsize']= 14
    plt.rcParams['ytick.labelsize']=14
    plt.rcParams['figure.subplot.left'] = 0.12
    plt.rcParams['figure.subplot.right'] = .96
    plt.rcParams['figure.subplot.top'] = 0.94
    plt.rcParams['figure.subplot.bottom'] = 0.05
    plt.rcParams['figure.subplot.hspace'] = 0.07
    plt.rcParams['figure.subplot.wspace'] = 0.06
    plt.rcParams['figure.figsize']=fig_size
    
def  calculate_corr ( cov ):
    corr = cov *0.0
    d = np.sqrt(cov.diagonal())
    for i in xrange ( cov.shape[0] ):
        for j in xrange ( cov.shape[1] ):
            corr[i,j] = cov[i,j]/(d[i]*d[j])
    return corr
    
def plot_matrix ( ax, matrix, cmap, vmin=0, vmax=1, label=False ):
    
    ax.imshow ( matrix, cmap=cmap, interpolation='nearest' )
    
        
    ax.set_yticks([0, 366,  365*2+1,  365*3+1, 365*4+1, 365*5+1])
    ax.set_xticks([0, 366,  365*2+1,  365*3+1, 365*4+1, 365*5+1])
    if label:
        ax.set_yticklabels([r'$TLAI^{(1)}$', r'$TCab^{(1)}$',r'$TCw^{(1)}$', \
        r'$TCdm^{(1)}$', r'$N^{(1)}$', r'$s1^{(1)}$'])
    else:
        ax.set_yticklabels(["", "","",""])
    ax.set_xticklabels([r'$TLAI^{(1)}$', r'$TCab^{(1)}$',r'$TCw^{(1)}$', \
        r'$TCdm^{(1)}$', r'$N^{(1)}$', r'$s1^{(1)}$'])
    [ ax.axvline(i,c='k', lw=0.1) for i in [365,365*2,365*3,365*4, 365*5] ]
    [ ax.axhline(i,c='k', lw=0.1) for i in [365,365*2,365*3, 365*4, 365*5] ]
    return ax
    
if __name__ == "__main__":
    PreparePlotsParams()
    fname_o1 = sys.argv[1]
    fname_o2 = sys.argv[2]
    fname_out = sys.argv[3]
    gamma_o1 = fname_o1.split(".")[-2]
    gamma_o2 = fname_o2.split(".")[-2]
    f = np.load( fname_o1 )
    cov_o1=f['IHsmall']

    f = np.load( fname_o2 )
    cov_o2=f['IHsmall']

    corr_o1 = calculate_corr ( cov_o1 )
    corr_o2 = calculate_corr ( cov_o2 )
    #corr_o1=np.array(cov_o1) / np.array(np.sqrt(cov_o1.diagonal()).T * np.sqrt(cov_o1.diagonal()))
    #corr_o2=np.array(cov_o2) / np.array(np.sqrt(cov_o2.diagonal()).T * np.sqrt(cov_o2.diagonal()))
    f = np.load ( "../single/single_inversion_posterior_mxs_FBP.npz" )
    single_cov = f['single_cov']
    single_corr = f['single_corr']
    cov_o1_i = cov_o1*0.0
    cov_o2_i = cov_o2*0.0
    corr_o1_i = cov_o1*0.0
    corr_o2_i = cov_o2*0.0
    single_cov_i = single_cov *0.
    single_corr_i = single_corr *0.
    for i in xrange ( 6 ):
        for j in xrange ( 6 ):
            cov_o1_i[ (365*i):((i+1)*365), (365*j):((j+1)*365) ] = \
                cov_o1[i::6, j::6]
            cov_o2_i[ (365*i):((i+1)*365), (365*j):((j+1)*365) ] = \
                    cov_o2[i::6, j::6]
            corr_o1_i[ (365*i):((i+1)*365), (365*j):((j+1)*365) ] = \
                    corr_o1[i::6, j::6]
            corr_o2_i[ (365*i):((i+1)*365), (365*j):((j+1)*365) ] = \
                    corr_o2[i::6, j::6]
            single_cov_i[ (365*i):((i+1)*365), (365*j):((j+1)*365) ] = \
                    single_cov[i::6, j::6]
            single_corr_i[ (365*i):((i+1)*365), (365*j):((j+1)*365) ] = \
                    single_corr[i::6, j::6]
                    
    
            
    #corr_o1_i = np.ma.array ( corr_o1_i, mask=np.abs(corr_o1_i)<1e-3)
    #corr_o2_i = np.ma.array ( corr_o2_i, mask=np.abs(corr_o2_i)<1e-3)
    #cov_o1_i = np.ma.array ( cov_o1_i, mask=np.abs(cov_o1_i)<0.001)
    #cov_o2_i = np.ma.array ( cov_o2_i, mask=np.abs(cov_o2_i)<0.001)
    #single_cov = np.ma.array ( single_cov, mask=np.abs(single_cov)<0.001)
    #single_corr = np.ma.array ( single_corr, mask=np.abs(single_corr)<1e-2)

    cmap = plt.cm.RdBu_r
    #cmap.set_bad='g'
    #cmap.set_under='w'
    #cmap.set_over='k'
    

    ###fig1 = plt.figure()
    ###sbp = fig1.add_subplot ( 1,3,1 )
    ###plot_matrix ( sbp, single_cov, cmap, vmin=-1./8, vmax=1./8, label=True )
    ###sbp = fig1.add_subplot ( 1,3,2 )
    ###plot_matrix ( sbp, cov_o1_i, cmap, vmin=-1./8, vmax=1./8. )
    ###sbp = fig1.add_subplot ( 1,3,3 )
    ###plot_matrix ( sbp, cov_o2_i, cmap, vmin=-1./8, vmax=1./8.)

    
    #fig1 = plt.figure()
    #sbp = fig1.add_subplot ( 1,3,1 )
    #plot_matrix ( sbp, single_cov_i, cmap, label=True )
    #sbp = fig1.add_subplot ( 1,3,2 )
    #plot_matrix ( sbp, cov_o1_i, cmap,vmin=-1./64, vmax=1./64)
    #sbp = fig1.add_subplot ( 1,3,3 )
    #plot_matrix ( sbp, cov_o2_i, cmap,vmin=-1./64, vmax=1./64 )
    
    
    fig2 = plt.figure()
    #sbp = fig2.add_subplot ( 1,3,1 )
    #plot_matrix ( sbp, single_corr_i, cmap, vmin=-0.9, vmax=0.9, label=True )
    sbp = fig2.add_subplot ( 1,2,1 )
    ax = plot_matrix ( sbp, corr_o1_i, cmap, vmin=-0.9, vmax=0.9, label=True )
    ax.set_title (r'1\textsuperscript{st} order constraint $\;\gamma=%s$'%gamma_o1)
    sbp = fig2.add_subplot ( 1,2,2 )
    ax = plot_matrix ( sbp, corr_o2_i, cmap, vmin=-0.9, vmax=0.9 )
    ax.set_title (r'2\textsuperscript{nd} order constraint $\;\gamma=%s$'%gamma_o2)
    
    
    cax = fig2.add_axes([0.12, 0.9, 0.8, 0.05])
    
    cbase = matplotlib.colorbar.ColorbarBase( cax, cmap=cmap, \
        orientation='horizontal',  norm=matplotlib.colors.normalize(-0.9, 0.9))
    
    #plt.show()
    plt.savefig ("%s.pdf" % fname_out, dpi=300)
    #plt.savefig ("%s.png" % fname_out, dpi=300)
