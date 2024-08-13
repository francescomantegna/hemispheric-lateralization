
import numpy as np
import matplotlib.pyplot as plt
plt.ion()

times = np.arange(0,1.001,0.001)
n_times = len(times)

# load neural data

# data_covert = np.load('data/meg_covert_erp.npy', allow_pickle=True)
# data_viewing = np.load('data/meg_viewing_erp.npy', allow_pickle=True)
data_covert = np.load('meg_covert_erp.npy', allow_pickle=True)
data_viewing = np.load('meg_viewing_erp.npy', allow_pickle=True)
n_subj = data_covert.shape[0]
n_labels = data_covert.shape[1]
assert n_times == data_covert.shape[2]

# plot erps

fig, ax = plt.subplots(1,1,figsize=(8,6))
[ax.plot(times,data_covert.mean(0)[ii]*1e15, 'k', lw=0.5) for ii in range(157)]
ax.set_ylim([-100, 100])
ax.set_xlim([0, 1])
ax.set_yticks([-100,-50, 0, 50, 100])
ax.tick_params(labelsize=14)
ax.set_ylabel('fT', fontsize=14)
ax.set_xlabel('Time [s]', fontsize=14)
ax.set_title(' ')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

fig, ax = plt.subplots(1,1,figsize=(8,6))
[ax.plot(times,data_viewing.mean(0)[ii]*1e15, 'k', lw=0.5) for ii in range(157)]
ax.set_ylim([-100, 100])
ax.set_xlim([0, 1])
ax.set_yticks([-100,-50, 0, 50, 100])
ax.tick_params(labelsize=14)
ax.set_ylabel('fT', fontsize=14)
ax.set_xlabel('Time [s]', fontsize=14)
ax.set_title(' ')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# root mean square

rms_covert = np.array([np.sqrt((data_covert[ii]**2).mean(0)) for ii in range(n_subj)])
rms_viewing = np.array([np.sqrt((data_viewing[ii]**2).mean(0)) for ii in range(n_subj)])
conddiff = rms_covert - rms_viewing

# plot rms

fig, ax = plt.subplots(1,1,figsize=(8,6))
ax.plot(times, rms_covert.mean(0), color='g', lw=3)
ax.fill_between(times,rms_viewing.mean(0), rms_covert.mean(0), color= 'g', alpha=0.6, label='covert speech')
ax.plot(times, rms_viewing.mean(0), color='y', lw=3)
ax.fill_between(times,np.zeros_like(times),rms_viewing.mean(0), color= 'y', alpha=0.6, label='passive viewing')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.set_ylabel('RMS', fontsize=18)
ax.set_xlabel('Time [s]', fontsize=18)
ax.set_xlim([0,1])
ax.set_ylim([0,3.5e-14])
ax.tick_params(labelsize=18)
ax.legend(loc=1,fontsize=17)

fig, ax = plt.subplots(1,1,figsize=(8,6))
ax.plot(times,conddiff.mean(0), color='b', lw=3, label='covert speech - \npassive viewing')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.set_ylabel('RMS', fontsize=18)
ax.set_xlabel('Time [s]', fontsize=18)
ax.set_xlim([0,1])
ax.set_ylim([0,1.2e-14])
ax.tick_params(labelsize=18)
ax.legend(loc=1,fontsize=17)

