# PTB_yokogawa_mne
This is an example project, how to convert the yokogawa SQUID measurements at PTB to the MNE .fif format with geometry..

To run the main.py script you need to install: mne, pyvistaqt, traitlets, pyqt5, nibabel, scikit-learn(optional)

Run the file as "`python main.py`". At the end of main.py file comment or uncomment if you want to run the conversion with or without geometry.

To obtain the head-mri-transformation file, you have to use the coregistration tool "in code `mne.gui.coregistration(subjects_dir=subject_dir, subject="urma", block=True)`". You have to follow the instructions in the gui program. Dont forget! You have to use the filename-raw.fif with zebris data included.

To test this script you can download the example files from https://nextcloud.urbanmarhl.com/s/F9fnGDiDWmA3Y32

Requirements:
- Measurement file, from yokogava SQUID system (filename.con)
If you need geometry, you will also need
- Zebris machine file (filename.sfp)
- Marker file, from yokogava SQUID system (filename.mrk)
- Subject directory (output form the software freesurfer)

If you have any questions please contact me: urban.marhl@imfm.si
