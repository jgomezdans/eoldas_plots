#!/usr/bin/env python
import sys
import numpy as np
sel_cols = [0, 3,  4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] + range(17,30)
order1s = [ "../xval/reruns/reruns_rse1_test.150.dat", \
        "../xval_cloudy/reruns/reruns_rse1_test.100.dat"]
order2s = [ "../xval/reruns/reruns_rse1_test.530.dat", \
        "../xval_cloudy/reruns/reruns_rse1_test.630.dat"]
def chunguez ( x ):
    lx = np.sum( 0.5*np.log( x) )
    retval = 1.96*np.exp(lx/float(x.shape[0]))
    return retval
    
for nfile in xrange(2):
    o1_data = np.loadtxt( order1s[nfile], usecols=sel_cols)
    o2_data = np.loadtxt( order2s[nfile], usecols=sel_cols )
    print order1s[nfile]
    print order2s[nfile]
    true_data = np.loadtxt("../xval/input/truth.400.dat")
    true_data = true_data[:, [0]+range(3,16)]
    
    if order1s[nfile].find ( "cloudy") >=0:
        single_data = np.loadtxt("../single/single_inversions_results_cloudy_FBP.dat" )
    else:
        single_data = np.loadtxt("../single/single_inversions_results_FBP.dat" )


    params = ['TLAI', 'TKAB', 'TKW', 'TKDM', 'N', 'S1']
    param_loc = [1, 4, 6,7,8,9] 
    for i in xrange(6):
        prior = np.ones(365)*(1./(64.))
        prior [np.in1d ( np.arange(1,366), single_data[:,0])] = \
        (single_data [ :, 13+param_loc[i]])**2
        posterior1 = (o1_data [ :, 13+param_loc[i]])**2
        posterior2 = (o2_data [ :, 13+param_loc[i]])**2
        #print "%8s"%params[i], "%5.3g,"%prior.mean(),"%5.3g,"%posterior1.mean(),"%5.3g,"%posterior2.mean()
    #print "========================================="
    #for i in xrange(6):
        sel = np.in1d ( np.arange(1,366), single_data[:,0])
        
        prioro= (single_data [ :, 13+param_loc[i]])**2
        posterior1o = (o1_data [ sel, 13+param_loc[i]])**2
        posterior2o = (o2_data [ sel, 13+param_loc[i]])**2
        print "%8s"%params[i], "%5.3g (%5.3g),"%(chunguez(prior), chunguez(prioro)), \
        "%5.3g (%5.3g),"%(chunguez(posterior1), chunguez(posterior1o)), \
        "%5.3g (%5.3g)"%(chunguez(posterior2), chunguez(posterior2o))
        

    ####for i in xrange(6):
        ####prior = np.ones(365)*(1./(64.))
        ####prior [np.in1d ( np.arange(1,366), single_data[:,0])] = \
                ####(single_data [ :, 13+param_loc[i]])**2
        ####posterior = (o1_data [ :, 13+param_loc[i]])**2
        
        ####unc = -np.sum( -0.5*np.log( prior) + 0.5*np.log(posterior) )
        ####sd_equiv = np.exp(unc/float(prior.shape[0]))
        ####print "%8s"%params[i], "%5.3g,"%sd_equiv,
        ####posterior = (o2_data [ :, 13+param_loc[i]])**2
        ####unc = -np.sum( -0.5*np.log( prior) + 0.5*np.log(posterior) )
        ####sd_equiv = np.exp(unc/float(prior.shape[0]))
        ####print "%5.3g,"%sd_equiv,
        ####pcntge_true_o1 = 100.*np.sum(np.logical_and ( true_data[:,param_loc[i]] >= \
            ####(o1_data[:,param_loc[i]]-1.96*o1_data[:,13+param_loc[i]] ), \
            ####true_data[:,param_loc[i]] <= (o1_data[:,param_loc[i]]+1.96*o1_data[:,13+param_loc[i]] )))/float(prior.shape[0])
        ####pcntge_true_o2 = 100.*np.sum(np.logical_and ( true_data[:,param_loc[i]] >= \
            ####(o2_data[:,param_loc[i]]-1.96*o2_data[:,13+param_loc[i]] ), \
            ####true_data[:,param_loc[i]] <= (o2_data[:,param_loc[i]]+1.96*o2_data[:,13+param_loc[i]] )))/float(prior.shape[0])
            
        ####print "%4.3g,"%pcntge_true_o1, "%4.3g"%pcntge_true_o2#, pcntge_true_sgl
    ####print "========================================="
    ####for i in #xrange(6):
        ####sel = np.in1d ( np.arange(1,366), single_data[:,0])
        ####prior = (single_data [ :, 13+param_loc[i]])**2
        ####posterior = (o1_data [ :, 13+param_loc[i]][np.in1d ( np.arange(1,366), single_data[:,0])])**2
        ####unc = -np.sum( -0.5*np.log( prior) + 0.5*np.log(posterior) )
        ####sd_equiv = np.exp(unc/float(prior.shape[0]))
        ####print "%8s"%params[i], "%5.3g,"%sd_equiv,
        ####posterior = (o2_data [ :, 13+param_loc[i]][np.in1d ( np.arange(1,366), single_data[:,0])])**2
        ####unc = -np.sum( -0.5*np.log( prior) + 0.5*np.log(posterior) )
        ####sd_equiv = np.exp(unc/float(prior.shape[0]))
        ####print "%5.3g,"%sd_equiv,
        ####pcntge_true_sgl = 100.*np.sum( np.logical_and ( true_data[sel,param_loc[i]] >= \
            ####single_data[:,param_loc[i]]-1.96*np.sqrt(prior[:] ), \
            ####true_data[sel,param_loc[i]] <= (single_data[:,param_loc[i]]+1.96*np.sqrt(prior[:]))))/float(prior.shape[0])
        ####pcntge_true_o1 = 100.*np.sum(np.logical_and ( true_data[sel,param_loc[i]] >= \
            ####(o1_data[sel,param_loc[i]]-1.96*o1_data[sel,13+param_loc[i]] ), \
            ####true_data[sel,param_loc[i]] <= (o1_data[sel,param_loc[i]]+1.96*o1_data[sel,13+param_loc[i]] )))/float(prior.shape[0])
        ####pcntge_true_o2 = 100.*np.sum(np.logical_and ( true_data[sel,param_loc[i]] >= \
            ####(o2_data[sel,param_loc[i]]-1.96*o2_data[sel,13+param_loc[i]] ), \
            ####true_data[sel,param_loc[i]] <= (o2_data[sel,param_loc[i]]+1.96*o2_data[sel,13+param_loc[i]] )))/float(prior.shape[0])
        ####print "%4.3g,"%pcntge_true_o1, "%4.3g,"%pcntge_true_o2, "%4.3g"%pcntge_true_sgl