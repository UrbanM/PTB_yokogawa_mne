# This is a sample Python script.
# Created by Urban Marhl

def import_coregistration2(zebris_file):
    import re
    import numpy as np

    elp_zebris = np.zeros((8, 3))

    zeb = []
    F = open(zebris_file, 'r')
    num_lines = sum(1 for line in open(zebris_file))
    i = 0
    while i < num_lines:
        f = F.readline()
        f = f.replace('"', '')
        f = f.replace(':', ',')
        f = f.replace('\n', '')
        f = f.replace('\t\t', ' ')
        f = f.replace('\t', '')
        ff = list(filter(None, re.split(" ", f)))
        ffd = np.array(ff[1:4], dtype=float)
        if (ff[0] == 'Coil1'):
            elp_zebris[3] += ffd
        elif (ff[0] == 'Coil2'):
            elp_zebris[4] += ffd
        elif (ff[0] == 'Coil3'):
            elp_zebris[5] += ffd
        elif (ff[0] == 'Coil4'):
            elp_zebris[6] += ffd
        elif (ff[0] == 'Coil5'):
            elp_zebris[7] += ffd
        elif (ff[0] == 'Na'):
            elp_zebris[0] += ffd
        elif (ff[0] == 'LP'):
            elp_zebris[1] += ffd
        elif (ff[0] == 'RP'):
            elp_zebris[2] += ffd
        elif (i > 2):
            zeb.append(ff[1:4])
        i += 1

    zeb = np.array(zeb, dtype=float)
    elp_zebris[:, :] /= 2

    return elp_zebris * 10 ** (-3), zeb * 10 ** (-3)


def preprocess_geometry():
    import mne

    con_name = "DATA/urma181019.0300.con"
    zebris_file = "DATA/urma181019.0300.sfp"
    marker_file = "DATA/urma181019.0300.mrk"
    subject_dir = "DATA/subjects/"

    elp, hsp = import_coregistration2(zebris_file)

    raw = mne.io.read_raw_kit(con_name, mrk=marker_file, elp=elp, hsp=hsp)
    raw.save("urma181019.0300-raw.fif", overwrite=True)
    raw.plot(block=True)

    mne.bem.make_scalp_surfaces(subjects_dir=subject_dir, subject="urma")
    mne.gui.coregistration(subjects_dir=subject_dir, subject="urma", block=True)

    return


def_preprocess():
    con_name = "DATA/urma181019.0300.con"
    raw = mne.io.read_raw_kit(con_name)
    raw.plot(block=True)
    return


if __name__ == '__main__':
    # Converting con file to .fif with geometry
    preprocess_geometry()
    # Converting con file to .fif without geometry
    preprocess()
