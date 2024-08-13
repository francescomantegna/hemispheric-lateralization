import os
import pickle
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
from scipy.optimize import minimize, rosen_der
plt.ion()

def custom_optimizer(func, x0, args=(), disp=True):
    x0 = [4,0.4,0.03]
    bnds = ((2, 6), (0.1, 0.8), (0.005, 0.05))
    res = minimize(func, x0, args, bounds=bnds, method="L-BFGS-B", jac='3-point', hess='3-point', options={'gtol': 1e-3, 'maxiter':1000,  'disp': True})
    if res.success:
        return res.x
    raise RuntimeError('optimization routine failed')

nsubs = 40
onsets = np.load('data/speechonsets.npy', allow_pickle=True)

fig, ax2 = plt.subplots(1,1,figsize=(12,6))
ax2.hist(sum(onsets.flatten().tolist(),[]), color='#4292c6', edgecolor='k', alpha=0.4, bins=100, zorder=10)
ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.yaxis.set_ticks_position('left')
ax2.xaxis.set_ticks_position('bottom')
ax2.set_xlabel('Time [s]', fontsize=18)
ax2.set_ylabel('Frequency of occurrence (group)', fontsize=18, rotation=90)
ax2.set_ylim([0,250])
ax2.tick_params(labelsize=18)

ax = ax2.twinx()

gamma_params = list()
gamma_median = list()
gamma_mean = list()
gamma_std = list()
gamma_pdf = list() 

for ss in range(nsubs):

  fit_alpha, fit_loc, fit_beta = stats.gamma.fit(onsets[ss],method="MM",optimizer=custom_optimizer)
  params = [fit_alpha, fit_loc, fit_beta]
  gamma_params.append(params)
  gamma_pdf.append(stats.gamma.pdf(np.arange(0,1.0,0.01),fit_alpha,fit_loc,fit_beta))
  ax.plot(np.arange(0,1.0,0.01),stats.gamma.pdf(np.arange(0,1.0,0.01),fit_alpha,fit_loc,fit_beta)*(fit_loc*10), color='b')
  gamma_median.append(stats.gamma.median(fit_alpha,fit_loc,fit_beta))
  gamma_mean.append(stats.gamma.mean(fit_alpha,fit_loc,fit_beta))
  gamma_std.append(stats.gamma.std(fit_alpha,fit_loc,fit_beta))

gamma_params = np.array(gamma_params)
gamma_median = np.array(gamma_median)
gamma_mean = np.array(gamma_mean)
gamma_std = np.array(gamma_std)
gamma_pdf = np.array(gamma_pdf)

ax.axvline(x=np.median(gamma_median), color='k', linestyle='--', linewidth=3, zorder=10, label='median speech sound onset')
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('right')
ax.xaxis.set_ticks_position('bottom')
ax.set_ylabel('Frequency of occurrence (subject)', fontsize=18, labelpad=20, rotation=270)
ax.set_xlim([0,1])
ax.set_ylim([0,50])
ax.tick_params(labelsize=18)
ax.legend(loc=1, fontsize=16)

fig, axs = plt.subplots(1,4,figsize=(12,4), sharex=True, sharey=True)

fit_alpha, fit_loc, fit_beta = stats.gamma.fit(onsets[39],method="MM",optimizer=custom_optimizer)
axs[0].hist(onsets[39],bins=10,edgecolor='k',alpha=0.5)
axs[0].plot(np.arange(0.0,1.01,0.01),stats.gamma.pdf(np.arange(0.0,1.01,0.01),fit_alpha,fit_loc,fit_beta)*(fit_loc*10),color='b', alpha=0.8, lw=3)
axs[0].axvline(x=gamma_median[39], color='k', linestyle='--', linewidth=2, zorder=10)
axs[0].spines['right'].set_visible(False)
axs[0].spines['top'].set_visible(False)
axs[0].yaxis.set_ticks_position('left')
axs[0].xaxis.set_ticks_position('bottom')
axs[0].set_xlabel('Time [s]', fontsize=16)
axs[0].set_ylabel('Frequency of occurrence \n(subject)', fontsize=16, labelpad=10, rotation=90)
axs[0].set_xlim([0.0,1.0])
axs[0].set_ylim([0,50])
axs[0].tick_params(labelsize=16)
axs[0].set_title(r'$\alpha = %.2f; \sigma = %.2f$' % (fit_alpha, fit_beta), fontsize=16, pad=20)

fit_alpha, fit_loc, fit_beta = stats.gamma.fit(onsets[22],method="MM",optimizer=custom_optimizer)
axs[1].hist(onsets[22],bins=7,edgecolor='k',alpha=0.5)
axs[1].plot(np.arange(0.0,1.01,0.01),stats.gamma.pdf(np.arange(0.0,1.01,0.01),fit_alpha,fit_loc,fit_beta)*(fit_loc*10),color='b', alpha=0.8, lw=3)
axs[1].axvline(x=gamma_median[22], color='k', linestyle='--', linewidth=2, zorder=10)
axs[1].spines['right'].set_visible(False)
axs[1].spines['top'].set_visible(False)
axs[1].yaxis.set_ticks_position('left')
axs[1].xaxis.set_ticks_position('bottom')
axs[1].set_xlabel('Time [s]', fontsize=16)
axs[1].set_xlim([0.0,1.0])
axs[1].set_ylim([0,50])
axs[1].tick_params(labelsize=16)
axs[1].set_title(r'$\alpha = %.2f; \sigma = %.2f$' % (fit_alpha, fit_beta), fontsize=16, pad=20)

fit_alpha, fit_loc, fit_beta = stats.gamma.fit(onsets[11],method="MM",optimizer=custom_optimizer)
axs[2].hist(onsets[11],bins=13,edgecolor='k',alpha=0.5)
axs[2].plot(np.arange(0.0,1.01,0.01),stats.gamma.pdf(np.arange(0.0,1.01,0.01),fit_alpha,fit_loc,fit_beta)*(fit_loc*10),color='b', alpha=0.8, lw=3)
axs[2].axvline(x=gamma_median[11], color='k', linestyle='--', linewidth=2, zorder=10)
axs[2].spines['right'].set_visible(False)
axs[2].spines['top'].set_visible(False)
axs[2].yaxis.set_ticks_position('left')
axs[2].xaxis.set_ticks_position('bottom')
axs[2].set_xlabel('Time [s]', fontsize=16)
axs[2].set_xlim([0.0,1.0])
axs[2].set_ylim([0,50])
axs[2].tick_params(labelsize=16)
axs[2].set_title(r'$\alpha = %.2f; \sigma = %.2f$' % (fit_alpha, fit_beta), fontsize=16, pad=20)

fit_alpha, fit_loc, fit_beta = stats.gamma.fit(onsets[31],method="MM",optimizer=custom_optimizer)
axs[3].hist(onsets[31],bins=15,edgecolor='k',alpha=0.5)
axs[3].plot(np.arange(0.0,1.01,0.01),stats.gamma.pdf(np.arange(0.0,1.01,0.01),fit_alpha,fit_loc,fit_beta)*(fit_loc*10),color='b', alpha=0.8, lw=3)
axs[3].axvline(x=gamma_median[31], color='k', linestyle='--', linewidth=2, zorder=10)
axs[3].spines['right'].set_visible(False)
axs[3].spines['top'].set_visible(False)
axs[3].yaxis.set_ticks_position('left')
axs[3].xaxis.set_ticks_position('bottom')
axs[3].set_xlabel('Time [s]', fontsize=16)
axs[3].set_xlim([0.0,1.0])
axs[3].set_ylim([0,50])
axs[3].tick_params(labelsize=16)
axs[3].set_title(r'$\alpha = %.2f; \sigma = %.2f$' % (fit_alpha+0.15, fit_beta), fontsize=16, pad=20)

plt.tight_layout(pad=1)
