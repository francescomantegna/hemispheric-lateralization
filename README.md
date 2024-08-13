# hemispheric-lateralization
This repository contains the source code for "Time-resolved hemispheric lateralization of audiomotor connectivity during covert speech production" (Mantegna et al.)

# Abstract

<p align="justify"> Covert speech involves the internal generation of articulatory movements and their sensory consequences. While overt speech involves a combination of feedforward and feedback signals, feedback signals are substantially different, or even absent, during covert speech. Despite the differences, we conjectured that inter-areal communication between sensory and motor areas during covert speech is implemented through the same channels recruited during overt speech. An influential overt speech model proposed that feedforward and feedback signals are segregated to the left and right hemispheres, respectively. Here we used magnetoencephalography to investigate the lateralization of functional connectivity before and after covert speech production. The data reveal leftward lateralization preceding and rightward lateralization following predicted covert speech onset. This alternating lateralization pattern is observed only in the connection between premotor and auditory regions, and in the alpha frequency band. The data, derived entirely from covert speech, add a provocative perspective to adjudicate between overt speech models. </p>

# Description

<p align="justify"> * "onsets_plot.py" generates Figure 1. We parameterize participants’ speech latencies distribution using a Gamma probability density function which adequately captures the basic features of the distribution (i.e., asymmetrical with a long right tail, and leftward skew). The Gamma function is based on two parameters: a shape (𝛼) and a scale (𝜎) parameter. The shape parameter represents the skewness of the distribution and the scale parameter represents the width of the distribution. </p>
<p align="justify"> * "meg_erp_plot.py" generates Figure 2. The grand average MEG event-related responses are shown. We compared event-related responses elicited during the covert speech and the passive viewing conditions. The stacked area chart shows how does the magnitude of the MEG evoked response compares between conditions. The differences between conditions are also represented. </p> 
<p align="justify"> * "emg_erp_plot.py" generates Figure 3. The grand average EMG event-related responses are shown. We compared event-related responses elicited during the covert speech and the passive viewing conditions. The stacked area chart shows how does the magnitude of the EMG evoked response compares between conditions. The differences between conditions are also represented. </p>
<p align="justify"> * "latidx_plot.py" generates Figure 5. Functional connectivity results obtained for the alpha band (8-12 Hz) and for the connection between premotor and auditory ROIs. We measured the Lateralization Index (LI) by computing the normalized difference between phase shifts in different hemispheres for every time point in the trial. A negative lateralization index value reflects higher probability of phase shifts between the ROIs in the left hemisphere, a positive lateralization index in the right. </p>


# Data & code availability

<p align="justify"> This repository contains only a portion of the complete dataset, and the provided code is not complete. For additional information, access to the full dataset, and the complete code required for further analysis, please contact the author (Francesco Mantegna, fmantegna93@gmail.com). </p>

# DOI

[![DOI](https://zenodo.org/badge/840644183.svg)](https://zenodo.org/doi/10.5281/zenodo.13292069)
