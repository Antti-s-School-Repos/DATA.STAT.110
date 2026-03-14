import numpy as np

males = np.array([(175, 80), (180, 84), (165, 74), (190, 95), (174, 78), (191, 88)], 
                 dtype=[('height', 'i4'), ('weight', 'i4')])

females = np.array([(170, 70), (162, 62), (165, 59), (160, 55), (158, 52), (174, 66)],
                    dtype=[('height', 'i4'), ('weight', 'i4')])

sum_heights = np.sum(males['height']) + np.sum(females['height'])
print(sum_heights)