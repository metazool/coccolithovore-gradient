import sys, os
sys.path.append('stylegan2')
sys.path.append('forambulator')
import forams.train

# Restart from scratch
# resume_from_filename = os.path.join(home, 'results/00035-stylegan2-tfrecords_cg-1gpu-config-f/network-snapshot-000216.pkl')
resume_from_filename = None

forams.train.train(data_dir='.',
                   dataset='tfrecords_cg',
                   metrics=[],
                   total_kimg=3000,
                   resume_from=resume_from_filename,
                   result_dir='/storage/coccoliths'
                   save_ticks=1)
