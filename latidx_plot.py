
import numpy as np
import matplotlib.pyplot as plt
plt.ion()

task_name = 'covert' # 'viewing' # 

times = np.arange(0,0.801,0.004)
n_times = len(times)

# load behavioral data

onsets = np.load('data/speechonsets.npy', allow_pickle=True)
medons = [np.median(onsets[ii]) for ii in range(len(onsets))]

# load neural data

data = np.load('data/wpli_%s.npy' % task_name, allow_pickle=True)
n_subj = data.shape[0]
n_labels = data.shape[1]

# sigmoidal normalization

data_norm = np.zeros_like(data)
for ii in range(n_subj):
    for jj in range(n_labels):
        data_norm[ii,jj,:] = np.abs(1.0/(1.0+np.exp((data[ii,jj,:]-np.mean(data[ii,jj,:]))/np.std(data[ii,jj,:])))-1)

# lateralization index

lat_idx = np.zeros((n_subj, n_times))
lat_left = np.zeros((n_subj, n_times))
lat_right = np.zeros((n_subj, n_times))
for ii in range(n_subj):
    for jj in range(n_times):
        tmp_left = data_norm[ii,0,jj]
        tmp_right = data_norm[ii,1,jj]
        lat_idx[ii,jj] = (tmp_right - tmp_left) /  (tmp_right + tmp_left)
        lat_left[ii,jj] = tmp_left
        lat_right[ii,jj] = tmp_right

avg_lat_idx = lat_idx.mean(0)
sem_lat_idx = (lat_idx.std(0)) / np.sqrt(n_subj)

avg_left = lat_left.mean(0)
sem_left = (lat_left.std(0)) / np.sqrt(n_subj)

avg_right = lat_right.mean(0)
sem_right = (lat_right.std(0)) / np.sqrt(n_subj)

# visualization

fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

axs[0].annotate(' expected \n speech onset', xy=(0.38,-0.175), fontsize=10, rotation=90, zorder=8) 
axs[0].annotate('before', xy=(0.25,0.15), fontsize=10, rotation=0, zorder=8)
axs[0].annotate('after', xy=(0.49,-0.15), fontsize=10, rotation=0, zorder=8)
axs[0].axvspan(xmin=0.2,xmax=np.median(medons),ymin=-0.15,ymax=1, color='#4292c6', alpha=0.2,zorder=-1)
axs[0].axvspan(xmin=np.median(medons),xmax=0.64,ymin=-0.15,ymax=1, color='#ef3b2c', alpha=0.2, zorder=-1)
axs[0].plot(times, avg_lat_idx, color='k', lw=2, alpha=1)
axs[0].fill_between(times, avg_lat_idx-sem_lat_idx, avg_lat_idx+sem_lat_idx, color='k', alpha=0.3,zorder=8)
axs[0].axhline(y=0, color='gray', linestyle='--', linewidth=1,zorder=-1)
axs[0].set_xlim([0,0.8])
axs[0].set_ylim([-0.18,0.18])
axs[0].tick_params(labelsize=16)
axs[0].set_xticks([0,0.2,0.4,0.6,0.8])
axs[0].set_yticks([-0.18,-0.12,-0.06,0,0.06,0.12,0.18])
axs[0].set_ylabel('left<       LI       >right', fontsize=16)
axs[0].set_xlabel('Time [s]', fontsize=16)
axs[0].spines['right'].set_visible(False)
axs[0].spines['top'].set_visible(False)
axs[0].xaxis.set_ticks_position('bottom')
axs[0].yaxis.set_ticks_position('left')

taskimg = plt.imread('data/%s.png' % task_name)
if task_name == 'covert':
    inset = axs[0].inset_axes([-0.01, 0.736, 0.27, 0.24], zorder=-10)
else:
    inset = axs[0].inset_axes([0.07, 0.83, 0.11, 0.17], zorder=-10)
inset.imshow(taskimg,aspect='auto')
inset.axis('off')
plt.setp(inset,xticks=[],yticks=[])

axs[1].plot(times,avg_left,color='#542788',label='left hemisphere',alpha=1)
axs[1].plot(times,avg_right,color='#e08214',label='right hemisphere',alpha=1)
axs[1].axvline(x=np.median(medons), color='gray', linestyle='--', linewidth=1)
axs[1].annotate(' expected \n speech onset', xy=(0.38,0.354), fontsize=10, rotation=90, zorder=8) 
axs[1].set_yticks([0.35,0.4,0.45,0.5,0.55,0.6,0.65])
axs[1].set_xticks([0,0.2,0.4,0.6,0.8])
axs[1].set_ylim([0.35,0.65])
axs[1].set_xlim([0,0.8])
leg = axs[1].legend(loc=9,bbox_to_anchor=(0.4, 1.25),ncol=2,fontsize=11)
axs[1].fill_between(times, avg_left-sem_left, avg_left+sem_left, color='#542788', alpha=0.3)
axs[1].fill_between(times, avg_right-sem_right, avg_right+sem_right, color='#e08214', alpha=0.3)
axs[1].set_ylabel('wPLI', fontsize=16) # 'normalized wPLI'
axs[1].set_xlabel('Time [s]', fontsize=16)
axs[1].tick_params(labelsize=16)
axs[1].spines['right'].set_visible(False)
axs[1].spines['top'].set_visible(False)
axs[1].xaxis.set_ticks_position('bottom')
axs[1].yaxis.set_ticks_position('left')

axs[2].boxplot([lat_idx[:,50:102].mean(1),lat_idx[:,102:160].mean(1)],labels=['before','after'], notch='True', showfliers='False',sym=' ',widths=[0.4,0.4], medianprops=dict(color="black",linewidth=1.5))
xsbef = list()
for ii in range(len(lat_idx[:,50:102].mean(1))):
    xsbef.append(np.random.normal(1, 0.1))
xsaft = list()
for ii in range(len(lat_idx[:,102:160].mean(1))):
    xsaft.append(np.random.normal(2, 0.1))
xs = np.array([xsbef,xsaft]).T
for ii in range(len(lat_idx[:,50:102].mean(1))):
    axs[2].scatter(xs[ii,0],lat_idx[ii,50:102].mean(),40,'b',alpha=0.4)
    axs[2].plot(np.array([xs[ii,0],xs[ii,1]]),np.array([lat_idx[ii,50:102].mean(),lat_idx[ii,102:160].mean()]),color='gray',lw=1,alpha=0.5)
for ii in range(len(lat_idx[:,102:160].mean(1))):
    axs[2].scatter(xs[ii,1],lat_idx[ii,102:160].mean(),40,'r',alpha=0.4)

if task_name == 'covert':
    axs[2].plot([1, 1, 2, 2], [0.6, 0.63, 0.63,0.6], lw=1.5, c='k', clip_on=False)
    axs[2].plot(1.425,0.68,' ',color='k',marker='*', markersize=10, clip_on=False)
    axs[2].plot(1.575,0.68,' ',color='k',marker='*', markersize=10, clip_on=False)
    axs[2].plot(1,0.55,' ',color='k',marker='*', markersize=10)
    axs[2].plot([0.75, 0.75, 1.25, 1.25], [0.47, 0.5, 0.5,0.47], lw=1.5, c='k')
    axs[2].plot(2,0.55,' ',color='k',marker='*', markersize=10)
    axs[2].plot([1.75, 1.75, 2.25, 2.25], [0.47, 0.5, 0.5,0.47], lw=1.5, c='k')
else:
    axs[2].annotate('n.s.',xy=(1.35,0.57),fontsize=14)
    axs[2].plot([1, 1, 2, 2], [0.49, 0.54, 0.54,0.49], lw=1.5, c='k', clip_on=False)

axs[2].set_ylim([-0.6,0.6])
axs[2].set_yticks(ticks=[-0.6,-0.4,-0.2,0,0.2,0.4,0.6])
axs[2].set_xticklabels(labels=['before','after'], fontsize=12)
axs[2].set_ylabel('left<       LI       >right', fontsize=16)
axs[2].set_xlabel('Time Window', fontsize=16)
axs[2].tick_params(labelsize=16)
axs[2].spines['right'].set_visible(False)
axs[2].spines['top'].set_visible(False)
axs[2].xaxis.set_ticks_position('bottom')
axs[2].yaxis.set_ticks_position('left')

plt.tight_layout(pad=2)
