#!/bin/bash

PLOT_PARAM=~/Data/python/EOLDAS_clean/EOLDAS_clean_noise2/plots/do_parameter_plots_6plots.py
PLOT_COV=~/Data/python/EOLDAS_clean/EOLDAS_clean_noise2/plots/plot_posterior_mxs.py
# Central region of the crossval plot
#Central xvals
#    Cloudy
#        O1 100
#        O2 630
#
#    NonCloudy
#        O1 150
#        O2 530



# # # # # ${PLOT_PARAM} ../xval/reruns/SAFE_reruns_rse1_test.150.dat \
# # # # #         ../xval/reruns/SAFE_reruns_rse1_test.530.dat \
# # # # #         ../single/single_inversions_results_FBP.dat \
# # # # #         params_central_xval_complete_SAFE \
# # # # #         spot_obs_complete.dat
# # # # # 
# # # # # ${PLOT_COV} ../xval/reruns/SAFE_reruns_rse1_test.150.npz \
# # # # #         ../xval/reruns/SAFE_reruns_rse1_test.530.npz \
# # # # #         cov_central_xval_complete_SAFE
# # # # #         
# # # # # ${PLOT_PARAM} ../xval_cloudy/reruns/SAFE_reruns_rse1_test.100.dat \
# # # # #         ../xval_cloudy/reruns/SAFE_reruns_rse1_test.630.dat \
# # # # #         ../single/single_inversions_results_cloudy_FBP.dat \
# # # # #         params_central_xval_cloudy_SAFE \
# # # # #         spot_obs_cloudy.dat
# # # # #         
# # # # # ${PLOT_COV} ../xval_cloudy/reruns/SAFE_reruns_rse1_test.100.npz \
# # # # #         ../xval_cloudy/reruns/SAFE_reruns_rse1_test.630.npz \
# # # # #         cov_central_xval_cloudy_SAFE
        
        
# Left xvals
#     Cloudy
#         O1 75
#         O2 530
# 
#     NonCloudy
#         O1 100
#         O2 35


        
# # # # ${PLOT_PARAM} ../xval/reruns/SAFE_reruns_rse1_test.100.dat \
# # # #         ../xval/reruns/SAFE_reruns_rse1_test.35.dat \
# # # #         ../single/single_inversions_results_FBP.dat \
# # # #         params_left_xval_complete_SAFE \
# # # #         spot_obs_complete.dat
# # # # 
# # # # ${PLOT_COV} ../xval/reruns/SAFE_reruns_rse1_test.100.npz \
# # # #         ../xval/reruns/SAFE_reruns_rse1_test.35.npz \
# # # #         cov_left_xval_complete_SAFE
# # # #         
# # # # ${PLOT_PARAM} ../xval_cloudy/reruns/SAFE_reruns_rse1_test.75.dat \
# # # #         ../xval_cloudy/reruns/SAFE_reruns_rse1_test.530.dat \
# # # #         ../single/single_inversions_results_cloudy_FBP.dat \
# # # #         params_left_xval_cloudy_SAFE \
# # # #         spot_obs_cloudy.dat
# # # #         
# # # # 
# # # # ${PLOT_COV} ../xval_cloudy/reruns/SAFE_reruns_rse1_test.75.npz \
# # # #         ../xval_cloudy/reruns/SAFE_reruns_rse1_test.530.npz \
# # # #         cov_left_xval_cloudy_SAFE
# # # #         
        
        
        
## Narrow bands
# # # # ${PLOT_PARAM} ../xval/reruns/NB_reruns_rse1_test.150.dat \
# # # #         ../xval/reruns/NB_reruns_rse1_test.530.dat \
# # # #         ../single/single_inversions_results.dat \
# # # #         params_central_xval_complete_NB \
# # # #         spot_obs_complete.dat
# # # # 
# # # # ${PLOT_COV} ../xval/reruns/NB_reruns_rse1_test.150.npz \
# # # #         ../xval/reruns/NB_reruns_rse1_test.530.npz \
# # # #         cov_central_xval_complete_NB
# # # #         
# # # # ${PLOT_PARAM} ../xval_cloudy/reruns/NB_reruns_rse1_test.100.dat \
# # # #         ../xval_cloudy/reruns/NB_reruns_rse1_test.630.dat \
# # # #         ../single/single_inversions_results_cloudy.dat \
# # # #         params_central_xval_cloudy_NB \
# # # #         spot_obs_cloudy.dat
# # # #         
# # # # ${PLOT_COV} ../xval_cloudy/reruns/NB_reruns_rse1_test.100.npz \
# # # #         ../xval_cloudy/reruns/NB_reruns_rse1_test.630.npz \
# # # #         cov_central_xval_cloudy_NB
# # # #         
# # # # ${PLOT_PARAM} ../xval/reruns/NB_reruns_rse1_test.100.dat \
# # # #         ../xval/reruns/NB_reruns_rse1_test.35.dat \
# # # #         ../single/single_inversions_results.dat \
# # # #         params_left_xval_complete_NB \
# # # #         spot_obs_complete.dat
# # # # 
# # # # ${PLOT_COV} ../xval/reruns/NB_reruns_rse1_test.100.npz \
# # # #         ../xval/reruns/NB_reruns_rse1_test.35.npz \
# # # #         cov_left_xval_complete_NB
# # # #         
# # # # ${PLOT_PARAM} ../xval_cloudy/reruns/NB_reruns_rse1_test.75.dat \
# # # #         ../xval_cloudy/reruns/NB_reruns_rse1_test.530.dat \
# # # #         ../single/single_inversions_results_cloudy.dat \
# # # #         params_left_xval_cloudy_NB \
# # # #         spot_obs_cloudy.dat
# # # # 
# # # # ${PLOT_COV} ../xval_cloudy/reruns/NB_reruns_rse1_test.75.npz \
# # # #         ../xval_cloudy/reruns/NB_reruns_rse1_test.530.npz \
# # # #         cov_left_xval_cloudy_NB
# # # #         

        
        
        
### Full pachanga

## Narrow bands
${PLOT_PARAM} ../xval/reruns/reruns_rse1_test.150.dat \
../xval/reruns/reruns_rse1_test.530.dat \
../single/single_inversions_results_FBP.dat \
params_central_xval_complete_FBP \
spot_obs_complete.dat

${PLOT_COV} ../xval/reruns/reruns_rse1_test.150.npz \
../xval/reruns/reruns_rse1_test.530.npz \
cov_central_xval_complete_FBP

${PLOT_PARAM} ../xval_cloudy/reruns/reruns_rse1_test.100.dat \
../xval_cloudy/reruns/reruns_rse1_test.630.dat \
../single/single_inversions_results_cloudy_FBP.dat \
params_central_xval_cloudy_FBP \
spot_obs_cloudy.dat

${PLOT_COV} ../xval_cloudy/reruns/reruns_rse1_test.100.npz \
../xval_cloudy/reruns/reruns_rse1_test.630.npz \
cov_central_xval_cloudy_FBP

${PLOT_PARAM} ../xval/reruns/reruns_rse1_test.100.dat \
../xval/reruns/reruns_rse1_test.35.dat \
../single/single_inversions_results_FBP.dat \
params_left_xval_complete_FBP \
spot_obs_complete.dat

${PLOT_COV} ../xval/reruns/reruns_rse1_test.100.npz \
../xval/reruns/reruns_rse1_test.35.npz \
cov_left_xval_complete_FBP

${PLOT_PARAM} ../xval_cloudy/reruns/reruns_rse1_test.75.dat \
../xval_cloudy/reruns/reruns_rse1_test.530.dat \
../single/single_inversions_results_cloudy_FBP.dat \
params_left_xval_cloudy_FBP \
spot_obs_cloudy.dat

${PLOT_COV} ../xval_cloudy/reruns/reruns_rse1_test.75.npz \
../xval_cloudy/reruns/reruns_rse1_test.530.npz \
cov_left_xval_cloudy_FBP

